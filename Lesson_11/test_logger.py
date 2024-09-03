# test_logger.py
import unittest
from unittest.mock import patch
import logging
from logger import log_event


class TestLogEvent(unittest.TestCase):

    @patch('logger.logging.getLogger')
    def test_log_event_success(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        mock_logger.info = unittest.mock.MagicMock()

        log_event('user1', 'success')

        mock_logger.info.assert_called_once_with('Login event - Username: user1, Status: success')

    @patch('logger.logging.getLogger')
    def test_log_event_expired(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        mock_logger.warning = unittest.mock.MagicMock()

        log_event('user2', 'expired')

        mock_logger.warning.assert_called_once_with('Login event - Username: user2, Status: expired')

    @patch('logger.logging.getLogger')
    def test_log_event_failed(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        mock_logger.error = unittest.mock.MagicMock()

        log_event('user3', 'failed')

        mock_logger.error.assert_called_once_with('Login event - Username: user3, Status: failed')


if __name__ == '__main__':
    unittest.main()
