1. 투표를 위한 설문조사 앱을 만들려고한다. 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇표를 받았는지 저장하는 기능을 가지고 있다. 설문조사 앱은 Question 모델과 Choice 모델을 가지고 있다. 그리고 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 가지고 있다.

   

   ​Question 하나를 보여주는 페이지에서 Choice를 위의 오른쪽 그림과 같이 출력하려고 한다. html파일에서 내용과 투표수를 출력해주는 코드를 작성하세요. 현재 html파일에는 아래와 같은 코드가 들어있다고 가정한다.	

   ```html
   <h1>
       {{question.title}}
   </h1>
   {% for choice in question.choice_set.all %}
   	<h5>{{choice.content}}</h5>
   	<h5>{{choice.votes}}</h5>
   {% endfor %}
   ```

   

