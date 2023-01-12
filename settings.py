
CONVERSION_RATE_URI = f"https://api.apilayer.com/exchangerates_data/"
CONVERSION_RATE_QUERY_STRING = {
    "base": "USD",
    "symbols": "EUR,GBP,RON"
}

KINAXIS_INSTANCE = "ETND02_DEV01"
KINAXIS_FILES = [ 
                    { 
                        "DataSource": "load_currencies_ds",
                        "Name": "CurrencyConversionForecast",
                        "Payload": {
                                "Scenario": {
                                    "Name": "load currency data",
                                    "Scope": "Public"
                                },
                                "Columns": ["Currency.Value", "Date", "Rate"],
                                "Rows": None,
                                "Timestamp": None,
                                "OperationType": "Full",
                                "FileFormat": "Tab Delimited (*.tab)",
                                # "FinishExtract": "True"
                        }
                    },
                ]

KINAXIS_FILE_UPLOAD_URI = "https://na3.kinaxis.net/{instance}/integration/V1/dataload/{data_source}/{file}"
