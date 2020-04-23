FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["waitress-serve", "--call", "nlp_movie_backend:create_app"]
