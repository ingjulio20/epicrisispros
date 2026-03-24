from app.database import db

def listar_medico_firma(num_documento):
    medico = None
    conn = db.connection()
    sql = """ SELECT f.firma, rtrim(m.nombre), m.especialidad, m.codigo, m.registro_medico
              FROM firmamedicos f, medicos01 m 
              WHERE f.codigo = m.codigo and m.codigo = ? """
    
    params = (num_documento)
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        result = cursor.fetchone()
        medico = result

    conn.close()
    return medico    