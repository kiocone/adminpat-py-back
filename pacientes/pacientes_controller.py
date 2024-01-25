from flask import Blueprint, request
from pacientes import pacientes_service

pacientes = Blueprint('pacientes', __name__)


@pacientes.get('/pacientes')
def get_pacientes():
    queryParasms = request.args
    pageIndex = queryParasms.get('pageIndex')
    pageSize = queryParasms.get('pageSize')
    response = pacientes_service.get_pacientes(int(pageIndex), int(pageSize))
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
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = pacientes_service.create_paciente(request.json)
    else:
        response = {'message': 'Content-Type not supported!'}, 400
    return response


@pacientes.put('/pacientes/<index>')
def update_paciente(index):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = pacientes_service.update_paciente(
            index,
            request.json
        )
    else:
        response = {'message': 'Content-Type not supported!'}, 400
    return response


@pacientes.delete('/pacientes/<int:index>')
def eliminar_patologo(index):
    if pacientes_service.get_paciente_by_id(index) is not False:
        response = pacientes_service.eliminar_paciente(index)
    else:
        response = {"message": "No existe el paciente"}, 400
    return response
