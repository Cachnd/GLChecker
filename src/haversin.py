from math import sin, cos, sqrt, atan2, radians

def distance(lat_1, long_1, lat_2, long_2, R):

    latitud_1 = radians(lat_1)
    longitud_1 = radians(long_1)
    latitud_2 = radians(lat_2)
    longitud_2 = radians(long_2)
    
    distance_lat = latitud_2 - latitud_1
    distance_long = longitud_2 - longitud_1

    a = sin(distance_lat / 2)**2 + cos(latitud_1) * cos(latitud_2) * sin(distance_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance