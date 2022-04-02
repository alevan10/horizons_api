.PHONY: build
build:
		export HORIZONS_TAG=$(shell poetry version -s)
		docker buildx build -f src/docker/Dockerfile --platform linux/amd64 --tag levan.home:5000/horizons-api:${HORIZONS_TAG} --build-arg PYPI_USER=${PYPI_USER} --build-arg PYPI_PASSWORD=${PYPI_PASSWORD} --load .
		docker buildx build -f src/docker/Dockerfile --platform linux/arm64 --tag levan.home:5000/horizons-api:${HORIZONS_TAG} --build-arg PYPI_USER=${PYPI_USER} --build-arg PYPI_PASSWORD=${PYPI_PASSWORD} --load .

.PHONY: push-prod
push-prod: build
		docker push levan.home:5000/horizons-api:$(shell poetry version -s)
