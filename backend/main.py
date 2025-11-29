import json
import os
import datetime
import uuid
from fetcher import fetch_all_news
from processor import process_article

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, '../data/news.json')

def main():
    print("Starting AI News Aggregation...")
    
    # 1. Fetch Raw News
    raw_articles = fetch_all_news()
    print(f"Fetched {len(raw_articles)} raw articles.")
    
    # 2. Process with AI
    processed_items = []
    for article in raw_articles:
        print(f"Processing: {article['title'][:50]}...")
        result = process_article(article)
        
        if result:
            # Filter by relevance
            if result.get('ai_relevance_score', 0) < 0.6:
                print(f"  -> Skipped (Low relevance: {result.get('ai_relevance_score')})")
                continue
                
            # Add ID if not present
            if 'id' not in result:
                result['id'] = str(uuid.uuid4())
            
            # Ensure date format
            if 'date' not in result or not result['date']:
                result['date'] = datetime.date.today().strftime('%Y-%m-%d')
                
            processed_items.append(result)
            print(f"  -> Added: {result['title_ja']}")
        else:
            print("  -> Failed to process")

    # 3. Save to JSON
    data = {
        "generated_at": datetime.datetime.now().isoformat(),
        "items": processed_items
    }
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved {len(processed_items)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
