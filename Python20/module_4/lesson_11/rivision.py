""""""
from math import log2

"""
          DBMS
    sql         nosql
    
PostgreSql
    DDL -> create , drop , alter 
    DML -> select  , update , delete , insert , truncate
    TCL -> grant , revoke
    DCL -> begin , rollback , commit

table
    create table table_name(
        col1 type constraint,
        col1 type constraint,
        col1 type constraint,
        col1 type constraint,
        col1 type constraint,
    )
    drop table table_name CASCADE;
    
    alter table table_name [add column , drop column , rename , alter column, rename column] column_name options
    
function
    create function func_name
    return [trigger , table () , setof table]
    language plpgsql
    as
    
    $$
        declare
            var data type;
            var data type;
        begin 
            # logic query
        end;
    $$
    drop function func_name;
    
VIEW
    create VIEW view_name as query id,  name long ;
    
    
    select name from view_name;
    
    drop view view_name;
    
sequence
    create sequence sequence_name 
    INCREMENT 1
    START 1
    MINVALUE 1 
    MAXVALUE 3
    cycle;
    
    drop sequence sequence_name;
    
trigger 
    create trigger trigger_name
    [before , after] [update , insert, delete] on table_name
    for each row
    execute function function_name;
    
    
    drop trigger trigger_name on table_name;
    
    
data type
    int       -2^31 to +2^31     4 bytes
    integer   -2^31 to +2^31     4 bytes
    bigint    -2^63 to 2^63      8 bytes
    float     1.0 , 2.0        
    smallint  -2^15 to +2^15     2 bytes
    numeric   1.0 , 2.0 
    varchar   default 255
    text      bez limit
    char      default 1     10
    decimal   1.0 , 2.0 
    date      YY-mm-dd
    timestamp YY-mm-dd HH:MM:SS
    year      YY
    time      HH:MM:SS
    jsonb     {key : value , key : value} or [1,2,3,4,5,5,6,7]
    array     {1,2,3,4,5,6,7,8}
    bool      
        True  1 , t , yes
        False 0 , f , no


constraint
    not null 
    unique
    check
    varchar(255)
    primary key -> not null , unique
    foreign key

CONDITIONAL EXPRESSIONS & OPERATORS

    case  
        '''
        case 
            when cond then value
            when cond then value
            when cond then value
            else value
        end case;
            
        '''
    coalesce
        balance - coalesce(amount , 0)
        
    nullif
        nullif()
        
    cast
        CAST(DATA AS INTEGER)
        DATA::INTEGER
        
SET OPERATORS

    UNION
        SELECT TABLE1
        UNION
        SELECT TABLE2
        
        SELECT TABLE1
        INTERSECT
        SELECT TABLE2
        
        SELECT TABLE2
        EXCEPT
        SELECT TABLE1
        
        
    FILTERING DATA
        WHERE 
        AND Operator
        OR Operator
        OFFSET 5 LIMIT 1
        OFFSET 5 FETCH FIRST 1 ROW ONLY 
        IN        6 IN (1,2,3,4,5)  
        COLUMN_NAME BETWEEN 3 AND 10  
        LIKE && ILIKE   startswith 'ba%' ,  endswith '%ba_' , '%ba%' , '_ba%'
        COLUMN_NAME IS NULL 
        COLUMN_NAME IS NOT NULL 
        
        
DML 
    select distinct [* , cols] from table_name where cond1 and cond2 or cond3 [order , group , limit]
    insert into table_name(col1 , col2 , col3) values (val1 , val2 , val3)
    insert into table_name(col1 , col2 , col3) values (%s , %s , %s) returning id , col1   in python
    delete from table_name where col1 = val1 and cond2 or cond3 returning *;
    update table_name set col1 = new_value , col2 = new_value where cond returning col1;
    truncate table_name;
    
    
TCL
    grant    permission berish [insert , update , delete , truncate , select, all]
        grant [insert , update , delete , truncate , select, all] on [table_name, public] to user_name
    revoke   permission olish  [insert , update , delete , truncate , select, all]
        revoke [insert , update , delete , truncate , select, all] on [table_name, public] from user_name
        
join:
    inner join = join      to'plamlarni bog'langan sohasi
    left join              chap to'plam full sohasi
    right join             o'ng to'plam full sohasi
    full join              barcha soha
    join cross             combinatsiya  
    
subquery
    query (query (query))    
    
functions:
    min
    max
    div
    mod
    sum
    count
    avg
    array_agg  {val1 , val2}
    string_agg "val1,val2"
    cast()
    replace 
    substr
    left
    right
    length
    ceil
    round
    floor
    EXP
    LOG
    power
    pi
    sign
    sqrt 
    trunc
    random
    current_date
    current_timestamp
    current_time
    
index
    create index index_name on table_name(col_name);
    
    drop index index_name;
    
    
backup
    sudo chown -R '$postgres:postgres' dir_path   
    sudo chown -R '$postgres:postgres' ~
    
    sudo -u postgres pg_dump -F tar -f dir_path/file.tar -d lesson_11;
    sudo -u postgres pg_restore -d lesson_11 dir_path/file.tar
    
    
linux command:
    touch file_name     ->  file create
    mkdir  papka_create ->  papka create
    cd path             -> location change
    cp file_or_dir_path other_location
    mv file_or_dir_path other_location
    cat file_name       -> read
    nano file_name      -> write
    ls                  show file or dir
    rm                  -> remove file or dir
    chmod               -> permission file dir
    chown               -> permission file dir for user
    cd ..               -> back
    clear               -> terminalni tozalash
    poweroff            -> off laptop
    reboot              -> restart laptop
    history             -> command list

postgres command:
    \dt             -> table list
    \d+             -> table list + 
    \du+            -> users list
    \df+            -> functions list
    \d table_name  -> table info
    \dv             -> views list
    \c database_name
    set time zone = 'Asia/Tashkent'
    \timing
    
    
having
    select a.* , count(fa.actor_id) from actor a
    join film_actor fa on a.actor_id = fa.actor_id
    where a.actor_id = 1
    group by a.actor_id
    having  count(fa.actor_id) > 30;
    
    
crontab 
    in terminal : crontab -e
    in crontab : * * * * * /home/dilshod/backups/backup.sh


backup.sh
    BACKUP_DIR="/home/dilshod/backups/"
    FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S-%p`.tar
    PGPASSWORD='1' pg_dump -U postgres -h localhost lesson_7 -F tar -f $FILE_NAME
    
"""





