
clean:
	rm -rf *.csv

init: update

update:
	./update.py
