from app.database import db_mysql

#Metodo Listar todos los registros de epicrisis por medico
def listar_epicrisis(medico):
    reg_epicrisis = []
    conn = db_mysql.mysql_connection()
    operation = """ SELECT id_epicrisis, fecha, hora, codigo, nombre FROM epicrisis WHERE medico = %s"""
    with conn.cursor() as cursor:
        cursor.execute(operation, (medico, ))
        result = cursor.fetchall()
        for row in result:
            reg_epicrisis.append({'id': row[0], 'ingreso': row[1], 'egreso': row[2], 'codigo': row[3], 'nombre': row[4]})

    conn.close()
    return reg_epicrisis

#Metodo Listar epicrisis individual
def listar_epicrisis_id(id_epicrisis):
    epicrisis = None
    conn = db_mysql.mysql_connection()
    operation = """ SELECT * FROM epicrisis WHERE id_epicrisis = %s """
    with conn.cursor() as cursor:
        cursor.execute(operation, (id_epicrisis, ))
        result = cursor.fetchone()
        epicrisis = result

    conn.close()
    return epicrisis        

#Metodo Insertar Nueva epicrisis en BD
def insert_epicrisis(fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
                    tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan):
    
    conn = db_mysql.mysql_connection()
    operation = """ INSERT INTO epicrisis (fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
                    tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

    params = (fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
              tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan)
    with conn.cursor() as cursor:
        cursor.execute(operation, params)
        conn.commit()
        conn.close()

#Metodo Modificar epicrisis en BD
def update_epicrisis(fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
                     tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan, id_epicrisis):

    conn = db_mysql.mysql_connection()
    operation = """ UPDATE epicrisis SET fecha = %s, hora = %s, fecha_ingreso = %s, fecha_egreso = %s, codigo = %s, nombre = %s, medico = %s,
                    motivo_consulta = %s, evolucion_clinica = %s, tratamiento = %s, examen_clinico = %s, continua = %s,
                    cod_diag = %s, nom_diag = %s, plan = %s WHERE id_epicrisis = %s """ 

    params = (fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica, tratamiento,
              examen_clinico, continua, cod_diag, nom_diag, plan, id_epicrisis)

    with conn.cursor() as cursor:
        cursor.execute(operation, params)
        conn.commit()
        conn.close()       

#Metodo listar todas las epicrisis por rango de fecha y medico
def listar_epicrisis_report(fechaInicio, fechaFin, medico):
    list_epicrisis = []
    conn = db_mysql.mysql_connection()
    operation = """ SELECT e.fecha, e.hora, e.fecha_ingreso, e.fecha_egreso, e.motivo_consulta, e.evolucion_clinica, e.tratamiento, e.examen_clinico, e.continua, e.cod_diag, e.nom_diag, e.plan 
                    FROM epicrisis e 
                    WHERE e.fecha_ingreso BETWEEN %s AND %s and e.medico = %s """
    params = (fechaInicio, fechaFin, medico)
    with conn.cursor() as cursor:
        cursor.execute(operation, params)
        result = cursor.fetchall()
        for row in result:
            list_epicrisis.append({})

    conn.close()
    return list_epicrisis                    