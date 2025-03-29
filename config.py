from pathlib import Path

from pydantic import BaseModel, Field


class Settings(BaseModel):
    # Rutas base
    BASE_DIR: Path = Path(__file__).resolve().parent

    # Carpeta para modelos (sin Field)
    MODEL_DIR: Path = BASE_DIR / "ml-web-app/src/model/"

    # Rutas para modelos y columnas
    MODEL_PATH: Path = MODEL_DIR / "model.pkl"
    FEATURES_PATH: Path = MODEL_DIR / "x_train_columns.pkl"

    # Rutas para datos
    RAW_DATA_DIR: Path = Field(
        default=BASE_DIR / "ml-ds/datalake/raw/",
        description="Ruta a los datos crudos"
    )
    PROCESSED_DATA_DIR: Path = Field(
        default=BASE_DIR / "ml-ds/datalake/processed/",
        description="Ruta a los datos procesados"
    )

    # Configuración del servidor
    HOST: str = Field(
        default="127.0.0.1",
        description="Dirección del host para el servidor Flask"
    )
    PORT: int = Field(default=5000, description="Puerto para el servidor Flask")
    DEBUG: bool = Field(default=True, description="Modo de depuración para Flask")


settings = Settings()
