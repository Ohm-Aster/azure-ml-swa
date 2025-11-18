import json
import requests
from .config import ENDPOINT, API_KEY, DEPLOYMENT_NAME

def main(req):
    body = req.get_json()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "azureml-model-deployment": DEPLOYMENT_NAME
    }

    response = requests.post(ENDPOINT, headers=headers, json=body)
    
    return {
        "status": response.status_code,
        "result": response.json()
    }
