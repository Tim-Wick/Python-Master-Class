def odds():
    start = 1
    while True:
        yield start
        start += 2


def defpi_series():
    oddnumbers = odds()
    approx = 0
    while True:
        approx += (4 / next(oddnumbers))
        yield approx
        approx -= (4 / next(oddnumbers))
        yield approx


approx_pi = defpi_series()

for x in range(100000):
    print(next(approx_pi))
