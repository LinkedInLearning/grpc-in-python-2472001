from datetime import datetime
from socket import socket
from unittest.mock import MagicMock

import grpc
import pytest

import rides_pb2 as pb
import rides_pb2_grpc as rpc
import server


def test_start():
    request = pb.StartRequest(
        car_id=7,
        driver_id='Bond',
        passenger_ids=['M', 'Q'],
        type=pb.POOL,
        location=pb.Location(
            lat=51.4871871,
            lng=-0.1266743,
        ),
    )
    request.time.FromDatetime(datetime(2022, 2, 22, 22, 22, 22, 22))
    context = MagicMock()

    rides = server.Rides()
    resp = rides.Start(request, context)
    assert resp.id != ''


def free_port():
    with socket() as sock:
        sock.bind(('localhost', 0))
        _, port = sock.getsockname()
        return port


@pytest.fixture
def conn():
    port = free_port()
    srv = server.build_server(port)
    srv.start()

    with grpc.insecure_channel(f'localhost:{port}') as chan:
        stub = rpc.RidesStub(chan)

        yield srv, stub

    srv.stop(grace=0.1)


def test_start_server(conn):
    srv, stub = conn

    request = pb.StartRequest(
        car_id=7,
        driver_id='Bond',
        passenger_ids=['M', 'Q'],
        type=pb.POOL,
        location=pb.Location(
            lat=51.4871871,
            lng=-0.1266743,
        ),
    )
    request.time.FromDatetime(datetime(2022, 2, 22, 22, 22, 22, 22))
    response = stub.Start(request)
    assert response.id != ''
