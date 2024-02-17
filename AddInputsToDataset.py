import requests
import json

url = "https://api.clarifai.com/v2/users/qj7itgikynyv/apps/my-first-application-i7adqk/datasets/user-input/inputs"

headers = {
    "Authorization": "Key f85f784cf89946078344980521f17f0d",
    "Content-Type": "application/json"
}

data = {
    "dataset_inputs": [
        {
            "input": {
                "id": "demo"
            }
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())