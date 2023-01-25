import argparse

from datetime import datetime
from settings import KINAXIS_DATA_UPDATE_TRIGGER_PAYLOAD, KINAXIS_DSM

# from DataExtractServices.CurrencyXChangeRateService import GetXChangeRate
from KinaxisWebServices.KinaxisWebServices import KinaxisWebService

import sys
import importlib.util


# TODO: implement logs and tests
def UploadDataFiles(triggerUpdate: bool=False):
    ts = datetime.now().strftime("%Y%m%d.%H%M%S")
    kws = KinaxisWebService()
    for ds in KINAXIS_DSM:
        data_source = ds['DataSource']
        integration_scenario = ds['IntegrationScenario']

        for file in ds['files']:
            xtract_svc_name = file['ExtractService']
            file_name = file['Name']
            payload = file['Payload']

            # dynamically import module
            extract_svc_module = import_xtract_svc_module(xtract_svc_name)
            # dynamically create class instance
            extract_svc = eval(f'extract_svc_module.{xtract_svc_name}()')

            data = extract_svc.get_source_data()

            if data is None:
                print("No data returned from service, no file to push up")
                continue

            # add data to payload
            payload['Rows'] = data
            payload['Timestamp'] = ts

            # push to rapid
            kws.upload_data_file(data_source, file_name, payload)
            print(payload)

        if triggerUpdate:
            # trigger data update
            payload = KINAXIS_DATA_UPDATE_TRIGGER_PAYLOAD
            payload['IntegrationScenario'] = integration_scenario
            kws.trigger_data_update(payload)


def import_xtract_svc_module(xtract_svc_name: str):
    file_path = 'DataExtractServices/' + xtract_svc_name + '.py'
    module_name = xtract_svc_name
    
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module


parser = argparse.ArgumentParser(description='Run Eaton File Upload service manually.\n\n/!', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--triggerDataUpdate', default='False', choices=['True', 'False'], help='Indicates if a data update will be triggered after the file upload', required=False)
args = parser.parse_args()

triggerUpdate = (args.triggerDataUpdate == 'True')
UploadDataFiles(triggerUpdate)