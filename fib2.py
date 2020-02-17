import time
import matplotlib.pyplot as plt

terms = []
run_time = []



def iterfib1():

    print("Range from 0 to 40000")
    nterms = int(input("No. of terms: "))
    start_time = time.time()
    terms.append(nterms)


    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    run_time.append(runTime)

iterfib1()


def iterfib2():

    print("----------------------------------------------")
    print("Range from 0 to 40000")
    nterms = int(input("No. of terms: "))
    start_time = time.time()
    terms.append(nterms)


    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    run_time.append(runTime)

iterfib2()


def iterfib3():
    print("----------------------------------------------")
    print("Range from 0 to 40000")
    nterms = int(input("No. of terms: "))
    start_time = time.time()
    terms.append(nterms)


    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    run_time.append(runTime)

iterfib3()


def iterfib4():
    print("----------------------------------------------")
    print("Range from 0 to 40000")
    nterms = int(input("No. of terms: "))
    start_time = time.time()
    terms.append(nterms)


    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    run_time.append(runTime)

iterfib4()


def iterfib5():
    print("----------------------------------------------")
    print("Range from 0 to 40000")
    nterms = int(input("No. of terms: "))
    start_time = time.time()
    terms.append(nterms)


    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    run_time.append(runTime)

iterfib5()


plt.plot(terms,run_time, 'bo')
plt.xlabel('Integers (Positive)')
plt.ylabel('Execution Time')
plt.axis([0, 40000, 0, 20])
plt.title("Fibonacci Graph")
plt.show()
