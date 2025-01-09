#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" <<-EOSQL
    create role chirpstack with login password 'chirpstack';
    create database chirpstack with owner chirpstack;
EOSQL