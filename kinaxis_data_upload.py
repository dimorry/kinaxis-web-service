from settings import KINAXIS_FILE_UPLOAD_URI, KINAXIS_INSTANCE, KINAXIS_DATA_UPDATE_TRIGGER_URI
from secret import KINAXIS_WS_CREDS

import requests


def upload_file(dataSource, fileName, payload):
    url = KINAXIS_FILE_UPLOAD_URI \
            .replace("{instance}", KINAXIS_INSTANCE) \
            .replace("{data_source}", dataSource) \
            .replace("{file}", fileName)
    headers = KINAXIS_WS_CREDS
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)


def trigger_data_update(payload):
    url = KINAXIS_DATA_UPDATE_TRIGGER_URI \
            .replace("{instance}", KINAXIS_INSTANCE)
    headers = KINAXIS_WS_CREDS
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)        