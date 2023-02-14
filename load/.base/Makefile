TABLE_NAME=base
WORKDIR=${PWD}/usr/src/app/loader

up:
	@echo ""
	@docker run -it --rm --name do_${TABLE_NAME}_loader -v $(WORKDIR) -w /usr/src/app ${TABLE_NAME}-loader python loader.py
	@echo ""


build:
	docker build -t ${TABLE_NAME}-loader .
