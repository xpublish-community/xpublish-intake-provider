"""Xpublish-Intake-Provider loads datasets from Intake catalogs."""

from xpublish_intake_provider.dataset_provider_plugin import IntakeDatasetProviderPlugin

__all__ = [
    "IntakeDatasetProviderPlugin",
]

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"
