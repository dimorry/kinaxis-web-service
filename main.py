from datetime import date, datetime, timedelta
from conversion_rate import GetCurrencyXChangeRate
from settings import KINAXIS_DATA_UPDATE_TRIGGER_PAYLOAD, KINAXIS_DSM
from kinaxis_data_upload import upload_file, trigger_data_update


def UploadDataFiles():
    yesterday = date.today() + timedelta(days= -1)
    ts = datetime.now().strftime("%Y%m%d.%H%M%S")
    for ds in KINAXIS_DSM:
        data_source = ds['DataSource']
        integration_scenario = ds['IntegrationScenario']
        
        for file in ds['files']:
            file_name = file['Name']
            if file_name == "CurrencyConversionForecast":
                payload = file['Payload']
                
                # call service to get data
                data = GetCurrencyXChangeRate(yesterday)
                
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