## Developing the UI of chatbot application by using Flask and Docker

### Install Docker
Follow this link: https://docs.docker.com/engine/install/ubuntu/

  Note: fixbug "docker-permission-denied"
  ```
  $ chmod 777 /var/run/docker.sock
  ```
  
### Dockerize a Flask application
  1. Modify the Dockerfile.
  2. ``` $ docker build --tag <folder-docker-name> . ```
  3. ``` $ docker image ```
  4. ``` $ docker run <image-name> ```
