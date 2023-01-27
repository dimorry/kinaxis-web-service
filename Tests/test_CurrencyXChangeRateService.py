import unittest
from unittest.mock import patch
from datetime import date, timedelta
from DataExtractServices.DataExtractServiceBase import DataExtractServiceBase
from DataExtractServices.CurrencyXChangeRateService import CurrencyXChangeRateService
from settings import CONVERSION_RATE_QUERY_STRING, CONVERSION_RATE_URI
from secret import CONVERSION_RATE_API_KEY


class CurrencyXChangeRateServiceTests(unittest.TestCase):
    
    def test_baseclass_instance(self):
        service = CurrencyXChangeRateService()
        self.assertIsInstance(service, DataExtractServiceBase)
    
    @patch('requests.request')
    def test_get_source_data(self, mock_request):
        # Set up mock response
        mock_response = {
            "success": True,
            "timestamp": 1672617599,
            "historical": True,
            "base": "USD",
            "date": "2023-01-01",
            "rates": {
                "EUR": 0.934185,
                "GBP": 0.826446,
                "RON": 4.63494
            }
        }
        mock_request.return_value.json.return_value = mock_response

        service = CurrencyXChangeRateService()
        data = service.get_source_data()

        # Assert the response has the correct structure
        self.assertEqual(len(data), 3)
        for item in data:
            self.assertIsInstance(item, dict)
            self.assertEqual(list(item.keys()), ["Values"])
            self.assertEqual(len(item["Values"]), 3)
            self.assertIsInstance(item["Values"][0], str)
            self.assertIsInstance(item["Values"][1], str)
            self.assertIsInstance(item["Values"][2], float)

        # Assert the correct date is used in the request
        yesterday = date.today() + timedelta(days=-1)
        expected_date = yesterday.strftime("%Y-%m-%d")
        mock_request.assert_called_once_with("GET", CONVERSION_RATE_URI + expected_date, data="", headers=CONVERSION_RATE_API_KEY, params=CONVERSION_RATE_QUERY_STRING)

if __name__ == '__main__':
    unittest.main()