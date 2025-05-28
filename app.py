from flask import Flask, request, render_template_string, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # necesario para usar sesiones

HTML_PAGE = '''
<!doctype html>
<title>Adivina el número</title>
<h1>Adivina un número entre 1 y 100</h1>
{% if message %}
    <p><strong>{{ message }}</strong></p>
{% endif %}
<form method="post" action="/">
    <input type="number" name="guess" min="1" max="100" required autofocus>
    <input type="submit" value="Adivinar">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)

    message = None

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            number = session['number']
            if guess < number:
                message = "Demasiado bajo. Intenta otra vez."
            elif guess > number:
                message = "Demasiado alto. Intenta otra vez."
            else:
                message = f"¡Correcto! El número era {number}. Se ha generado uno nuevo para ti."
                session['number'] = random.randint(1, 100)
        except ValueError:
            message = "Por favor ingresa un número válido, CAPULLO."


    return render_template_string(HTML_PAGE, message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
