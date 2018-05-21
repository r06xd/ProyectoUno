from peewee import *

db=SqliteDatabase('students.db')

class Student(Model):
    username=CharField(max_length=255,unique=True)
    points=IntegerField(default=0)

    class Meta:
        database = db
students=[
    {'username':'Rogger','points':10},
    {'username':'Andres','points':11},
    {'username':'Michael','points':12},
    {'username':'Kripton','points':13}
    ]

def add_student():
    for i in students:
        Student.create(username=i['username'],points=i['points'])

if __name__ == '__main__':
    db.connect() #permite conectar a la base de datos
    db.create_tables([Student],safe=True)
    add_student()
