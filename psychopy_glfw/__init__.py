from .glfwbackend import GLFWBackend

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("package-name")
except PackageNotFoundError:
    # package is not installed
    pass
del version, PackageNotFoundError  # no longer needed and confusing for users?
