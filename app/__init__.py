from flask import Flask, render_template, request, redirect, url_for, flash, session

#Importe de Blueprints
from app.routes.index_routes import bp_index
from app.routes.epicrisis_routes import bp_epicrisis
from app.routes.prevaloraciones_routes import bp_prevaloraciones

#Instancia Principal
def create_app():
    app = Flask(__name__, template_folder="templates")

    #Configuración
    app.secret_key = '3p1cr1s15_K3&'

    #Registro de Blueprints
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_epicrisis)
    app.register_blueprint(bp_prevaloraciones)

    #Verificar las URL y Redireccionar a Login
    @app.before_request
    def verificar():
        ruta = request.path
        if(
            "codigo" not in session
            and ruta != "/"
            and ruta != "/login"
            and not ruta.startswith("/static")
        ):
            flash("Debe iniciar sesión", "warning")
            return render_template("login.html")
        
    return app    

application = create_app()