#! /usr/bin/env sh

echo -e '\n\n--------- DATABASE MIGRATION ---------';
alembic upgrade head
echo -e '--------- END OF DATABASE MIGRATION ---------\n\n';
