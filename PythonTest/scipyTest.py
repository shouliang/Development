import numpy as np


def main():
    # 1 Integrate
    from scipy.integrate import quad, dblquad, nquad
    print(quad(lambda x: np.exp(-x), 0, np.inf))
    print(dblquad(lambda t, x: np.exp(-x * t) / t ** 3, 0, np.inf, lambda x: 1, lambda x: np.inf))

    def f(x, y):
        return x * y

    def bound_y():
        return [0, 0.5]

    def boud_x(y):
        return [0, 1 - 2 * y]

    print(nquad(f, [boud_x, bound_y]))

    # 2 Optimizer
    from scipy.optimize import minimize
    def rosen(x):
        return sum(100.0 * (x[1:] - x[:-1] ** 2) ** 2.0 + (1 - x[:-1]) ** 2.0)

    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
    res = minimize(rosen, x0, method="nelder-mead", options={"xtol":1e-8,"disp": True})
    print("ROSE MINI:",res)

if __name__ == '__main__':
    main()
