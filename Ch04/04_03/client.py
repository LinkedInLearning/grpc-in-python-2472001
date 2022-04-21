import grpc

import log
import rides_pb2 as pb
import rides_pb2_grpc as rpc


class Client:
    def __init__(self, addr):
        self.chan = grpc.insecure_channel(addr)
        self.stub = rpc.RidesStub(self.chan)
        log.info('connected to %s', addr)

    def close(self):
        self.chan.close()

    def ride_start(self, car_id, driver_id, passenger_ids, type, lat, lng, time):
        request = pb.StartRequest(
            car_id=car_id,
            driver_id=driver_id,
            passenger_ids=passenger_ids,
            type=pb.POOL if type == 'POOL' else pb.REGULAR,
            location=pb.Location(lat=lat, lng=lng),
        )
        request.time.FromDatetime(time)
        log.info('ride started: %s', request)

        response = self.stub.Start(request)
        return response.id


if __name__ == '__main__':
    import config
    from datetime import datetime

    addr = f'{config.host}:{config.port}'
    client = Client(addr)
    ride_id = client.ride_start(
        car_id=7,
        driver_id='Bond',
        passenger_ids=['M', 'Q'],
        type='POOL',
        lat=51.4871871,
        lng=-0.1266743,
        time=datetime(2021, 9, 30, 20, 15),
    )
    log.info('ride ID: %s', ride_id)
