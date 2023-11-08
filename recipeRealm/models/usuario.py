class Usuario:
  def __init__(self, id_usuario, nombre_usuario, correo_electronico, contraseña):
      self.id_usuario = id_usuario
      self.nombre_usuario = nombre_usuario
      self.correo_electronico = correo_electronico
      self.contraseña = contraseña
      self.recetas_guardadas = []  # Lista de recetas guardadas por el usuario
      self.lista_compras = []  # Lista de compras creadas por el usuario

  def iniciar_sesion(self, correo, contraseña):
      if correo == self.correo_electronico and contraseña == self.contraseña:
          return True
      return False

  def agregar_calificacion(self, receta, calificacion):
      receta.agregar_calificacion(calificacion)

  def agregar_comentario(self, receta, comentario):
      receta.agregar_comentario(comentario)

  def crear_lista_compra(self, nombre_lista, items):
      lista_compra = ListaCompra(nombre_lista, items, self)
      self.lista_compras.append(lista_compra)

  def agregar_receta(self, titulo, ingredientes, instrucciones):
      receta = Receta(titulo, ingredientes, instrucciones, self)
      self.recetas_guardadas.append(receta)

  def guardar_receta(self, receta):
      self.recetas_guardadas.append(receta)

  def obtener_recetas_guardadas(self):
      return self.recetas_guardadas

  def obtener_lista_compras(self):
      return self.lista_compras
