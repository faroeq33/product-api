FROM python:3.10
WORKDIR /app
# Caching the requirements layer here!
COPY ./requirements.txt /tmp
RUN pip install --upgrade -r /tmp/requirements.txt
COPY . /app
EXPOSE 8000
CMD ["python", "api/main.py"]
