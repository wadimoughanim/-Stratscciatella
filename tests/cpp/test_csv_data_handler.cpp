#include "csv_data_handler.h"
#include <gtest/gtest.h>
#include <fstream>   // For file I/O
#include <string>
#include <filesystem> // For directory creation
#include <cstdio>     // For std::remove

// Function to create mock data for testing
void create_mock_data(const std::string& file_path) {
    // Ensure the directory exists
    std::filesystem::create_directories("mock_data");

    std::ofstream file(file_path);
    if (!file.is_open()) {
        throw std::runtime_error("Could not create mock data file.");
    }

    // Write header
    file << "date,open,high,low,close,volume\n";
    // Write data
    file << "2023-01-01,100.0,105.0,99.0,104.0,1000\n";
    file << "2023-01-02,105.0,106.0,103.0,105.0,1500\n";
    file << "2023-01-03,107.0,110.0,106.0,109.0,2000\n";

    file.close();
}

TEST(CSVDataHandlerTest, LoadData) {
    const std::string file_path = "mock_data/mock_data_ohlcv_daily.csv";
    create_mock_data(file_path);

    CSVDataHandler handler;
    EXPECT_TRUE(handler.load_data(file_path));

    std::remove(file_path.c_str());  // Remove the file after the test
}

TEST(CSVDataHandlerTest, GetData) {
    const std::string file_path = "mock_data/mock_data_ohlcv_daily.csv";
    create_mock_data(file_path);

    CSVDataHandler handler;
    handler.load_data(file_path);

    EXPECT_DOUBLE_EQ(handler.get_data("2023-01-01", "close"), 104.0);
    EXPECT_DOUBLE_EQ(handler.get_data("2023-01-02", "high"), 106.0);

    std::remove(file_path.c_str());  // Remove the file after the test
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
