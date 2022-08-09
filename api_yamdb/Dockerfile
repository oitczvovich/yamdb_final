FROM python:3.7-slim
WORKDIR /app
COPY /api_yamdb ./app
RUN ls .
RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
