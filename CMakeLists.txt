cmake_minimum_required(VERSION 3.21)
project(VTKWriter CXX)

include(cmake/StandardProjectSettings.cmake)

# Link this 'library' to set the c++ standard / compile-time options requested
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_20)

# Link this 'library' to use the warnings specified in CompilerWarnings.cmake
add_library(project_warnings INTERFACE)
include(cmake/CompilerWarnings.cmake)
set_project_warnings(project_warnings)

find_package(spdlog REQUIRED)
find_package(fmt REQUIRED)

option(ENABLE_TESTING "Build with unit test" ON)
if(ENABLE_TESTING)
    enable_testing()
    message("Building Tests")
    add_subdirectory(tests)
endif()

option(ENABLE_BENCHMARKS "Build with benchmarks" ON)
if (ENABLE_BENCHMARKS)
    message("Building Benchmarks")
    add_subdirectory(benchmarks)
endif()

set(SCR
        scr/VTKWriter.cpp)

set(HDR
        include/VTKWriter/VTKWriter.h)

add_library(VTKWriter ${SCR} ${HDR})

target_link_libraries(VTKWriter
        PRIVATE
            project_options
            project_warnings
            spdlog
            fmt
        )

target_include_directories(VTKWriter
        PUBLIC
            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
            $<INSTALL_INTERFACE:include>
        PRIVATE
            src)