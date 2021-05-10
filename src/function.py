from haversin import distance

def studentsInClasses ( students_list, classroom_list):
    students_inAClass = []
    R = 6371.0
    for classroom in classroom_list:
        for student in students_list:
            latitude_range = reverseLatitude(classroom["latitude"], classroom["longitude"], R)
            longitud_range = reverseLongitude(classroom["latitude"], classroom["longitude"], R)
            northWall = classroom["latitude"] + latitude_range
            southWall = classroom["latitude"] - latitude_range
            eastWall = classroom["longitude"] + longitud_range
            westWall = classroom["longitude"] - longitud_range
            if ( southWall <= student["latitude"] <= northWall and
                    westWall <= student["longitude"] <= eastWall
                ):
                if (not(student in students_inAClass)):
                    students_inAClass.append(student)

    return students_inAClass

def reverseLatitude(latitude, longitud, R):
    d = x = 0
    x2 = 1
    for c in range(1, 1000000):
        x = 0.001*c
        d = distance(latitude, longitud, latitude+x, longitud, R)
        if (d>10):
            break
    return x


def reverseLongitude(latitude, longitud, R):
    d = x = 0
    x2 = 1
    for c in range(1, 1000000):
        x = 0.001*c
        d = distance(latitude, longitud, latitude, longitud+x, R)
        if (d>10):
            break
    return x