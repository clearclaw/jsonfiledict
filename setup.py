from setuptools import setup, find_packages

__version__ = "unknown"

import pyver
__version__, __version_info__ = pyver.get_version (pkg = "jsondict")

setup (name = "jsondict",
  version = __version__,
  description = "A dict optionally backed by an auto-updating JSON file.",
  long_description = "A dict optionally backed by an auto-updating JSON file.",
  classifiers = [],
  keywords = "",
  author = "J C Lawrence",
  author_email = "claw@kanga.nu",
  url = "http://kanga.nu/~claw/",
  license = "GPL v3",
  packages = find_packages (exclude = ["tests",]),
  package_data = {
  },
  zip_safe = True,
  install_requires = [
    "logtool",
    "pyver",
  ],
  entry_points = {
    "console_scripts": [
      ],
    },
  )
