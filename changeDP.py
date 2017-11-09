def change(amount, denominations):
    n_cents = [0] * (amount + 1)

    # 1 way of making 0 cents
    n_cents[0] = 1

    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            remainder = higher_amount - coin
            n_cents[higher_amount] += n_cents[remainder]

    return n_cents[amount]