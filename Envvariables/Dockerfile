FROM alpine:latest
#example of using env variables
ENV WELCOME_MESSAGE="Welcome to Docker World"

CMD ["sh", "-c", "echo $WELCOME_MESSAGE"]

docker build -t envvariables:v1 .