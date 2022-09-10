FROM python:3.9.12
ARG PYPI_USER
ARG PYPI_PASSWORD
WORKDIR /opt/horizons
COPY src/ api/
ENV PYTHONPATH "/opt/horizons:/opt/horizons/api:/opt/horizons/api/horizons_web_service"
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN pip install --upgrade pip;\
    pip install poetry;\
    poetry config http-basic.home $PYPI_USER $PYPI_PASSWORD;\
    poetry config virtualenvs.create false && poetry install -v --no-dev
CMD ["uvicorn", "api.horizons_web_service.app:app", "--host", "0.0.0.0", "--port", "80"]
