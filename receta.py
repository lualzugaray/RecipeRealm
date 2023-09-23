class Receta:
    def __init__(self, id_receta, titulo, ingredientes, instrucciones, autor):
        self.id_receta = id_receta
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.comentarios = []  # Inicialmente, la lista de comentarios está vacía.
        self.calificaciones = []  # Inicialmente, la lista de calificaciones está vacía.
        self.autor = autor

    def agregar_calificacion(self, calificacion):
        """
        Agrega una calificación a la receta.
        :param calificacion: La calificación a agregar.
        """
        self.calificaciones.append(calificacion)

    def agregar_comentario(self, comentario):
        """
        Agrega un comentario a la receta.
        :param comentario: El comentario a agregar.
        """
        self.comentarios.append(comentario)