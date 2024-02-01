from datetime import datetime, timedelta
from base64 import b64encode
from bcrypt import checkpw
from functools import wraps
from flask import abort, request
from database import query


date_time = datetime


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            abort(401)
        token_values = request.headers['Authorization'].split(" ")
        if token_values[0].lower() == "bearer":
            token = token_values[1]
            response = get_token(token)
            if response == False:
                abort(401)
            else:
                return f(*args, **kws)       
    return decorated_function


# Primera version de validador de token
""" def valid_auth(token):
    if token is None:
        return False
    token_values = token.split(" ")
    if token_values[0].lower() == "bearer":
        token = token_values[1]
        response = users_service.get_token(token)
        if response == False:
            return False
        else:
            return True """


def loginUser(username, password):

    q_response = query(f"SELECT username, password FROM users WHERE username='{username}'")
    
    if q_response is not None: 
        if (q_response[0]['username'] == username) and checkpw(password, q_response[0]['password']):
            user_data = query(f"SELECT id, username, fullname, email FROM users WHERE username='{username}'")
            user_id = user_data[0]['id']
            token_seed = {'created_at': date_time.now().timestamp(), 'email': user_data[0]['email']}
            encoded_data = str(token_seed).encode("utf-8")
            new_token = b64encode(encoded_data)
            update_token_by_user_id(user_id, new_token)
            response = new_token
            response = True , response
        else:
            response = False, False
    else:
        response = False, False
    return response


def get_token(token:str):
    query_response = query(f"SELECT id, user_id, created_at, token from activetokens where token='{token}';")
    if query_response is None:
        return False
    created_at = query_response[0]['created_at']
    plus_12_hours = timedelta(hours=12)
    date_now = date_time.now()
    expired_time = created_at + plus_12_hours
    if query_response is None or (expired_time < date_now):
        return False
    else:
        return query_response[0]['token']
    

def set_token_by_user_id(id: int, token: str):
    date_now = date_time.now()
    query(f"INSERT INTO activetokens SET user_id='{id}',created_at='{date_now}',  token='{token}';")
    return


def update_token_by_user_id(id: int, token: str):
    date_now = date_time.now()
    token = str(token)
    token = token.split("'")[1]
    token_exist = query(f"SELECT id, user_id, created_at, token from activetokens where token='{token}';")
    if token_exist is None:
        set_token_by_user_id(id, token)
    else:
        query(f"UPDATE activetokens SET created_at='{date_now}', token='{token}' WHERE user_id='{id}';")
    return