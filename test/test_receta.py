import unittest
from recipeRealm.models.receta import Receta
from recipeRealm.models.usuario import Usuario
# Asegúrate de importar la clase Usuario también si la estás utilizando


class test_receta(unittest.TestCase):

  def test_agregar_calificacion(self):
    usuario = Usuario(1, 'Usuario1', 'usuario1@example.com', 'contraseña1')
    receta = Receta(1, 'Receta 1', 'Ingredientes de la receta 1',
                    'Instrucciones de la receta 1', usuario)
    receta.agregar_calificacion(4)
    self.assertEqual(receta.calificaciones, [4])

  def test_agregar_comentario(self):
    usuario = Usuario(1, 'Usuario1', 'usuario1@example.com', 'contraseña1')
    receta = Receta(1, 'Receta 1', 'Ingredientes de la receta 1',
                    'Instrucciones de la receta 1', usuario)
    receta.agregar_comentario('Un comentario')
    self.assertEqual(receta.comentarios, ['Un comentario'])


if __name__ == '__main':
  unittest.main()
