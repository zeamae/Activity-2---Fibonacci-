#  fib3 FINAAAAL!!!!

import time
import matplotlib.pyplot as plt
import numpy as np

x1 = []
y1 = []
x2 = []
y2 = []

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


def main():

    print("  FIBONACCI  ")

#recursion_1
print("---- Fibonacci Sequence using Recursion ----")
r1 = int(input("No. of terms: "))
x1.append(r1)

start_time = time.time()
for i in range(1, r1 + 1):
    fibonacci = fib1(i)

    print(i,":", fibonacci)

end_time = time.time()
runtime1 = end_time - start_time
print("Execution time:", runtime1)


#iteration_1
print("---- Fibonacci Sequence using Iteration ----")
i1 = int(input("No. of terms: "))
x2.append(i1)

start_timeiter = time.time()
for i in range(1, i1 + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime2 = end_time - start_timeiter
print("Execution time:", runtime2)


#recursion_2
print("---- Fibonacci Sequence using Recursion ----")
r2 = int(input("No. of terms: "))
x1.append(r2)


start_time = time.time()
for i in range(1, r2 + 1):
        fibonacci = fib1(i)

        print(i,":", fibonacci)

end_time = time.time()
runtime3 = end_time - start_time
print("Execution time:", runtime3)


#iteration_2
print("---- Fibonacci Sequence using Iteration ----")
i2 = int(input("No. of terms: "))
x2.append(i2)


start_timeiter = time.time()
for i in range(1, i2 + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime4 = end_time - start_timeiter
print("Execution time:", runtime4)

# recursion_3
print("---- Fibonacci Sequence using Recursion ----")
r3 = int(input("No. of terms: "))
x1.append(r3)


start_time = time.time()
for i in range(1, r3 + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime5 = end_time - start_time
print("Execution time:", runtime5)


# iteration_3
print("---- Fibonacci Sequence using Iteration ----")
i3 = int(input("No. of terms: "))
x2.append(i3)


start_timeiter = time.time()
for i in range(1, i3 + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime6 = end_time - start_timeiter
print("Execution time:", runtime6)



# recursion_4
print("---- Fibonacci Sequence using Recursion ----")
r4 = int(input("No. of terms: "))
x1.append(r4)


start_time = time.time()
for i in range(1, r4 + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime7 = end_time - start_time
print("Execution time:", runtime7)



# iteration_4
print("---- Fibonacci Sequence using Iteration ----")
i4 = int(input("No. of terms: "))
x2.append(i4)


start_timeiter = time.time()
for i in range(1, i4 + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime8 = end_time - start_timeiter
print("Execution time:", runtime8)


# recursion_5
print("---- Fibonacci Sequence using Recursion ----")
r5 = int(input("No. of terms: "))
x1.append(r5)


start_time = time.time()
for i in range(1, r5 + 1):
        fibonacci = fib1(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime9 = end_time - start_time
print("Execution time:", runtime9)


# iteration_5
print("---- Fibonacci Sequence using Iteration ----")
i5 = int(input("No. of terms: "))
x2.append(i5)

start_timeiter = time.time()
for i in range(1, i5 + 1):
        fibonacci = fib2(i)

        print(i, ":", fibonacci)

end_time = time.time()
runtime10 = end_time - start_timeiter
print("Execution time:", runtime10)


main()

left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
height = [runtime1, runtime2, runtime3, runtime4, runtime5, runtime6, runtime7, runtime8, runtime9, runtime10]

tick_label = [r1, i1, r2, i2, r3, i3, r4, i4, r5, i5]

plt.bar(left, height, tick_label=tick_label,
            width=0.5, color=['red','blue'], label="Iteration")

plt.bar(left, height, tick_label=tick_label,
            width=0.5, color=['blue','red'], label="Recursion")

plt.xlabel('Fibonacci Numbers Generated')
plt.ylabel('Execution Time (seconds)')
plt.title("Fibonacci (Runtime)")



plt.legend()
plt.show()
