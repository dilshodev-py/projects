BACKUP_DIR="/home/dilshod/PycharmProjects/Python23/module_4/lesson_7/backups/"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S-%p`.csv
PGPASSWORD='1' sudo -S <<< "123" -u postgres psql -U postgres -d lesson_7 -c "copy departments to '$FILE_NAME'  delimiter ',' csv header "