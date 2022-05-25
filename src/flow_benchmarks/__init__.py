"""
flow-benchmarks
--------
Benchmarking normalising flows using PyTorch Lightning.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass
