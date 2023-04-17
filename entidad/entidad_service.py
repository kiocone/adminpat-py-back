import types
from database import query
from shared import utilities


def get_entidad():
    response = query("SELECT * FROM entidad")
    return response


def get_entidad_by_id(index: int):
    response = query(f"SELECT * FROM entidad WHERE id={index}")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def create_entidad(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO entidad SET {value_set}")
    return {"message": "Entidad created", }, 200


def update_entidad(index: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE entidad SET {value_set} WHERE id = {index}")
    return {"message": "Entidad updated", }, 200


def eliminar_entidad(index: int):
    query(f"DELETE from entidad WHERE id = {index};")
    return {"message": "Entidad deleted"}, 200
