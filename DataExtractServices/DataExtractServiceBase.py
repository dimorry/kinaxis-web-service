from abc import ABC, abstractmethod

# abstract class
class DataExtractServiceBase(ABC):

    @abstractmethod
    def get_source_data(*args) -> list:
        """Load data from source service
        
        The class implementing this abstract class must have the same name as defined in:  DSM settings -> files -> ExtractService

        https://help.kinaxis.com/20162/GlobalHelp/Content/RR_WebService/External/datauploadrest_upload.htm

        As per Kinaxis docs, the data needs to be in a list with on the following format for each row:

        {"Values": [column1_value, column2_value, column3_value,..., columnn_value]}
        
        """
