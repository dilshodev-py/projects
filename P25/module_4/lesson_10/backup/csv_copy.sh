BACKUP_DIR="/home/dilshod/PycharmProjects/P25/module_4/lesson_10/backup/"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S`.tar
PGPASSWORD='1' pg_dump -h localhost -U postgres -F tar -f $FILE_NAME -d lesson_8



#  sudo chown "$postgres:postgres" backup/backup_command.sh
#  sudo chmod 777 backup/backup_command.sh
