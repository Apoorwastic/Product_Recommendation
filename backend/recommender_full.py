# recommender_full.py
import numpy as np
from indexer import DATA, INDEX
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations_for_user(user_id):
    user_profile = INDEX["customer_profiles"].get(user_id)
    if user_profile is None:
        return None

    # Product similarity
    product_sims = cosine_similarity(
        [user_profile],
        INDEX["product_embeddings"]
    )[0]

    product_ids = DATA["products"]["product_id"].tolist()
    top_product_indices = np.argsort(product_sims)[::-1][:4]
    top_products = DATA["products"].iloc[top_product_indices]

    # Offer similarity
    offer_sims = cosine_similarity(
        [user_profile],
        INDEX["offer_embeddings"]
    )[0]

    offer_ids = DATA["offers"]["offer_id"].tolist()
    top_offer_indices = np.argsort(offer_sims)[::-1][:3]
    top_offers = DATA["offers"].iloc[top_offer_indices]

    return top_products, top_offers
