run:
	uvicorn account_api.main:app --host 0.0.0.0 --port 8000 --reload

make-migrations:
	alembic revision --autogenerate -m "update database table"

run-migrations:
	alembic upgrade head
	