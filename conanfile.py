from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.layout import cmake_layout

class VTKWriterConan(ConanFile):
    name = "vtkwriter"
    version = "0.1.0"
    description = "A minimal VTK file writer"
    topics = ("conan", "vtk")
    license = "MIT"
    homepage = "https://github.com/jellespijker/vtkwriter"
    url = "https://github.com/jellespijker/vtkwriter"
    settings = "os", "compiler", "build_type", "arch"
    exports = "LICENSE*"
    options = {
        "tests": [True, False],
        "benchmarks": [True, False],
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "tests": True,
        "benchmarks": True,
        "shared": True,
        "fPIC": False
    }
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",
        "revision": "auto"
    }

    def build_requirements(self):
        if self.options.tests:
            self.tool_requires("catch2/2.13.8")
        if self.options.benchmarks:
            self.tool_requires("benchmark/1.6.1")

    def requirements(self):
        self.requires("fmt/8.1.1")
        self.requires("spdlog/1.10.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):

        deps = CMakeDeps(self)
        deps.build_context_activated = ["benchmark", "catch2"]
        deps.build_context_build_modules = ["benchmark", "catch2"]
        deps.generate()

        tc = CMakeToolchain(self)
        tc.variables["ENABLE_TESTS"] = self.options.tests
        tc.variables["ENABLE_BENCHMARKS"] = self.options.benchmarks
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
