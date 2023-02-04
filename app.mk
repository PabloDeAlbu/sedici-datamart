
.PHONY: example
example:
	@docker-compose run app

.PHONY: run
run:
	python3 app/main.py 

debug:
	python3 -m pdb app/main.py 

.PHONY: scopus-extract

base-extractor:
	docker build -t base-extractor app/extract/.base
	docker run -it --rm --name ckan-extract -v $(PWD)/app/extract/.base:/usr/src/extractor -w /usr/src/extractor ckan-extract python extractor.py

scopus-extract:
	python3 app/etl/scopus/extract.py
#	@docker-compose -f docker-compose.yml -f app/scopus/docker-compose.yml run --rm app -m pdb scopus/extract.py 

down-scopus:
	@docker-compose -f docker-compose.yml -f app/scopus/docker-compose.yml down -v

build-scopus:
	@docker-compose -f docker-compose.yml -f app/scopus/docker-compose.yml build