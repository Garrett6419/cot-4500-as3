import numpy as np  # type: ignore


def euler_method(f, t0, y0, t_end, iterations):
    h = (t_end - t0) / iterations
    t = t0
    y = y0
    for i in range(iterations):
        y += h * f(t, y)
        t += h
    return y


def runge_kutta(f, t0, y0, t_end, iterations):
    h = (t_end - t0) / iterations
    t = t0
    y = y0
    for i in range(iterations):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

# Function to be used in the methods
def function(t, y):
    return t - y**2

# Example usage of the algorithms
if __name__ == "__main__":
    # Task 1: Euler Method
    t0 = 0
    y0 = 1
    t_end = 2
    iterations = 10
    result_euler = euler_method(function, t0, y0, t_end, iterations)
    print("Euler Method Result:", result_euler)

    # Task 2: Runge-Kutta Method
    result_rk = runge_kutta(function, t0, y0, t_end, iterations)
    print("Runge-Kutta Method Result:", result_rk)