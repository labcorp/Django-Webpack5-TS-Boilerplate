FROM node:18-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    yarn

# Python 3.11 stuff
RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED

# setup python and pip since we're using node image as base
RUN python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools==45 && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . .

RUN pip install -r requirements-dev.txt
RUN yarn install --frozen-lockfile --non-interactive --no-progress --ignore-optional

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
