#FINAL fib2.py !!!!!!!!


import time
import matplotlib.pyplot as plt

terms = []
run_time = []


print("Fibonacci using Iteration")
print("(Note: Best if not more than 40000)")

i1 = int(input("No. of terms: "))
start_time = time.time()
terms.append(i1)

def iterfib1():



    n1, n2 = 0, 1
    count = 0

    if i1 <= 0:
        print("Please enter a positive integer")
    elif i1 == 1:
        print("Fibonacci sequence upto", i1, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < i1:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

iterfib1()

end_time = time.time()
runTime1 = end_time - start_time
print("Execution time:", runTime1)


print("----------------------------------------------")
print("(Note: Best if not more than 40000)")
i2 = int(input("No. of terms: "))
start_time = time.time()
terms.append(i2)

def iterfib2():

    n1, n2 = 0, 1
    count = 0

    if i2 <= 0:
        print("Please enter a positive integer")
    elif i2 == 1:
        print("Fibonacci sequence upto", i2, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < i2:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1
iterfib2()

end_time = time.time()
runTime2 = end_time - start_time
print("Execution time:", runTime2)



print("----------------------------------------------")
print("(Note: Best if not more than 40000)")
i3 = int(input("No. of terms: "))
start_time = time.time()
terms.append(i3)

def iterfib3():
    n1, n2 = 0, 1
    count = 0

    if i3 <= 0:
        print("Please enter a positive integer")
    elif i3 == 1:
        print("Fibonacci sequence upto", i3, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < i3:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

iterfib3()

end_time = time.time()
runTime3 = end_time - start_time
print("Execution time:", runTime3)


print("----------------------------------------------")
print("(Note: Best if not more than 40000)")
i4 = int(input("No. of terms: "))
start_time = time.time()
terms.append(i4)

def iterfib4():
    n1, n2 = 0, 1
    count = 0

    if i4 <= 0:
        print("Please enter a positive integer")
    elif i4 == 1:
        print("Fibonacci sequence upto", i4, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < i4:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

iterfib4()

end_time = time.time()
runTime4 = end_time - start_time
print("Execution time:", runTime4)



print("----------------------------------------------")
print("(Note: Best if not more than 40000)")
i5 = int(input("No. of terms: "))
start_time = time.time()
terms.append(i5)

def iterfib5():
    n1, n2 = 0, 1
    count = 0

    if i5 <= 0:
        print("Please enter a positive integer")
    elif i5 == 1:
        print("Fibonacci sequence upto", i5, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < i5:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1
iterfib5()

end_time = time.time()
runTime5 = end_time - start_time
print("Execution time:", runTime5)




left = [1, 2, 3, 4, 5]
height = [runTime1, runTime2, runTime3, runTime4, runTime5]

tick_label = [i1, i2, i3, i4, i5]

plt.bar(left, height, tick_label=tick_label,
        width=0.5, color=['red'])

plt.xlabel('Fibonacci Numbers Generated')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Runtime (Iteration)')

plt.show()
