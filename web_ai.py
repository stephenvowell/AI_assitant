import requests
from bs4 import BeautifulSoup
import spacy
import json

# Initialize spaCy
nlp = spacy.load('en_core_web_sm')

# Function to scrape news
def scrape_news():
    url = 'https://cnn.com/ai-news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.find_all('div', class_='news-item'):
        title = item.find('h2').text
        link = item.find('a')['href']
        articles.append({'title': title, 'link': link})
    
    return articles

# Function to fetch news from NewsAPI
def fetch_news(api_key):
    url = f'https://newsapi.org/v2/everything?q=AI&apiKey=f9f9f63d636e47aba0e9e6f0f98e6fb6'
    response = requests.get(url)
    articles = response.json().get('articles')
    
    return [{'title': article['title'], 'url': article['url']} for article in articles]

# Function to filter relevant articles
def filter_relevant_articles(articles):
    relevant_articles = []
    for article in articles:
        doc = nlp(article['title'])
        if any(token.text.lower() in ['ai', 'artificial intelligence'] for token in doc):
            relevant_articles.append(article)
    
    return relevant_articles

# Function to save data to JSON
def save_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Main function
def main():
    api_key = ''
    
    # Scrape news
    scraped_news = scrape_news()
    
    # Fetch news from API
    fetched_news = fetch_news(api_key)
    
    # Combine news articles
    all_news = scraped_news + fetched_news
    
    # Filter relevant articles
    relevant_articles = filter_relevant_articles(all_news)
    
    # Save to JSON
    save_to_json(relevant_articles)

if __name__ == "__main__":
    main()