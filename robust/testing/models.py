from gpkit import Variable, Model


def test_model():
    x = Variable('x')
    y = Variable('y')

    a = Variable('a', 0.6, pr=10)
    b = Variable('b', 0.5, pr=10)

    constraints = [a * b * x + a * b* y <= 1,
                   b * x / y + b * x * y + a*b**2 * x ** 2 <= 1]
    return Model((x * y) ** -1, constraints)
