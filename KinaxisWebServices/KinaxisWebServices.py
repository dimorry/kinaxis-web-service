from settings import KINAXIS_FILE_UPLOAD_URI, KINAXIS_INSTANCE, KINAXIS_DATA_UPDATE_TRIGGER_URI
from secret import KINAXIS_WS_CREDS

import requests


# TODO: implement method to upload an extract.done file to allow this service to be used in conjunction with a scheduled data update job

class KinaxisWebService():
    """

     This class is a wrapper to Kinaxis' REST web services.
     It allows to upload data files based on the DSM configuration and trigger data updates

     Kinaxis' API documentation can be found here: https://help.kinaxis.com/20162/GlobalHelp/Content/RR_WebService/@PartsIndex/part3.htm

    """

    def __init__(self, useOAuth=False) -> None:
        self.headers = KINAXIS_WS_CREDS
        self.useOAuth = useOAuth

    def upload_data_file(self, dataSource, fileName, payload):
        url = KINAXIS_FILE_UPLOAD_URI \
            .replace("{instance}", KINAXIS_INSTANCE) \
            .replace("{data_source}", dataSource) \
            .replace("{file}", fileName)

        # TODO: implement paging for over 5M rows
        response = requests.request(
            "POST", url, json=payload, headers=self.headers)

        print(response.text)

    def trigger_data_update(self, payload):
        """
        Trigger a data update.
        This call will load any files in the Extract folder and subfolders, regardless if they have an extract.done file created or not

        Args:
            payload (_type_): _description_
        """
        url = KINAXIS_DATA_UPDATE_TRIGGER_URI \
            .replace("{instance}", KINAXIS_INSTANCE)

        response = requests.request(
            "POST", url, json=payload, headers=self.headers)

        print(response.text)
