import unittest
from unittest.mock import patch, Mock
from timeular import TimeularClient
from typing import Any

class TestTimeularClient(unittest.TestCase):

    def setUp(self) -> None:
        self.client = TimeularClient("fake_api_key", "fake_api_secret")

    @patch('timeular.requests.post')
    def test_init_and_get_access_token(self, mock_post: Any) -> None:
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
    def test_get_activities(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"activities": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        activities = self.client.get_activities()
        self.assertEqual(activities, {"activities": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/activities",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_create_activity(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"activity": {"name": "Test Activity", "color": "#FFFFFF"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        activity = self.client.create_activity("Test Activity", "#FFFFFF")
        self.assertEqual(activity, {"activity": {"name": "Test Activity", "color": "#FFFFFF"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/activities",
            headers={"Authorization": "Bearer fake_token"},
            json={"name": "Test Activity", "color": "#FFFFFF"}
        )

    @patch('timeular.requests.request')
    def test_edit_activity(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"activity": {"name": "Updated Activity", "color": "#000000"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        activity = self.client.edit_activity("activity_id", "Updated Activity", "#000000")
        self.assertEqual(activity, {"activity": {"name": "Updated Activity", "color": "#000000"}})
        mock_request.assert_called_once_with(
            "PATCH",
            "https://api.timeular.com/api/v4/activities/activity_id",
            headers={"Authorization": "Bearer fake_token"},
            json={"name": "Updated Activity", "color": "#000000"}
        )

    @patch('timeular.requests.request')
    def test_archive_activity(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.archive_activity("activity_id")
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/activities/activity_id",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_get_time_entries(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"timeEntries": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        time_entries = self.client.get_time_entries()
        self.assertEqual(time_entries, {"timeEntries": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/time-entries",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_stop_current_activity(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.stop_current_activity()
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/tracking",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_get_current_tracking(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"currentTracking": {}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        current_tracking = self.client.get_current_tracking()
        self.assertEqual(current_tracking, {"currentTracking": {}})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/tracking",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_start_tracking(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"tracking": {"activityId": "activity_id"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        tracking = self.client.start_tracking("activity_id")
        self.assertEqual(tracking, {"tracking": {"activityId": "activity_id"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/tracking",
            headers={"Authorization": "Bearer fake_token"},
            json={"activityId": "activity_id"}
        )

    @patch('timeular.requests.request')
    def test_edit_tracking(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"tracking": {"startedAt": "start_time", "stoppedAt": "stop_time"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        tracking = self.client.edit_tracking("tracking_id", "start_time", "stop_time")
        self.assertEqual(tracking, {"tracking": {"startedAt": "start_time", "stoppedAt": "stop_time"}})
        mock_request.assert_called_once_with(
            "PATCH",
            "https://api.timeular.com/api/v4/tracking/tracking_id",
            headers={"Authorization": "Bearer fake_token"},
            json={"startedAt": "start_time", "stoppedAt": "stop_time"}
        )

    @patch('timeular.requests.request')
    def test_remove_tracking(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.remove_tracking("tracking_id")
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/tracking/tracking_id",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_cancel_tracking(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.cancel_tracking()
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/tracking",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_find_time_entry(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"timeEntry": {"id": "time_entry_id"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        time_entry = self.client.find_time_entry("time_entry_id")
        self.assertEqual(time_entry, {"timeEntry": {"id": "time_entry_id"}})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/time-entries/time_entry_id",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_create_time_entry(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"timeEntry": {"activityId": "activity_id", "startedAt": "start_time", "stoppedAt": "stop_time"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        time_entry = self.client.create_time_entry("activity_id", "start_time", "stop_time")
        self.assertEqual(time_entry, {"timeEntry": {"activityId": "activity_id", "startedAt": "start_time", "stoppedAt": "stop_time"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/time-entries",
            headers={"Authorization": "Bearer fake_token"},
            json={"activityId": "activity_id", "startedAt": "start_time", "stoppedAt": "stop_time"}
        )

    @patch('timeular.requests.request')
    def test_edit_time_entry(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"timeEntry": {"startedAt": "start_time", "stoppedAt": "stop_time"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        time_entry = self.client.edit_time_entry("time_entry_id", "start_time", "stop_time")
        self.assertEqual(time_entry, {"timeEntry": {"startedAt": "start_time", "stoppedAt": "stop_time"}})
        mock_request.assert_called_once_with(
            "PATCH",
            "https://api.timeular.com/api/v4/time-entries/time_entry_id",
            headers={"Authorization": "Bearer fake_token"},
            json={"startedAt": "start_time", "stoppedAt": "stop_time"}
        )

    @patch('timeular.requests.request')
    def test_delete_time_entry(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.delete_time_entry("time_entry_id")
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/time-entries/time_entry_id",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_generate_report(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"report": {}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        report = self.client.generate_report("2023-01-01", "2023-01-31")
        self.assertEqual(report, {"report": {}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/reports/time-entries",
            headers={"Authorization": "Bearer fake_token"},
            json={"startDate": "2023-01-01", "endDate": "2023-01-31"}
        )

    @patch('timeular.requests.request')
    def test_get_tags(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"tags": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        tags = self.client.get_tags()
        self.assertEqual(tags, {"tags": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/tags",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_create_tag(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"tag": {"label": "Test Tag"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        tag = self.client.create_tag("Test Tag")
        self.assertEqual(tag, {"tag": {"label": "Test Tag"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/tags",
            headers={"Authorization": "Bearer fake_token"},
            json={"label": "Test Tag"}
        )

    @patch('timeular.requests.request')
    def test_edit_tag(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"tag": {"label": "Updated Tag"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        tag = self.client.edit_tag("tag_id", "Updated Tag")
        self.assertEqual(tag, {"tag": {"label": "Updated Tag"}})
        mock_request.assert_called_once_with(
            "PATCH",
            "https://api.timeular.com/api/v4/tags/tag_id",
            headers={"Authorization": "Bearer fake_token"},
            json={"label": "Updated Tag"}
        )

    @patch('timeular.requests.request')
    def test_delete_tag(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.delete_tag("tag_id")
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/tags/tag_id",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_get_mentions(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"mentions": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        mentions = self.client.get_mentions()
        self.assertEqual(mentions, {"mentions": []})
        mock_request.assert_called_once_with(
            "GET",
            "https://api.timeular.com/api/v4/mentions",
            headers={"Authorization": "Bearer fake_token"}
        )

    @patch('timeular.requests.request')
    def test_create_mention(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"mention": {"label": "Test Mention"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        mention = self.client.create_mention("Test Mention")
        self.assertEqual(mention, {"mention": {"label": "Test Mention"}})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.timeular.com/api/v4/mentions",
            headers={"Authorization": "Bearer fake_token"},
            json={"label": "Test Mention"}
        )

    @patch('timeular.requests.request')
    def test_edit_mention(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {"mention": {"label": "Updated Mention"}}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        mention = self.client.edit_mention("mention_id", "Updated Mention")
        self.assertEqual(mention, {"mention": {"label": "Updated Mention"}})
        mock_request.assert_called_once_with(
            "PATCH",
            "https://api.timeular.com/api/v4/mentions/mention_id",
            headers={"Authorization": "Bearer fake_token"},
            json={"label": "Updated Mention"}
        )

    @patch('timeular.requests.request')
    def test_delete_mention(self, mock_request: Any) -> None:
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = self.client.delete_mention("mention_id")
        self.assertEqual(response, {})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.timeular.com/api/v4/mentions/mention_id",
            headers={"Authorization": "Bearer fake_token"}
        )

if __name__ == '__main__':
    unittest.main()