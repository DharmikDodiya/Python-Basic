# import requests

# # Prompt user for dynamic input
# search_term = input("Enter search term (e.g. bitcoin): ")
# from_date = input("Enter start date (YYYY-MM-DD): ")
# to_date = input("Enter end date (YYYY-MM-DD): ")
# language = input("Enter language (e.g. en, hi): ")
# sort_by = input("Enter sort type (relevancy, popularity, publishedAt): ")
# page_size = input("Enter number of articles to fetch (1–100): ")

# # API endpoint and key
# url = "https://newsapi.org/v2/everything"
# api_key = "037bf8b8a30e426ab689192ddea30b1b"

# # Build query params
# params = {
#     "q": search_term,
#     "from": from_date,
#     "to": to_date,
#     "language": language,
#     "sortBy": sort_by,
#     "pageSize": int(page_size),
#     "page": 1,
#     "apiKey": api_key
# }

# # Make the API call
# response = requests.get(url, params=params)

# # Handle response
# if response.status_code == 200:
#     data = response.json()
#     articles = data.get("articles", [])
#     print(f"{articles}")
#     print(f"\n🔎 Total articles found: {data.get('totalResults', 0)}\n")

#     # for i, article in enumerate(articles, start=1):
#     #     print(f"📰 Article {i}:")
#     #     print(f"  Title      : {article['title']}")
#     #     print(f"  Author     : {article.get('author', 'Unknown')}")
#     #     print(f"  Source     : {article['source']['name']}")
#     #     print(f"  Published  : {article['publishedAt']}")
#     #     print(f"  URL        : {article['url']}")
#     #     print(f"  Description: {article.get('description', 'No description')}\n")
# else:
#     print(f"❌ Error: {response.status_code}")
#     print(response.text)


# import requests
# from datetime import datetime, timedelta

# # NewsAPI details
# url = "https://newsapi.org/v2/everything"
# api_key = "037bf8b8a30e426ab689192ddea30b1b"

# # Max days allowed for free plan
# max_days = 30
# today = datetime.now()
# min_allowed_date = today - timedelta(days=max_days)

# # Get user input
# search_term = input("Enter search term (e.g. bitcoin): ")
# from_date_input = input(f"Enter start date (YYYY-MM-DD) [After {min_allowed_date.strftime('%Y-%m-%d')}]: ")
# to_date_input = input(f"Enter end date (YYYY-MM-DD) [Up to {today.strftime('%Y-%m-%d')}]: ")
# language = input("Enter language (e.g. en, hi): ")
# sort_by = input("Enter sort type (relevancy, popularity, publishedAt): ")
# page_size = input("Enter number of articles to fetch (1–100): ")

# # Validate date input
# try:
#     from_date = datetime.strptime(from_date_input, "%Y-%m-%d")
#     to_date = datetime.strptime(to_date_input, "%Y-%m-%d")
    
#     if from_date < min_allowed_date:
#         print(f"❌ Your start date is too far in the past. Try {min_allowed_date.strftime('%Y-%m-%d')} or later.")
#     elif to_date > today:
#         print("❌ Your end date is in the future. Use today's date or earlier.")
#     elif from_date > to_date:
#         print("❌ Start date must be before end date.")
#     else:
#         params = {
#             "q": search_term,
#             "from": from_date_input,
#             "to": to_date_input,
#             "language": language,
#             "sortBy": sort_by,
#             "pageSize": int(page_size),
#             "page": 1,
#             "apiKey": api_key
#         }

#         # Request
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             articles = data.get("articles", [])

#             print(f"\n🔎 Found {data.get('totalResults', 0)} articles\n")

#             for i, article in enumerate(articles, start=1):
#                 print(f"📰 Article {i}:")
#                 print(f"  Title      : {article['title']}")
#                 print(f"  Author     : {article.get('author', 'Unknown')}")
#                 print(f"  Source     : {article['source']['name']}")
#                 print(f"  Published  : {article['publishedAt']}")
#                 print(f"  URL        : {article['url']}")
#                 print(f"  Description: {article.get('description', 'No description')}\n")
#         else:
#             print(f"❌ API Error {response.status_code}:")
#             print(response.text)

# except ValueError:
#     print("❌ Invalid date format. Please use YYYY-MM-DD.")



# With Text to Speech
import requests
import pyttsx3
from datetime import datetime, timedelta

# Init text-to-speech engine
engine = pyttsx3.init()

# Use system's default voice (Windows uses SAPI5)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # Adjust rate as needed

# --- NewsAPI Setup ---
url = "https://newsapi.org/v2/everything"
api_key = "037bf8b8a30e426ab689192ddea30b1b"
max_days = 30
today = datetime.now()
min_allowed_date = today - timedelta(days=max_days)

# --- Input from user ---
search_term = input("🔍 Enter search term (e.g. bitcoin): ")
from_date_input = input(f"📅 Start date [After {min_allowed_date.strftime('%Y-%m-%d')}]: ")
to_date_input = input(f"📅 End date [Up to {today.strftime('%Y-%m-%d')}]: ")
language = input("🌐 Language (en, hi, etc.): ")
sort_by = input("🔃 Sort by (relevancy, popularity, publishedAt): ")
page_size = input("📄 Number of articles (1–100): ")

# --- Validate and Fetch News ---
try:
    from_date = datetime.strptime(from_date_input, "%Y-%m-%d")
    to_date = datetime.strptime(to_date_input, "%Y-%m-%d")

    if from_date < min_allowed_date or to_date > today or from_date > to_date:
        print("❌ Invalid date range.")
    else:
        params = {
            "q": search_term,
            "from": from_date_input,
            "to": to_date_input,
            "language": language,
            "sortBy": sort_by,
            "pageSize": int(page_size),
            "page": 1,
            "apiKey": api_key
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            print(f"\n🔎 Found {len(articles)} articles\n")

            for i, article in enumerate(articles, start=1):
                title = article['title']
                message = f"Article {i}: {title}"
                engine.say(message)
                print(message)
                engine.runAndWait()

        else:
            print(f"❌ API Error {response.status_code}")
            print(response.text)

except ValueError:
    print("❌ Invalid date format. Use YYYY-MM-DD")

