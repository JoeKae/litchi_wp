ifeq ($(OS),Windows_NT)
    RM = del /Q /F
    RRM = rmdir /Q /S
else
    RM = rm -f
    RRM = rm -f -r
endif

stubs-test:
	stubtest litchi_wp

stubs:
	stubgen src/litchi_wp -o src

tests:
	python -m unittest discover -s tests -t tests -v

major: tests
	python -m bumpver update --major

minor: tests
	python -m bumpver update --minor

patch: tests
	python -m bumpver update --patch

docs:
	python -m pdoc --docformat google ./src/litchi_wp/action.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/altitude.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/enums.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/gimbal.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/photo.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/poi.py -o ./docs
	python -m pdoc --docformat google ./src/litchi_wp/waypoint.py -o ./docs

build: tests
	$(RRM) dist
	python -m build

publish-test: docs build
	twine upload -r testpypi dist/*

publish: docs build
	twine upload dist/*


.PHONY: docs tests