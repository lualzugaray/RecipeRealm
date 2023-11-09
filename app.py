from flask import Flask, render_template, request, redirect, url_for
from recipeRealm.database.conexion import Conexion

app = Flask(__name__, template_folder="recipeRealm/templates")


@app.route('/', methods=['GET'])
def inicio():
  mensaje_bienvenida = "Bienvenido a RecipeRealm. Tu lugar para descubrir y compartir recetas deliciosas."
  return render_template('inicio.html', mensaje_bienvenida=mensaje_bienvenida)


# Ruta para agregar una receta
@app.route('/registro', methods=['GET', 'POST'])
def registro():
  if request.method == 'POST':

    nombre_usuario = request.form['nombre_usuario']
    correo_electronico = request.form['correo_electronico']
    contraseña = request.form['contraseña']
    conexion = Conexion()
    conexion.insertar_usuario(nombre_usuario, correo_electronico, contraseña)
    conexion.cerrar_conexion()

    return redirect(url_for('login'))

  return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':

    correo_electronico = request.form['correo_electronico']
    contraseña = request.form['contraseña']

    return redirect(url_for('home'))

  return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
