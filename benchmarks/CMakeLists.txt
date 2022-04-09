# Copyright (c) 2022 Jelle Spijker
# VTKWriter is released under the terms of the AGPLv3 or higher

find_package(benchmark REQUIRED)

add_executable(benchmarks main.cpp)
target_link_libraries(benchmarks PRIVATE project_warnings project_options VTKWriter benchmark::benchmark)