from app.database import db

def listar_pacientes():
    pacientes = []
    conn = db.connection()
    sql = """ SELECT codigo, CONCAT(ppellido,' ',sapellido,' ',nombre,' ',snombre) FROM paciente"""
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            pacientes.append({'codigo': row[0], 'nombre': row[1]})

    conn.close()
    return pacientes

def listar_paciente_doc(codigo):
    paciente = None
    conn = db.connection()
    sql = """ SELECT rtrim(p.tipo_c), rtrim(p.codigo), CONCAT(rtrim(p.ppellido),' ',rtrim(p.sapellido),' ',rtrim(p.nombre),' ',rtrim(p.snombre)), 
                CONVERT(varchar, p.fecha_nac, 110), 
                CASE
                    WHEN p.Estadocivil = 1 THEN 'SOLTERO(A)' 
                    WHEN p.Estadocivil = 2 THEN 'CASADO(A)'
                    WHEN p.Estadocivil = 3 THEN 'SEPARADO(A)'
                    WHEN p.Estadocivil = 4 THEN 'VIUDO(A)'
                    WHEN p.Estadocivil = 5 THEN 'UNIÓN LIBRE'
                END, p.acompañante,
                CASE
                    WHEN p.sexo = 1 THEN 'MASCULINO'
                    WHEN p.sexo = 2 THEN 'FEMENINO'
                END,
                p.ocupacion, p.telacompañante, SUBSTRING(p.direccion, 0, 30), p.telefono, p.responsable, p.nom_mun, p.parentesco, p.telresponsable
                FROM paciente p WHERE p.codigo = ? """
    
    params = (codigo)
    with conn.cursor() as cursor:
        cursor.execute(sql, params) 
        result = cursor.fetchone()
        paciente = result

    conn.close()
    return paciente

def listar_paciente_documento(codigo):
    paciente = None
    conn = db.connection()
    sql = """ SELECT rtrim(p.tipo_c), rtrim(p.codigo), CONCAT(rtrim(p.ppellido),' ',rtrim(p.sapellido),' ',rtrim(p.nombre),' ',rtrim(p.snombre)), 
                CONVERT(varchar, p.fecha_nac, 110), CONCAT(DATEDIFF(YEAR , p.fecha_nac, SYSDATETIME()),' ',RTRIM(p.vlr_edad)),
                CASE
                    WHEN p.sexo = 1 THEN 'MASCULINO'
                    WHEN p.sexo = 2 THEN 'FEMENINO'
                END, SUBSTRING(p.direccion, 0, 30), p.telefono, p.nom_mun, 'MUTUAL SER', p.ocupacion,
                CASE
                    WHEN p.Estadocivil = 1 THEN 'SOLTERO(A)' 
                    WHEN p.Estadocivil = 2 THEN 'CASADO(A)'
                    WHEN p.Estadocivil = 3 THEN 'SEPARADO(A)'
                    WHEN p.Estadocivil = 4 THEN 'VIUDO(A)'
                    WHEN p.Estadocivil = 5 THEN 'UNIÓN LIBRE'
                END, p.acompañante,  p.telacompañante, p.parentesco, p.responsable, p.telresponsable
                FROM paciente p WHERE p.codigo = ? """
    
    params = (codigo)
    with conn.cursor() as cursor:
        cursor.execute(sql, params) 
        result = cursor.fetchone()
        paciente = result

    conn.close()
    return paciente
