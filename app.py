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
    # Obtener datos del formulario
    nombre_usuario = request.form['nombre_usuario']
    correo_electronico = request.form['correo_electronico']
    contraseña = request.form['contraseña']

    # Verificar si el correo electrónico ya está en uso

    # Si no está en uso, insertar el usuario en la base de datos
    conexion = Conexion()
    conexion.insertar_usuario(nombre_usuario, correo_electronico, contraseña)
    conexion.cerrar_conexion()

    # Redirigir al inicio de sesión o a otra página
    return redirect(url_for('login'))

  return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Obtener datos del formulario
    correo_electronico = request.form['correo_electronico']
    contraseña = request.form['contraseña']

    # Verificar las credenciales del usuario en la base de datos

    # Si las credenciales son válidas, redirigir a la página de inicio o a otra página
    return redirect(url_for('home'))

  return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
