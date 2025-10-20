from functools import partial

# Lambda function
f = lambda x, y: x + y
print(f(2, 3))  # Output: 5

# Currying
g = partial(f, 2)
print(g(3))  # Output: 5
