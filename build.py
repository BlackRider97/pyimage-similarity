#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")

name = "pyimage_similarity"
version = "0.0.1"

summary = "Python project to find out similarity between images"
url = "https://github.com/awwsmm/PybGit"

description = """An example PyBuilder / Git project for project management
and file version control. See blog post at http://bit.ly/2QY65wO for a
more through explanation."""

authors = [Author("Rajneesh Mitharwal", "rajneeshmitharwal@gmail.com")]
license = "None"
default_task = "publish"


@init
def initialize(project):
    project.depends_on_requirements('requirements.txt')


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)  # default is True
