import unittest
from unittest.mock import patch, Mock
from src.fetch import api_response

#
class FetchTest(unittest.TestCase):

    # test api returning a 200 response
    @patch('requests.get')
    def test_api_response_200(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'Items': []}
        mock_get.return_value = mock_response

        status, retrieved, items = api_response('http://fake-api', 'good_key', 60)
        self.assertEqual(status, 200)

    # test api returning 401 response
    @patch('requests.get')
    def test_api_response_401(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {'Items': []}
        mock_get.return_value = mock_response

        status, retrieved, items = api_response('http://fake-api', 'bad_key', 60)
        self.assertEqual(status, 401)

    # test function correctly returning valid data, and ability to navigate it
    @patch('requests.get')
    def test_api_returns_items_matching_total_record_count(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Items": [
                {
                    "Id": 0,
                },
                {
                    "Id": 1
                }
            ],
            "TotalRecordCount": 2,
            "StartIndex": 0
        }
        mock_get.return_value = mock_response

        status, retrieved, items = api_response('http://fake-api', 'good_key', 60)
        self.assertEqual(status, 200)
        self.assertEqual(len(items), retrieved['TotalRecordCount'])

    # test function's to retrieve items and store them in a separate list
    @patch('requests.get')
    def test_api_response_items(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'Items': [
            {'Type': 'VideoPlayback'},
            {'Type': 'SessionEnded'}
        ]}
        mock_get.return_value = mock_response

        status, retrieved, items = api_response('http://fake-api', 'good_key', 60)
        self.assertEqual(status, 200)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['Type'], 'VideoPlayback')

