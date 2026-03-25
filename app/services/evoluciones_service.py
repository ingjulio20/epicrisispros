from app.database import db

def listar_evos_psiq(fechaInicio, fechaFin, medico, paciente):
    evoluciones = []
    conn = db.connection()
    sql = """ SELECT h.fecha 'FECHA', h.evolucion 'EVOLUCIÓN', h.historia 'HISTORIA'
              FROM histopsicologiaevo h 
              WHERE h.fecha BETWEEN CAST(? AS DATE) AND CAST(? AS DATE)
              AND h.medico = ? AND h.codigo = ? """
    
    params = (fechaInicio, fechaFin, medico, paciente)
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        result = cursor.fetchall()
        for row in result:
            evoluciones.append({'fecha': row[0], 'contenido': row[1], 'historia': row[2]})

    conn.close()
    return evoluciones        