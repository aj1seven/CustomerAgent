import requests
from dotenv import load_dotenv
import os 

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "bb5adadf-ab3a-42c5-bc27-dfd1b4bdad8a"
FLOW_ID = "45106305-2608-4cd2-8f32-efda78cccba5"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "Customer1" # The endpoint name of the flow

def run_flow(message: str) -> dict:

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


result = run_flow("what are the shipment times")
print(result)
