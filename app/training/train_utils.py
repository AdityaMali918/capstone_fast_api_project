from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent   # -> capstone_project/app

DATA_DIR = APP_DIR / "data"
DATA_FILE_PATH = DATA_DIR / "car-details.csv"

MODEL_DIR = APP_DIR / "models"
MODEL_PATH = MODEL_DIR / "model.joblib"