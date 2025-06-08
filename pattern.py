# Lower Triangular
print("Lower Triangle:")
n = 5
for i in range(1, n + 1):
    print("* " * i)

print()

# Upper Triangular
print("\nUpper Triangle:")
for i in range(n):
    print("* " * (n - i))

print()

# Pyramid
print("\nPyramid Pattern:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
