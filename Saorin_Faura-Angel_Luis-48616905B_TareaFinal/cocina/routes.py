from flask import Flask, render_template, redirect, url_for, request, flash, session
from functools import wraps  # Para manejar decoradores como la verificación de roles

app = Flask(__name__)
# app.secret_key = "supersecretkey"  # Cambia esto por una clave más segura en producción

# ==============================
# Decoradores para verificar roles
# ==============================

def login_required(f):
    """
    Decorador para asegurarse de que un usuario está autenticado.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_role" not in session:
            flash("Por favor, inicia sesión para acceder a esta página.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def role_required(role):
    """
    Decorador para asegurarse de que el usuario tiene el rol adecuado.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get("user_role") != role:
                flash("No tienes permiso para acceder a esta página.", "danger")
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Rutas principales

@app.route("/")
def index():
    """
    Página de inicio.
    """
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Página de inicio de sesión.
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Simulación de autenticación (reemplazar con la lógica real)
        if email == "cliente@ejemplo.com" and password == "cliente123":
            session["user_role"] = "cliente"
            session["user_email"] = email
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("dashboard_cliente"))
        elif email == "trabajador@ejemplo.com" and password == "trabajador123":
            session["user_role"] = "trabajador"
            session["user_email"] = email
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("dashboard_trabajador"))
        else:
            flash("Correo o contraseña incorrectos.", "danger")
    
    return render_template("auth/login.html")


@app.route("/logout")
@login_required
def logout():
    """
    Cierra la sesión del usuario.
    """
    session.clear()
    flash("Has cerrado sesión exitosamente.", "info")
    return redirect(url_for("index"))

# Rutas para Clientes

@app.route("/cliente/dashboard")
@login_required
@role_required("cliente")
def dashboard_cliente():
    """
    Panel principal para clientes.
    """
    return render_template("cliente/dashboard.html")


@app.route("/cliente/perfil")
@login_required
@role_required("cliente")
def perfil_cliente():
    """
    Gestión del perfil del cliente.
    """
    return render_template("cliente/perfil.html")


@app.route("/cliente/pedidos")
@login_required
@role_required("cliente")
def pedidos_cliente():
    """
    Historial de pedidos del cliente.
    """
    return render_template("cliente/pedidos.html")

# Rutas para Trabajadores

@app.route("/trabajador/dashboard")
@login_required
@role_required("trabajador")
def dashboard_trabajador():
    """
    Panel principal para trabajadores.
    """
    return render_template("trabajador/dashboard.html")


@app.route("/trabajador/gestion-clientes")
@login_required
@role_required("trabajador")
def gestion_clientes():
    """
    Gestión de los clientes por parte de los trabajadores.
    """
    return render_template("trabajador/gestion_clientes.html")


@app.route("/trabajador/gestion-productos")
@login_required
@role_required("trabajador")
def gestion_productos():
    """
    Gestión de productos por parte de los trabajadores.
    """
    return render_template("trabajador/gestion_productos.html")


@app.route("/trabajador/reportes")
@login_required
@role_required("trabajador")
def reportes_trabajador():
    """
    Generación de reportes por parte de los trabajadores.
    """
    return render_template("trabajador/reportes.html")

# Manejo de errores

@app.errorhandler(404)
def page_not_found(e):
    """
    Página de error 404.
    """
    return render_template("error/404.html"), 404


@app.errorhandler(403)
def forbidden(e):
    """
    Página de error 403 (prohibido).
    """
    return render_template("error/403.html"), 403


@app.errorhandler(500)
def internal_server_error(e):
    """
    Página de error 500 (error interno del servidor).
    """
    return render_template("error/500.html"), 500

