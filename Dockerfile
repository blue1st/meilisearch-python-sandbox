FROM python:3
COPY ./app/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN curl --compressed -OL https://docs.meilisearch.com/movies.json && mv movies.json /tmp/movies.json
