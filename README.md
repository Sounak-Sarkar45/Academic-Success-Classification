Academic Success Classification: Dropout, Enrolled, or Graduate

Project Overview

This project focuses on building a classification system to predict the academic success of students, classifying them as one of the following categories:

Dropout

Enrolled

Graduate

The system is powered by a machine learning model and provides a web interface for users to interact with the model.

Features

Prediction Categories: Dropout, Enrolled, or Graduate.

Web Application: Built using Flask, HTML, CSS, and JavaScript.

Cloud Deployment: The model is hosted on an AWS EC2 instance.

Prerequisites

Python: Version 3.10.

Libraries: Listed in requirements.txt. Install them using:

pip install -r requirements.txt

AWS EC2 Instance: Ensure your instance is properly configured to host the Flask application and provide public access.

File Structure

app/:

Contains the Flask application code.

HTML, CSS, and JS files for the web interface.

model/:

Pre-trained machine learning model.

Scripts for model loading and inference.

requirements.txt:

List of required Python libraries.

README.md:

Project documentation.

Setup Instructions

Clone the Repository:

git clone <repository_url>
cd academic-success-classification

Install Dependencies:

pip install -r requirements.txt

Run the Flask Application:

python app.py

Access the Web Application:
Open your web browser and navigate to http://127.0.0.1:5000 (or the public IP if hosted on AWS).

Deployment

The web application and model are deployed on an AWS EC2 instance:

Launch an EC2 instance with the necessary configuration.

Transfer the project files to the instance using SCP or any preferred method.

Install Python 3.10 and required libraries on the instance.

Start the Flask application.

Ensure the security group allows HTTP traffic on port 80 (or your chosen port).

Usage

Navigate to the web interface.

Input the required student data.

View the prediction result: Dropout, Enrolled, or Graduate.

Technologies Used

Programming Language: Python 3.10

Framework: Flask

Frontend: HTML, CSS, JavaScript

Cloud: AWS EC2

License

This project is licensed under the MIT License. See LICENSE for details.

Contributors

[Your Name] - Developer and Maintainer

Feel free to reach out for any questions or contributions!
