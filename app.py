from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(_name_)

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="",  
    database="db_academica"
)


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/registro')
def registro_page():
    return render_template('registro.html')


@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    usuario = datos['usuario']
    clave = datos['clave']
    nombre = datos['nombre']
    direccion = datos['direccion']
    telefono = datos['telefono']

    cursor = db.cursor()
    query = "INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (usuario, clave, nombre, direccion, telefono))
    db.commit()

    return jsonify({'message': 'Usuario registrado con éxito'}), 200


@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos['usuario']
    clave = datos['clave']

    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE usuario = %s AND clave = %s"
    cursor.execute(query, (usuario, clave))
    user = cursor.fetchone()

    if user:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 401

if _name_ == '_main_':
    app.run(debug=True)