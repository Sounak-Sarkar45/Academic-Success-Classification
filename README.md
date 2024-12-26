# Academic Success Classification: Dropout, Enrolled, or Graduate


## Project Overview

This project focuses on building a classification system to predict the academic success of students, classifying them as one of the following categories:

- Dropout

- Enrolled

- Graduate

The system is powered by a machine learning model and provides a web interface for users to interact with the model.


## Features

- Prediction Categories: Dropout, Enrolled, or Graduate.

- Web Application: Built using Flask, HTML, CSS, and JavaScript.

- Cloud Deployment: The model is hosted on an AWS EC2 instance.


## Prerequisites

1. Python: Version 3.10.

2. Libraries: Listed in requirements.txt. Install them using:

   ```
   pip install -r requirements.txt
   ```

3. AWS EC2 Instance: Ensure your instance is properly configured to host the Flask application and provide public access.


## Setup Instructions

1. Clone the Repository:

   ```
   git clone https://github.com/Sounak-Sarkar45/Academic-Success-Classification.git
   cd Academic-Success-Classification
   ```
   
2. Install Dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the Flask Application:

   ```
   python app.py
   ```
   
4. Access the Web Application: Open your web browser and navigate to http://127.0.0.1:5000 (or the public IP if hosted on AWS).


## Deployment

The web application and model are deployed on an AWS EC2 instance:

1. Launch an EC2 instance with the necessary configuration.

2. Transfer the project files to the instance using SCP or any preferred method.

3. Install Python 3.10 and required libraries on the instance.

4. Start the Flask application.

5. Ensure the security group allows HTTP traffic on port 80 (or your chosen port).


## Usage

1. Navigate to the web interface.

2. Input the required student data.

3. View the prediction result: Dropout, Enrolled, or Graduate.


## DOCKER -

This Docker image hosts a Flask-based web application for predicting academic outcomes using a machine learning model. The application is lightweight, easy to deploy, and ready for integration into various environments.

### Quick Start

To pull and run the application, use the following commands:

```
docker pull sounaksarkar/academic-class-app:latest
docker run -d -p 5000:5000 sounaksarkar/academic-class-app:latest
```


## Contributors

```Sounak Sarkar``` - Developer and Maintainer

Feel free to reach out for any questions or contributions!
