from kfp.components._yaml_utils import load_yaml
from kfp.components._yaml_utils import dump_yaml
from kfp import components

SPEC = \
"""
name: dkube-viewer
description: |
    Viewer component which renders UI as static HTML in KF Output viewer.
    Support view types,
    * A web application to test inference for Dkube examples Only.
    * In future will add TFMA, Tensorboard etc..
metadata:
  annotations: {platform: 'Dkube'}
  labels: {platform: 'Dkube', wfid: '{{workflow.uid}}', runid: '{{pod.name}}', stage: 'viewer'}
inputs:
  - {name: auth_token,      type: String,   optional: false,
     description: 'Required. Dkube authentication token.'}
  - {name: servingurl,      type: String,   optional: false,
     description: 'Required. URL where the model is deployed for serving in Dkube.'}
  - {name: servingexample,  type: String,   optional: false,
     description: 'Required. Name of the Dkube example which is deployed for serving.
                   Possible options - digits/catsdogs/bolts'}
  - {name: viewtype,        type: String,   optional: true,     default: 'inference',
     description: 'Optional. Currently on viewtype=inference is only supported.'}
  - {name: access_url,      type: String,   optional: true,     default: '',
     description: 'Optional. URL at which dkube is accessible, copy paste from the browser of this window. Required for cloud deployments.'}
outputs:
  - {name: rundetails,       description: 'Details of the run'}
implementation:
  container:
    image: ocdr/dkubepl:1.4.0
    command: ['dkubepl']
    args: [
      viewer,
      --accessurl, {inputValue: access_url},
      --viewtype, {inputValue: viewtype},
      --token, {inputValue: auth_token},
      --servingurl, {inputValue: servingurl},
      --servingexample, {inputValue: servingexample},
      --runid, '{{pod.name}}'
    ]
    fileOutputs:
      rundetails: /tmp/rundetails
"""

def DkubeViewerOp(name='dkube-viewer'):
    cdict = load_yaml(SPEC)
    cdict['name'] = name
    cyaml = dump_yaml(cdict)

    return components.load_component_from_text(cyaml)
