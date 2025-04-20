editable:
	@echo "Making the project editable"
	uv pip install -e .

dev: 
	@echo "Installing development dependencies"
	uv pip install -e .[dev]

test:
	@echo "Running tests"
	pytest -v ./tests

