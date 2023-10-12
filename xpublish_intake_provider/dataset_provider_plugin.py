"""Intake Xpublish dataset provider.

Loads datasets from a single intake catalog
via the regular `deps.dataset` interface.
"""
from pathlib import Path
from typing import Union

import intake
from pydantic import Field
from xpublish import Plugin, hookimpl


class IntakeDatasetProviderPlugin(Plugin):
    """Intake Xpublish dataset provider.

    Loads datasets from a single intake catalog
    via the regular `deps.dataset` interface.

    It does not handle nested catalogs, and probably
    gets confused if Pandas dataframes are mixed in.
    """

    name: str = "intake-dataset-provider"

    uri: Union[str, Path] = Field(description="URI of catalog to load")
    _catalog: intake.Catalog

    def __init__(self, **data):
        """Open intake catalog."""
        super().__init__(**data)
        self._catalog = intake.open_catalog(self.uri)

    @hookimpl
    def get_datasets(self):
        """List the datasets available in the Intake catalog."""
        return list(self._catalog)

    @hookimpl
    def get_dataset(self, dataset_id: str):
        """Return Xarray Dataset in Intake catalog for given dataset_id.

        If it's not found, None is returned.
        """
        try:
            return self._catalog[dataset_id].to_dask()
        except KeyError:
            return None
