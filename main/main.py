from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Ejercicio 1
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        edad = request.form.get("edad", "")
        cantidad_tarros = request.form.get("cantidad_tarros", "")

        if nombre and edad and cantidad_tarros:
            try:
                edad = int(edad)
                cantidad_tarros = int(cantidad_tarros)
                precio_unitario = 9000
                total_sin_descuento = cantidad_tarros * precio_unitario

                if 18 <= edad <= 30:
                    descuento = 0.15
                elif edad > 30:
                    descuento = 0.25
                else:
                    descuento = 0.0

                total_con_descuento = total_sin_descuento * (1 - descuento)

                resultado = {
                    "nombre": nombre,
                    "total_sin_descuento": total_sin_descuento,
                    "total_con_descuento": total_con_descuento,
                    "descuento": (
                        f"{int(descuento*100)}%" if descuento > 0 else "Sin descuento"
                    ),
                    "descontado": total_sin_descuento - total_con_descuento,
                }

            except ValueError:
                resultado = {
                    "error": "Por favor ingresa números válidos en edad y cantidad."
                }

    return render_template("ejercicio1.html", resultado=resultado)


# Ejercicio 2
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido Administrador Juan"
        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido Usuario Pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
