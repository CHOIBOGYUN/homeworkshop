```SQLITE
CREATE TABLE bands(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    debut INTEGER NOT NULL
);

INSERT INTO bands VALUES(1, "Queen", 1973);
INSERT INTO bands VALUES(2, "Coldplay", 1998);
INSERT INTO bands VALUES(3, "MCR", 2001);
```

### bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```sqlite
SELECT id, name FROM bands;
```

### bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

```sqlite
SELECT name FROM bands WHERE debut<2000;
```

