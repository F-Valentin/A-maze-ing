.PHONY: install run debug clean lint

install:
	pip install -e .
	pip install flake8 mypy build

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pycache__ .mypy_cache build/ dist/ mazegen.egg-info/ *.whl *.tar.gz mazegen/__pycache__
	rm -f maze.txt coords.txt

lint:
	flake8 .
	mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

build_package:
	python3 -m build
