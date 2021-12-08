def cosine_similarity(a, b):
    """
    Calculate cosine similarity between given two vectors
    """
    if len(a) != len(b):
        raise ValueError("The two vectors must be the same length. Got shape " + str(len(a)) + " and " + str(len(b)))

    norm_a = _l2_distance(a)
    norm_b = _l2_distance(b)

    similarity = 0.

    # Calculate the dot product of two vectors
    for ae, be in zip(a, b):
        similarity += ae * be

    similarity /= (norm_a * norm_b)

    return similarity