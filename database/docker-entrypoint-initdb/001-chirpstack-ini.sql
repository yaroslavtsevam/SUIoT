CREATE ROLE root
LOGIN ;
ALTER USER root WITH SUPERUSER;
CREATE ROLE chirpstack 
LOGIN 
PASSWORD 'chirpstack';
CREATE DATABASE chirpstack WITH 
    OWNER chirpstack;
