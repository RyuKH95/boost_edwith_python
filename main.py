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

# # split
# items = 'zero one two three'.split()
# print(items)

# example = 'python,jquery,javascript'
# print(example.split(","))
# a, b, c = example.split(",")  # unpacking
# print(a, b, c)

# # join
# colors = ["red", "blue", "green", "yellow"]
# result = ''.join(colors)
# print(result)
# result = ' '.join(colors)
# print(result)
# result = ', '.join(colors)
# print(result)
# result = '-'.join(colors)
# print(result)


# for loog + append 사용하기
result = []
for i in range(10):
    result.append(i)
print(result)

# list Comprehension 사용하기
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

# Nested For loop
# 한 배열에 모두 들어감
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

# Nested For loop + if문
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [i+j for i in case_1 for j in case_2 if i != j]
print(result)
result.sort()
print(result)

# split + list Comprehension
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)
