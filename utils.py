# Package: cognize
# File: utils.py

import numpy as np
from typing import Callable

# Optional: use OpenAI or HuggingFace embeddings here

def get_embedding(text: str) -> np.ndarray:
    """
    Placeholder embedding function. Replace with OpenAI/HF model.
    Returns a random vector for now.
    """
    np.random.seed(abs(hash(text)) % (10 ** 8))  # for consistency
    return np.random.rand(768)

def scalar_drift(V, R, embed_fn: Callable = None) -> float:
    """
    Simple scalar drift: |R - V| if both are numbers.
    """
    return abs(float(R) - float(V))

def semantic_drift(V, R, embed_fn: Callable) -> float:
    """
    Cosine similarity-based drift using embeddings.
    Returns: 1 - cosine_sim → high = more drift
    """
    e1 = embed_fn(str(V))
    e2 = embed_fn(str(R))
    dot = np.dot(e1, e2)
    norm = np.linalg.norm(e1) * np.linalg.norm(e2)
    return 1 - (dot / norm) if norm != 0 else 1.0
