# Instagram Highlights Scraper Downloader

> This tool pulls detailed Instagram story highlight data from public profiles. It helps anyone who needs structured insights from highlight collections without manual digging. The scraper focuses on clean extraction, accuracy, and consistent results for analysis or reporting.

> If you work with Instagram highlights often, this gives you a dependable way to gather complete media and metadata in one place.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Highlights Scraper Downloader</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project collects story highlights from public Instagram profiles and provides structured JSON output. It solves the problem of manually fetching highlight media and metadata, especially for teams that track content patterns, monitor brand activity, or evaluate influencers. Researchers, marketers, analysts, and automation builders can all use it to streamline their workflows.

### Why Highlights Matter

- Reveals long-term storytelling themes that profiles keep pinned.
- Helps compare content styles across profiles.
- Useful for repetitive monitoring at scale.
- Supports influencer evaluation with media-level insights.
- Helps track brand communication strategies.

## Features

| Feature | Description |
|--------|-------------|
| Profile-based highlight extraction | Pull highlights from any public Instagram username or profile link. |
| Media URL collection | Captures direct links to photo or video media. |
| Metadata enrichment | Includes highlight IDs, titles, timestamps, and media type. |
| Thumbnail retrieval | Provides thumbnail URLs for each piece of media. |
| Structured JSON output | Easy to export, store, or integrate with automation tools. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| username | Instagram handle of the scraped profile. |
| id | Unique identifier of the Instagram profile. |
| highlightId | Unique ID for a highlight collection. |
| highlightTitle | Title assigned to the highlight folder. |
| media | Direct URL to the highlight photo or video. |
| mediaType | Indicates whether the media is a photo or video. |
| timestamp | Unix timestamp of when the highlight was created. |
| thumbnail | URL pointing to the highlight’s thumbnail image. |

---

## Example Output


    {
      "username": "findajourney",
      "id": "36030724332",
      "highlightId": "18006150200295066",
      "highlightTitle": "South UK",
      "media": "https://instagram.examplecdn.net/sample.jpg",
      "mediaType": "photo",
      "mentions": [],
      "timestamp": 1716460322,
      "thumbnail": "https://fetcher.examplecdn.net/fetcher?file=sample.jpg"
    }

---

## Directory Structure Tree


    Instagram Highlights Scraper Downloader/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── instagram_parser.py
    │   │   └── utils_time.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Marketing teams** use it to track how brands evolve their highlight storytelling, helping them refine their own content strategies.
- **Influencer agencies** use it to gather consistent highlight data, so they can evaluate content style and engagement factors.
- **Analysts** use it to monitor competitor highlights and spot changes or new campaigns quickly.
- **Researchers** use it to build datasets of visual content patterns for social media studies.
- **Automation builders** use it to feed structured highlight data into dashboards, alerts, or scheduled reporting systems.

---

## FAQs

**Do I need login credentials to run this scraper?**
No. It works with publicly accessible Instagram profiles and does not require authentication.

**Can it download videos as files?**
The scraper returns direct media URLs. You can download them externally if needed.

**What if a profile has hundreds of highlights?**
The scraper handles large highlight collections and processes them sequentially to maintain stability.

**Does it work on private profiles?**
No. Only public profiles are supported because their data is accessible without authentication.

---

## Performance Benchmarks and Results

**Primary Metric:**
Processes highlight metadata in under a second per item on average, depending on network conditions.

**Reliability Metric:**
Maintains a consistent success rate across repeated runs, handling profiles with large highlight collections without interruption.

**Efficiency Metric:**
Optimized request handling reduces unnecessary calls and minimizes overall runtime.

**Quality Metric:**
Extracted media and metadata consistently match the actual highlight content, providing high completeness and dependable accuracy.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
