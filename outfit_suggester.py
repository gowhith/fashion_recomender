import random

# Define outfit tags for each weather + event
weather_event_tags = {
    ("sunny", "casual"): ["t-shirt", "shorts", "sunglasses", "jeans"],
    ("sunny", "formal"): ["blazer", "chinos", "oxfords"],
    ("rainy", "casual"): ["hoodie", "raincoat", "boots", "jeans"],
    ("rainy", "formal"): ["trench coat", "umbrella", "loafers"],
    ("cold", "casual"): ["jacket", "sweater", "beanie", "jeans"],
    ("cold", "formal"): ["coat", "scarf", "boots"],
    ("sunny", "party"): ["dress", "polo shirt", "sneakers"],
    ("cold", "party"): ["sweater", "coat", "boots"]
}

def generate_outfit(items, weather, event):
    """
    items: list of clothing strings from closet (like ["jeans", "blazer"])
    weather: one of ['sunny', 'rainy', 'cold']
    event: one of ['casual', 'formal', 'party']
    """
    # Tags for current context
    tags = weather_event_tags.get((weather, event), [])
    
    # Score items by relevance to tags
    scored = [(item, sum(tag in item.lower() for tag in tags)) for item in items]
    scored.sort(key=lambda x: x[1], reverse=True)

    # Remove duplicates
    seen, selected = set(), []
    for item, score in scored:
        if item not in seen and score > 0:
            selected.append(item)
            seen.add(item)

    # Fallback: Add random items if <3
    if len(selected) < 3:
        remaining = list(set(items) - seen)
        random.shuffle(remaining)
        selected.extend(remaining[:3 - len(selected)])

    return selected[:3]
