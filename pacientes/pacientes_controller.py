from flask import Blueprint, request
from pacientes import pacientes_service
pacientes = Blueprint('pacientes', __name__)


@pacientes.get('/pacientes')
def get_pacientes():
    response = pacientes_service.get_pacientes()
    return response


@pacientes.get('/pacientes/<int:index>')
def get_paciente_by_id(index):
    response = pacientes_service.get_paciente_by_id(index)
    if response is False:
        response = {
            "message": "Paciente not found",
        }, 404
    return response


@pacientes.post('/pacientes')
def create_paciente():
    if len(request.form):
        response = pacientes_service.create_paciente(request.form.to_dict())
    elif request.data.decode():
        response = {
            "message": "Data should come in form-data",
            "error": "Bad request"
        }, 400
    else:
        response = {
            "message": "There is no data",
            "error": "Bad request"
        }, 400
    return response


@pacientes.put('/pacientes/<index>')
def update_paciente(index):
    if len(request.form):
        response = pacientes_service.update_paciente(
            index,
            request.form.to_dict()
        )
    elif request.data.decode():
        response = {
            "message": "Data should come in form-data",
            "error": "Bad request"
        }, 400
    else:
        response = {
            "message": "There is no data",
            "error": "Bad request"
        }, 400
    return response


@pacientes.delete('/pacientes/<int:index>')
def eliminar_patologo(index):
    response = pacientes_service.eliminar_paciente(index)
    return response
