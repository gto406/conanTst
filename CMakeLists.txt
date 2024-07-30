cmake_minimum_required(VERSION 3.23)

project(bazfoo
    VERSION 0.3.0
    DESCRIPTION "Arbitrary C++ library"
    LANGUAGES CXX)

set(ATSS_SRCS
    baz/foo/example.cpp
)
set(ATSS_TEST_SRCS 
    baz/foo/bazfoo-units.test.cpp
)

find_package(nlohmann_json CONFIG REQUIRED)

add_library(${PROJECT_NAME} ${ATSS_SRCS}) 
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

# For now, repurpose example as our test-app
add_executable(${PROJECT_NAME}-test ${ATSS_SRCS})

target_include_directories(${PROJECT_NAME} 
    PRIVATE
        ${nlohmann_json_INCLUDE_DIRS}
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include>  # <prefix>/include
)

target_link_libraries(${PROJECT_NAME}-test 
    PRIVATE 
        nlohmann_json::nlohmann_json
        ${PROJECT_NAME}
)

# Install targets
install(TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}Targets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(DIRECTORY baz/foo/ DESTINATION include/baz/foo)

# Generate and install CMake configuration files
include(CMakePackageConfigHelpers)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake/${PROJECT_NAME}Config.cmake.in"
  "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
  INSTALL_DESTINATION lib/cmake/${PROJECT_NAME}
)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
  DESTINATION lib/cmake/${PROJECT_NAME}
)

install(EXPORT ${PROJECT_NAME}Targets
  FILE ${PROJECT_NAME}Targets.cmake
  DESTINATION lib/cmake/${PROJECT_NAME}
)

