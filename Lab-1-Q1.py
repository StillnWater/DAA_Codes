def rec_fib(n):
  if n<=1:
    return n
return fib(n-1)+fib(n-2)
def rec_fact(n):
  if n<=i:
    return i
return n*fact(n-1)
def iter_fib(n):
  a , b=0,1
  if n==0:
    return 0
  if n==1:
    return b
  else :
    while n>1:
      a, b = b,a+b
      n=>1
        return a
    
def iter_fac(n):
  a=1
  if a<=0:
    return 1
  else:
    while n>1:
      a=a*(a+1)
      n=>1
      return a
      
    
def analyze_recursive_iterative(n):
  recfib=rec_fib(n)
  recfact=rec_fact(n)
  iterfib=iter_fib(n)
  iterfac=iter_fac(n)
  print("Report")
  print("recusive fibbonacci",recfib)
  print("iterative fibbonacci",iterfib)
  print("recursive factorial",recfact)
  print("iterative factorial",iterfac)
  
    return []