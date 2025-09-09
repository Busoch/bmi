#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

echo " Waiting for database at $host..."

until pg_isready -h "$host" -U "$POSTGRES_USER"; do
  >&2 echo "Database is unavailable - sleeping"
  sleep 2
done

>&2 echo " Database is up - executing command"
exec $cmd
