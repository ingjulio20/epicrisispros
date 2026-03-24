from app.database import db

def listar_diagnosticos():
    diagnosticos = []
    conn = db.connection()
    sql = """ SELECT rtrim(codigo), rtrim(nombre) FROM diagnosticos ORDER BY nombre ASC """
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            diagnosticos.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return diagnosticos        