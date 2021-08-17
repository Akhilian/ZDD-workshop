FROM tecktron/python-bjoern

COPY ./app /app
RUN pip install -r ./requirements.txt
