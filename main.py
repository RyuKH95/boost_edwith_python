# Lambda
# 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
# 수학의 람다 대수에서 유래함
# Reduce
from functools import reduce

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
