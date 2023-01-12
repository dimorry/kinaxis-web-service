from settings import KINAXIS_FILE_UPLOAD_URI, KINAXIS_INSTANCE
from secret import KINAXIS_WS_CREDS

import requests

url = ""


def upload_file(dataSource, fileName, payload):
    url = KINAXIS_FILE_UPLOAD_URI \
            .replace("{instance}", KINAXIS_INSTANCE) \
            .replace("{data_source}", dataSource) \
            .replace("{file}", fileName)
    headers = KINAXIS_WS_CREDS
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)