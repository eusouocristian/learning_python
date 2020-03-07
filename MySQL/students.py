from peewee import *

db = SqliteDatabase('students.db')

students = [
    {'username': 'eusouocristian',
    'points': 5888},
    {'username': 'gabrielakauer',
    'points': 4999},  
    {'username': 'pabloyague',
    'points': 4900},
    {'username': 'djiovaneka',
    'points': 4777}   
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
    
def top_student():
    # retorna o primeito item da lista de estudantes ordenada descendente pelo numero de pontos
    student = Student.select().order_by(Student.points.desc()).get() 
    return student



# Criação de um modelo Student com dois campos, username (char, tamanho 255) e points (int)
class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    # criar Metaclasse, e atribuir o atributo database a db
    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print('Our Top Student right now is: {0.username}'.format(top_student()))

# O codigo devera criar um arquivo students.db na pasta
# navegar no terminal digitando 'sqlite students.db'
# ira aparecer 'sqlite>'. 
# comando '.tables'    -> retorna a tabela 'students' criada em db.create_tables(...)
# '.exit' pra sair

# .create() - creates a new instance all at once
# .select() - finds records in a table
# .save() - updates an existing row in the database
# .get() - finds a single record in a table
# .delete_instance() - deletes a single record from the table
# .order_by() - specify how to sort the records
# if __name__ == '__main__' - a common pattern for making code only run
#    when the script is run and not when it's imported
# db.close() - not a method we used, but often a good idea. Explicitly
#    closes the connection to the database.
# .update() - also something we didn't use. Offers a way to update a record 
#    without .get() and .save(). Example: 
#    Student.update(points=student['points']).where(Student.username == student['username']).execute()


