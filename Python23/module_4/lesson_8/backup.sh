BACKUP_DIR="/home/dilshod/backups/"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S`.tar
PGPASSWORD='1' pg_dump -U postgres -h localhost -d lesson_7 -F tar -f $FILE_NAME