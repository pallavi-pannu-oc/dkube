import os
import numpy as np
import pandas as pd
import argparse
import time
import requests
import io

# import sys
import yaml
from dkube.sdk import *

TRAIN_CSV_LINK="https://dkube.s3.amazonaws.com/datasets/titanic/train.csv"

USER_COMPUTES_METADATA=1
DKUBE_COMPUTES_METADATA=0

# Ensure the following environment parameters are present
"""
DKUBE_JOB_UUID=cb581648-448d-494a-bcf7-90548572d4d2
DKUBE_USER_STORE=/var/dkube/dkube-store/dkube/users/trump
DKUBE_DATA_BASE_PATH=/var/dkube/dkube-store/dkube
DKUBE_USER_ACCESS_TOKEN=blah
USERNAME=trump
DKUBE_USER_LOGIN_NAME=trump
DKUBE_JOB_CLASS=notebook
"""

# Run as
# python featureset-titanic.py --url https://dkube-url:32222

if __name__ == "__main__":

    ########--- Parse for parameters ---########

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", dest="url", default=None, type=str, help="DKube access URL")

    global FLAGS
    FLAGS, unparsed = parser.parse_known_args()

    ########--- Download titanic data ---########
    with requests.Session() as s:
        download = s.get('https://dkube.s3.amazonaws.com/datasets/titanic/train.csv')

    if (download.ok):
        data = download.content.decode('utf8')
        train_data = pd.read_csv(io.StringIO(data))
    print(train_data)


    ########--- Get DKube client handle ---########

    dkubeURL = FLAGS.url
    # Dkube user access token for API authentication
    authToken = os.getenv("DKUBE_USER_ACCESS_TOKEN")
    # Get client handle
    api = DkubeApi(URL=dkubeURL, token=authToken)

    # create featureset
    train_fs = generate('train-fs')
    print(f"Featureset name {train_fs}\n")
    featureset = DkubeFeatureSet(name=train_fs, description="Titanic FeatureSet experiments")
    print(f"---- Featureset name {train_fs} -- Create featureset \n")
    api.create_featureset(featureset)


    ########--- Process raw data  ---########

    # Fill in null values with median
    train_data["Age"].fillna(value=train_data["Age"].median(), inplace=True)
    # Drop rows where fare is less than 100
    train_data = train_data[train_data["Fare"] < 100]
    # Fill in null values
    train_data["Embarked"].fillna(method="ffill", inplace=True)
    # Select features for training
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    train_df = pd.get_dummies(train_data[features])
    train_df = pd.concat([train_data[["Age", "Fare", "Survived", "PassengerId"]], train_df], axis=1)
    print(train_df.head())

    ########--- commit features ---########

    if DKUBE_COMPUTES_METADATA:
        resp = api.commit_featureset(name=train_fs, df=train_df)

    elif USER_COMPUTES_METADATA:

        # Prepare featurespec - Name, Description, Schema for each feature
        keys = train_df.keys()
        schema = train_df.dtypes.to_list()
        featureset_metadata = []
        for i in range(len(keys)):
            metadata = {}
            metadata["name"] = str(keys[i])
            metadata["description"] = None
            metadata["schema"] = str(schema[i])
            featureset_metadata.append(metadata)
        
        ########--- Commit features ---########
        resp = api.commit_featureset(name=train_fs, df=train_df, metadata=featureset_metadata)

    # Read the features
    df = api.read_featureset(name=train_fs)
    print(df.head())
    assert(df.equals(train_df)), "not equal"
