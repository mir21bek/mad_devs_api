.DEFAULT_GOAL := help

install:
		pip install $(LIBRARY)

migrate-create:
		alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
		alembic upgrade head