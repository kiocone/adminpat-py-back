from flask import Blueprint, request
from users import users_service

users = Blueprint('users', __name__)


@users.get('/users')
def get_users():
    response = users_service.get_users()
    return response


@users.get('/users/<int:index>')
def get_users_by_id(index):
    print('Get one user', index)
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
        print('Content-Type not supported!')

    #if len(request.form):
    #    response = users_service.create_user(dict(request.json))
    #elif request.data.decode():
    #    response = {
    #            "message": "Data should come in form-data",
    #            "error": "Bad request"
    #        }, 400
    #else:
    #    response = {
    #            "message": "There is no data",
    #            "error": "Bad request"
    #        }, 400
    return response


@users.put('/users/<int:index>')
def update_user(index):
    if len(request.form):
        respuesta = users_service.update_user(
            index,
            request.form.to_dict()
        )
    elif request.data.decode():
        respuesta = "Data should come in form-data"
    else:
        respuesta = "There is no data"
    return respuesta


@users.delete('/users/<int:index>')
def delete_user(index):
    respuesta = users_service.delete_user(index)
    return respuesta


@users.post('/users/<int:index>/update-password')
def update_password(index):
    password = request.form['password']
    new_password = request.form['new_password']
    matched = users_service.update_password(index, password, new_password)
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


@users.post('/users/signin')
def signin():
    # Pending implementaion of JWT strategy
    username = request.form['username']
    password = request.form['password']
    response = users_service.signin(username, password)
    if response:
        response = {
                "message": "Authentication Valid!",
                "data": None,
                "error": "No error"
            }, 200
    else:
        response = {
                "message": "Authentication is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
    return response
