"""DATABASE -> malumotlar ombori"""
from math import log2

"""
                DATABASE
RDBMS                           NORDBMS
sql                             nosql


"""


"""
file
    json
    txt
    csv
    excel



service
    Postgresql
    MySql
    Oracle
    

DBMS -> DataBase Management System
    SQL   - Structured Query Language 
        DML - Data Manipulation Language
            select , update , delete , insert
        DDL - Data Definition Language
            create , alter , drop , truncate
        DCL - Data Control Language
            Grant , Revoke -> USER , ROLL
        TCL - Transaction Control Language
            Save point , Roll back , Commit
       
       
"""
print(log2(9223372036854775808))


"""
DATA TYPE
    boolean -> true , false , 0 , t , f , 1 , yes  , no
    character -> char , varchar , text
        char(8) -> 1234              
        varchar -> hello
        text    -> description
    numeric int -> smallint , integer , bigint
        smallint limit -> -2^15 to 32,767
        integer limit -> -2^31 to 2,147,483,647
        bigint limit  -> -2^63 to +9223372036854775807
    
    Float -> float(2) , real or float8 , numeric(9,2)
    
    Temporal -> date , timestamp, timestamptz , time , interval
        date -> %Y-%m-%d
        timestamp -> %Y-%m-%d %H:%M:%S
        timestamptz ->  %Y-%m-%d %H:%M:%S
        time     -> %S
    JSON - json , JSONB
        json -> {"id" : 1 , }
        jsonb -> b{"id" : 1 , }
        
    UUID -> UUID date time  
        
    serial -> integer , autoincrement
    
"""




