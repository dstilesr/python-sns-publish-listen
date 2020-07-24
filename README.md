# A Pair of API to Publish / Listen to SNS

## Contents

* [About](#about)
* [Run the Project](#run-the-project)
  * [Run with docker-compose](#run-with-docker-compose)
  * [Test locally with live SNS](#test-locally-with-live-sns)
* [Built With](#built-with)

## About
This project consists of a pair of `fastAPI` apis, one that publishes simple
messages to an `SNS` topic and one that listens to the topic via HTTP. I did
this to gain familiarity with the subject and perhaps to use the code as
templates or guidance later on.

## Run the Project

### Run with docker-compose
To start both APIs you can use `docker-compose`:
```bash
docker-compose up
```
This will start both services. The publisher listens on port 8000 and the
subscriber listens on 3000. The publisher will publish any messages posted
to it to `SNS`. Both services have documentation URL `/redoc`.

### Test locally with live SNS
In order to test locally with `SNS`, you must make the subscriber's port
public. You can do this with [ngrok](https://ngrok.com/):
```bash
ngrok http 3000
```
Remember to add the ngrok URL to the subscriber's `.env` file!

## Built With

* [Python](https://www.python.org/)
* [AWS SNS](https://aws.amazon.com/sns/)
* [Docker](https://www.docker.com/)
* [FastAPI](https://fastapi.tiangolo.com/)

[Back to top.](#a-pair-of-api-to-publish--listen-to-sns)