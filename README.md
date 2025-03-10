# DevOps Project

## Overview

This is a simple web application built with Flask.

## Features

- **Simple Web Application:** A Flask-based web app that allows the user to pick a team.
- **Dockerized Application:** Containerized using Docker.
- **CI/CD Pipeline:** Automated build, test, and deploymet process configured via GitHub Actions.
- **Security Analysis:** Vulnerability scanning using Trivy.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- Git
- A GitHub account (for repository hosting and GitHub Actions)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/btw02/devops_class.git
   cd devops_class
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t myflaskapp .
   ```

3. **Run the Application in a Docker container**

   ```bash
   docker run -p 5000:5000 myflaskapp
   ```
Then, open your browser and navigate to http://localhost:5000 to view the application.

## Pipelines
I created a Continuous Integration Pipeline, as well as a Continuous Compliance Pipeline.

**The CI pipeline takes care of testing, creating a docker image and pushing this image to Github Container Registry.**

**The CC pipeline takes care of security scans and runs daily at midnight (UTC time).**

**In the future I would add a CD pipeline that deploys the docker image on a cluster (using Azure/IBM Cloud) and runs additional tests on the application**
