import json
import random
import datetime
import uuid
import os

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, '../data/news.json')

# Mock Data Sources
CATEGORIES = ['product', 'business', 'research', 'policy', 'hack']
COMPANIES = ['OpenAI', 'Google DeepMind', 'Anthropic', 'Microsoft', 'Meta', 'NVIDIA', 'Stability AI']
TECH_TAGS = ['LLM', 'Generative AI', 'Computer Vision', 'Reinforcement Learning', 'Robotics', 'Multimodal']
INDUSTRIES = ['Healthcare', 'Finance', 'Manufacturing', 'Retail', 'Education', 'Government']

# Templates for generating content
TITLES = {
    'product': [
        "{company}が新モデル「{model}」を発表、推論能力が大幅向上",
        "{company}、画像生成AI「{model}」の最新版をリリース",
        "{company}のAIアシスタントが大型アップデート、プラグイン機能拡充"
    ],
    'business': [
        "{industry}業界で生成AI導入が加速、{company}と提携",
        "大手{industry}企業がAI活用で業務効率化、コスト削減を実現",
        "{company}、法人向けAIソリューションの提供を開始"
    ],
    'research': [
        "{company}、新たな学習手法「{method}」を論文発表",
        "LLMのハルシネーションを抑制する新技術、{company}が開発",
        "自己進化するAIエージェントの基礎研究、{company}が公開"
    ],
    'policy': [
        "EU、AI規制法案の最終合意に到達、{year}年施行へ",
        "米国政府、AI安全性評価のための新機関設立を発表",
        "G7、生成AIの国際的な行動規範を策定"
    ],
    'hack': [
        "LLMの回答精度を劇的に高めるプロンプトエンジニアリング術",
        "ローカル環境で動く軽量LLMの構築・運用ガイド",
        "RAG（検索拡張生成）の実装ベストプラクティス"
    ]
}

def generate_metrics(category):
    metrics = []
    if category == 'product':
        metrics.append({"label": "Context Window", "value": f"{random.choice([32, 128, 200])}k"})
        metrics.append({"label": "Params", "value": f"{random.randint(7, 70)}B"})
        metrics.append({"label": "Speed", "value": f"{random.randint(10, 50)}% UP"})
    elif category == 'business':
        metrics.append({"label": "Cost Red.", "value": f"{random.randint(20, 60)}%"})
        metrics.append({"label": "Efficiency", "value": f"{random.randint(2, 5)}x"})
        metrics.append({"label": "ROI", "value": f"{random.randint(100, 300)}%"})
    elif category == 'research':
        metrics.append({"label": "Accuracy", "value": f"+{random.randint(5, 15)}%"})
        metrics.append({"label": "SOTA", "value": "Yes"})
        metrics.append({"label": "Citations", "value": f"{random.randint(10, 100)}"})
    elif category == 'policy':
        metrics.append({"label": "Status", "value": random.choice(["Draft", "Passed", "Active"])})
        metrics.append({"label": "Impact", "value": "High"})
        metrics.append({"label": "Region", "value": random.choice(["EU", "US", "JP", "Global"])})
    elif category == 'hack':
        metrics.append({"label": "Time Saved", "value": f"{random.randint(30, 90)} min/day"})
        metrics.append({"label": "Difficulty", "value": random.choice(["Easy", "Medium", "Hard"])})
        metrics.append({"label": "Cost", "value": "$0"})
    return metrics

def generate_news_item():
    category = random.choice(CATEGORIES)
    company = random.choice(COMPANIES)
    industry = random.choice(INDUSTRIES)
    model = f"Model-{random.choice(['X', 'Y', 'Z', 'Alpha', 'Omega'])}"
    method = f"Method-{random.randint(1, 100)}"
    year = 2025

    title_template = random.choice(TITLES[category])
    title = title_template.format(company=company, industry=industry, model=model, method=method, year=year)

    summary_short = f"これは{category}に関するニュースです。{company}が中心となり、{industry}分野や技術開発において重要な進展がありました。詳細なデータや影響については詳細ページをご覧ください。"
    
    summary_long = f"""
    <p><strong>{title}</strong></p>
    <p>本記事では、{company}による最新の発表について詳しく解説します。この動きは、{category}分野において非常に重要な意味を持ちます。</p>
    <p>具体的には、以下の3つの点が注目されています。</p>
    <p>第一に、技術的なブレークスルーです。従来のモデルと比較して、処理速度や精度が大幅に向上しています。特に{random.choice(TECH_TAGS)}の領域での応用が期待されています。</p>
    <p>第二に、実用性の高さです。{industry}業界をはじめとする多くの現場で、即座に導入可能なレベルに達していると評価されています。</p>
    <p>第三に、今後の展望です。{company}は今回の発表を皮切りに、さらなるエコシステムの拡大を目指しています。</p>
    <p>専門家は、「この技術は今後数年間のスタンダードになる可能性がある」と指摘しています。</p>
    """

    return {
        "id": str(uuid.uuid4()),
        "title_ja": title,
        "summary_short_ja": summary_short,
        "summary_long_ja": summary_long,
        "date": (datetime.date.today() - datetime.timedelta(days=random.randint(0, 7))).strftime('%Y-%m-%d'),
        "category": category,
        "metrics": generate_metrics(category),
        "tech_tags": random.sample(TECH_TAGS, k=random.randint(1, 3)),
        "key_points": [
            f"{company}による革新的な発表",
            f"{industry}業界への大きなインパクト",
            "技術的なベンチマークを更新",
            "今後のロードマップが明確化"
        ],
        "sources": [
            {
                "media": "TechCrunch",
                "title": "Original English Article Title",
                "url": "https://example.com",
                "date": "2025-11-28"
            },
            {
                "media": "Official Blog",
                "title": "Company Announcement",
                "url": "https://example.com",
                "date": "2025-11-28"
            }
        ]
    }

def main():
    # Generate 12 items
    items = [generate_news_item() for _ in range(12)]
    
    data = {
        "generated_at": datetime.datetime.now().isoformat(),
        "items": items
    }

    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully generated {len(items)} news items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
