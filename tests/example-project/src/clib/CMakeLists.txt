
cmake_minimum_required(VERSION 2.8)

project (cython_example_clib)
add_library(sqrc SHARED sqrc.c)
add_library(sqrcpp SHARED sqrcpp.cpp)
