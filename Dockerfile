FROM python
LABEL maintainer='anmolch8'

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./climate_mutation /climate_mutation

WORKDIR /climate_mutation

EXPOSE 8000

RUN python -m venv /climate_env && \
    /climate_env/bin/pip install --upgrade pip && \
    /climate_env/bin/pip install --upgrade setuptools && \
    /climate_env/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home climate_mutation && \
    mkdir -p /vol/static && \
    mkdir -p /vol/media && \
    chown -R climate_mutation:climate_mutation /vol && \
    chmod -R 755 /vol

  
ENV PATH="/climate_env/bin:$PATH"

USER climate_mutation

