import grpc

import log
import rides_pb2_grpc as rpc


class Client:
    def __init__(self, addr):
        self.chan = grpc.insecure_channel(addr)
        self.stub = rpc.RidesStub(self.chan)
        log.info('connected to %s', addr)

    def close(self):
        self.chan.close()


if __name__ == '__main__':
    import config

    addr = f'{config.host}:{config.port}'
    client = Client(addr)
