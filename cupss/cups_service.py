import types
from database import query
from shared import utilities


def get_cups():
    response = query("SELECT * FROM cups")
    return response


def get_cups_by_id(index: int):
    response = query(f"SELECT * FROM cups WHERE id={index}")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def create_cups(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO cups SET {value_set}")
    return {"message": "CUPS created", }, 200


def update_cups(index: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE cups SET {value_set} WHERE id = {index}")
    return {"message": "CUPS updated", }, 200


def eliminar_cups(index: int):
    query(f"DELETE from cups WHERE id = {index};")
    return {"message": "CUPS deleted"}, 200
