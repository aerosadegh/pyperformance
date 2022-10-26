ARG pyversion

FROM python:${pyversion}-bullseye

WORKDIR /home/
RUN apt update && apt upgrade

RUN pip install pyperformance pyperf