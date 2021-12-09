ARG ARCH=
FROM ${ARCH}python:3.8.6-slim-buster
RUN pip3 install flask
ENV CONTENT="Default Content"
WORKDIR /scripts
ADD app.py .
CMD ["python3","app.py"]
