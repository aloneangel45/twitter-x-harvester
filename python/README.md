# 🐦 Twitter (X) Data Harvester Python SDK

Bypass Twitter's $100/mo API paywall with dynamic `x-guest-token` generation and public GraphQL data extraction.

```python
from twitter_harvester.client import TwitterHarvester

harvester = TwitterHarvester(api_key="YOUR_RAPIDAPI_KEY")
token = harvester.get_guest_token()
print("Guest Token:", token["guest_token"])
```
