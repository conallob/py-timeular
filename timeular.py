import requests
from typing import Dict, Any
import vcr

class TimeularClient:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.timeular.com/api/v4"
        self.token = self._get_access_token()

    @vcr.use_cassette('cassettes/get_access_token.yaml')
    def _get_access_token(self) -> str:
        url = f"{self.base_url}/developer/sign-in"
        response = requests.post(url, json={"apiKey": self.api_key, "apiSecret": self.api_secret})
        response.raise_for_status()
        return response.json()["token"]

    @vcr.use_cassette('cassettes/request.yaml')
    def _request(self, method: str, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()

    @vcr.use_cassette('cassettes/get_activities.yaml')
    def get_activities(self) -> Dict[str, Any]:
        return self._request("GET", "/activities")

    @vcr.use_cassette('cassettes/create_activity.yaml')
    def create_activity(self, name: str, color: str) -> Dict[str, Any]:
        data = {"name": name, "color": color}
        return self._request("POST", "/activities", json=data)

    @vcr.use_cassette('cassettes/edit_activity.yaml')
    def edit_activity(self, activity_id: str, name: str, color: str) -> Dict[str, Any]:
        data = {"name": name, "color": color}
        return self._request("PATCH", f"/activities/{activity_id}", json=data)

    @vcr.use_cassette('cassettes/archive_activity.yaml')
    def archive_activity(self, activity_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/activities/{activity_id}")

    @vcr.use_cassette('cassettes/get_time_entries.yaml')
    def get_time_entries(self) -> Dict[str, Any]:
        return self._request("GET", "/time-entries")

    @vcr.use_cassette('cassettes/stop_current_activity.yaml')
    def stop_current_activity(self) -> Dict[str, Any]:
        return self._request("DELETE", "/tracking")

    @vcr.use_cassette('cassettes/get_current_tracking.yaml')
    def get_current_tracking(self) -> Dict[str, Any]:
        return self._request("GET", "/tracking")

    @vcr.use_cassette('cassettes/start_tracking.yaml')
    def start_tracking(self, activity_id: str) -> Dict[str, Any]:
        data = {"activityId": activity_id}
        return self._request("POST", "/tracking", json=data)

    @vcr.use_cassette('cassettes/edit_tracking.yaml')
    def edit_tracking(self, tracking_id: str, started_at: str, stopped_at: str) -> Dict[str, Any]:
        data = {"startedAt": started_at, "stoppedAt": stopped_at}
        return self._request("PATCH", f"/tracking/{tracking_id}", json=data)

    @vcr.use_cassette('cassettes/remove_tracking.yaml')
    def remove_tracking(self, tracking_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/tracking/{tracking_id}")

    @vcr.use_cassette('cassettes/cancel_tracking.yaml')
    def cancel_tracking(self) -> Dict[str, Any]:
        return self._request("DELETE", "/tracking")

    @vcr.use_cassette('cassettes/find_time_entry.yaml')
    def find_time_entry(self, time_entry_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/time-entries/{time_entry_id}")

    @vcr.use_cassette('cassettes/create_time_entry.yaml')
    def create_time_entry(self, activity_id: str, started_at: str, stopped_at: str) -> Dict[str, Any]:
        data = {
            "activityId": activity_id,
            "startedAt": started_at,
            "stoppedAt": stopped_at
        }
        return self._request("POST", "/time-entries", json=data)

    @vcr.use_cassette('cassettes/edit_time_entry.yaml')
    def edit_time_entry(self, time_entry_id: str, started_at: str, stopped_at: str) -> Dict[str, Any]:
        data = {
            "startedAt": started_at,
            "stoppedAt": stopped_at
        }
        return self._request("PATCH", f"/time-entries/{time_entry_id}", json=data)

    @vcr.use_cassette('cassettes/delete_time_entry.yaml')
    def delete_time_entry(self, time_entry_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/time-entries/{time_entry_id}")

    @vcr.use_cassette('cassettes/generate_report.yaml')
    def generate_report(self, start_date: str, end_date: str) -> Dict[str, Any]:
        data = {
            "startDate": start_date,
            "endDate": end_date
        }
        return self._request("POST", "/reports/time-entries", json=data)

    @vcr.use_cassette('cassettes/get_tags.yaml')
    def get_tags(self) -> Dict[str, Any]:
        return self._request("GET", "/tags")

    @vcr.use_cassette('cassettes/create_tag.yaml')
    def create_tag(self, label: str) -> Dict[str, Any]:
        data = {"label": label}
        return self._request("POST", "/tags", json=data)

    @vcr.use_cassette('cassettes/edit_tag.yaml')
    def edit_tag(self, tag_id: str, label: str) -> Dict[str, Any]:
        data = {"label": label}
        return self._request("PATCH", f"/tags/{tag_id}", json=data)

    @vcr.use_cassette('cassettes/delete_tag.yaml')
    def delete_tag(self, tag_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/tags/{tag_id}")

    @vcr.use_cassette('cassettes/get_mentions.yaml')
    def get_mentions(self) -> Dict[str, Any]:
        return self._request("GET", "/mentions")

    @vcr.use_cassette('cassettes/create_mention.yaml')
    def create_mention(self, label: str) -> Dict[str, Any]:
        data = {"label": label}
        return self._request("POST", "/mentions", json=data)

    @vcr.use_cassette('cassettes/edit_mention.yaml')
    def edit_mention(self, mention_id: str, label: str) -> Dict[str, Any]:
        data = {"label": label}
        return self._request("PATCH", f"/mentions/{mention_id}", json=data)

    @vcr.use_cassette('cassettes/delete_mention.yaml')
    def delete_mention(self, mention_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/mentions/{mention_id}")