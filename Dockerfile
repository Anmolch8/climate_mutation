FROM python
LABEL maintainer='anmolch7'
ENV PYTHONUNBUFFERED 1

COPY ./climate_mutation /climate_mutation
COPY ./requirements.txt /requirements.txt
COPY ./pscripts /pscripts

WORKDIR /climate_mutation

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home climate_user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R climate_user:climate_user /vol && \
    chmod -R 755 /vol  && \
    chmod -R +x /pscripts   && \
    chown climate_user:climate_user /climate_mutation && \
    chown climate_user:climate_user /climate_mutation/db.sqlite3

ENV PATH="/pscripts:/py/bin:$PATH"

USER climate_user

CMD ["run.sh"]


