import unittest
from recipeRealm.models.receta import Receta
from recipeRealm.models.usuario import Usuario


class test_usuario(unittest.TestCase):

  def test_iniciar_sesion(self):
    usuario = Usuario(1, 'Usuario1', 'usuario1@example.com', 'contraseña1')
    self.assertTrue(
        usuario.iniciar_sesion('usuario1@example.com', 'contraseña1'))
    self.assertFalse(
        usuario.iniciar_sesion('usuario1@example.com', 'contraseña2'))

  def test_agregar_calificacion(self):
    usuario = Usuario(1, 'Usuario1', 'usuario1@example.com', 'contraseña1')
    receta = Receta(1, 'Receta 1', 'Ingredientes de la receta 1',
                    'Instrucciones de la receta 1', usuario)
    usuario.agregar_calificacion(receta, 5)
    self.assertEqual(receta.calificaciones, [5])


if __name__ == '__main__':
  unittest.main()
