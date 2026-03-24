from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services import usuarios_service

bp_index = Blueprint('index', __name__)

@bp_index.get('/')
def index():
    session.clear()
    medicos = usuarios_service.listar_usuarios()
    return render_template('login.html', medicos = medicos)

@bp_index.get('/main')
def main():
    return render_template('dashboard.html')

@bp_index.post('/login')
def login():
    if request.method == 'POST':
        usuario = request.form['user']
        passw = request.form['password']

        if len(usuario)>0 and len(passw)>0:
            session['codigo'] = passw
            return redirect(url_for('index.main'))
        else:
            flash("Contraseña Vacia")
            return redirect(url_for('index.index'))
        
    else:
        return redirect(url_for('index.index'))
    
@bp_index.get('/logout')
def logout():
    return redirect(url_for('index.index'))    