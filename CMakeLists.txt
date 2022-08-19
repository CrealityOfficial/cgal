cmake_minimum_required (VERSION 3.1)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/")
include(ConfigureAllModules)    

project(CGAL)

include(CGAL)
__build_info_header()
__find_boost_root()
__cc_find(tbb)

include_directories(${boost_INCLUDE_DIR})
set(CGAL_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/include)

add_definitions(-DCGAL_NO_GMP=1)
add_definitions(-DCGAL_NO_MPFR=1)
add_definitions( -DNOMINMAX -DCGAL_LINKED_WITH_TBB )

find_package(OpenMP)
__cgal_include_common_packages()

add_subdirectory(src)
