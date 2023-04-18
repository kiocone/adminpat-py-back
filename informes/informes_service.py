import types

from database import query


def get_seciencia_informes():
    response = query(f"SELECT * FROM secuenciainforme WHERE id=1")
    if types.NoneType == type(response):
        response = [False]
    return response[0]
