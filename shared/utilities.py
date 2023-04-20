import datetime


def payload_to_valueset(payload):
    value_set = ""
    for value in dict(payload).keys():
        if key_value_valid(value, dict(payload)[value]):
            value_set += f"{value}='{dict(payload)[value]}',"
    return value_set[0:-1]


def key_value_valid(key, value):
    """
    :param key: str | bool
    :param value: str
    :return: bool
    Verifies if key is True or not empty string and has value
    """
    if type(key) == bool:
        return bool(key) and str(value).strip() != ""
    else:
        return str(key).strip() != "" and str(value).strip() != ""


def generar_codigo_inf(tipo_inf, ult_cod):
    fecha = datetime.datetime.now()
    year = str(fecha.year)[2:4]
    month = f"0{fecha.month}"[0:2]
    return f"{tipo_inf}{year}{month}-{ult_cod}"
