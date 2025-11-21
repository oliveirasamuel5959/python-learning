run:
	uvicorn account_api.main:app --host 0.0.0.0 --port 8000 --reload --log-level info

make-migrations:
	alembic revision --autogenerate -m "$(msg)"

migrate:
	alembic upgrade head

# Rollback
downgrade:
	alembic downgrade -1
	