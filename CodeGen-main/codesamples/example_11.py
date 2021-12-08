def nearest_neighbor(x, tSet):
    """[summary]
    Implements the nearest neighbor algorithm
    Arguments:
        x {[tupel]} -- [vector]
        tSet {[dict]} -- [training set]
    Returns:
        [type] -- [result of the AND-function]
    """
    assert isinstance(x, tuple) and isinstance(tSet, dict)
    current_key = ()
    min_d = float('inf')
    for key in tSet:
        d = distance(x, key)
        if d < min_d:
            min_d = d
            current_key = key
    return tSet[current_key]