all: test build

test:
	pep8 kibana_import_indexes.py
	pep257 kibana_import_indexes.py
build:
	docker build -t elk:local .
	kubectl apply -f manifest.yml
