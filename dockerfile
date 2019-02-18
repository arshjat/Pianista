FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y python3-pip && \
    apt-get install -y sudo curl wget locales && \
    rm -rf /var/lib/apt/lists/*

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install unicode-slugify
RUN pip install --upgrade setuptools
RUN pip3 install --upgrade setuptools
RUN localedef -i en_US -f UTF-8 C.UTF-8 
ENV LANG="C.UTF-8"
ENV LC_LANG="C.UTF-8"
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]