print("El código se está ejecutando")
from recipeRealm.database.conexion import Conexion
from recipeRealm.models.usuario import Usuario
from recipeRealm.models.receta import Receta


def main():
  print("Iniciando la función main")

  # Inicializar la base de datos
  conexion = Conexion()
  conexion.crear_tablas()

  # Crear instancias de usuarios, recetas, etc.
  usuario1 = Usuario(1, 'Usuario1', 'usuario1@example.com', 'contraseña1')
  usuario2 = Usuario(2, 'Usuario2', 'usuario2@example.com', 'contraseña2')
  receta1 = Receta(1, 'Receta 1', 'Ingredientes de la receta 1',
                   'Instrucciones de la receta 1', usuario1)

  # Realizar operaciones con las clases
  usuario1.guardar_receta(receta1)
  usuario2.agregar_comentario(receta1, 'Un comentario')

  # Cerrar la conexión con la base de datos
  conexion.cerrar_conexion()

  print("Terminando la función main")


if __name__ == "__main__":
  main()
