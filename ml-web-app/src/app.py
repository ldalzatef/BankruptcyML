import sys
from pathlib import Path
from flask import Flask, request, render_template
import joblib
import pandas as pd

# Agregar el directorio raíz del proyecto al PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[2]  # Subir dos niveles desde src/
sys.path.append(str(ROOT_DIR))

from config import settings

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo y las columnas
modelo = joblib.load(settings.MODEL_PATH)
columnas = joblib.load(settings.FEATURES_PATH)

@app.route('/')
def home():
    """Renderiza la página principal."""
    return render_template('index.html', columns=columnas)

@app.route('/predict', methods=['POST'])
def predict():
    """Procesa los datos del formulario y realiza la predicción."""
    try:
        # Obtener datos del formulario
        input_data = {col: float(request.form[col]) for col in columnas}

        # Crear DataFrame con los datos de entrada
        entrada = pd.DataFrame([input_data])

        # Realizar la predicción
        resultado = modelo.predict(entrada)[0]

        # Retornar el resultado
        return render_template('index.html', prediction=f'Predicción: {resultado}')
    except Exception as e:
        return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)