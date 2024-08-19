init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
extract:
	pybabel extract -k _:1,1t -k _:1,2 -k __ --input-dirs=. -o locales/messages.pot

compile:
	pybabel compile -d locales -D messages

update:
	pybabel update -d locales -D messages -i locales/messages.pot