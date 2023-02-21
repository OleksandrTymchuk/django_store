FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_project
WORKDIR /django_project
ADD . /django_project/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /django_project/

ENTRYPOINT ["./docker/python/entrypoint.sh"]