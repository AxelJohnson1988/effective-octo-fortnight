"""
Warden Toolkit - Production-Ready Google Colab Framework
Part of the effective-octo-fortnight repository

A modular toolkit for secure, high-performance data workflows in Google Colab.
Provides GPU acceleration, secrets management, and file integrity verification.

Version: 1.0.0
License: MIT
"""

from .m_accelerator import check_resources, enable_cudf_acceleration
from .m_sentry import get_secret, verify_vault
from .m_io_guardian import verify_file_integrity, scaffold_directory

__version__ = "1.0.0"
__all__ = [
    "check_resources",
    "enable_cudf_acceleration",
    "get_secret",
    "verify_vault",
    "verify_file_integrity",
    "scaffold_directory",
]
