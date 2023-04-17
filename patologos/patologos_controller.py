from flask import Blueprint, request
from markupsafe import escape
from patologos import patologos_service

patologos = Blueprint('patologos', __name__)


@patologos.get('/patologos')
def get_patologos():
    response = patologos_service.get_patologos()
    return response


@patologos.get('/patologos/<int:index>')
def get_patologos_by_id(index):
    response = patologos_service.get_patologo_by_id(escape(index))
    if response is False:
        response = {
                "message": "Patologo not found",
            }, 404
    return response


@patologos.post('/patologos')
def crear_patologo():
    if len(request.form):
        response = patologos_service.crear_patologo(request.form.to_dict())
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


@patologos.put('/patologos/<int:index>')
def update_patologo(index):
    if len(request.form):
        response = patologos_service.update_patologo(
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


@patologos.delete('/patologos/<int:index>')
def eliminar_patologo(index):
    response = patologos_service.eliminar_patologo(index)
    return response
