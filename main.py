import datetime
from flask import Flask
from markupsafe import escape

from cupss import cups_controller
from entidad import entidad_controller
from eps import eps_controller
from informes import informes_controller
from patologos import patologos_controller
from users import users_controller
from pacientes import pacientes_controller


def update_log(datos):
    archivo = open('eventos.txt', 'a')
    archivo.write(f'{datetime.datetime.now()} - {datos}\n')
    archivo.close()


app = Flask(__name__)
app.register_blueprint(patologos_controller.patologos)
app.register_blueprint(users_controller.users)
app.register_blueprint(pacientes_controller.pacientes)
app.register_blueprint(eps_controller.eps)
app.register_blueprint(entidad_controller.entidad)
app.register_blueprint(cups_controller.cups)
app.register_blueprint(informes_controller.informes)


@app.get('/<parametro>')
def panel_param(parametro):
    update_log(parametro)
    return f"<h1>{parametro}</h1><p>La ruta [/{parametro}] no esta definida</p>"


@app.get('/')
def panel():
    return "<h1>panel</h1>"
