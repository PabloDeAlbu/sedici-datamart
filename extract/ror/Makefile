EXTRACTOR_NAME=ror
WORKDIR=${PWD}/usr/src/app/ror

up:
	@echo ""
	@docker run -d -it --rm --name do_${EXTRACTOR_NAME}_extractor -v $(WORKDIR) -w /usr/src/app ${EXTRACTOR_NAME}-extractor 
	@echo ""


build:
	docker build -t ${EXTRACTOR_NAME}-extractor .
