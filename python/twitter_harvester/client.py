import httpx
from typing import Dict, Any

class TwitterHarvester:
    """
    Harvester for Twitter (X) public user profiles, search, and dynamic guest tokens.
    """
    def __init__(
        self,
        api_key: str,
        host: str = "twitter-x-data-harvester-guest-token-api.p.rapidapi.com"
    ):
        self.api_key = api_key
        self.host = host
        self.base_url = f"https://{self.host}/api/v1/twitter"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.host,
            "Content-Type": "application/json"
        }

    def get_guest_token(self) -> Dict[str, Any]:
        """Generate a valid Twitter x-guest-token."""
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(f"{self.base_url}/guest-token", headers=self.headers)
            resp.raise_for_status()
            return resp.json()

    def get_user_profile(self, screen_name: str) -> Dict[str, Any]:
        """Fetch user profile metadata (followers, bio, verified status)."""
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{self.base_url}/user-profile",
                headers=self.headers,
                json={"screen_name": screen_name}
            )
            resp.raise_for_status()
            return resp.json()
