import math
def find_fib(n,c=0):
  c+=1
  if n==0 or n==1:
    return n,c
  l,c=find_fib(n-2,c)
  r,c=find_fib(n-1,c)
  return l+r , c
  
def generate_execution_observation_table(sizes):
  out=[]
  out.append("Algorithm Execution Observation Table")
  out.append("InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci 
IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort")
  for n in sizes:
    rec_fact=n+1
    iter_fact=n
    fib,rec_fib=find_fib(n)
    iter_fib=n
    lin_search=n
    bin_search=int(math.floor(math.log(n,2))+1)
    bs_sort=int((n*(n-1))/2)
    is_sort=int((n*(n-1))/2)
    out.append(f"{n} {rec_fact} {iter_fact} {rec_fib} {iter_fib} {lin_search} {bin_search} 
{bs_sort} {is_sort}")
  
  return out