FROM ubuntu:latest
MAINTAINER 0neb1n "barcodecrow@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["/bin/bash"]
CMD ["python", "app.py"]
