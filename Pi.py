from decimal import *

def nilakantha(reps):
        result = Decimal(3.0)
        op = 1
        n = 2
        for n in range(2, 2*reps+1, 2):
                result += 4/Decimal(n*(n+1)*(n+2)*op)
                op *= -1
        return result
  
while True:
  False
  print("How many repetitions?")
  repetitions = int(input())
  print("How many significant numbers?")
  signum = int(input())
  getcontext().prec = (signum)
  print(nilakantha(repetitions))
  True
