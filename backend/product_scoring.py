def score_product(product_record, user_history):
    recency_score = 30.0
    freq = len(user_history)
    freq_score = min(1.0, freq/5.0)
    rating = float(product_record.get('avg_rating', 3.5))
    rating_score = (rating - 1.0) / 4.0
    price = float(product_record.get('price', 100.0))
    price_score = max(0.0, 1 - (price / 1000.0))
    raw = 0.4*freq_score + 0.35*rating_score + 0.15*price_score + 0.1*(recency_score/30.0)
    return int(min(100, max(0, round(raw*100))))
