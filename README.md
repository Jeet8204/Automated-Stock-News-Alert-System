# 📈 Stock News Notifier

A Python script that tracks **stock price changes** (for Microsoft in this case), and if the change is significant (more than 0.5%), it fetches the latest **news** related to the company and sends you summaries via **SMS** using **Twilio**.

---

## 🚀 Features
- Fetches **daily stock price data** using [Alpha Vantage API](https://www.alphavantage.co/documentation/).
- Checks for **percentage change** between yesterday's and the day-before-yesterday’s closing prices.
- If the change exceeds **0.5%**, it fetches the **top 3 news articles** using [News API](https://newsapi.org/).
- Sends **formatted news summaries via SMS** using [Twilio API](https://www.twilio.com/).

---

## 📦 Tech Stack
- **Python**
- **Requests** (for making HTTP requests)
- [Alpha Vantage API](https://www.alphavantage.co/)
- [News API](https://newsapi.org/)
- [Twilio](https://www.twilio.com/)

---

## ⚙️ How It Works
1. Uses **Alpha Vantage** to get the latest two days’ closing prices of **MSFT** stock.
2. Calculates the **percentage change** between the two days’ closing prices.
3. If the change is greater than **0.5%**, it uses **NewsAPI** to search for recent **Microsoft**-related news.
4. Sends the top **3 headlines and descriptions** to your phone via **Twilio**.
