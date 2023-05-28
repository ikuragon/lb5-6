# from flask import Blueprint
# from sqlalchemy.orm import Session
#
# from app import db
# from app.models import Employee, Position, Division, Job
# from sqlalchemy.orm import sessionmaker
#
# bp = Blueprint('bp', __name__)
#
# @bp.route('/', methods=['GET'])
# def index():
#
# #    employees = Employee.join(Job, Employee.id == Job.employee_id).all()
#     job = Job.query.get(1)
#
#     employee_data = {
#         "second_name": "Voronova",
#         "first_name": "Daria",
#         "surname": "Dmitrievna",
#         "address": "c.Arkh s.Moskovskiy h.1 ",
#         "date_of_birth": "05.03.1982",
#
#         "employee_id": Employee.id
#
#     }
#
#     new_employee = Employee(**employee_data)
#
#     db.session.add(new_employee)
#     db.session.commit()
#
#     return '1'