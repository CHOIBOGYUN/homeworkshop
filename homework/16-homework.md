아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.



```sqlite
create table friends(
    id INTEGER.
    name TEXT,
    location TEXT
);
```

해당 테이블에 다음과 같이 데이터를 입력한다.

```sqlite
insert into friends values (1, "Justin", "Seoul");
insert into friends values (2, "Simon", "New York");
insert into friends values (3, "Chang", "Las Vegas");
insert into friends values (4, "John", "Sydney");
```

스키마를 다음과 같이 변경한다.

```sqlite
alter table friends add column married INTEGER;
```

데이터를 다음과 같이 추가한다.

```sqlite
update friends set location="LA" where id=1;
update firends set location="LasVegas" where id=2;
update friends set married=1 where id=1;
update friends set married=0 where id=2;
update friends set married=0 where id=3;
update friends set married=1 where id=4;
```

아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

married 가 0 인 데이터를 모두 삭제한다.

```sqlite
delete from friends where married=0;
```

테이블을 삭제한다.

```sqlite
drop table friends
```

