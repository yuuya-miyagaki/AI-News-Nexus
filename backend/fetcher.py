import feedparser
import requests
from bs4 import BeautifulSoup
import time
from config import SOURCES

def fetch_rss(url):
    """Fetch and parse RSS feed"""
    try:
        feed = feedparser.parse(url)
        items = []
        for entry in feed.entries[:5]:  # Limit to 5 latest items
            items.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.get('published', entry.get('updated', '')),
                'summary': entry.get('summary', entry.get('description', '')),
                'content': '' # Will be populated by scraping the link if needed
            })
        return items
    except Exception as e:
        print(f"Error fetching RSS {url}: {e}")
        return []

def fetch_content(url):
    """Fetch article body text from URL"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Simple heuristic to find main content
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
            
        text = soup.get_text(separator='\n')
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:10000] # Limit content length for API
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return ""

def fetch_all_news():
    """Fetch news from all configured sources"""
    all_news = []
    
    for source in SOURCES:
        print(f"Fetching from {source['name']}...")
        items = []
        
        if source['type'] == 'rss':
            items = fetch_rss(source['url'])
        elif source['type'] == 'scrape':
            # Basic scraping logic for list pages (Simplified for now)
            # In a real scenario, this would need specific selectors per site
            # For now, we skip complex scraping and rely on RSS or simple link extraction if implemented
            print(f"Scraping not fully implemented for {source['name']}, skipping...")
            continue
            
        # Enrich items with full content
        for item in items:
            print(f"  - Processing: {item['title'][:30]}...")
            content = fetch_content(item['link'])
            if content:
                item['content'] = content
                item['source_name'] = source['name']
                all_news.append(item)
            time.sleep(1) # Be polite
            
    return all_news

if __name__ == "__main__":
    news = fetch_all_news()
    print(f"Fetched {len(news)} items.")
