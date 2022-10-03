install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main tests/test_main.py

format:
	black main.py

lint:
	pylint --disable=R,C main.py

deploy:
	echo "deploy command goes here"

build:
	docker build -t worldbosskafka .

push:
	docker push worldbosskafka

run:
	python main.py

all: install lint test format deploy run