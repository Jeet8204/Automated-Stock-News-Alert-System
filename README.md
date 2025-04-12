📈 Stock News Notifier
A Python script that tracks stock price changes (for Microsoft in this case), and if the change is significant (more than 0.5%), it fetches the latest news related to the company and sends you summaries via SMS using Twilio.

🚀 Features
Fetches daily stock price data using Alpha Vantage API.

Checks for percentage change between yesterday's and the day-before-yesterday’s closing prices.

If the change exceeds 0.5%, it fetches the top 3 news articles using News API.

Sends formatted news summaries via SMS using Twilio API.

📦 Tech Stack
Python

Requests

Alpha Vantage API

News API

Twilio

⚙️ How It Works
Uses Alpha Vantage to get the latest two days’ closing prices of MSFT stock.

Calculates the percentage change.

If the change is > 0.5%, uses NewsAPI to search for recent Microsoft-related news.

Sends the top 3 headlines and descriptions to your phone via Twilio.
