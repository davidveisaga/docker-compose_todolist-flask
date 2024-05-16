from flask import Flask, request, render_template, redirect, url_for
from db_op import add_text, get_data

app = Flask(__name__)
@app.route("/")
def home():
    tareas = get_data()
    return render_template('index.html', lista_tareas = tareas)

@app.route("/add_text", methods=["POST", "GET"])
def AddText():
    if request.method == "POST":
        text_value = request.form["tarea"]
        add_text(text_value)
        return redirect(url_for('home'))
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')