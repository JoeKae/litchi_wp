patch:
	python -m bumpver update --patch

docs:
	python -m pdoc ./src/litchi_wp/action.py -o ./docs
	python -m pdoc ./src/litchi_wp/altitude.py -o ./docs
	python -m pdoc ./src/litchi_wp/enums.py -o ./docs
	python -m pdoc ./src/litchi_wp/gimbal.py -o ./docs
	python -m pdoc ./src/litchi_wp/photo.py -o ./docs
	python -m pdoc ./src/litchi_wp/poi.py -o ./docs
	python -m pdoc ./src/litchi_wp/waypoint.py -o ./docs

build:
	rm dist/*
	python -m build

publish-test: docs build
	twine upload -r testpypi dist/*

publish: docs build
	twine upload dist/*


.PHONY: docs