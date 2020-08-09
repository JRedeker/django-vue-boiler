# django-vue-boiler
A boilerplate / github template (and quick example) for using Django and Postgres with a Vue frontend

# Instructions
load initial test data with:
`python manage.py loaddata setup_data.yaml`

build with:
``

run with:
`python manage.py runserver &`
`cd frontend`
`npm run dev &`

# Note
This uses the full js experience of vue-cli with npm/webpack to serve the front end rather than using Django templates.

# Todos
- pass shopping list data to vue frontend
- create vue frontend cards for shopping list
- add fonts and material icons