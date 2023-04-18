import types

from database import query
from shared import utilities


def get_secuencia_informes():
    response = query(f"SELECT * FROM secuenciainforme WHERE id=1")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def update_secuencia_informes(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE secuenciainforme set {value_set} WHERE id=1;")
    return {"message": "Secuencia informes updated", }, 200
