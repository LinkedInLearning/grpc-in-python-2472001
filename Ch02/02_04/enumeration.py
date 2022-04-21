import rides_pb2 as pb

print(pb.POOL)
print(pb.RideType.Name(pb.POOL))
print(pb.RideType.Value('REGULAR'))

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
    type=pb.POOL,
)
print(request)
