# 🐦 Twitter (X) Data Harvester & Guest Token API SDK

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Active%20Listing-blue.svg?logo=rapidapi)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitter-x-data-harvester-guest-token-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-Sub--40ms-brightgreen.svg)]()
[![Free Tier](https://img.shields.io/badge/Free%20Plan-50%20Calls%2Fmo-green.svg)]()

> **High-speed Twitter (X) Public Data Harvester and Dynamic Guest Token (`x-guest-token`) Generator. Ingest public user profiles, timelines, search queries, and tweets without requiring expensive official API subscriptions or user login credentials.**

---

## 🚀 Instant Free Access (50 Free Calls/Month)

Subscribe and get your live API key in 5 seconds:  
👉 **[Subscribe on RapidAPI Hub (Free Plan Available)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitter-x-data-harvester-guest-token-api)**

- **RapidAPI Host:** `twitter-x-data-harvester-guest-token-api.p.rapidapi.com`
- **Base Gateway:** `https://twitter-x-data-harvester-guest-token-api.p.rapidapi.com`

---

## ⚡ Why Use Twitter (X) Guest Harvester?

* **Zero Login Friction:** No rotating cookies or account ban risks.
* **Cost Efficiency:** Official Twitter API v2 starts at **\$100 to \$5,000/month** for restricted read quotas.
* **Instant Guest Tokens:** Valid, pre-activated `x-guest-token` issued in `<30ms`.
* **Clean GraphQL Ingestion:** Direct proxy to public user profiles, tweets, and media links.

---

## 💻 Quickstart Examples

### 1. cURL (Instant Terminal Test)
```bash
curl --request POST \
  --url https://twitter-x-data-harvester-guest-token-api.p.rapidapi.com/api/v1/twitter/guest-token \
  --header 'x-rapidapi-host: twitter-x-data-harvester-guest-token-api.p.rapidapi.com' \
  --header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### 2. Python (`requests`)
```python
import requests

API_KEY = "YOUR_RAPIDAPI_KEY"

# Step 1: Generate dynamic guest token
url = "https://twitter-x-data-harvester-guest-token-api.p.rapidapi.com/api/v1/twitter/guest-token"
headers = {
    "x-rapidapi-host": "twitter-x-data-harvester-guest-token-api.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

token_resp = requests.post(url, headers=headers).json()
print("Issued Guest Token:", token_resp.get("guest_token"))

# Step 2: Fetch public user profile
profile_url = f"https://twitter-x-data-harvester-guest-token-api.p.rapidapi.com/api/v1/twitter/profile/elonmusk"
profile_resp = requests.get(profile_url, headers=headers).json()
print("Twitter User Data:", profile_resp)
```

### 3. Node.js / TypeScript (`axios`)
```typescript
import axios from "axios";

async function harvestTwitterUser(screenName: string) {
  const headers = {
    "x-rapidapi-host": "twitter-x-data-harvester-guest-token-api.p.rapidapi.com",
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY"
  };

  const profile = await axios.get(
    `https://twitter-x-data-harvester-guest-token-api.p.rapidapi.com/api/v1/twitter/profile/${screenName}`,
    { headers }
  );

  console.log("X Profile Data:", profile.data);
}

harvestTwitterUser("elonmusk");
```

---

## 🎯 Endpoints Available

1. `POST /api/v1/twitter/guest-token` — Dynamically generate an authenticated guest session token for Twitter GraphQL.
2. `GET /api/v1/twitter/profile/{username}` — Retrieve full user profile metadata, bio, follower count, verified badge, and avatar URLs.
3. `GET /api/v1/twitter/user-tweets/{username}` — Retrieve recent public tweets and media attachments.

---

## 🔍 SEO & Use Cases
- **Social Media Monitoring:** Brand mentions, sentiment tracking, and competitor intelligence.
- **AI / LLM Fine-Tuning Datasets:** Ingest public tweets without paying \$100/mo.
- **Crypto & Web3 Tracking:** Monitor influencer updates and breaking market signals.

---

## 📄 License
MIT © [Aether Protocol Labs](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default)
