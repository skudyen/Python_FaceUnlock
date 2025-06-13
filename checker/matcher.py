import numpy as np

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def find_best_match(embedding, database, threshold=0.5):
    best_match = "Unknown"
    best_score = -1

    for name, vectors in database.items():
        for vec in vectors:
            score = cosine_similarity(embedding, vec)
            if score > best_score:
                best_score = score
                best_match = name

    if best_score >= threshold:
        return best_match, best_score
    else:
        return "Unknown", best_score