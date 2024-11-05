#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

// We expose to python the log function that call the python logger
void log(const std::string& level, const std::string& message) {
    py::module logger = py::module::import("utils.logger");
    logger.attr("log")(level, message);
}

// Define the Python module and add bindings
PYBIND11_MODULE(Stratscciatella, m) {
    m.def("log", &log, "Log a message with the specified level");
}
