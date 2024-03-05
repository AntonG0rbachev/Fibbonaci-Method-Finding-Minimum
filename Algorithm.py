import matplotlib.pyplot as pyplot
import numpy


def bufferedFibonacci(number, buffer=None):
    number = int(number)
    if number == 1 or number == 0:
        return 1
    if buffer is None:
        buffer = {}
    if number in buffer:
        return buffer[number]
    result = bufferedFibonacci(number - 1, buffer) + bufferedFibonacci(number - 2, buffer)
    buffer[number] = result
    return result


def findingMinimumByFibonacciMethod(interval, delta, epsilon, function):
    def findFibonacciNumber():
        target = sum(interval) / delta
        num = 0
        while bufferedFibonacci(num) < target:
            num += 1
        return num

    x_min: float
    number = findFibonacciNumber()
    iterations = 0
    y_k = interval[0] + (bufferedFibonacci(number - 2) / bufferedFibonacci(number)) * (interval[1] - interval[0])
    z_k = interval[0] + (bufferedFibonacci(number - 1) / bufferedFibonacci(number)) * (interval[1] - interval[0])
    y_k_prev = y_k
    while iterations != number - 3:
        iterations += 1
        if function(y_k) <= function(z_k):
            interval[1] = z_k
            y_k_prev = y_k
            z_k = y_k
            y_k = interval[0] + (bufferedFibonacci(number - iterations - 3) /
                                 bufferedFibonacci(number - iterations - 1)) * (interval[1] - interval[0])
        elif function(y_k) > function(z_k):
            interval[0] = y_k
            y_k_prev = y_k
            y_k = z_k
            z_k = interval[0] + (bufferedFibonacci(number - iterations - 2) /
                                 bufferedFibonacci(number - iterations - 1)) * (interval[1] - interval[0])
    else:
        y_k = y_k_prev
        z_k = y_k_prev + epsilon
        if function(y_k) <= function(z_k):
            interval[1] = z_k
        elif function(y_k) > function(z_k):
            interval[0] = y_k
        x_min = sum(interval) / 2
    convergence = 1 / bufferedFibonacci(number)
    return ("x_min = " + str(x_min), "f(x_min) = " + str(function(x_min)), "interval = " + str(interval),
            "iterations = " + str(iterations), "convergence = " + str(convergence))


f = lambda x: 2 * x ** 2 - 2 * x + 3 / 2
L = [-2, 8]
eps = 0.2
l = 0.5
x = numpy.arange(L[0] - 1, L[1] + 1, 0.01)
pyplot.plot(x, f(x))
pyplot.show()
print(findingMinimumByFibonacciMethod(L, l, eps, f))