import pytest
import vcr
from unittest.mock import patch, Mock
from timeular import TimeularClient

class TestTimeularClient:

    @pytest.mark.vcr()
    def test_init_and_get_access_token(self, vcr_cassette_dir: str) -> None:
        with vcr.use_cassette(f'{vcr_cassette_dir}/get_access_token.yaml'):
            client = TimeularClient("fake_api_key", "fake_api_secret")
            assert client.token == "fake_token"

    @pytest.mark.vcr()
    def test_get_activities(self, vcr_cassette_dir: str) -> None:
        with vcr.use_cassette(f'{vcr_cassette_dir}/get_activities.yaml'):
            client = TimeularClient("fake_api_key", "fake_api_secret")
            activities = client.get_activities()
            assert activities == {"activities": []}

    @pytest.mark.vcr()
    def test_create_activity(self, vcr_cassette_dir: str) -> None:
        with vcr.use_cassette(f'{vcr_cassette_dir}/create_activity.yaml'):
            client = TimeularClient("fake_api_key", "fake_api_secret")
            activity = client.create_activity("Test Activity", "#FFFFFF")
            assert activity == {"activity": {"name": "Test Activity", "color": "#FFFFFF"}}

    @pytest.mark.vcr()
    def test_get_time_entries(self, vcr_cassette_dir: str) -> None:
        with vcr.use_cassette(f'{vcr_cassette_dir}/get_time_entries.yaml'):
            client = TimeularClient("fake_api_key", "fake_api_secret")
            time_entries = client.get_time_entries()
            assert time_entries == {"timeEntries": []}

    @pytest.mark.vcr()
    def test_stop_current_activity(self, vcr_cassette_dir: str) -> None:
        with vcr.use_cassette(f'{vcr_cassette_dir}/stop_current_activity.yaml'):
            client = TimeularClient("fake_api_key", "fake_api_secret")
            response = client.stop_current_activity()
            assert response == {"status": "stopped"}

if __name__ == '__main__':
    pytest.main()