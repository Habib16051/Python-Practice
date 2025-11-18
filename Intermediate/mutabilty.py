# Problem 1 — Mutability: Why this changes both lists?

a = [[1,2,3]] * 3
a[0][0] = 100
print(a) # All rows reference the same inner list, since * performs shallow replication.

# Output: [[100, 2, 3], [100, 2, 3], [100, 2, 3]]
x = [[1,2,3] for _ in range(3)]
print(x)
