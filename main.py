# Enumerate
# list에 있는 index와 값을 unpacking
for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v)

mylist = ["a", "b", "c", "d"]
# list에 있는 index와 값을 unpacking하여 list로 저장
l = list(enumerate(mylist))
print(l)
# 문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장
e = {i: j for i, j in enumerate(
    'Gachon University is an academic institute located in South Korea.'.split())}
print(e)

# Zip
# for loop + zip
# 두 개의 list의 값을 병렬적으로 추출함
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
# list comprehension + zip
# 각 tuple의 같은 index끼리 묶음
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

# 각 tuple의 같은 index를 묶어 합을 list로 변환
sum = [sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(sum)

#enumerate + zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
# 첫번째 인수는 index
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)
