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

        status, items = api_response('http://fake-api', 'good_key', 60)
        self.assertEqual(status, 200)


    @patch('requests.get')
    def test_api_response_401(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {'Items': []}
        mock_get.return_value = mock_response

        status, items = api_response('http://fake-api', 'bad_key', 60)
        self.assertEqual(status, 401)


    @patch('requests.get')
    def test_api_response_data_retrieve(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'Items': [
            {'Type': 'VideoPlayback'},
            {'Type': 'SessionEnded'}
        ]}
        mock_get.return_value = mock_response

        status, items = api_response('http://fake-api', 'good_key', 60)
        self.assertEqual(status, 200)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['Type'], 'VideoPlayback')