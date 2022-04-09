# Copyright (c) 2022 Jelle Spijker
# VTKWriter is released under the terms of the AGPLv3 or higher

cmake_minimum_required(VERSION 3.21)
project(VTKWriterTestPackage CXX)

find_package(vtkwriter REQUIRED)

add_executable(test main.cpp)
target_link_libraries(test PRIVATE vtkwriter::vtkwriter)