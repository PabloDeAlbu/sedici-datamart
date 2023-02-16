TABLE_NAME=dim_institution

up:
	@docker run -it --rm --name do_load_${TABLE_NAME} -v ${PWD}/data:/usr/src/app/data -w /usr/src/app ${TABLE_NAME}-loader python loader.py

bash:
	@docker run -it --rm --name do_load_${TABLE_NAME} -v ${PWD}/data:/usr/src/app/data -w /usr/src/app ${TABLE_NAME}-loader bash

build:
	docker build -t ${TABLE_NAME}-loader .

init:
	@echo "Copying data from staging\n"
	@cp -R ../../transform/dim_institution/data/staging/ data
	@ls data/staging
	@echo "\nCopy succesfull"

prune:
	@echo "Pruning data"
	@rm -rf data/*
	@echo "OK"
