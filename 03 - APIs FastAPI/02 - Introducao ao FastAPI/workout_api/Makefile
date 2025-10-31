run:
	uvicorn workout_api.main:app --host 0.0.0.0 --port 8000 --reload

create-migrations:
	alembic revision --autogenerate -m "migrations"

run-migrations:
	alembic upgrade head

# PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(d)"

# Manually activate the poetry virtualenv in cmd
# "C:\Users\2TT Temperado\AppData\Local\pypoetry\Cache\virtualenvs\workout-api-BecsGRBk-py3.12\Scripts\activate.bat"
