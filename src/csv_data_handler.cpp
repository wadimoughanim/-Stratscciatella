#include "csv_data_handler.h"
#include <fstream>
#include <sstream>
#include <stdexcept>

bool CSVDataHandler::load_data(const std::string& source) {
    std::ifstream file(source);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + source);
        return false;
    }

    std::string line;
    if (!std::getline(file, line)) {
        throw std::runtime_error("CSV file is empty or header missing");
        return false;
    }

    // Parse the header to get column names
    std::vector<std::string> columns = parse_header(line);

    // Ensure date is not included in columns to be parsed as double
    if (!columns.empty() && columns[0] == "date") {
        columns.erase(columns.begin()); // Remove "date" from columns
    } else {
        throw std::runtime_error("Expected 'date' column in header");
    }

    // Read each row and store the data
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string date;
        std::getline(ss, date, ','); // Read first token as date

        std::map<std::string, double> row_data;
        for (const auto& column : columns) {
            std::string value;
            std::getline(ss, value, ',');

            try {
                row_data[column] = std::stod(value); // Convert string to double
            } catch (const std::invalid_argument& e) {
                throw std::runtime_error("Invalid value for double conversion in column '" + column + "': " + value);
            }
        }
        data_[date] = row_data;
    }

    file.close();
    return true;
}

double CSVDataHandler::get_data(const std::string& date, const std::string& column) const {
    auto date_it = data_.find(date);
    if (date_it == data_.end()) {
        throw std::runtime_error("Date not found: " + date);
    }

    const auto& row_data = date_it->second;
    auto column_it = row_data.find(column);
    if (column_it == row_data.end()) {
        throw std::runtime_error("Column not found: " + column);
    }

    return column_it->second;
}

std::vector<std::string> CSVDataHandler::parse_header(const std::string& header_line) {
    std::vector<std::string> columns;
    std::stringstream ss(header_line);
    std::string column;

    while (std::getline(ss, column, ',')) {
        columns.push_back(column);
    }
    return columns;
}
