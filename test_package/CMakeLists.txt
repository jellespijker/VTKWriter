cmake_minimum_required(VERSION 3.21)
project(VTKWriterTestPackage CXX)

find_package(vtkwriter REQUIRED)

add_executable(test main.cpp)
target_link_libraries(test PRIVATE vtkwriter::vtkwriter)