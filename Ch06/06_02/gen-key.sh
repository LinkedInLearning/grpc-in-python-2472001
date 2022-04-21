#!/bin/bash

set -e
set -x

openssl req \
    -newkey rsa:4096 \
    -x509 \
    -days 365 \
    -nodes \
    -subj '/CN=localhost' \
    -keyout key.pem \
    -out cert.pem \
