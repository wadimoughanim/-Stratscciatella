cmake_minimum_required(VERSION 3.14)
project(my_backtesting_platform)

set(CMAKE_CXX_STANDARD 17)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

set(SOURCES
    src/data_handler.cpp
    src/strategy.cpp
    src/moving_average_strategy.cpp
    src/python_strategy.cpp
    src/backtest_engine.cpp
    src/position_manager.cpp
)

pybind11_add_module(my_backtesting_platform ${SOURCES} python/bindings.cpp)
