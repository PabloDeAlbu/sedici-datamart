EXTRACTOR_NAME=datasets.datos.mincyt
WORKDIR=${PWD}/app/extract/${EXTRACTOR_NAME}

up:
	@echo ""
	@docker run -it --rm \
		--name do_${EXTRACTOR_NAME}_extractor \
		--mount type=bind,source=${WORKDIR}/data,target=/usr/src/app/data \
		-w /usr/src/app ${EXTRACTOR_NAME}-extractor \
		python -m ckan_downloader
	@echo ""


build:
	docker build -t ${EXTRACTOR_NAME}-extractor .

bash:
	@echo ""
	@docker run -it --rm --name do_${EXTRACTOR_NAME}_extractor -v $(WORKDIR) -w /usr/src/app ${EXTRACTOR_NAME}-extractor bash
	@echo ""
