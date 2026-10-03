import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Course, Homework

DSN = 'postgresql://postgres:<.l;tncnhfys888@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)


create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

course1 = Course(name='Python')

session.add(course1)
session.commit()

hw1 = Homework(number=1, description='простая домашняя работа', course=course1)
hw2 = Homework(number=1, description='сложная домашняя работа', course=course1)
session.add_all([hw1, hw2])
session.commit()

# for c in session.query(Homework).filter(Homework.description.like('%сложн%')).all():
#     print(c)

# session.query(Course).join(Homework.course).filter(Homework.number == 2).all()

c2 = Course(name='Java')
session.add(c2)
session.commit()

# subq = session.query(Homework).filter(Homework.description.like('%сложн%')).subquery()
# for c in session.query(Course).join(subq, Course.id == subq.c.course_id).all():
#     print(c)

session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
session.commit()

session.query(Course).filter(Course.name == 'JavaScript').delete()
session.commit()

for c in session.query(Course).all():
    print(c)

session.close()

