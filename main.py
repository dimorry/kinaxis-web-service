from datetime import datetime
from conversion_rate import GetCurrencyXChangeRate
from settings import KINAXIS_DATA_UPDATE_TRIGGER_PAYLOAD, KINAXIS_DSM
from kinaxis_data_upload import upload_file, trigger_data_update


def UploadDataFiles():
    ts = datetime.now().strftime("%Y%m%d.%H%M%S")
    for ds in KINAXIS_DSM:
        data_source = ds['DataSource']
        integration_scenario = ds['IntegrationScenario']

        for file in ds['files']:
            file_name = file['Name']
            payload = file['Payload']

            if file_name == "CurrencyConversionActual":
                data = GetCurrencyXChangeRate() # call service to get data

            if data is None:
                print("No data returned from service")
                continue

            # add data to payload
            payload['Rows'] = data
            payload['Timestamp'] = ts

            # push to rapid
            upload_file(data_source, file_name, payload)
            print(payload)

        # trigger data update
        payload = KINAXIS_DATA_UPDATE_TRIGGER_PAYLOAD
        payload['IntegrationScenario'] = integration_scenario
        trigger_data_update(payload)

UploadDataFiles()