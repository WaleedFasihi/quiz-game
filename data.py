import requests

ENDPOINT_URL = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean",
}

connection = requests.get(ENDPOINT_URL, parameters)
connection.raise_for_status()
data = connection.json()
question_data = data["results"]
