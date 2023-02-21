EXTRACTOR_NAME=base
WORKDIR=${PWD}/usr/src/app/.base

up:
	@echo ""
	@docker run -it --rm --name do_${EXTRACTOR_NAME}_extractor -v $(WORKDIR) -w /usr/src/app ${EXTRACTOR_NAME}-extractor python extractor.py
	@echo ""


build:
	docker build -t ${EXTRACTOR_NAME}-extractor .
