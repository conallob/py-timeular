import requests

class TimeularClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.timeular.com/api/v4"
        self.token = self._get_access_token()

    def _get_access_token(self):
        url = f"{self.base_url}/developer/sign-in"
        response = requests.post(url, json={"apiKey": self.api_key, "apiSecret": self.api_secret})
        response.raise_for_status()
        return response.json()["token"]

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_activities(self):
        return self._request("GET", "/activities")

    def create_activity(self, name, color):
        data = {"name": name, "color": color}
        return self._request("POST", "/activities", json=data)

    def get_time_entries(self):
        return self._request("GET", "/time-entries")

    def create_time_entry(self, activity_id, started_at, stopped_at):
        data = {
            "activityId": activity_id,
            "startedAt": started_at,
            "stoppedAt": stopped_at
        }
        return self._request("POST", "/time-entries", json=data)

# Example usage:
# client = TimeularClient(api_key="your_api_key", api_secret="your_api_secret")
# activities = client.get_activities()
# print(activities)