import pandas as pd


def transform_data(df):

    columns = [
        'id',
        'symbol',
        'name',
        'current_price',
        'market_cap',
        'market_cap_rank',
        'total_volume',
        'high_24h',
        'low_24h',
        'price_change_percentage_24h',
        'circulating_supply',
        'total_supply',
        'max_supply',
        'last_updated'
    ]

    df = df[columns].copy()

    df['last_updated'] = pd.to_datetime(
        df['last_updated']
    )

    df['symbol'] = df['symbol'].str.upper()

    return df