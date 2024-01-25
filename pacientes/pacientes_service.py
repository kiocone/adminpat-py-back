import types
from database import query
from shared import utilities


def get_pacientes(pageIndex:int = 0, pageSize:int = 10):
    offset = pageIndex * pageSize
    response = query(f"SELECT * FROM paciente LIMIT {pageSize} OFFSET {offset}")
    return response


def get_paciente_by_id(index: int):
    response = query(f"SELECT * FROM paciente WHERE id={index}")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def create_paciente(payload):
    payload['user_id'] = 1  # TODO: Get user_id from request.headers after JWT implementations
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO paciente SET {value_set}")
    return {"message": "Patologo created", }, 200


def update_paciente(index: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE paciente SET {value_set} WHERE id = {index};")
    return {"message": "Patologo updated", }, 200


def eliminar_paciente(index: int):
    query(f"DELETE from paciente WHERE id = {index};")
    return {"message": "Paciente deleted"}, 200
