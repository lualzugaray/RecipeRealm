import sqlite3


class Conexion:

  def __init__(self, db_name='recipe_realm.db'):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()

  def crear_tablas(self):
    # Crear la tabla de usuarios si no existe
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY,
                nombre_usuario TEXT,
                correo_electronico TEXT,
                contraseña TEXT
            )
        ''')

    # Crear la tabla de recetas si no existe
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS recetas (
                id_receta INTEGER PRIMARY KEY,
                titulo TEXT,
                ingredientes TEXT,
                instrucciones TEXT,
                autor_id INTEGER,
                FOREIGN KEY (autor_id) REFERENCES usuarios(id_usuario)
            )
        ''')

    # Crear la tabla de comentarios si no existe
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS comentarios (
                id_comentario INTEGER PRIMARY KEY,
                texto TEXT,
                autor_id INTEGER,
                receta_id INTEGER,
                FOREIGN KEY (autor_id) REFERENCES usuarios(id_usuario),
                FOREIGN KEY (receta_id) REFERENCES recetas(id_receta)
            )
        ''')

    # Crear la tabla de listas de compra si no existe
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lista_compras (
                id_lista INTEGER PRIMARY KEY,
                nombre_lista TEXT,
                items TEXT,
                propietario_id INTEGER,
                FOREIGN KEY (propietario_id) REFERENCES usuarios(id_usuario)
            )
        ''')

    self.conn.commit()

  def cerrar_conexion(self):
    self.conn.close()

  def insertar_usuario(self, nombre_usuario, correo_electronico, contraseña):
    self.cursor.execute(
        '''
            INSERT INTO usuarios (nombre_usuario, correo_electronico, contraseña)
            VALUES (?, ?, ?)
        ''', (nombre_usuario, correo_electronico, contraseña))
    self.conn.commit()

  def insertar_receta(self, titulo, ingredientes, instrucciones, autor_id):
    self.cursor.execute(
        '''
            INSERT INTO recetas (titulo, ingredientes, instrucciones, autor_id)
            VALUES (?, ?, ?, ?)
        ''', (titulo, ingredientes, instrucciones, autor_id))
    self.conn.commit()

  def insertar_comentario(self, texto, autor_id, receta_id):
    self.cursor.execute(
        '''
            INSERT INTO comentarios (texto, autor_id, receta_id)
            VALUES (?, ?, ?)
        ''', (texto, autor_id, receta_id))
    self.conn.commit()

  def insertar_lista_compra(self, nombre_lista, items, propietario_id):
    self.cursor.execute(
        '''
            INSERT INTO lista_compras (nombre_lista, items, propietario_id)
            VALUES (?, ?, ?)
        ''', (nombre_lista, items, propietario_id))
    self.conn.commit()

  def obtener_lista_de_recetas(self):
    self.cursor.execute("SELECT * FROM recetas")
    recetas = self.cursor.fetchall()
    return recetas


if __name__ == "__main__":
  # Si ejecutamos este archivo directamente, se crearán las tablas
  conexion = Conexion()
  conexion.crear_tablas()
  conexion.cerrar_conexion()
