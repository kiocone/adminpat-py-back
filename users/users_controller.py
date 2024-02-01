from flask import Blueprint, request
from users import users_service
from authentication.auth import authorize, loginUser
users = Blueprint('users', __name__)


@users.get('/users')
@authorize
def get_users():
    queryParasms = request.args
    pageIndex = queryParasms.get('pageIndex')
    pageSize = queryParasms.get('pageSize')
    response = users_service.get_users(int(pageIndex), int(pageSize))
    return response, 200


@users.get('/users/<int:index>')
def get_users_by_id(index):
    response = users_service.get_user_by_id(index)
    if response is False:
        response = {
                "message": "User not found",
            }, 404
    return response


@users.post('/users')
def create_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = users_service.create_user(request.json)
    else:
        response = {'message': 'Content-Type not supported!'}, 400
    return response


@users.put('/users/<int:index>')
def update_user(index):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = users_service.update_user(index, request.json)
    else:
        response = {'message': 'Content-Type not supported!'}, 400
    return response


@users.delete('/users/<int:index>')
def delete_user(index):
    if users_service.get_user_by_id(index) is not False:
        respuesta = users_service.delete_user(index)
    else:
        respuesta = {'message': 'No existe el usuario'}, 404
    return respuesta

@users.post('/users/<int:index>/update-password')
def update_password(index):
    if users_service.get_user_by_id(index) is False:
        return {'message': 'User do not exist'}, 404
    matched = users_service.update_password(index, request.json)
    if matched:
        response = {
                "message": "Password updated",
            }, 200
    else:
        response = {
                "message": "Password do not match",
                "error": "401"
            }, 401
    return response


@users.post('/users/login')
def login():
    json_keys = dict(request.json).keys()
    if 'username' not in json_keys or 'password' not in json_keys:
        return "bad request", 400
    username = request.json['username']
    password = request.json['password']
    valid, token = loginUser(username, password)
    if valid:
        if type(token) == bytes:
            token=str(token).split("'")[1]
        response = {
                "token": token
            }, 200
    else:
        response = {
                "message": "Authentication is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
    return response
