PYTHON ?= .venv/bin/python
PIP ?= $(PYTHON) -m pip
UVICORN ?= $(PYTHON) -m uvicorn

USER_SERVICE_DIR := services/user_service
QUIZ_SERVICE_DIR := services/quiz_service

.PHONY: help install clean check lint run-user run-quiz run-all

help:
	@echo "Available commands:"
	@echo "  make install          # Install dependencies in .venv"
	@echo "  make clean            # Remove .venv and __pycache__"
	@echo "  make check            # Check Python syntax"
	@echo "  make run-user         # Run User Service"
	@echo "  make run-quiz         # Run Quiz Service"
	@echo "  make run-all          # Run both services in parallel (background)"
	@echo "  make prep             # Prepare project for git push"

install:
	python3.11 -m venv .venv
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +

check:
	@echo "Checking Python syntax..."
	find . -name "*.py" | xargs python -m py_compile
	@echo "All syntax checks passed!"

run-user:
	$(UVICORN) services.user_service.app.main:app --reload --port 8000

run-quiz:
	$(UVICORN) service.quiz_service.app.main:app --reload --port 8001

run-all:
	$(UVICORN) $(USER_SERVICE_DIR)/app.main:app --reload --port 8000 & \
	$(UVICORN) $(USER_SERVICE_DIR)/app.main:app --reload --port 8001 & \
	wait

prep:
	$(MAKE) check
	
