.PHONY: build
build:
		export HORIZONS_TAG=$(shell poetry version -s)
		docker buildx build -f src/docker/Dockerfile --platform linux/amd64 --tag levan.home:5000/horizons-api:${HORIZONS_TAG} --build-arg PYPI_USER=${PYPI_USER} --build-arg PYPI_PASSWORD=${PYPI_PASSWORD} --load .
		docker buildx build -f src/docker/Dockerfile --platform linux/arm64 --tag levan.home:5000/horizons-api:${HORIZONS_TAG} --build-arg PYPI_USER=${PYPI_USER} --build-arg PYPI_PASSWORD=${PYPI_PASSWORD} --load .

.PHONY: push-prod
push-prod: build
		docker push levan.home:5000/horizons-api:$(shell poetry version -s)

HORIZONS_TAG ?= dev
PLATFORM ?= linux/amd64
.PHONY: build-test
build-test:
	docker buildx build -f src/docker/Dockerfile --platform ${PLATFORM} --tag levan.home:5000/horizons-api:${HORIZONS_TAG} --build-arg PYPI_USER=${PYPI_USER} --build-arg PYPI_PASSWORD=${PYPI_PASSWORD} --load .

HORIZONS_TAG ?= dev
.PHONY: run-test-container
run-test-container:
	docker run --rm -p 8003:80 --env DEBUG=true levan.home:5000/horizons-api:${HORIZONS_TAG}
