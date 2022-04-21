#!/bin/bash

set -e
set -x

pb_dir=gateway/pb

mkdir -p gateway/pb

protoc \
    -I . \
    -I ${GAPI_PATH} \
    --go_out=${pb_dir} \
    --go_opt=paths=source_relative \
    --go-grpc_out=${pb_dir} \
    --go-grpc_opt=paths=source_relative \
    rides.proto
protoc \
    -I . \
    -I ${GAPI_PATH} \
    --grpc-gateway_out ${pb_dir} \
    --grpc-gateway_opt logtostderr=true \
    --grpc-gateway_opt paths=source_relative \
    rides.proto
    
