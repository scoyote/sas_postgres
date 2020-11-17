#!/bin/bash

table=$1;
function is_database() {
  psql -lqt | cut -d \| -f 1 | grep -wq $1
}

echo database:
read
if is_database $1
then
  echo $1 exists
else
  echo $1 does not exist
  createdb dvdrental
  pg_restore -U postgres -d dvdrental dvdrental.tar
fi
