#ifndef DATA_HANDLER_H
#define DATA_HANDLER_H

#include <iostream>

class DataHandler {
public:
// virtual because must be inherited
    virtual ~DataHandler() = default;
    virtual bool load_data(const std::string& source) = 0;
    virtual double get_data(const std::string& date, const std::string& column) const = 0;
};
#endif
