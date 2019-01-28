## Python 1. 파이썬 기초

Background

```
String,List,Dictionary
if
for
```

goal

```
python programming 언어의 기본 문법이해
반복문에 대한 이해
조건문에 대한 이해
```

problem

1.두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```python
n = input("n을입력해주세요 : ")
m = input("m을입력해주세요 : ")


a ="*"*n
b = f"{a}\n" *m
print(b)
```

2.다음 딕셔너리에서 평균 점수를 출력하시오. ->87.75

```python
student = {'python':80, 'algorithm':99, 'django':89, 'flask':83}
ave = 0
i = 0
for val in student.values():
    ave = ave + val
    i = i + 1
print(f"{ave/i}")

```

3.다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형별 학생수의 합계를 구하시오.

```python
blood_type = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
A = []
B = []
O = []
AB = []

for i in blood_type:
    if i == "A":
        A.append(i)
    elif i == "B":
        B.append(i)
    elif i == "AB":
        AB.append(i)
    elif i == "O":
        O.append(i)
print(len(A))
print(len(B))
print(len(AB))
print(len(O))
```



