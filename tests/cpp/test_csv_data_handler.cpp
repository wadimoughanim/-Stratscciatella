#include "csv_data_handler.h"
#include <gtest/gtest.h>

TEST(CSVDataHandlerTest, LoadData) {
    CSVDataHandler handler;
    EXPECT_TRUE(handler.load_data("mock_data/mock_data_ohlcv_daily.csv"));  // Adjust path as needed
}

TEST(CSVDataHandlerTest, GetData) {
    CSVDataHandler handler;
    handler.load_data("mock_data/mock_data_ohlcv_daily.csv");  // Adjust path as needed

    // Example check: Assuming we know specific values in mock data
    EXPECT_DOUBLE_EQ(handler.get_data("2023-01-01", "close"), 104.0);
    EXPECT_DOUBLE_EQ(handler.get_data("2023-01-02", "high"), 106.0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
