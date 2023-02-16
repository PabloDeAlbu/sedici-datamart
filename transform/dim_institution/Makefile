TABLE_NAME=dim_institution

up:
	@docker run -it --rm --name do_transform_${TABLE_NAME} -v ${PWD}/data:/usr/src/app/data -w /usr/src/app ${TABLE_NAME}-transformer python transformer.py

bash:
	@docker run -it --rm --name do_transform_${TABLE_NAME} -v ${PWD}/data:/usr/src/app/data -w /usr/src/app ${TABLE_NAME}-transformer bash

build:
	docker build -t ${TABLE_NAME}-transformer .

init:
	@echo "Copying data validated from ckan.mincyt"
	@cp -R ../../validation/ckan.mincyt/data .
	@echo "OK"
	@echo "Creating staging area"
	@mkdir -p data/staging
	@echo "OK"
