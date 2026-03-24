from app.database import db

def listar_usuarios():
    usuarios = []
    conn = db.connection()
    sql = """ SELECT rtrim(codigo) as codigo, rtrim(nombre) as nombre FROM medicos01
              WHERE especialidad in ('MEDICINA GENERAL','PSIQUIATRIA') and observaciones not like '%INACTIVO' ORDER BY nombre ASC """
    
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            usuarios.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return usuarios        