#!/bin/sh




export PGUSER='postgres'


psql -c "CREATE DATABASE invertory"

psql -c "CREATE EXTENSION IF NOT EXIST \"uuid-ossp"\;"