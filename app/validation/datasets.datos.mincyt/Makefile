SOURCE=datasets.datos.mincyt
WORKDIR=${PWD}/app/validation/${SOURCE}
RAW_DATA=${PWD}/app/extract/${SOURCE}/data


init:
	@echo ""
	@mkdir -p ${WORKDIR}/data
	@cp -R ${RAW_DATA} ${WORKDIR}/
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		great_expectations init 
	@echo ""


build:
	docker build -t ${SOURCE}-validator .

bash:
	@echo ""
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		bash
	@echo ""

datasource_new:
	@echo "Pulling data from ${RAW_DATA}"
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		great_expectations datasource new
	@echo ""


checkpoint_new:
	@echo ""
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		great_expectations datasource new
	@echo ""

suite_help:
	@echo ""
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		great_expectations suite --help
	@echo ""

docs_help:
	@echo ""
	@docker run -it --rm\
		--name do_${SOURCE}_validation \
		--mount type=bind,source=${RAW_DATA},target=/usr/src/app/data \
		--mount type=bind,source=${WORKDIR},target=/usr/src/app/ \
		-w /usr/src/app ${SOURCE}-validator \
		great_expectations docs --help
	@echo ""
