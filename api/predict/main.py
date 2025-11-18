import os
import json
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    endpoint = os.getenv("AZUREML_ENDPOINT")
    api_key = os.getenv("AZUREML_API_KEY")
    deploy = os.getenv("AZUREML_DEPLOY")

    if not endpoint or not api_key:
        return func.HttpResponse(
            "Missing configuration variables",
            status_code=500
        )

    try:
        body = req.get_json()
    except:
        return func.HttpResponse(
            "Invalid JSON body",
            status_code=400
        )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "azureml-model-deployment": deploy
    }

    try:
        response = requests.post(endpoint, headers=headers, json=body)
        return func.HttpResponse(
            response.text,
            status_code=response.status_code,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            f"Request error: {str(e)}",
            status_code=500
        )
