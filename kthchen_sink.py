import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from flask import Flask, render_template, jsonify
import spacy

# Initialize Flask app
app = Flask(__name__)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to fetch AI news articles
def fetch_google_news(api_key, cse_id, query):
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}'
    response = requests.get(url)
    results = response.json().get('items', [])
    
    articles = []
    for item in results:
        title = item['title']
        link = item['link']
        articles.append({'title': title, 'link': link})
    
    return articles

# Function to scrape article content
def scrape_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([para.text for para in paragraphs])
    return content

# Function to summarize articles
def summarize_articles(articles):
    summarizer = pipeline('summarization')
    summaries = []
    for article in articles:
        content = scrape_article_content(article['link'])
        summary = summarizer(content, max_length=150, min_length=30, do_sample=False)
        summaries.append({'title': article['title'], 'summary': summary[0]['summary_text'], 'link': article['link']})
    return summaries

# Fetch, summarize, and store articles
api_key = 'AIzaSyBpKMEQ7AzU520g5ZxoIefJKvbZF6B6GoU'
cse_id = 'f4c0f38bccfeb401b'
query = 'AI news'

news_articles = fetch_google_news(api_key, cse_id, query)
summarized_articles = summarize_articles(news_articles)

# Flask routes
@app.route('/')
def home():
    return render_template('index.html', articles=summarized_articles)

@app.route('/api/articles', methods=['GET'])
def get_articles():
    return jsonify(summarized_articles)

if __name__ == '__main__':
    app.run(debug=True)