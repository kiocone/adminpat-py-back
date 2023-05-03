from flask import Blueprint, request
from cupss import cups_service
cups = Blueprint('cups', __name__)


@cups.get('/cups')
def get_pacientes():
    response = cups_service.get_cups()
    return response


@cups.get('/cups/<int:index>')
def get_paciente_by_id(index):
    response = cups_service.get_cups_by_id(index)
    if response is False:
        response = {
            "message": "CUPS not found",
        }, 404
    return response


@cups.post('/cups')
def create_cups():
    if len(request.form):
        response = cups_service.create_cups(request.form.to_dict())
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


@cups.put('/cups/<index>')
def update_cups(index):
    if len(request.form):
        response = cups_service.update_cups(
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


@cups.delete('/cups/<int:index>')
def eliminar_cups(index):
    response = cups_service.eliminar_cups(index)
    return response
