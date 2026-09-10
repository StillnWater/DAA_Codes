def rec_fac(n, c=0):
    c += 1
    if n == 0:
        return 1, c
    fac, c = rec_fac(n-1, c)
    return n * fac, c

def iter_fac(n):
    c = 0
    fac = 1
    for i in range(1, n+1):
        c += 1
        fac *= i
    return fac, c

def rec_fib(n, c=0):
    c += 1
    if n == 0 or n == 1:
        return n, c
    left, c = rec_fib(n-2, c)
    right, c = rec_fib(n-1, c)
    return left + right, c

def iter_fib(n):
    a , b = 0 , 1
    c = 0
    for i in range(1, n+1):
        c += 1
        a , b = b , a+b
    return a , c

def analyze_recursive_iterative(n):
    fac1, fac_c1 = rec_fac(n)
    fac2, fac_c2 = iter_fac(n)
    fib1, fib_c1 = rec_fib(n)
    fib2, fib_c2 = iter_fib(n)
    output = []
    output.append("Computation Analysis Report")
    output.append(f"Recursive Factorial: {fac1}")
    output.append(f"Iterative Factorial: {fac2}")
    output.append(f"Recursive Fibonacci: {fib1}")
    output.append(f"Iterative Fibonacci: {fib2}")
    output.append("Operation Count Comparison")
    output.append(f"Recursive Factorial Count: {fac_c1}")
    output.append(f"Iterative Factorial Count: {fac_c2}")
    output.append(f"Recursive Fibonacci Count: {fib_c1}")
    output.append(f"Iterative Fibonacci Count: {fib_c2}")
    return output

def run():
    testcases = [1,5,10]
    for i in range(len(testcases)):
        case = testcases[i]
        out = analyze_recursive_iterative(case)
        print(f"Case {i+1}")
        for output in out:
            print(output)
        print(f"{'-'*30}")
run()