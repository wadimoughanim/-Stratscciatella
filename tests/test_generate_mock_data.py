import unittest
import os
import pandas as pd
from utils import generate_mock_data

class TestGenerateMockData(unittest.TestCase):
    def setUp(self):
        # Path to mock data
        self.mock_data_dir = "mock_data"
        
        # Ensure the mock data directory is empty before
        if os.path.exists(self.mock_data_dir):
            for filename in os.listdir(self.mock_data_dir):
                file_path = os.path.join(self.mock_data_dir, filename)
                os.remove(file_path)

    def test_generate_mock_data_files(self):
        generate_mock_data.save_mock_data()
        expected_files = [
            "mock_data_ohlcv_daily.csv",
            "mock_data_high_only_daily.csv",
            "mock_data_ohlcv_hourly.csv",
            "mock_data_price_index.csv"
        ]
        
        # Check if files exist
        for file in expected_files:
            file_path = os.path.join(self.mock_data_dir, file)
            self.assertTrue(os.path.exists(file_path), f"File {file} does not exist")

    def test_file_structure(self):
        # Run data generation to ensure files exist
        generate_mock_data.save_mock_data()

        # Test the structure of each generated file
        daily_df = pd.read_csv(os.path.join(self.mock_data_dir, "mock_data_ohlcv_daily.csv"))
        high_only_df = pd.read_csv(os.path.join(self.mock_data_dir, "mock_data_high_only_daily.csv"))
        hourly_df = pd.read_csv(os.path.join(self.mock_data_dir, "mock_data_ohlcv_hourly.csv"))
        price_index_df = pd.read_csv(os.path.join(self.mock_data_dir, "mock_data_price_index.csv"))

        # Check columns for daily OHLCV data
        self.assertListEqual(list(daily_df.columns), ["date", "open", "high", "low", "close", "volume"])

        # Check columns for high-only daily data
        self.assertListEqual(list(high_only_df.columns), ["date", "high"])

        # Check columns for hourly OHLCV data
        self.assertListEqual(list(hourly_df.columns), ["date", "open", "high", "low", "close", "volume"])

        # Check columns for price index data
        self.assertListEqual(list(price_index_df.columns), ["index", "price"])

    def tearDown(self):
        # Clean up generated files after tests
        for filename in os.listdir(self.mock_data_dir):
            file_path = os.path.join(self.mock_data_dir, filename)
            os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
