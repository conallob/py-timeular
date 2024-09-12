import requests
from typing import Dict, Any

class TimeularClient:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.timeular.com/api/v4"
        self.token = self._get_access_token()

    def _get_access_token(self) -> str:
        url = f"{self.base_url}/developer/sign-in"
        response = requests.post(url, json={"apiKey": self.api_key, "apiSecret": self.api_secret})
        response.raise_for_status()
        return response.json()["token"]

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_activities(self) -> Dict[str, Any]:
        return self._request("GET", "/activities")

    def create_activity(self, name: str, color: str) -> Dict[str, Any]:
        data = {"name": name, "color": color}
        return self._request("POST", "/activities", json=data)

    def get_time_entries(self) -> Dict[str, Any]:
        return self._request("GET", "/time-entries")

    def stop_current_activity(self) -> Dict[str, Any]:
        return self._request("DELETE", "/tracking")