=================
NLP Movie Backend
=================

A part of 2019 NLP SYS project at Chulalongkorn University

***************
Set up
***************
1. Create your environment with ``python -m venv venv``
2. Activate your environment with ``source venv/bin/activate``
3. Install dependencies with ``pip install -r requirements.txt``
4. Setup .env ``cp .example.env .env`` and edit the ``.env`` for api keys

****************
Start the server
****************
- For Windows users, just run ``start.ps1``
- For Linux/OSX users, just run ``./start.sh``

The server should be available at port 8080

*********************
Build docker image
*********************
Build with this command ``docker build -t repository:tagname .``

************************
Run the server on docker
************************
1. Pull the docker image with ``docker pull compisit/nlp-movie-backend:latest``
2. Start the server with ``docker run --rm -p 8080:8080 compisit/nlp-movie-backend:latest``
3. Server will be available on ``localhost:8080``

*****************
API documentation
*****************
The documentation is provided in swagger ui, please go to ``{your_host:your_port}/apidocs/``
