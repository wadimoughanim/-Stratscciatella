cmake_minimum_required(VERSION 3.10)
project(Stratscciatella)

set(CMAKE_CXX_STANDARD 17)

# Set runtime library to MDd for Debug and MD for Release
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MD")

# Add Google Test as a subdirectory
add_subdirectory(third_party/googletest)

# Include Google Test headers and your project headers
include_directories(third_party/googletest/googletest/include)
include_directories(include)

# Configure GoogleTest to use /MDd and /MD
target_compile_options(gtest PRIVATE "$<$<CONFIG:Debug>:/MDd>" "$<$<CONFIG:Release>:/MD>")
target_compile_options(gtest_main PRIVATE "$<$<CONFIG:Debug>:/MDd>" "$<$<CONFIG:Release>:/MD>")

# Add your executable
add_executable(test_csv_data_handler 
    src/csv_data_handler.cpp
    tests/cpp/test_csv_data_handler.cpp
)

# Link Google Test libraries to your executable
target_link_libraries(test_csv_data_handler gtest gtest_main)
