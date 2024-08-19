mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver

celery:
	celery -A root worker -l INFO

flower:
	celery -A root.celery.app flower --port=5001

bit:
	celery -A root beat -l info


