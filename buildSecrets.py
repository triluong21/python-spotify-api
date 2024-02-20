from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
token_url = os.getenv("TOKEN_URL")

def getToken() -> str:
    authString = client_id + ":" + client_secret
    authBytes = authString.encode("utf-8")
    authBase64 = str(base64.b64encode(authBytes), "utf-8")

    headers = {
        "Authorization": "Basic " + authBase64,
        "Content-Type": "application/x-www-form-urlencoded"
    }    

    data = {"grant_type": "client_credentials"}
    result = post(token_url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token: str = json_result["access_token"]
    return token

def getAuthHeader(token) -> dict:
    return {"Authorization": "Bearer " + token}

