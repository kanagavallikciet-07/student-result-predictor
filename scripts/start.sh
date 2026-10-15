#!/bin/bash
set -e
docker run -d --name student-app -p 80:5000 -e MODEL_VERSION=1.0 student-app:latest
