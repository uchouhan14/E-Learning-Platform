# E-Learning Platform
### Stack we used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## Open Source Student Portal

## Features!

- Student login
- Teacher Login
- Teacher Add & Delete the Subject
- Quiz (Take, Submission, Result)
- Assigment (Take, Submission, Grade)
- Teacher Check the assigment and Upload the Chapter
- Notification
- Individiual Chat
- Broadcast Chat

This is a Django web application that has been Dockerized for system independence. By using Docker, you can easily deploy the application on any system without worrying about specific dependencies.

## Overview
The Django LMS Application is a comprehensive learning platform designed to streamline and enhance the educational experience. Built on the Django web framework, this application offers a robust set of features to facilitate online learning, course management, and collaboration between educators and students.

## Getting Started
Follow these steps to set up and run the project on your local machine.

### Prerequisites
Make sure you have Docker installed on your machine.

### Installation
1. Clone the repository: git clone https://github.com/your-username/django-dockerized-app.git
2. Navigate to the project directory: cd django-dockerized-app
3. Build the Docker image: docker build .

OR,

For further simplification of the deployment process, we have created a docker-compose file. In order to run the application simply go to your terminal and write the command: docker-compose up
The application must be running at port 8000.

### Usage
To run the application, use the following Docker command: docker run -d -p 8000:8000 <your-docker-image-name>
NOTE- The name of your docker image will be unique, and you can view it using- "docker images ls" command

Access the application by navigating to http://localhost:8000 in your web browser.


## Brute-Force-Installation Guide

This requires Python Django to run. Install the dependencies and devDependencies and start the server

```bash
  git clone https://github.com/utkarshchouhan/E-Learning-Platform
```

```bash
 cd E-Learning-Platform
```

```bash
 python manage.py migrate
```

```bash
 python manage.py createsuperuser
```

```bash
$ python manage.py runserver
```
## Demo Screenshots
![git](https://user-images.githubusercontent.com/79878896/122668007-6fdb2380-d1cf-11eb-8ce4-493505565212.JPG)

![singup](https://user-images.githubusercontent.com/79878896/208314336-c51516df-ae28-4c21-95e7-dc2fa1a0c081.png)

![login](https://user-images.githubusercontent.com/79878896/208314342-38b6c6d0-40ad-4e34-a030-55c5e576f12b.png)

