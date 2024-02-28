run_server:
	uvicorn api:app --host 0.0.0.0 --port 8000 --reload

generate_requirements:
	poetry export -f requirements.txt --output requirements.txt

generate_dev_requirements:
	poetry export -f requirements.txt --output requirements-dev.txt --dev

run_tests_with_coverage:
	pytest tests -x -vv --cov=. --cov-report=term-missing --cov-fail-under=95

lint:
	ruff .

format:
	black .

push-check:
	@echo "Checking if the code is ready to be pushed"
	@echo "Running tests"
	@make run_tests_with_coverage
	@echo "Running linter"
	@make lint
	@echo "Running formatter"
	@make format
	@echo "All checks passed"
