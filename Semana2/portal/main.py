from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# URL de los microservicios
authentication_service_url = "http://localhost:8000"
customer_service_url = "http://localhost:8001"
invoice_service_url = "http://localhost:8002"
generic_service_url = "http://localhost:8003"
notification_service_url = "http://localhost:8004"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    # Realiza una solicitud al servicio de autenticación
    username = request.form["username"]
    password = request.form["password"]
    response = requests.post(f"{authentication_service_url}/login", data={"username": username, "password": password})
    data = response.json()

    if data.get("status") == 'autorizado':
        return redirect(url_for("dashboard"))  # Redirigir a la página de inicio después de iniciar sesión
    else:
        return "Error de autenticación"
    return f"Token de autenticación: {token}"

@app.route("/customers")
def list_customers():
    # Realiza una solicitud al servicio de clientes
    response = requests.get(f"{customer_service_url}/customers")
    customers = response.json()
    return jsonify(customers)

@app.route("/invoices")
def list_invoices():
    # Realiza una solicitud al servicio de facturas
    response = requests.get(f"{invoice_service_url}/invoices")
    invoices = response.json()
    return jsonify(invoices)

@app.route("/generic")
def generic_service():
    # Realiza una solicitud al servicio genérico
    response = requests.get(f"{generic_service_url}/generic")
    message = response.json().get("message")
    return message

@app.route("/send_notification")
def send_notification():
    # Realiza una solicitud al servicio de notificaciones
    user_id = request.args.get("user_id")
    message = request.args.get("message")
    response = requests.post(f"{notification_service_url}/send_notification", params={"user_id": user_id, "message": message})
    return response.text

if __name__ == '__main__':
    app.run(debug=True)