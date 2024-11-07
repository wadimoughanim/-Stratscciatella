#ifndef CSV_DATA_HANDLER_H
#define CSV_DATA_HANDLER_H

#include "data_handler.h"
#include <string>
#include <map>
#include <vector>

class CSVDataHandler : public DataHandler {
public:
    CSVDataHandler() = default;
    ~CSVDataHandler() override = default;
    bool load_data(const std::string& source) override;
    double get_data(const std::string& date, const std::string& column) const override;

private:
    std::map<std::string, std::map<std::string, double>> data_;
    std::vector<std::string> parse_header(const std::string& header_line);
};

#endif
