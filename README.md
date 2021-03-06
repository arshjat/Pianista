![alt-image](https://img.shields.io/badge/license-GPL-brightgreen.svg)
# Pianista

## Why Pianista?
Have you ever come to a point in life where you came across a nice song and you just wish to play it on a piano even if you don't know how to play one ? But then you try to seek people who can teach you (just that song on the piano) and you can't find anyone since they only offer their pre-customized courses where you only have few choices to select from. So from now on don't worry, Pianista got your back !! 

## What is Pianista?
Pianista is a platform where you can search any song and can get corresponding seemingly-live piano sessions generated with the help of machine learning. It provides a near to real interactive experience to the user. 
 


## Installation with Git

You need to have Python(>=3) and pip3 installed on your local machine.

Git Clone.

```
git clone https://github.com/arshjat/Pianista.git
```

Create and start a virtual environment.

```
virtualenv venv
source venv/bin/activate
```

Install dependencies.

```
cd Pianista
pip3 install -r requirements.txt
```
To run the project.

```
python app.py
```

## Installation with Docker

Build a docker Image using Dockerfile

```
docker build pianista:latest .
```
If you are behind a proxy environment, do 

```
docker build --build-arg http_proxy=" " --build-arg https_proxy=" " -t pianista:latest .
```

Then run a container using the docker image
```
docker run -d -p 5000:5000 pianista
```
we are using port 5000 because unlike other frmeworks/micro frameworks **Flask** uses 5000 port.
