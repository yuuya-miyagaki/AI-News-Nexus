import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from config import SYSTEM_PROMPT

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def process_article(article):
    """
    Process a single article using Gemini API.
    """
    model = genai.GenerativeModel('gemini-flash-latest')
    
    prompt = f"""
    {SYSTEM_PROMPT}

    Article Input:
    Title: {article['title']}
    Source: {article['source_name']}
    Date: {article['published']}
    Content:
    {article['content'][:8000]} 
    """

    try:
        response = model.generate_content(prompt)
        text = response.text
        
        # Robust JSON extraction using regex
        import re
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            json_str = match.group(0)
            data = json.loads(json_str)
        else:
            # Fallback: try to parse the whole text if no braces found (unlikely but possible)
            data = json.loads(text)
        
        # Add metadata
        data['original_url'] = article['link']
        data['original_date'] = article['published']
        data['source_name'] = article['source_name']
        
        return data
    except Exception as e:
        print(f"Error processing article '{article['title']}': {e}")
        return None

if __name__ == "__main__":
    # Test with dummy data
    dummy_article = {
        'title': 'Test AI Article',
        'source_name': 'Test Source',
        'published': '2025-01-01',
        'content': 'This is a test article about a new AI model called GPT-5. It has 100T parameters and is 10x faster.'
    }
    result = process_article(dummy_article)
    print(json.dumps(result, indent=2, ensure_ascii=False))
