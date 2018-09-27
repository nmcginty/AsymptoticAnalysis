# Given a list of numbers and an integer find a pair of numbers in list
# that equals the integer. If no pair exists return false otherwise false.
 
import matplotlib.pyplot as plt
import numpy as np
import random, time

POPULATION = 2000
SAMPLE = 300
# changing target value shows some interesting results
# target = random.randint(0, POPULATION)
target = POPULATION // 2
# target = 0
# target = 100

def main():

    print("\n")

    x_quad, y_quad, x_log, y_log, x_linear, y_linear = ([] for x in range(6))

    for n in range(SAMPLE):
        sequence = random.sample(range(POPULATION), n)
        sequence.sort()

        quadIn = time.time()
        quadraticSolution(sequence, target)
        quadOut = time.time() - quadIn

        logIn = time.time()
        nLogNSolution(sequence, target)
        logOut = time.time() - logIn

        linearIn = time.time()
        linearSolution(sequence, target)
        linearOut = time.time() - linearIn

        x_quad.append(n)
        y_quad.append(quadOut*10**3) # y axis to milliseconds
        x_log.append(n)
        y_log.append(logOut*10**3)
        x_linear.append(n)
        y_linear.append(linearOut*10**3)

    fig, ax = plt.subplots()

    ax.plot(x_quad, y_quad)
    ax.plot(x_log, y_log)
    ax.plot(x_linear, y_linear)

    plt.yticks(np.arange(0, y_quad[-1], step=0.5))
    ax.set(xlabel="n", ylabel="time (ms)", title="Asymptotic Analysis")

    ax.grid()
    fig.savefig("timeComplexityAnalysis.png")
    plt.show()
    print("\n")

# just really slow... 
def quadraticSolution(sequence, target): 
    
    pairs = [(x, y) for x in sequence for y in sequence if(x+y == target)]    

# uses binary search to locate complement of number if it exist
# allows single iteration of the list but a cost of log(n) for each n 
# due to binarysearch call
def nLogNSolution(sequence, target):
    
    pairs = [] 
    for x in sequence:
        index = binarysearch(sequence, target - x)
        if(index is not None):
            complement = sequence[index]
            pairs.append((x, complement))


# bi-directional search, two indexes at first and last element
# check some of elements at left/right index, move accordingly
def linearSolution(sequence, target):
    pairs = []
    left, right = 0, len(sequence) - 1

    while left < right:
        l, r = sequence[left], sequence[right]
        if l + r  == target:
            pairs.append((l, r))
            left += 1   
        elif l + r < target:    # left is too small
            left += 1           
        else:                   # right is too large
            right -= 1

# returns index if target exists in sequence otherwise returns None, takes log(n)
def binarysearch(sequence, target):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < target:
            lo = mid + 1
        elif target < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return None

main()