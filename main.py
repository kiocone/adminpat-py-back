from flask import Flask
from markupsafe import escape

from cups import cups_controller
from entidad import entidad_controller
from eps import eps_controller
from patologos import patologos_controller
from users import users_controller
from pacientes import pacientes_controller

app = Flask(__name__)
app.register_blueprint(patologos_controller.patologos)
app.register_blueprint(users_controller.users)
app.register_blueprint(pacientes_controller.pacientes)
app.register_blueprint(eps_controller.eps)
app.register_blueprint(entidad_controller.entidad)
app.register_blueprint(cups_controller.cups)


@app.get('/<parametro>')
def panel_param(parametro):
    print(escape(parametro))
    return f"<h1>{parametro}</h1><p>La ruta [/{parametro}] no esta definida</p>"


@app.get('/')
def panel():
    return "<h1>panel</h1>"
