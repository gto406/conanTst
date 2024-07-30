import os

from conan import ConanFile
from conan.tools.files import load, copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

#
# Package: bazfoo
# 
# Description: provides C++ blah-blah
#
class BazfooConan(ConanFile):
    name = "bazfoo"
    version = "0.3.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "CMakeLists.txt", "baz/*", "cmake/*"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["bazfoo"]

    def requirements(self):
        self.requires("nlohmann_json/3.11.3")

    # Build tool requirements listed here...
    def build_requirements(self):
        self.tool_requires("cmake/3.25.3")

