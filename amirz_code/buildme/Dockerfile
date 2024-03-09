# syntax=docker/dockerfile:1
# FROM golang:1.20-alpine
# WORKDIR /src
#  COPY . .
# COPY go.mod go.sum .
# RUN go mod download
# COPY . .
# RUN go build -o /bin/client ./cmd/client
# RUN go build -o /bin/server ./cmd/server
# ENTRYPOINT [ "/bin/server" ]
# ******** BETTER BUILD ********
# FROM golang:1.21-alpine AS base
# WORKDIR /src
# COPY go.mod go.sum .
# RUN go mod download
# COPY . .
# FROM base AS build-client
# RUN go build -o /bin/client ./cmd/client
# FROM base AS build-server
# RUN go build -o /bin/server ./cmd/server

# FROM scratch
# COPY --from=build-client /bin/client /bin/
# COPY --from=build-server /bin/server /bin/
# ENTRYPOINT ["/bin/server"]
# ******** YET BETTER BUILD ********
# clear the cache first -> docker builder prune -af
FROM golang:1.21-alpine AS base
  WORKDIR /src
  COPY go.mod go.sum .
  RUN --mount=type=cache,target=/go/pkg/mod/ \
      go mod download -x
  COPY . .

  FROM base AS build-client
  RUN --mount=type=cache,target=/go/pkg/mod/ \
      go build -o /bin/client ./cmd/client

  FROM base AS build-server
  RUN --mount=type=cache,target=/go/pkg/mod/ \
      go build -o /bin/server ./cmd/server

  FROM scratch AS client
  COPY --from=build-client /bin/client /bin/
  ENTRYPOINT [ "/bin/client" ]

  FROM scratch AS server
  COPY --from=build-server /bin/server /bin/
  ENTRYPOINT [ "/bin/server" ]