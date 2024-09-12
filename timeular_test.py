# test_timeular.py
import unittest
from unittest.mock import patch, Mock
from timeular import TimeularClient

class TestTimeularClient(unittest.TestCase):

    @patch('timeular.requests.post')
    def test_init_and_get_access_token(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"token": "fake_token"}
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = TimeularClient("fake_api_key", "fake_api_secret")
        self.assertEqual(client.token, "fake_token")
        mock_post.assert_called_once_with(
            "https://api.timeular.com/api/v4/developer/sign-in",
            json={"apiKey": "fake_api_key", "apiSecret": "fake_api_secret"}
        )

    @patch('timeular.requests.request')
    def test_get_activities(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = {"activities": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        client = TimeularClient("fake_api_key", "fake_api_secret")
        activities = client.get_activities()
        self.assertEqual(activities, {"activities": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/activities",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_create_activity(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = {"activity": {"name": "Test Activity", "color": "#FFFFFF"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        client = TimeularClient("fake_api_key", "fake_api_secret")
        activity = client.create_activity("Test Activity", "#FFFFFF")
        self.assertEqual(activity, {"activity": {"name": "Test Activity", "color": "#FFFFFF"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/activities",
            headers={"Authorization": "Bearer fake_token"},
            json={"name": "Test Activity", "color": "#FFFFFF"}
        )

    @patch('timeular.requests.request')
    def test_get_time_entries(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = {"timeEntries": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        client = TimeularClient("fake_api_key", "fake_api_secret")
        time_entries = client.get_time_entries()
        self.assertEqual(time_entries, {"timeEntries": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/time-entries",
            headers={"Authorization": "Bearer fake_token"}
        )

if __name__ == '__main__':
    unittest.main()