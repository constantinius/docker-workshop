FROM debian:stable-slim AS build-stage

RUN apt-get update ; apt-get -y install gcc
ADD hello.c .
RUN gcc hello.c

FROM debian:stable-slim AS run-stage
COPY --from=build-stage a.out .

CMD ./a.out
