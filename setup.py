#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Define the name for your package, this will be used when calling `loadPlugin`.
# Note, for packages containing only a single module defining objects to export,
# you should name it something based off this name of the project to avoid
# import collisions with other packages.
name = "psychopy-glfw"

# Version for the package. Use setuptools conventions for specifying the version
# string.
version = "0.1"

# Define packages to be included with this plugin.
packages = [
    'psychopy_glfw'
]

# Define package directories.
package_dir = {
    'psychopy_glfw': 'psychopy_glfw'
}

# Define package data. This is required for including icons or any other
# non-Python resource (e.g. documentation, images, videos, etc.) needed by the
# plugin.
package_data = {
   "": ["*.txt", "*.md"]
}

# Define entry points. PsychoPy's plugin framework scans packages and looks for
# entry points advertised in the package metadata which pertains to PsychoPy.
# Entry points are a dictionary, where keys are fully qualified names to
# modules and unbound classes which you want to add/modify attributes. Values
# can be single strings, or lists of strings specifying what attributes of those
# PsychoPy objects are to reference objects defined in the plugin module.
entry_points = {
    'psychopy.visual.backends': [
        'GLFWBackend = psychopy_glfw:GLFWBackend']
}

# Run the setup function.
setup(
    name=name,  # set the name
    version=version,  # put your plugin version here
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    author="Matthew D. Cutone",
    author_email="mcutone@opensciencetools.org",
    description="GLFW window backend plugin for PsychoPy.",
    url="https://github.com/mdcutone/psychopy-glfw",
    classifiers=[
        "License :: OSI Approved :: GPL3",
        'Programming Language :: Python :: 3'],
    keywords="psychopy visual window backend screen display",
    zip_safe=False,
    entry_points=entry_points  # set our entry points in the package metadata
)
