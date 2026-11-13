# 🤖 Finance-Bot-TG — Financial Telegram Bot & Analytics Scraper

> **Project Status:** Archived portfolio project (demonstrating external API integration, financial data scraping, and advanced Telegram bot architecture).

## 📌 About the Project
**Finance-Bot-TG** is a comprehensive financial assistant tool built in Python. The application integrates external cryptographic/financial APIs, scrapes currency and market data, and delivers structured financial updates, news, and analytics directly to users via an interactive Telegram interface.

---

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Telegram Bot API:** `aiogram` (asynchronous framework)
* **Data Sources & APIs:** Custom web scrapers (`BeautifulSoup` / `requests`) and external API integrations for crypto and forex markets (`API_site/`, `parser/`)[cite: 2]
* **Architecture:** Asynchronous handlers, custom pagination factories, FSM (Finite State Machine), modular structure[cite: 2]

---

## 📂 Project Architecture
```text
Finance-Bot-TG-main/
│
├── API_site/               # External API integrations (Crypto API handlers)
├── bot/                    # Telegram bot core logic
│   ├── database/           # Database integration layers
│   ├── factory/            # UI components (e.g., custom pagination)
│   ├── handler/            # Command, callback query, and admin handlers
│   ├── keyboard/           # Dynamic inline keyboards
│   └── other/              # FSM states and utilities
│
├── parser/                 # Web scrapers for currency, crypto, and Forex news
├── tool_data/              # Data processing and shared constants
├── app.py                  # Application entry point
└── README.md               # Project documentation
