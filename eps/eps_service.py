import types
from database import query
from shared import utilities


def get_eps():
    response = query("SELECT * FROM eps")
    return response


def get_eps_by_id(index: int):
    response = query(f"SELECT * FROM eps WHERE id={index}")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def create_eps(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO eps SET {value_set}")
    return {"message": "EPS created", }, 200


def update_eps(index: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE eps SET {value_set} WHERE id = {index}")
    return {"message": "EPS updated", }, 200


def eliminar_eps(index: int):
    query(f"DELETE from eps WHERE id = {index};")
    return {"message": "EPS deleted"}, 200
