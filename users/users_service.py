import types
from database import query
import bcrypt
from shared import utilities, config

default_page_size = config.default_page_size()
salt = bcrypt.gensalt(10)


def get_users(pageIndex:int = 0, pageSize:int = default_page_size):
    offset = pageIndex * pageSize
    resp = query(f"SELECT * from users LIMIT {pageSize} OFFSET {offset};")
    return resp


def get_user_by_id(*args):
    response = query(f"SELECT * FROM users where id = ?;", *args)
    if types.NoneType == type(response):
        response = False
    return response


def delete_user(index):
    query(f"DELETE from users WHERE id = {index};")
    return {
                "message": "User deleted",
            }, 204


def create_user(payload):
    username = payload['username']
    q_response = query(f"SELECT id, username FROM users WHERE username='{username}'")
    if q_response is not None:
        return {"message": f"El usuario {username} ya existe"}, 400
    payload['password'] = bcrypt.hashpw(payload['password'], salt)
    value_set = utilities.payload_to_valueset(payload)
    query(f"INSERT INTO users SET {value_set};")
    return {"message": "User created"}, 200


def update_user(p_id: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE users set {value_set} WHERE id = {p_id};")
    return {"message": "User updated"}, 200


def update_password(index: int, password_set):
    hashed_password = query(f"SELECT password FROM users where id = ?;", index)
    if not hashed_password:
        return False
    matched = bcrypt.checkpw(password_set['password'], hashed_password[0]['password'])
    if matched:
        new_password = bcrypt.hashpw(password_set['new_password'], salt)
        query(f"UPDATE users set password='{new_password}' WHERE id = {index};")
    return matched

