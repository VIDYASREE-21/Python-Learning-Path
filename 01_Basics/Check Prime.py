n=11
 flag=True
 for i in range(2, n):
     if n%i==0:
         flag=False

 print("Prime" if flag else "Not Prime")
