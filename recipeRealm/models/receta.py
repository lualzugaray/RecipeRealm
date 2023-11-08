class Receta:
  def __init__(self, id_receta, titulo, ingredientes, instrucciones, autor):
      self.id_receta = id_receta
      self.titulo = titulo
      self.ingredientes = ingredientes
      self.instrucciones = instrucciones
      self.comentarios = []  # Lista de comentarios en la receta
      self.calificaciones = []  # Lista de calificaciones de la receta
      self.autor = autor

  def agregar_calificacion(self, calificacion):
      self.calificaciones.append(calificacion)

  def agregar_comentario(self, comentario):
      self.comentarios.append(comentario)
