from flask import Blueprint
from informes import informes_service
informes = Blueprint('informes', __name__)


@informes.get('/informes/secuencia-informes')
def get_secuenciainformes():
    response = informes_service.get_seciencia_informes()
    return response
