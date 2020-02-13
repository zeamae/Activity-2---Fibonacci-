# FINAL recursion fibonacci

import time
import matplotlib.pyplot as plt

terms = []
run_time = []



n = 0

def recfibo1(n):

   if n <= 1:
       return n
   else:
       return(recfibo1(n-1) + recfibo1(n-2))

nterms = int(input("How many terms? "))
terms.append(nterms)
start_time = time.time()
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recfibo1(i))

recfibo1(n)

end_time = time.time()
runTime = end_time - start_time
print("Execution time:", runTime, "seconds")
run_time.append(runTime)


def recfibo2(n):
    if n <= 1:
        return n
    else:
        return (recfibo2(n - 1) + recfibo2(n - 2))


nterms = int(input("How many terms? "))
terms.append(nterms)
start_time = time.time()
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recfibo1(i))

recfibo2(n)

end_time = time.time()
runTime = end_time - start_time
print("Execution time:", runTime, "seconds")
run_time.append(runTime)


def recfibo3(n):
    if n <= 1:
        return n
    else:
        return (recfibo3(n - 1) + recfibo3(n - 2))


nterms = int(input("How many terms? "))
terms.append(nterms)
start_time = time.time()
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recfibo1(i))

recfibo3(n)

end_time = time.time()
runTime = end_time - start_time
print("Execution time:", runTime, "seconds")
run_time.append(runTime)


def recfibo4(n):
    if n <= 1:
        return n
    else:
        return (recfibo4(n - 1) + recfibo4(n - 2))


nterms = int(input("How many terms? "))
terms.append(nterms)
start_time = time.time()
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recfibo1(i))

recfibo4(n)

end_time = time.time()
runTime = end_time - start_time
print("Execution time:", runTime, "seconds")
run_time.append(runTime)


def recfibo5(n):
    if n <= 1:
        return n
    else:
        return (recfibo5(n - 1) + recfibo5(n - 2))


nterms = int(input("How many terms? "))
terms.append(nterms)
start_time = time.time()
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recfibo1(i))

recfibo5(n)

end_time = time.time()
runTime = end_time - start_time
print("Execution time:", runTime, "seconds")
run_time.append(runTime)


plt.plot(terms,run_time, 'ro')
plt.xlabel('Integers (Positive)')
plt.ylabel('Execution Time')
plt.axis([0, 30, 0, 1.5])
plt.title("Fibonacci Graph")
plt.show()
