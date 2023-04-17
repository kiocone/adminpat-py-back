def payload_to_valueset(payload):
    value_set = ""
    for value in dict(payload).keys():
        if str(value).strip() != "":
            value_set += f"{value}='{dict(payload)[value]}',"
    return value_set[0:-1]
