FROM python:2.7

# install things
RUN apt update \
    && apt install -y ssh \
    && apt -s clean

# create workdir
ENV APP_DIR /app_root
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

# install app dependency
ADD ./requirements.txt ${APP_DIR}
RUN pip install -r requirements.txt

# copy app artifacts
COPY ./app ${APP_DIR}/app
COPY ./conf ${APP_DIR}/conf
COPY ./scripts ${APP_DIR}/scripts

# using gunicorn by default
# to use flask, replace to: ./scripts/flask-start.sh

ENTRYPOINT ["./scripts/gunicorn-start.sh"]
