.PHONY: build

# INSTALLATION #
install:
	python3 -m pip install --upgrade pip
	python3 -m pip install .

install-test:
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[test]"

install-dev:
	python3 -m pip install --upgrade pip
	python3 -m pip install -e ".[test,dev,docs,publish]"

freeze:
	python3 -m pip freeze > requirements.txt

# TESTING #
test:
	python3 -m pytest ./tests

performance:
	python -m kernprof -l -v demo/scope_demo.py
	
# BUILD #
lint:
	flake8 ./src

html:
	make -C docs html

build:
	python3 -m build

build-exe:
	pyinstaller nanograz.spec

publish:
	python3 -m twine upload --repository testpypi dist/*