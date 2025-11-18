import os
import json
import requests

def run(req):
    endpoint = os.getenv("AZUREML_ENDPOINT")
    api_key = os.getenv("AZUREML_API_KEY")
    deploy = os.getenv("AZUREML_DEPLOY")

    if not endpoint or not api_key:
        return {
            "status": 500,
            "body": "Missing configuration variables"
        }

    try:
        body = req.get_json()
    except:
        return {
            "status": 400,
            "body": "Invalid JSON body"
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "azureml-model-deployment": deploy
    }

    response = requests.post(endpoint, headers=headers, json=body)

    return {
        "status": response.status_code,
        "body": response.text
    }
