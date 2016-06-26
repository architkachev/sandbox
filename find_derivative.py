polinom = [2, 3, 5]  # 5x^2 + 3x + 2


def find_derivative(polinom):
    def derivative(k, step):
        return k * step

    return map(derivative, polinom, range(len(polinom)))

print(find_derivative(polinom))