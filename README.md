# kinaxis-web-service

This app contains a wrapper to Kinaxis' REST web services.
It allows to upload data files based on the DSM configuration and trigger data updates

It allows the implementation new DataExtractionServices and those should be done by implementing the DataExtractServiceBase class and it's 
get_source_data abstract method.

This method needs to return a list with the multiple rows on the following format:
{"Values": [column1_value, column2_value, column3_value,..., columnn_value]}

This list will be plugged in the payload for the data to be uploaded and the file created in Kinaxis' Servers
         
Kinaxis' API documentation can be found here: https://help.kinaxis.com/20162/GlobalHelp/Content/RR_WebService/@PartsIndex/part3.htm