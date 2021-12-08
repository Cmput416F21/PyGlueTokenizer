def gaussian(x, n):
    u = x.mean()
    s = x.std()

    # create a gaussian probability distribution
    x = linspace(x.min(), x.max(), n)

    a = ((x - u) ** 2) / (2 * (s ** 2))
    y = 1 / (s * sqrt(2 * pi)) * exp(-a)

    return x, y, x.mean(), x.std()