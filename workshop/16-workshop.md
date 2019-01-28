```sqlite
alter table bands add column members integer;

update bands
set members=4
where id=1;

update bands
set members=5
where id=2;

update bands
set members=9
where id=3;
```



```sqlite
update bands
set members=5
where id=3
```



```sqlite
delete from bands
where id=2;
```

