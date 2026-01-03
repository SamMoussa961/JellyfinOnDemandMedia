import unittest
from unittest.mock import patch, Mock
from src.wake_server import ping_host

class TestWakeServer(unittest.TestCase):

    # test for a reachable host
    @patch('subprocess.run')
    def test_ping_server_ping_reachable(self, mock_run):
        mock_response = Mock()
        mock_response.returncode = 0
        mock_run.return_value = mock_response

        value = ping_host('127.0.0.1')
        self.assertTrue(value)

    # test for an unreachable host
    @patch('subprocess.run')
    def test_ping_server_ip_unreachable(self, mock_run):
        mock_response = Mock()
        mock_response.returncode = 1
        mock_run.return_value = mock_response

        value = ping_host('127.0.0.1')
        self.assertFalse(value)

    # test function for an invalid ip address
    @patch('subprocess.run')
    def test_ping_host_invalid_ip(self, mock_run):
        mock_response = Mock()
        mock_response.returncode = 68
        mock_run.return_value = mock_response

        value = ping_host('0.1')
        self.assertFalse(value)
        mock_run.assert_not_called()

    # test it timeouts after set number
    @patch('subprocess.run')
    def test_ping_host_timeout(self, mock_run):
        mock_response = Mock()
        mock_response.returncode = 0
        mock_run.return_value = mock_response

        ping_host('127.0.0.1', timeout=10)

        mock_run.assert_called_once()
        call_args = mock_run.call_args
        self.assertEqual(call_args[1]['timeout'], 10)

