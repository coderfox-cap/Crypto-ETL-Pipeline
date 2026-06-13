from sqlalchemy import create_engine, text

from config import *
from logger import logger


engine = create_engine(
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

upsert_query = """
INSERT INTO crypto_prices (
    id,
    symbol,
    name,
    current_price,
    market_cap,
    market_cap_rank,
    total_volume,
    high_24h,
    low_24h,
    price_change_percentage_24h,
    circulating_supply,
    total_supply,
    max_supply,
    last_updated
)

VALUES (
    :id,
    :symbol,
    :name,
    :current_price,
    :market_cap,
    :market_cap_rank,
    :total_volume,
    :high_24h,
    :low_24h,
    :price_change_percentage_24h,
    :circulating_supply,
    :total_supply,
    :max_supply,
    :last_updated
)

ON CONFLICT(id)

DO UPDATE SET
    symbol = EXCLUDED.symbol,
    name = EXCLUDED.name,
    current_price = EXCLUDED.current_price,
    market_cap = EXCLUDED.market_cap,
    market_cap_rank = EXCLUDED.market_cap_rank,
    total_volume = EXCLUDED.total_volume,
    high_24h = EXCLUDED.high_24h,
    low_24h = EXCLUDED.low_24h,
    price_change_percentage_24h = EXCLUDED.price_change_percentage_24h,
    circulating_supply = EXCLUDED.circulating_supply,
    total_supply = EXCLUDED.total_supply,
    max_supply = EXCLUDED.max_supply,
    last_updated = EXCLUDED.last_updated;
"""
def load_data(df):

    logger.info("Loading current table...")

    with engine.begin() as conn:

        for _, row in df.iterrows():

            conn.execute(
                text(upsert_query),
                row.to_dict()
            )

    logger.info(
        f"{len(df)} rows loaded."
    )


def load_history(df):

    history_df = df[
        [
            'id',
            'symbol',
            'name',
            'current_price',
            'market_cap',
            'total_volume',
            'price_change_percentage_24h'
        ]
    ].copy()

    history_df.rename(
        columns={'id': 'coin_id'},
        inplace=True
    )

    history_df.to_sql(
        'crypto_price_history',
        engine,
        if_exists='append',
        index=False
    )

    logger.info(
        f"{len(history_df)} rows added to history."
    )