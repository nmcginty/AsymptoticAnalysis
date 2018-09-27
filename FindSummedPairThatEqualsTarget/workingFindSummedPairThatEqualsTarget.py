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
    
    # sequence = random.sample(range(POPULATION), SAMPLE)
    # sequence.sort()
    # target = random.randint(POPULATION//2, POPULATION)
    # print("Sequence size:", len(sequence))
    # print("Target:", target)

    x_quad, y_quad, x_log, y_log, x_linear, y_linear = ([] for x in range(6))


    # find a better way to record time... and store x,y coordinates
    sequence = [random.randint(0, POPULATION)]
    # sequence = random.sample(range(POPULATION), n)
    for n in range(SAMPLE):

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
        y_quad.append(quadOut*10**3) # y axis into microiseconds
        x_log.append(n)
        y_log.append(logOut*10**3) 
        x_linear.append(n)
        y_linear.append(linearOut*10**3)

        sequence.append(random.randint(0, POPULATION))

    # print("Quadratic Time: ", quadOut)
        sequence.sort()
    # print("n*log(n) Time: ", logOut)
    # print("Linear Time: ", linearOut)
    fig, ax = plt.subplots()

    # ax.plot((0, POPULATION), (0, quadOut*1000))
    # ax.plot((0, POPULATION), (0, logOut*1000))
    # ax.plot((0, POPULATION), (0, linearOut*1000))
    ax.plot(x_quad, y_quad, label="quadratic")
    ax.plot(x_log, y_log, label="n*log(n)")
    ax.plot(x_linear, y_linear, label="linear")

    plt.yticks(np.arange(0, y_quad[-1], step=0.5))

    ax.set(xlabel="n", ylabel="time (ms)", title="Asymptotic Analysis")
    ax.grid()
    fig.savefig("timeComplexityAnalysis.png")
    plt.legend()
    plt.show()
    print("\n")


def quadraticSolution(sequence, target): 
    
    pairs = [(x, y) for x in sequence for y in sequence if(x+y == target)]    
    # print("Pairs O(n^2):\t   ", pairs)

    # pairsBool = any([(x + y == target) for x in sequence for y in sequence])
    # print("pairsBOOL ", pairsBool)

def nLogNSolution(sequence, target):
    
    pairs = [] 
    for x in sequence:
        index = binarysearch(sequence, target - x)
        if(index is not None):
            complement = sequence[index]
            pairs.append((x, complement))

        # checking whether x <= target improves performance overall but gives odd osciliation   
        # as target is closer towards population this check becomes less cost saving
        # this check can only be made if we assume the list cannot contain negative numbers
        # which is most cases it probably could
        # if(x <= target):
        #     index = binarysearch(sequence, target - x)
        #     if(index is not None):
        #         complement = sequence[index]
        #         pairs.append((x, complement))
    
    # print("Pairs O(n*log(n)): ", pairs)

# bi-directional search
def linearSolution(sequence, target):
    pairs = []
    left, right = 0, len(sequence) - 1

    while left < right:
        l, r = sequence[left], sequence[right]
        if l + r  == target:
            pairs.append((l, r))
            left += 1           # does it matter what moves here?? leaning towards no... a TODO
        elif l + r < target:    # left is too small
            left += 1           
        else:                   # right is too large
            right -= 1

    # print("Pairs O(n):\t   ", pairs + [(y, x) for x, y in pairs])

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