from flask import Blueprint, request
from entidad import entidad_service
entidad = Blueprint('entidad', __name__)


@entidad.get('/entidad')
def get_pacientes():
    response = entidad_service.get_entidad()
    return response


@entidad.get('/entidad/<int:index>')
def get_paciente_by_id(index):
    response = entidad_service.get_entidad_by_id(index)
    if response is False:
        response = {
            "message": "Entidad not found",
        }, 404
    return response


@entidad.post('/entidad')
def create_entidad():
    if len(request.form):
        response = entidad_service.create_entidad(request.form.to_dict())
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


@entidad.put('/entidad/<index>')
def update_entidad(index):
    if len(request.form):
        response = entidad_service.update_entidad(
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


@entidad.delete('/entidad/<int:index>')
def eliminar_entidad(index):
    response = entidad_service.eliminar_entidad(index)
    return response
