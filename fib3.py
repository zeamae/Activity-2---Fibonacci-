# fib3

import time
import matplotlib.pyplot as plt

run_time = []
terms = []

def main():

    print("FIBONACCI")

    number = 30
    terms.append(number)


    print("---- Fibonacci Sequence using Recursion ----")
    start_time = time.time()
    for i in range(1, number + 1):
        fibonacci = fib1(i)

        print(i,":", fibonacci)

    end_time = time.time()
    recursionRuntime = end_time - start_time
    print("Execution time:", recursionRuntime, "seconds")
    run_time.append(recursionRuntime)


    number = 30
    terms.append(number)

    print("---- Fibonacci Sequence using Iteration ----")
    start_timeiter = time.time()
    for i in range(1, number + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

    end_time = time.time()
    iterationRuntime = end_time - start_timeiter
    print("Execution time:", iterationRuntime, "seconds")
    run_time.append(iterationRuntime)


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

plt.plot(terms,run_time, 'ro')
plt.xlabel('Fibonacci Numbers')
plt.ylabel('Execution Time')
plt.axis([0, 30, 0, 2])
plt.title("Fibonacci (Runtime)")
plt.show()