# Given a list of numbers and an integer find a pair of numbers in list
# that equals the integer. If no pair exists return false otherwise false.
 
import matplotlib.pyplot as plt
import numpy as np
import random, time
from scipy.constants import golden
from math import sqrt, floor

N_FIBS = 12
GOLDEN_RATIO=golden

def main():

    print("\n")
    x_log, y_log, x_linear, y_linear, x_exponential, y_exponential = ([] for x in range(6))

    for n in range(N_FIBS):

        logIn = time.time()
        log(n)
        logOut = time.time() - logIn
        linearIn = time.time()
        linear(n)
        linearOut = time.time() - linearIn
        exponentialIn = time.time()
        exponential(n)
        exponentialOut = time.time() - exponentialIn
        x_log.append(n)
        y_log.append(logOut*10**3)
        x_linear.append(n)
        y_linear.append(linearOut*10**3)
        x_exponential.append(n)
        y_exponential.append(exponentialOut*10**3) # y axis to milliseconds


    fig, ax = plt.subplots()

    ax.plot(x_log, y_log, label="logarithmic")
    ax.plot(x_linear, y_linear, label="Linear")
    ax.plot(x_exponential, y_exponential, label="Exponential")
    plt.yticks(np.arange(0, y_exponential[-1], step=5))
    # To compare just logarithmic and linear time complexities use this line below for the 
    #   y-axis interval and remove the exponential ax.plot(...) line above
    # plt.yticks(np.arange(0, y_linear[-1], step=2.5))
    plt.legend(loc="upper right")
    
    ax.set(xlabel="n", ylabel="time (ms)", title="Fibonacci Asymptotic Analysis")

    ax.grid()
    fig.savefig("fibonacciComplexityAnalysis.png")
    plt.show()
    print("\n")


# https://www.geeksforgeeks.org/g-fact-18-2/
# https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
def log(n):
    return n if n < 2 else floor(((GOLDEN_RATIO**n)/sqrt(5)) + 1.0/2.0)

def linear(n):
    fn = f1 = f2 = 1
    for _ in range(2, n):
        fn = f1 + f2
        f2, f1 = f1, fn

    return fn    

# 2**n
def exponential(n):
    return n if n < 2 else exponential(n-1) + exponential(n-2)

main()
