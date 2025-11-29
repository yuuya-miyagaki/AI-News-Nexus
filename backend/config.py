import os

# Data Sources
# Format: {'name': 'Source Name', 'url': 'URL', 'type': 'rss' or 'scrape'}
SOURCES = [
    # Japanese Tech Media
    {
        'name': 'ITmedia AI+',
        'url': 'https://rss.itmedia.co.jp/rss/2.0/aiplus.xml',
        'type': 'rss'
    },
    {
        'name': 'Ledge.ai',
        'url': 'https://ledge.ai/feed',
        'type': 'rss'
    },
    # Global Tech Giants (Official Blogs)
    {
        'name': 'Google AI Blog',
        'url': 'http://googleaiblog.blogspot.com/atom.xml',
        'type': 'rss'
    },
    # Note: Some official blogs might not have easy RSS, using known feeds or main pages
    {
        'name': 'OpenAI Blog',
        'url': 'https://openai.com/news', 
        'type': 'scrape',
        'selector': 'a.ui-link-group' # Hypothetical selector, will need adjustment or use a generic scraper
    },
    {
        'name': 'Anthropic News',
        'url': 'https://www.anthropic.com/news',
        'type': 'scrape',
        'selector': 'a' 
    },
    # Policy
    {
        'name': 'OECD.AI',
        'url': 'https://oecd.ai/en/news',
        'type': 'scrape',
        'selector': 'article'
    }
]

# Gemini System Prompt
SYSTEM_PROMPT = """
You are an expert AI News Analyst. Your task is to analyze a raw news article and extract structured intelligence.

Input:
- Title
- Content (Text)
- Source Name
- Date

Output:
Return a JSON object with the following schema. Do NOT use Markdown code blocks. Just the raw JSON.

{
  "title_ja": "Japanese Title (30-60 chars, catchy but accurate)",
  "summary_short_ja": "Short summary in Japanese (80-120 chars) for the card view.",
  "summary_long_ja": "Detailed explanation in Japanese (HTML format, <p> tags). 500-1000 chars. Break down the 'What', 'Why', 'How', and 'Impact'.",
  "category": "One of ['product', 'business', 'research', 'policy', 'hack']",
  "ai_relevance_score": 0.0 to 1.0 (Float. If below 0.6, this article will be discarded later, so judge strictly. Only AI related news.),
  "metrics": [
    {"label": "Short Label (e.g. 'Params')", "value": "Value (e.g. '70B')"},
    {"label": "Short Label", "value": "Value"}
  ],
  "tech_tags": ["Tag1", "Tag2"],
  "key_points": ["Point 1", "Point 2", "Point 3"]
}

Rules:
1. If the article is NOT about AI (Artificial Intelligence, Machine Learning, LLMs, Robotics, etc.), set "ai_relevance_score" to 0.1.
2. "metrics" should extract quantitative data if possible (e.g., performance improvement, model size, investment amount). If none, extract qualitative highlights (e.g., "Status": "Released"). Max 3 metrics.
3. Translate everything to natural, professional Japanese.
"""
