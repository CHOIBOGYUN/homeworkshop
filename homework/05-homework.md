## 함수190108

### 1.List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다.

### 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
my_list = [1,2,3,4,5,6,7,8]
#my_list = input()
for i in my_list:
    print(i)
```

### 2. 위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.

```python
my_list = [1,2,3,4,5,6,7,8]
#my_list = input()
#idx는 리스트의 인덱스이고 my는 my_list의 각 요소이다.
for idx,my in enumerate(my_list):
    print(idx,my)
```

### 3.딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.

```python
key : for key in my_dict.keys():
value : for value in my_dict.values():
key와 value : for key, value in my_dict.items():
```

### 4.result에 저장된 값은?

```python
def my_func(a, b):
	c = a + b
	print(c)
result = my_func(1, 5)

my_func함수에 return값이 없으므로 None이 저장되어있다..
```



