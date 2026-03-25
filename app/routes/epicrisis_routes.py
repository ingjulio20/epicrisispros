from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.services import pacientes_service, evoluciones_service, diagnosticos_service, epicrisis_service, medicos_service
from flask_weasyprint import HTML, render_pdf
from io import BytesIO
import base64
import mysql.connector.errors as error

bp_epicrisis = Blueprint('epicrisis', __name__)

@bp_epicrisis.get('/epicrisis/<medico>')
def epicrisis(medico):
    #medico = session['codigo']
    #registros = epicrisis_service.listar_epicrisis(medico)
    return render_template('tepl_epicrisis/epicrisis.html')

#Ruta AJAX para traer los registros segun la busqueda x documento
@bp_epicrisis.post('/getRegistrosEpicrisisDoc')
def getRegistrosEpicrisisDoc():
    try:
        data = request.get_json()
        medico = data.get('med')
        paciente = data.get('paciente')
        registros = epicrisis_service.listar_epicrisis_documento(medico, paciente)
        if registros:
            return jsonify(registros), 200
        else:
            return jsonify({"Error": f"No se encontraron registros asociados"}), 404
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500

    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500    

#Ruta AJAX para traer los registros según la busqueda x historia
@bp_epicrisis.post('/getRegistrosEpicrisisHisto')
def getRegistrosEpicrisisHisto():
    try:
        data = request.get_json()
        medico = data.get('med')
        historia = data.get('historia')
        registros = epicrisis_service.listar_epicrisis_atencion(medico, historia)
        if registros:
            return jsonify(registros), 200
        else:
            return jsonify({"Error": "No se encontraron registros asociados"}), 404
        
    except error.Error as e:
        return jsonify({"Error": f"{e.msg}"}), 500
    
    except Exception as ex:
        return jsonify({"Error": f"{ex}"}), 500

@bp_epicrisis.get('/add_epicrisis')
def add_epicrisis():
    pacientes = pacientes_service.listar_pacientes()
    diagnosticos = diagnosticos_service.listar_diagnosticos()
    return render_template('tepl_epicrisis/add_epicrisis.html', pacientes = pacientes, diagnosticos = diagnosticos)

@bp_epicrisis.post('/insert_epicrisis')
def insert_epicrisis():
    try:
        if request.method == 'POST':
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            fecha_ingreso = request.form["fecha_ingreso"]
            fecha_egreso = request.form["fecha_egreso"]
            codigo = request.form["codigo"]
            nombre = request.form["paciente"]
            medico = request.form["medico"]
            motivo_consulta = request.form["motivo_consulta"]
            evolucion_clinica = request.form["evolucion_clinica"]
            tratamiento = request.form["tratamiento"]
            examen_clinico = request.form["examen_clinico"]
            continua = request.form["continua"]
            cod_diag = request.form["cod_diag"]
            nom_diag = request.form["nom_diag"]
            plan = request.form["plan"]

            epicrisis_service.insert_epicrisis(fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
                                               tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan)
            
            flash("H.C. Epicrisis guardada exitosamente", "success")
            return redirect(url_for('epicrisis.epicrisis', medico = medico))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('epicrisis.epicrisis', medico = medico ))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('epicrisis.epicrisis', medico = medico))
    
@bp_epicrisis.get('/edit_epicrisis/<int:id>')
def edit_epicrisis(id):
    epicrisis = epicrisis_service.listar_epicrisis_id(id)
    pacientes = pacientes_service.listar_pacientes()
    diagnosticos = diagnosticos_service.listar_diagnosticos()
    return render_template('tepl_epicrisis/edit_epicrisis.html', epicrisis = epicrisis, pacientes = pacientes, diagnosticos = diagnosticos)

@bp_epicrisis.post('/update_epicrisis')
def update_epicrisis():
    try:
        if request.method == 'POST':
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            fecha_ingreso = request.form["fecha_ingreso"]
            fecha_egreso = request.form["fecha_egreso"]
            codigo = request.form["codigo"]
            nombre = request.form["paciente"]
            medico = request.form["medico"]
            motivo_consulta = request.form["motivo_consulta"]
            evolucion_clinica = request.form["evolucion_clinica"]
            tratamiento = request.form["tratamiento"]
            examen_clinico = request.form["examen_clinico"]
            continua = request.form["continua"]
            cod_diag = request.form["cod_diag"]
            nom_diag = request.form["nom_diag"]
            plan = request.form["plan"]
            id_epicrisis = request.form["id_epicrisis"]

            epicrisis_service.update_epicrisis(fecha, hora, fecha_ingreso, fecha_egreso, codigo, nombre, medico, motivo_consulta, evolucion_clinica,
                                               tratamiento, examen_clinico, continua, cod_diag, nom_diag, plan, id_epicrisis)
            
            flash("H. C. Epicrisis actualizada exitosamente", "success")
            return redirect(url_for('epicrisis.epicrisis', medico = medico ))
        
    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e.msg}", "error")
        return redirect(url_for('epicrisis.epicrisis', medico = medico ))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('epicrisis.epicrisis', medico = medico ))

@bp_epicrisis.get('/hc_epicrisis/<idpac>/<id>/<idmed>')
def hc_epicrisis(idpac, id, idmed):
    #Datos de paciente
    paciente = pacientes_service.listar_paciente_documento(idpac)
    #Datos Historia Epicrisis
    epicrisis = epicrisis_service.listar_epicrisis_id(id)
    #Datos Medico Profesional
    medico = medicos_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('tepl_epicrisis/hc_epicrisis.html', paciente = paciente, epicrisis = epicrisis, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))


""" Ruto AJAX para evoluciones """
@bp_epicrisis.post('/get_evoluciones')
def get_evoluciones():
    if request.method == 'POST':
        fechaInicio = request.form["fecha_ingreso"]
        fechaFin = request.form["fecha_egreso"]
        medico = request.form["medico"]
        paciente = request.form["codigo"]

        evoluciones = evoluciones_service.listar_evos_psiq(fechaInicio, fechaFin, medico, paciente)
        return render_template('tepl_epicrisis/tbl_evos.html', evoluciones = evoluciones)
    