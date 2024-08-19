"""
constraint
    NOT NULL Constraint
    UNIQUE key Constraint
    PRIMARY Key (unique , not null)
    FOREIGN Key
    CHECK Constraint

query (query)
any - or
10 > any(90 , 10 , 9)
10 > all(90 , 10 , 9)
where 1 or 0 <- EXISTS(query(select 0 or 1))
Set (timezone, role(user))

case
    when cond then result
    when cond then result
    else result
end
coalesce(null , 10)
nullif(1,10)
cast(value as data_type) -> type cast
value::data_type -> type cast

1. Subquery, ANY, ALL, EXISTS, Set
2. CONDITIONAL EXPRESSIONS & OPERATORS (case, coalesce, nullif, cast)
case
     when cond 1 then value
     when cond then value
     when cond then value
     when cond then value
end


ANY  or     -> 20 > any(10,20,30)
ALl  and    -> 20 > all(10,20,30)


Mackarro

    column name !
    table name !
    table1(1,1000) foreign key table2 (1,500)

    terminal :
        ~ = /home/botir
        ~: cd Downloads/
        ~/Downloads :ls
        users.sql
        ~/Downloads : mv users.sql /tmp
        ~/Downloads : cd /tmp
        /tmp : ls
        users.sql
        /tmp : sudo -u postgres psql database_name < users.sql



interview question:
    delete : delete from table_name; truncate table_name;
    update : update table_name set column_name = 'value',column_name = 'value' where cond;
    select : select [*, columns] from table_name where cond order by group by
    insert : insert into table_name(columns) values (values)


"""

