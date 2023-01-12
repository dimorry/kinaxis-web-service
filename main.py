from datetime import date, datetime, timedelta
from conversion_rate import GetCurrencyXChangeRate
from settings import KINAXIS_FILE_UPLOAD_URI, KINAXIS_FILES
from kinaxis_data_upload import upload_file


def UploadDataFiles():
    yesterday = date.today() + timedelta(days= -1)
    ts = datetime.now().strftime("%Y%m%d.%H%M%S")
    for file in KINAXIS_FILES:
        file_name = file['Name']
        if file_name == "CurrencyConversionForecast":
            data_source = file['DataSource']
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

UploadDataFiles()