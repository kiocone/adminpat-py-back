from flask import Blueprint, request
from eps import eps_service
eps = Blueprint('eps', __name__)


@eps.get('/eps')
def get_pacientes():
    response = eps_service.get_eps()
    return response


@eps.get('/eps/<int:index>')
def get_paciente_by_id(index):
    response = eps_service.get_eps_by_id(index)
    if response is False:
        response = {
            "message": "EPS not found",
        }, 404
    return response


@eps.post('/eps')
def create_eps():
    if len(request.form):
        response = eps_service.create_eps(request.form.to_dict())
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


@eps.put('/eps/<index>')
def update_eps(index):
    if len(request.form):
        response = eps_service.update_eps(
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


@eps.delete('/eps/<int:index>')
def eliminar_eps(index):
    response = eps_service.eliminar_eps(index)
    return response
