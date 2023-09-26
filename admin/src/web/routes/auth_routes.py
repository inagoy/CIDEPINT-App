from flask import Blueprint, render_template
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/registro', methods=['GET', 'POST'])
def register():
    return render_template('registro.html')


@auth_bp.route('/iniciar-sesion', methods=['GET', 'POST'])
def login():
    return render_template('iniciar-sesion.html')
