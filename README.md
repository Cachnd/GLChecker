# GLChecker

This program is a function that returns a students_list containing all students that are inside a classroom
it uses latitud, longitud to know the location of students and classrooms

Some assumptions  are:
- The earth is an perfect sphere with radius of 6,371 km
- The classes walls are aligned with latitude and longitude degrees of earth
- There are no overlap with the classrooms
- Height its not important for classes or students
- The program has a 1m of error margin without including the other assumptions

To run the program:
On the src/ folder you can call directly the examples1.py and example2.py as scripts
Or you can import the function studentsInClasses() from function.py and give the input manually

The program has been developed with Python 3.9.5 and hasn't been tested on other versions.
