# primitive types: int, float, bool, str, None, bytes

# compound types: list, tuple, set, dict

# list is a ordered collection of elements.
# Each individual element can be of any type.

l = [1, "abcd", 0.32, True, None, [1, 2, 3]]
# print(l)
# print(type(l))
# print(len(l))
# l.append(100)
# print(l)
# l.pop(2)
# print(l)
l.extend(["x", "y", "z"])

# extending list l1 with list l2 means adding all elements of l2 to l1 at the end
print(l)

# x += 3  # x = x + 3
# l += ["a", "b", "c"]
l = l + ["a", "b", "c"]  # l.extend(["a", "b", "c"])
print(l)

l2 = ["xyz", "hello", "foo", "bar", "abc"]  # l2[2] = "foo"
l2.sort()  # lexico-graphical order sorting or dictionary order sorting
print(l2)
l2.reverse()
print(l2)

## Tuple: ordered collection of elements
# Difference between list and tuple is that tuple is **immutable**.

# Example: coordinates of a point in 2D space
# (x, y)

x = 10
y = 20
point1 = (x, y)
point2 = (5.5, 10.6)

point3 = (point1[1], point1[0])
print(point1, point2, point3)

x = 10
y = 20
v1, v2, v3 = x, y, x  # (x, y, x) ==> tuple
print(v1, v2, v3)
# x, y -> (10, 20)
# y, x = (10, 20) ==> y = 10, x = 20

r, g, b = 255, 255, 0
col = (255, 255, 0)
# ffff00 -> 15 * 16 + 15 = 255

## Set: unordered collection of elements

# set is a collection of unique elements

s = {1, 2, 3, 4}
# s.add(11)
# s.pop() # delete the smallest element
print(s)

s2 = {3, 4, 5, 6}
s3 = s.union(s2)
print(s3)
print(s.intersection(s2))
print(s.difference(s2))
print(s.symmetric_difference(s2))

## Dictionary: unordered collection of key-value pairs

# key: value

d = {"name": "John", "age": 20, "city": "London"}
print(d)
print(d["name"])
try:
    print(d["xyz"])
except KeyError:
    print("Key does not exist")
print(d.get("surname", "Doe"))
print(d.get("age", 10))

d["surname"] = "Doe"
print(d)

for key in d:
    print(key, d[key])

print("---------")

for key, value in d.items():
    print(key, value)

print(list(d))
print(list(d.keys())) # same as above
print(list(d.values()))
print(list(d.items()))
