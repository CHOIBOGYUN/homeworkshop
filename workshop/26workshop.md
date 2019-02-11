1. 학생들의 이름과 나이를 저장하기 위한 폼 클래스를 정의하려고 한다. 다음과 같이 Student 모델이 선언되있다고 가정할때 어울리는 StudentForm 클래스를 작성하세요.

```python
from django import forms
from .models import Student

calss StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
```







2. 위에서 만든 폼클래스를 활용해 템플릿에서 활용하려고 한다. views.py의 코드가 다음과 같을때 new.html에서 사용자가 데이터를 입력할 수 있도록 코드를 작성하세요. (사용자가 데이터를 입력하고 submit 버튼을 누르면 /students/create/ 로 요청을 보내고 method는 post 방식이다.)

```html
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action= "/students/create/" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



