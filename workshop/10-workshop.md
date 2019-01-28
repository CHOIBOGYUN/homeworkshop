Background

```
HTML
```

Goal

```
 CSS Selector 를 이해한다.
 CSS 프로퍼티를 이해한다.
```

| Problem

Selector 를 활용한 DOM 탐색 실습.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <style>
        #ssafy > p:nth-child(2){
            color:red;}
        #ssafy > p:nth-of-type(2){
            color: blue;
        }
        
    </style>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
            
</body>
</html>
```



![1547540499745](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540499745.png)

```
어떤게 선택될까?
첫번째 단락(빨간 글씨)

두번째 단락(파란색 글씨)

세번째 단락

네번째 단락
```

