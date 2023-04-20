import types
from database import query
from shared import utilities


def get_secuencia_informes():
    response = query(f"SELECT * FROM secuenciainforme WHERE id=1")
    if types.NoneType == type(response):
        response = [False]
    else:
        response = dict(response[0])
    return response


def update_secuencia_informes(payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE secuenciainforme set {value_set} WHERE id=1;")
    return {"message": "Secuencia informes updated", }, 200


def get_informes_q():
    response = query("SELECT * from informe WHERE t_informe='Q'")
    return response


def get_informes_l():
    response = query("SELECT * from informe WHERE t_informe='L'")
    return response


def get_informes_c():
    response = query("SELECT * from informec")
    return response


def get_informes_q_by_id(index):
    response = query(f"SELECT * from informe WHERE t_informe='Q' AND id={index};")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def get_informes_l_by_id(index):
    response = query(f"SELECT * from informe WHERE t_informe='L' AND id={index};")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def get_informes_c_by_id(index):
    response = query(f"SELECT * from informec WHERE id={index};")
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def create_inform_q(payload):
    validated = True
    validate_fields = ['numdoc', 'entidad', 'eps', 'paciente', 'patologo']
    for item_to_validate in validate_fields:
        if item_to_validate not in payload or str(payload[item_to_validate]).strip() == "":
            response = f"key or value in {item_to_validate} doesn't exist - Validation has failed"
            validated = False
    if validated:
        ultimos_codigos = get_secuencia_informes()
        payload['informe_cod'] = utilities.generar_codigo_inf("Q", ultimos_codigos['ultQ'])
        value_set = utilities.payload_to_valueset(payload)
        query(f"INSERT INTO informe SET {value_set}")
        response = {"message": f"Informe {payload['informe_cod']} created", }, 200
        update_secuencia_informes({"ultQ": ultimos_codigos['ultQ'] + 1})
    return response
