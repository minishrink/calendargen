
YEAR=2020
DEST_DIR=generated
DEST=$(DEST_DIR)/$(YEAR).html

.PHONY: gen clean test default

default: gen

clean:
	rm -rf **/__pycache__ $(DEST_DIR)/*.html

gen:
	python3 main.py $(YEAR) $(DEST)


test:
	pytest

