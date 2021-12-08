# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cut_rod(price):
    n = len(price)
    val = [0] * (n + 1)

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = -10000000
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]