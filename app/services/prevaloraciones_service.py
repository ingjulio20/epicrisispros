from app.database import db

def listar_prevaloraciones(medico):
    prevaloraciones = []
    conn = db.connection()
    sql = """ SELECT pr.id, pr.fecha, pr.hora, rtrim(pr.codigo), CONCAT(rtrim(ppellido),' ',rtrim(sapellido),' ',rtrim(nombre),' ',rtrim(snombre))
              FROM prevaloracion pr, paciente p 
              WHERE pr.codigo = p.codigo AND pr.medico = ?"""
    params = (medico)
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        result = cursor.fetchall()
        for row in result:
            prevaloraciones.append({'id': row[0], 'fecha': row[1], 'hora': row[2], 'documento': row[3], 'paciente': row[4]})

    conn.close()
    return prevaloraciones

def listar_prevaloracion_id(id_prevaloracion):
    prevaloracion = None
    conn = db.connection()
    sql = "SELECT * FROM prevaloracion WHERE id = ?"
    params = (id_prevaloracion)
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        result = cursor.fetchone()
        prevaloracion = result

    conn.close()
    return prevaloracion

def insert_prevaloracion(fecha, hora, codigo, medico, motivo_consulta, examen_mental, examen_fisico, antecedentes,
                         enfermedad_actual, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, plan_trata):
    conn = db.connection()
    sql = """ INSERT INTO prevaloracion (fecha, hora, codigo, medico, motivo_consulta, examen_mental, examen_fisico, antecedentes,
              enfermedad_actual, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, plan_trata)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

    params = (fecha, hora, codigo, medico, motivo_consulta, examen_mental, examen_fisico, antecedentes,
              enfermedad_actual, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3, plan_trata)
    
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        conn.commit()
        
    conn.close()