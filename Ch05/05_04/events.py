from collections import namedtuple
from datetime import datetime, timedelta
from time import sleep

LocationEvent = namedtuple('LocationEvent', 'car_id time lat lng')


def rand_events(count):
    time = datetime(2022, 2, 22, 14, 36, 9)
    lat, lng = 51.4871871, -0.1266743
    for _ in range(count):
        yield LocationEvent(
            car_id=7,
            time=time,
            lat=lat,
            lng=lng,
        )

        time += timedelta(seconds=17.3)
        lat += 0.0001
        lng -= 0.0001
        sleep(0.1)
