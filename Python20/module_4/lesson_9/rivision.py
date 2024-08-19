""""""
"""
view
    create view view_name as 
    query;
    
select * from view_name;
==========================================

copy (select query) to '/home/dilshod/backups/table.csv'  with delimiter ',' csv header ;
copy table_name(column1 , column2 ....) from '/home/dilshod/backups/table.csv'  with delimiter ',' csv header ;


==========================================

sudo chown -R "$postgres:postgres" path
sudo chmod a+x path

sudo -u postgres pg_restore -d tg_db tg_db.tar

========================================

crontab -e

   time     run command
* * * * *   command

"""