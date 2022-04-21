from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

import grpc

import log
import rides_pb2 as pb
import rides_pb2_grpc as rpc


def new_ride_id():
    return uuid4().hex


class Rides(rpc.RidesServicer):
    def Start(self, request, context):
        log.info('ride: %r', request)

        # TODO: Store ride in database
        ride_id = new_ride_id()
        return pb.StartResponse(id=ride_id)


if __name__ == '__main__':
    import config

    server = grpc.server(ThreadPoolExecutor())
    rpc.add_RidesServicer_to_server(Rides(), server)

    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    log.info('server ready on %s', addr)
    server.wait_for_termination()
