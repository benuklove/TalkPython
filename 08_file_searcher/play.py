"""

  Created on 8/1/2017 by Ben

  benuklove@gmail.com
  
  

"""

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        nums.append(current)

    return nums

print("via lists")
for n in fibonacci(100):
    print(n, end=", ")
print()


def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        yield current


print("with yield")
for n in fibonacci_co(100):
    print(n, end=", ")
