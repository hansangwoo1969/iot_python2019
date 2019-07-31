import re

p = re.compile('Crow|Servo')
m = p.match('Nothin') # Not match
print(m)

m = p.match('Crow')
print(m)

m = p.match('Servo')
print(m)

m = p.match('CrowServo')
print(m)
