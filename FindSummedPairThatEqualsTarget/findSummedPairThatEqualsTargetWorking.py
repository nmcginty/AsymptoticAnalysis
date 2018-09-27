# Given a list of numbers and an integer find a pair of numbers in list
# that equals the integer. If no pair exists return false otherwise false.
 
import matplotlib.pyplot as plt
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
        y_quad.append(quadOut*10**4) # to provide y axis with some meaningful values
        x_log.append(n)
        y_log.append(logOut*10**4)
        x_linear.append(n)
        y_linear.append(linearOut*10**4)

    # print("Quadratic Time: ", quadOut)
    # print("n*log(n) Time: ", logOut)
    # print("Linear Time: ", linearOut)
    fig, ax = plt.subplots()

    # ax.plot((0, POPULATION), (0, quadOut*1000))
    # ax.plot((0, POPULATION), (0, logOut*1000))
    # ax.plot((0, POPULATION), (0, linearOut*1000))
    ax.plot(x_quad, y_quad)
    ax.plot(x_log, y_log)
    ax.plot(x_linear, y_linear)

    ax.set(xlabel="n", ylabel="Time", title="Asymptotic Analysis")
    ax.grid()
    fig.savefig("timeComplexityAnalysis.png")
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