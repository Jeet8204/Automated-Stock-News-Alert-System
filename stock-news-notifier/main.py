STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft"

import requests
from twilio.rest import Client
account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO AUTH TOCKEN"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "STOCK_API_KEY"
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "NEWS_API_KEY"
news_parameters = {
    "apiKey":NEWS_API_KEY,
    "qInTitle":COMPANY_NAME,
}
## Use https://www.alphavantage.co/documentation/#daily
"""When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News")."""
response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
#TODO: Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response.raise_for_status()
stock_data = response.json()
# print(stock_data)
stock_price_data = stock_data['Time Series (Daily)']
# print(stock_price_data)
data_list = [value for (key,value) in stock_price_data.items()]
# print(data_list)
yesterday_data_close_price = data_list[0]["4. close"]
print(yesterday_data_close_price)
#TODO: Get the day before yesterday's closing stock price
day_before_yesterday_close_price = data_list[1]["4. close"]
print(day_before_yesterday_close_price)
#TODO: Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = float(yesterday_data_close_price) - float(day_before_yesterday_close_price)
abs_diff = abs(diff)
emoji = None
if diff > 0:
    emoji = "🔺"
elif diff < 0:
    emoji = "🔻"


#TODO: Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = ((abs_diff)/float(yesterday_data_close_price))*100
print(percent_diff)


#TODO: Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percent_diff > 0.005:
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    articles = news_response.json()["articles"]


#TODO: Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    # print(three_articles)

#TODO: Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"\n{COMPANY_NAME}:{emoji}{abs(percent_diff)}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

#TODO: Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12512998318',
            to='+919334720389'
        )



#TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

