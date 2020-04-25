#!/bin/bash
docker-compose up $2

cat << EndOfMessage

L'application a démarré.

Api:        http://localhost
Pgadmin:    http://localhost:5050

EndOfMessage