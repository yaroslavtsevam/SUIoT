#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" --dbname="chirpstack" <<-EOSQL
    create extension pg_trgm;
    create extension hstore;
EOSQL