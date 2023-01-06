# DATA STRUCTURES

### #4.0 Methods

1. data structure - 데이터를 구조화하고 싶을 때 사용하는 것
2. method는 데이터에 결합된 function

   ```python
   name = 'nico'
   print(name.upper())
   #.upper()이 method
   ```

### #4.1 Lists

1. 리스트 작성법

   ```python
   list명 = [" " , " " , " "]
   ```

2. .count() ➡️ 리스트에 아이템이 얼마나(개수) 있는지
3. .clear() ➡️ 리스트 안에 있는 아이템 삭제
4. .reverse() ➡️ 아이템을 역뱡향으로 출력
5. .append() ➡️ 리스트에 아이템 추가
6. .remove() ➡️ 아이템 삭제

### #4.2 Tuples

```python
days = ("Mon","Tue","Wed")
```

1. tuple은 바뀔 수 없다

### #4.3 Dicts

```python
player = {
 'name' = 'noco'
	'age'=12
}
```

### #4.5 For Loops

```python
websites = (

)
for each in websites:
		print("hello")
```

### #4.6 URL Formatting

```python
for website in w3ebsites:
	if not website.startswith("https://"):
		website = f"https://{website}"
	print(website)
```

## #4.7 Requests

1. pypi ➡️ 다른 사람들이 만든 Project, module을 모아둔 곳
2. requests ➡️ python 코드에서 웹사이트로 request 보내는 걸 할 수 있게 해준다

```python
from requests import get
```

### #4.8 Status Codes
