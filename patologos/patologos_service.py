import types

from database import query
from shared import utilities


def get_patologos():
    resp = query("SELECT * from patologo;")
    return resp


def get_patologo_by_id(*args):
    response = query("SELECT * FROM patologo where id = ?;", *args)
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def crear_patologo(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO patologo SET {value_set};")
    return {"message": "Patologo created", }, 200


def eliminar_patologo(index: int):
    response = query(f"DELETE from patologo WHERE id = {index};")
    return {
                "message": "Patologo deleted",
            }, 200


def update_patologo(p_id: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE patologo set {value_set} WHERE id = {p_id};")
    return {"message": "Patologo updated"}, 200
