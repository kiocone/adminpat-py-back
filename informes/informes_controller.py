from flask import Blueprint
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



