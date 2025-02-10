from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar el modelo preentrenado
model = joblib.load("CreditCardFraudDetector.pkl")

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class InputData(BaseModel):
    # Recibe una lista de diccionarios con las columnas y valores
    data: list[dict]


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renderizar la página principal."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze")
async def analyze_data(input_data: InputData):
    """Recibir datos JSON, procesarlos y realizar predicciones."""
    try:
        # Convertir los datos JSON a un DataFrame de pandas
        df = pd.DataFrame(input_data.data)

        # Verificar columnas requeridas
        required_columns = ['V14', 'V10', 'V4', 'V17',
                            'V16', 'V12', 'V3', 'V9', 'V2', 'V11']
        if not all(col in df.columns for col in required_columns):
            faltantes = [
                col for col in required_columns if col not in df.columns]
            return JSONResponse(
                content={"error": f"Faltan columnas requeridas: {faltantes}."},
                status_code=400,
            )

        # Realizar predicciones
        predictions = model.predict(df[required_columns])

        # Retornar los resultados
        return JSONResponse(
            content={
                "predictions": predictions.tolist(),
                "total_transactions": len(predictions),
                "fraud_cases": int(sum(predictions)),
            }
        )
    except Exception as e:
        print(f"Error en el backend: {str(e)}")
        return JSONResponse(
            content={
                "error": f"Ocurrió un error al procesar los datos: {str(e)}"},
            status_code=500,
        )
