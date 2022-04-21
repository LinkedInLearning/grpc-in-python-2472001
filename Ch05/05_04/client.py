import grpc

import log
import rides_pb2 as pb
import rides_pb2_grpc as rpc


class ClientError(Exception):
    pass


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

        try:
            response = self.stub.Start(request, timeout=3)
        except grpc.RpcError as err:
            log.error('start: %s (%s)', err, err.__class__.__mro__)
            raise ClientError(f'{err.code()}: {err.details()}') from err
        return response.id

    def track(self, events):
        self.stub.Track(track_request(event) for event in events)


def track_request(event):
    request = pb.TrackRequest(
        car_id=event.car_id,
        location=pb.Location(lat=event.lat, lng=event.lng),
    )
    request.time.FromDatetime(event.time)
    return request


if __name__ == '__main__':
    import config
    from events import rand_events

    addr = f'{config.host}:{config.port}'
    client = Client(addr)
    events = rand_events(7)
    try:
        client.track(events)
    except ClientError as err:
        raise SystemExit(f'error: {err}')
