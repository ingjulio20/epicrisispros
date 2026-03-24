from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services import pacientes_service, diagnosticos_service, prevaloraciones_service, medicos_service
from flask_weasyprint import HTML, render_pdf
from io import BytesIO
import base64
import pyodbc as error

bp_prevaloraciones = Blueprint('prevaloraciones', __name__)

@bp_prevaloraciones.get('/prevaloraciones/<medico>')
def prevaloraciones(medico):
    medico = session['codigo']
    registros = prevaloraciones_service.listar_prevaloraciones(medico)
    return render_template('tepl_prevaloraciones/prevaloraciones.html', registros = registros)

@bp_prevaloraciones.get('/add_prevaloracion')
def add_prevaloracion():
    pacientes = pacientes_service.listar_pacientes()
    diagnosticos = diagnosticos_service.listar_diagnosticos()
    return render_template('tepl_prevaloraciones/add_prevaloracion.html', pacientes = pacientes, diagnosticos = diagnosticos)

@bp_prevaloraciones.post('/insert_prevaloracion')
def insert_prevaloracion():
    try:
        if request.method == 'POST':
            fecha = request.form["fechaAt"]
            hora = request.form["horaAt"]
            codigo = request.form["documentoPac"]
            medico = request.form["medico"]
            motivo_consulta = request.form["motivoConsulta"]
            examen_mental = request.form["examenMental"]
            examen_fisico = request.form["examenFisico"]
            antecedentes = request.form["antecedentes"]
            enfermedad_actual = request.form["enfActual"]
            cod_diag1 = request.form["codDiag1"]
            nom_diag1 = request.form["nomDiag1"]
            cod_diag2 = request.form["codDiag2"]
            nom_diag2 = request.form["nomDiag2"]
            cod_diag3 = request.form["codDiag3"]
            nom_diag3 = request.form["nomDiag3"]
            plan_trata = request.form["plan"]

            prevaloraciones_service.insert_prevaloracion(fecha, hora, codigo, medico, motivo_consulta, examen_mental, examen_fisico,
                                                         antecedentes, enfermedad_actual, cod_diag1, nom_diag1, cod_diag2, nom_diag2, cod_diag3, nom_diag3,
                                                         plan_trata)
            
            flash("H.C. Prevaloración guardada exitosamente", "success")
            return redirect(url_for('prevaloraciones.prevaloraciones', medico = medico ))

    except error.Error as e:
        flash(f"Se presentó un error inesperado: {e}", "error")
        return redirect(url_for('prevaloraciones.prevaloraciones', medico = medico ))
    
    except Exception as ex:
        flash(f"Se presentó un error inesperado: {ex}", "error")
        return redirect(url_for('prevaloraciones.prevaloraciones', medico = medico ))
    
@bp_prevaloraciones.get('/hc_prevaloracion/<idpac>/<id>/<idmed>')
def hc_prevaloracion(idpac, id, idmed):
    #Datos de paciente
    paciente = pacientes_service.listar_paciente_doc(idpac)
    #Datos historia Prevaloración
    prevaloracion = prevaloraciones_service.listar_prevaloracion_id(id)
    #Datos Medico Profesional
    medico = medicos_service.listar_medico_firma(idmed)
    imagen_firma = BytesIO(medico[0])
    if imagen_firma:
        firma = base64.b64encode(imagen_firma.read()).decode('utf-8')

    html = render_template('tepl_prevaloraciones/hc_prevaloracion.html', paciente = paciente, prevaloracion = prevaloracion, medico = medico, firma = firma)
    return render_pdf(HTML(string = html))