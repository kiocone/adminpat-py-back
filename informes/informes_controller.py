from flask import Blueprint, request
from informes import informes_service
informes = Blueprint('informes', __name__)


@informes.get('/informes/secuencia-informes')
def get_secuenciainformes():
    response = informes_service.get_secuencia_informes()
    return response


@informes.put('/informes/secuencia-informes')
def update_cups():
    from flask import request
    if len(request.form):
        response = informes_service.update_secuencia_informes(
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


@informes.get('/informes/<t_informe>')
def get_informes(t_informe):
    if t_informe == "Q":
        response = informes_service.get_informes_q()
    elif t_informe == "L":
        response = informes_service.get_informes_l()
    elif t_informe == "C":
        response = informes_service.get_informes_c()
    else:
        response = {
            "message": f"Tipo de informe '{t_informe}' no es valido",
            "error": "not found"
        }, 404
    return response


@informes.get('/informes/Q/<int:index>')
def get_informes_q_by_id(index=None):
    response = informes_service.get_informes_q_by_id(index)
    if response is False:
        response = {
            "message": f"Informe 'Q' with id:{index} not found",
        }, 404
    return response


@informes.get('/informes/L/<int:index>')
def get_informes_l_by_id(index=None):
    response = informes_service.get_informes_l_by_id(index)
    if response is False:
        response = {
            "message": f"Informe 'L' with id:{index} not found",
        }, 404
    return response


@informes.get('/informes/C/<int:index>')
def get_informes_c_by_id(index=None):
    response = informes_service.get_informes_c_by_id(index)
    if response is False:
        response = {
            "message": f"Informe 'C' with id:{index} not found",
        }, 404
    return response


@informes.post('/informes/Q')
def create_inform_q():
    if len(request.form):
        response = informes_service.create_inform_q(request.form.to_dict())
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


@informes.post('/informes/L')
def create_inform_l():
    if len(request.form):
        response = informes_service.create_inform_l(request.form.to_dict())
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
