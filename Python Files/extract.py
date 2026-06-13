import requests
import pandas as pd

from config import API_URL
from logger import logger


def extract_data():

    logger.info("Extracting data...")

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(
        API_URL,
        params=params
    )

    response.raise_for_status()

    df = pd.DataFrame(response.json())

    logger.info(f"{len(df)} rows extracted.")

    return df