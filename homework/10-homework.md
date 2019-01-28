### 1. CSS 는 무엇의 약자인가?

(1) Creative Style Sheets
(2) Cascading Style Sheets
(3) Computer Style Sheets
(4) Colorful Style Sheets

- 답 : 2번



### 2. 다음 중 맞으면 T, 틀리면 F 를 기입 하시오.

- HTML과CSS는 각자 문법을 갖는 별개의 언어이다. [ T ]
- 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. [ T ]
- 자식요소프로퍼티는 부모의 프로퍼티를 모두 상속받는다. [ F ]



### 3. 크기 단위 em 은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

```css
font-size: rem;
```

- rem 을 사용하면 된다.



### 4. 다음 예제를 통해 "후손 셀렉터"와 "자식 셀렉터"의 차이를 설명하시오.

```css
/* 후손셀렉터 */
div p {
    color: crimson;
}

/* 자식셀렉터 */
div > p {
    color: crimson;
}
```

- div p 의 경우 div 셀렉터 아래 있는 모든 p에 영향을 주기 때문에 위의 코드로 div 아래 있는 모든 p 셀렉터의 색을 crimson으로 변화시킨다.
- div > p 의 경우 div 셀렉터 바로 아래 자식 셀렉터의 p에만 영향을 주기 때문에 위의 코드로 div 바로 아래있는 p 셀렉터의 색을 crimson으로 변화시킨다.