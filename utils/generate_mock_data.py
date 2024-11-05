import pandas as pd
import numpy as np
from datetime import datetime
import os

# This code generate mock price series data in different formats for testing purposes.
# Create a directory to save the mock data files if it doesn't exist
MOCK_DATA_DIR = "mock_data"
os.makedirs(MOCK_DATA_DIR, exist_ok=True)

def generate_ohlcv_data(start_date, periods, freq="D"):
    """Generates a DataFrame with OHLCV data."""
    date_rng = pd.date_range(start=start_date, periods=periods, freq=freq)
    data = {
        "date": date_rng,
        "open": np.random.uniform(100, 200, size=periods),
        "high": np.random.uniform(200, 300, size=periods),
        "low": np.random.uniform(50, 100, size=periods),
        "close": np.random.uniform(100, 200, size=periods),
        "volume": np.random.randint(1000, 5000, size=periods)
    }
    df = pd.DataFrame(data)
    return df

def save_mock_data():
    """Generates and saves multiple mock data files in different formats."""
    # Format 1: Full OHLCV Data (Daily)
    df_ohlcv_daily = generate_ohlcv_data(start_date="2023-01-01", periods=30, freq="D")
    df_ohlcv_daily.to_csv(f"{MOCK_DATA_DIR}/mock_data_ohlcv_daily.csv", index=False)
    print("Generated: mock_data_ohlcv_daily.csv")

    # Format 2: Partial Data (Date, High) at Daily Granularity
    df_high_only = df_ohlcv_daily[["date", "high"]]
    df_high_only.to_csv(f"{MOCK_DATA_DIR}/mock_data_high_only_daily.csv", index=False)
    print("Generated: mock_data_high_only_daily.csv")

    # Format 3: Full OHLCV Data (Hourly)
    df_ohlcv_hourly = generate_ohlcv_data(start_date="2023-01-01", periods=30 * 24, freq="H")
    df_ohlcv_hourly.to_csv(f"{MOCK_DATA_DIR}/mock_data_ohlcv_hourly.csv", index=False)
    print("Generated: mock_data_ohlcv_hourly.csv")

    # Format 4: Price Index Only (Index, Price)
    price_index = np.random.uniform(100, 200, size=30)
    df_price_index = pd.DataFrame({"index": range(1, 31), "price": price_index})
    df_price_index.to_csv(f"{MOCK_DATA_DIR}/mock_data_price_index.csv", index=False)
    print("Generated: mock_data_price_index.csv")

if __name__ == "__main__":
    save_mock_data()
