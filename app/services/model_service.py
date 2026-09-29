import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_key, get_cached_prediction

model = joblib.load(settings.model_path)

def prediction(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached_data = get_cached_prediction(cache_key)
    if cached_data:
        return cached_data

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_key(cache_key, prediction)
    return prediction