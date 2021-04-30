clean:
	pip uninstall -y pincode
	rm -rf build src/pincode.egg-info
	rm -rf pincode.egg-info build dist

gen:
	./gen.sh

install: clean gen
	python setup.py sdist install
