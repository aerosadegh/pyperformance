ARG pyversion

FROM python:${pyversion}-bullseye

WORKDIR /home/
RUN apt update && apt upgrade

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "sh", "entrypoint.sh" ]
