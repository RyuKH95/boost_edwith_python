# # 일반 코드
# colors = ["a", "b", "c", "d", "e"]
# result = ""

# for s in colors:
#     result += s

# print(result)

# # pythonic code
# colors = ["red", "blue", "green", "yellow"]
# result = "".join(colors)

# print(result)

# split
items = 'zero one two three'.split()
print(items)

example = 'python,jquery,javascript'
print(example.split(","))
a, b, c = example.split(",")  # unpacking
print(a, b, c)

# join
colors = ["red", "blue", "green", "yellow"]
result = ''.join(colors)
print(result)
result = ' '.join(colors)
print(result)
result = ', '.join(colors)
print(result)
result = '-'.join(colors)
print(result)
