# FastAPI Poetry Example project

How to run fast API server:
uvicorn api:app --host 0.0.0.0 --port 8000 --reload

How to generate requirements:
poetry export -f requirements.txt --output requirements.txt

How to generate dev requirements:
poetry export --dev -f requirements.txt --output requirements-dev.txt