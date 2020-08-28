def prime(n):
  c=0
  for i in range(2,n//2):
    if n%i==0:c=c+1
  if n!=1 and c==0:return 1
  else : return 0
 n=int(input())
 if prime(n):print("prime")
 else : print("no no ")
