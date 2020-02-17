#  fib3 FINAAAAL!!!!

import time
import matplotlib.pyplot as plt
import numpy as np

x1 = []
y1 = []
x2 = []
y2 = []


def main():

    print("FIBONACCI")

    #recursion_1
    number = 34
    x1.append(number)


    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i,":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    y1.append(recursionRuntime)

    plt.plot(x1,y1, 'ro', label="Recursion")

    #iteration_1
    number = 3000
    x2.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    y2.append(iterationRuntime)

    plt.plot(x2,y2, 'bo', label='Iteration')

    plt.axis([0, 4500, 0, 12])



    #recursion_2
    number = 21
    x1.append(number)


    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i,":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    y1.append(recursionRuntime)

    plt.plot(x1,y1, 'ro')

    #iteration_2
    number = 1500
    x2.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    y2.append(iterationRuntime)

    plt.plot(x2,y2, 'bo')

    plt.axis([0, 4500, 0, 12])

    # recursion_3
    number = 29
    x1.append(number)

    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    y1.append(recursionRuntime)

    plt.plot(x1, y1, 'ro')

    # iteration_3
    number = 3500
    x2.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    y2.append(iterationRuntime)

    plt.plot(x2, y2, 'bo')

    plt.axis([0, 4500, 0, 12])

    # recursion_4
    number = 33
    x1.append(number)

    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    y1.append(recursionRuntime)

    plt.plot(x1, y1, 'ro')

    # iteration_4
    number = 4300
    x2.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    y2.append(iterationRuntime)

    plt.plot(x2, y2, 'bo')

    plt.axis([0, 4500, 0, 12])

    # recursion_5
    number = 25
    x1.append(number)

    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    y1.append(recursionRuntime)

    plt.plot(x1, y1, 'ro')

    # iteration_5
    number = 685
    x2.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    y2.append(iterationRuntime)

    plt.plot(x2, y2, 'bo')

    plt.axis([0, 4500, 0, 12])

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)



def fib2(number):


    fn1 = 1
    fn2 = 1


    for i in range(3, number + 1):
        fn2Aux = fn1
        fn1 = fn2 + fn1
        fn2 = fn2Aux

    return fn1

main()

plt.xlabel('Fibonacci Numbers Generated')
plt.ylabel('Execution Time (seconds)')
plt.title("Fibonacci (Runtime)")



plt.legend()
plt.show()
