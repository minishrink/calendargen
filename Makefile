
YEAR=2020
DEST=generated/$(YEAR).html

.PHONY: gen clean test default

default: gen

clean:
	rm -rf **/__pycache__ examples/*.html

gen:
	python3 main.py $(YEAR) $(DEST)


test:
	pytest

