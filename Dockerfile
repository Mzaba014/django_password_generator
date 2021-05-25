FROM python:3.7.2-alpine

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
RUN mkdir /app
WORKDIR /app

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . ./app

CMD ["python"]