FROM python:3

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR ./geekshop-server
COPY . ./geekshop-server
RUN pip install -r ./geekshop-server/requirements.txt
