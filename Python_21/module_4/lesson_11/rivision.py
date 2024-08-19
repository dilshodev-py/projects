""""""
"""
          DBMS - Data Base Management System
    sql         nosql
    DBMS        NoDBMS
    web         mobile
    
PostgreSql
    DDL -> create , alter , drop , truncate
    DML -> insert , update , select , delete
    TCL -> begin , commit , rollback , savepoint
    DCL -> grant , revoke

table [create , alter , drop]
    create table table_name( # primary key
        col1_name type constraint,
        col2_name type constraint,
        col3_name type constraint,
        col4_name type constraint,
        col5_name type constraint,
    )
    
    alter table table_name [drop , rename , add , alter] [col , column]  
    
    drop table if exists table_name cascade;
    
function

    create function function_name (arg1 type , arg2 type ....)
    returns [table ,setof , varchar , trigger]
    language plpgsql
    as 
    $$
        declare
            var1 type;
            var2 type;
            var3 type;
        begin 
            logic
        end
    $$
    
    
VIEW
    
    create view view_name as query;
    
    
select * from view_name;
    
trigger 
    create trigger trigger_name
    [before , after] [delete , insert , update] on table_name
    for each row execute function function_name();
    
    create trigger trigger_name
    [before , after] [delete , insert , update] on table_name
    insert into delete_table(col1 , col2) values (OLD.value)
    
    
data type
    int             -2^31 between +2^31    4 byte
    integer         -2^31 between +2^31    4 byte
    bigint          -2^61 between +2^61    8 byte
    smallint        -2^15 between +2^15    2 byte
    float           1.0 , 3.31
    numeric         1.0 , 3.31
    varchar         text (255)
    text            text (inf)
    char            char (200)
    decimal         1.0 , 3.31
    date            YY-mm-dd
    timestamp       YY-mm-dd HH:MM:SS +tz
    year, day , month , hour , min , sec     extract()
    time            HH:MM:SS +tz
    jsonb           {key : value}
    array           {1,2,3,4,5,6,7}
    bool           
        True   , t , yes , 1
        False  , f , no , 0


constraint
    not null
    unique
    foreign key
    primary key
    check
    

CONDITIONAL EXPRESSIONS & OPERATORS

    case 
        '''
        case 
            when cond1 then value
            when cond2 then value
            when cond3 then value
            when cond4 then value
            else value
        end 
            
        '''
         
        
        
    coalesce
        coalesce(20, 10)
        
        
    nullif
        nullif(1,10)
        
        
    cast
        cast('2024-04-16' as date)
        '2024-04-16'::datetime
        
        
SET OPERATORS
        
    FILTERING DATA
        WHERE 
        AND Operator
        OR Operator
        OFFSET 5 LIMIT 5
        OFFSET 5 FETCH FIRST 5 ROW ONLY 
        IN        6 IN (1,2,3,4,5)  
        COLUMN_NAME BETWEEN 3 AND 10  
        LIKE && ILIKE   startswith 'ba%' ,  endswith '%ba_' , '%ba%' , '_ba%'
        COLUMN_NAME IS NULL 
        COLUMN_NAME IS NOT NULL 
        
        
DML 
    select [* , columns] from table_name [join ....] where conds [group by ....]  [order by ...] [limit ...]
    insert into table_name (cols_name) values (cols_value),(cols_value), (cols_value), (cols_value), (cols_value) returning [col_name , *] 
    update table_name set column_name = 'New value' , ... where condition (subquery);
    delete from table_name where condition;
    
DCL
    grant 
        grant [insert , select , truncate , update , delete] on [table_name , all tables in schema schema_name] to role
    
    revoke 
        revoke [insert , select , truncate , update , delete , all privalages] on [table_name , all tables in schema schema_name] from role
    
    
    
    
join:
    inner join    kesishgan soxasi
    left join     chap table ni barcha soxasi
    right join    o'ng table ni barcha soxasi
    full join     full soxasi
    cross join    combinatsiya
    
    
    
    
    
    
subquery
    query (query)
    
    
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
    left(10)
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
    random        0 and 1
    current_date
    current_timestamp
    current_time
    

    
    
backup
    terminal : chown -R "$postgres:postgres" file or folder path
    terminal : chmod +rxwa folder_path
    
    terminal : sudo -U postgres pg_dump -u postgres -F tar -f file_path -d database_name
    terminal : sudo -U postgres pg_restore -d database_name < file_path.tar
    

    
linux command:
    touch file_name           create
    mkdir  papka_create ->    create
    cd path             ->    change location 
    cp                  ->    copy
    mv                  ->    file or folder ko'chirib o'tadi
    cat file_name       ->    file read
    nano file_name      ->    edit in file 
    ls                  ->    list
    cd ..               ->    back
    rm -rf              ->    remove  
    chmod               ->    permission to file or folder
    chown               ->    change user to file or folder
    clear               ->    tozalash
    poweroff            ->    
    reboot              ->    restart
    history             ->    commands list

postgres command:
    \dt             ->    current database table list
    \d+             ->    sequence + table list
    \du+            ->    user or role list
    \df+            ->    function list
    \d table_name  ->     table info
    \dv             ->    view list
    \c database_name ->  change database
    set time zone = 'Asia/Tashkent'
    \timing
    
    
having
    group by + having (condition agg_function)
    
    
    
crontab 
    terminal : crontab -e
        time format (* * * * *) run command
    
    
    


backup.sh
    BACKUP_DIR="/home/dilshod/backups/"
    FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S-%p`.tar
    PGPASSWORD='1' pg_dump -U postgres -h localhost dvdrental -F tar -f $FILE_NAME
    
"""

# . path/backup.sh


# d = {
#     1 : 'bir',
#     2 : 'bir',
#     3 : 'bir',
#     4 : 'bir',
# }

# l = [11,2,3,4,50]
# l[4]
# print(d[4])





