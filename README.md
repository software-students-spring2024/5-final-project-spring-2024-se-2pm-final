[![Web-app CI](https://github.com/software-students-spring2024/5-final-project-spring-2024-se-2pm-final/actions/workflows/web-app.yml/badge.svg)](https://github.com/software-students-spring2024/5-final-project-spring-2024-se-2pm-final/actions/workflows/web-app.yml)
# Final Project

We aim to design and produce a quiz-making app targeted to education market similar to that of quizzlet. Our service will allow the users to make and delete multiple-chioce quizzes
for their students. Also, the users can answer those question to test their knowledge for the subject.

## Teammates participating in this project

1. Brendan Tang: [Github profile](https://github.com/Tango117)
2. Joseph Lee: [Github profile](https://github.com/pastuhhhh)
3. Minjae Lee: [Github profile](https://github.com/minjae07206)
4. Yiwei Luo: [Github profile](https://github.com/yl7408)

## Docker image hosted on Dockerhub

https://hub.docker.com/r/minjae07206/quiz_app_final

## Link to Web App 

Deployed website can be located here [link](https://hub.docker.com/r/minjae07206/quiz_app_final)


## Instructions to run this project

To just open the website and use it, here is the [Link](https://quiz-app-zdp4b.ondigitalocean.app/)

If you want to contribute, you can make a pull request. Once the user makes a pull request, the following things happen:

1. A Docker Image is built from Dockerfile and the image is pushed(uploaded) to Dockerhub.

2. This Docker Image is used to download dependencies and deploys to Digital Ocean.

3. In order to contribute, you will need .env file and app-spec.yaml file. These files are given to stakeholders. .env file is for carrying information about the database, and app-spec.yaml is the configuration for deploying on Digital Ocean.
