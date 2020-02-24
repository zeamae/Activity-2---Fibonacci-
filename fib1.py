# FINAL fib1.py !!!!!

import time
import matplotlib.pyplot as plt

terms = []
run_time = []

print("Fibonacci using Recursion")

n = 0

def recfibo1(n):

   if n <= 1:
       return n
   else:
       return(recfibo1(n-1) + recfibo1(n-2))

r1 = int(input("No. of terms: "))
terms.append(r1)
start_time = time.time()
if r1 <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(r1):
       print(recfibo1(i))

recfibo1(n)

end_time = time.time()
runTime1 = end_time - start_time
print("Execution time:", runTime1)


def recfibo2(n):
    if n <= 1:
        return n
    else:
        return (recfibo2(n - 1) + recfibo2(n - 2))


r2 = int(input("No. of terms: "))
terms.append(r2)
start_time = time.time()
if r2 <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(r2):
        print(recfibo1(i))

recfibo2(n)

end_time = time.time()
runTime2 = end_time - start_time
print("Execution time:", runTime2)


def recfibo3(n):
    if n <= 1:
        return n
    else:
        return (recfibo3(n - 1) + recfibo3(n - 2))


r3 = int(input("No. of terms: "))
terms.append(r3)
start_time = time.time()
if r3 <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(r3):
        print(recfibo1(i))

recfibo3(n)

end_time = time.time()
runTime3 = end_time - start_time
print("Execution time:", runTime3)


def recfibo4(n):
    if n <= 1:
        return n
    else:
        return (recfibo4(n - 1) + recfibo4(n - 2))


r4 = int(input("No. of terms: "))
terms.append(r4)
start_time = time.time()
if r4 <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(r4):
        print(recfibo1(i))

recfibo4(n)

end_time = time.time()
runTime4 = end_time - start_time
print("Execution time:", runTime4)


def recfibo5(n):
    if n <= 1:
        return n
    else:
        return (recfibo5(n - 1) + recfibo5(n - 2))


r5 = int(input("No. of terms: "))
terms.append(r5)
start_time = time.time()
if r5 <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(r5):
        print(recfibo1(i))

recfibo5(n)

end_time = time.time()
runTime5 = end_time - start_time
print("Execution time:", runTime5)

left = [1, 2, 3, 4, 5]
height = [runTime1, runTime2, runTime3, runTime4, runTime5]

tick_label = [r1, r2, r3, r4, r5]

plt.bar(left, height, tick_label=tick_label,
        width=0.5, color=['green'])

plt.xlabel('Fibonacci Numbers Generated')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Runtime (Recursion)')

plt.show()
