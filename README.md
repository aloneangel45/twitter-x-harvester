# 🐦 Twitter (X) Data Harvester & Guest Token SDK

> **Official Open Source Client for Twitter (X) Public GraphQL & Dynamic Guest Token Ingestion**  
> Provided by **Aether Protocol Labs** • Available on RapidAPI Hub

![GitHub Workflow Status](https://img.shields.io/badge/tests-passing-brightgreen)
![Supported Languages](https://img.shields.io/badge/languages-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚡ Why Use This?
Official Twitter (X) API v2 pricing starts at **\$100/month** for minimal read access.  
This SDK utilizes dynamic `x-guest-token` generation to ingest public profiles, user timelines, and search results at high speeds for a fraction of the cost.

---

## 🔑 Free RapidAPI Key
Get 50 free requests per month on RapidAPI:  
👉 **[Get Free Key on RapidAPI Hub](https://rapidapi.com/organization/aether-protocol-labs)**

---

## 💻 Quickstart (Python)
```python
from twitter_harvester.client import TwitterHarvester

harvester = TwitterHarvester(api_key="YOUR_RAPIDAPI_KEY")

# 1. Generate fresh guest token
token = harvester.get_guest_token()
print("Guest Token:", token["guest_token"])

# 2. Fetch public user profile
profile = harvester.get_user_profile("elonmusk")
print(profile)
```
