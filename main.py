def factorial(value):
  if value == 1 or value == 0:
    return 1
  
  return value * factorial(value - 1)

def lopp(value):
  if value == 1 or value == 0:
    return 1
  i = 2
  total = 1

  while i <= value:
    total *= i
    i += 1

  return total


v = factorial(2)
t = lopp(2)


print(v)
print(t)