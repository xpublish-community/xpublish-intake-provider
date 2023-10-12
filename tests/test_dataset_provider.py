import pytest
import xpublish
from fastapi.testclient import TestClient

from xpublish_intake_provider import IntakeDatasetProviderPlugin


@pytest.fixture
def plugin():
    return IntakeDatasetProviderPlugin(
        name="gfs-dataset",
        uri="https://raw.githubusercontent.com/axiom-data-science/mc-goods/f61ba8e4cc3ac69b3a9c143d8ea43891f350d8bf/mc_goods/gfs-1-4deg.yaml",
    )


@pytest.fixture
def intake_xpublish(plugin: IntakeDatasetProviderPlugin):
    return xpublish.Rest({}, plugins={"gfs-dataset": plugin})


@pytest.fixture
def test_client(intake_xpublish: xpublish.Rest):
    app = intake_xpublish.app
    return TestClient(app)


def test_datasets(plugin: IntakeDatasetProviderPlugin):
    datasets = plugin.get_datasets()

    assert "ucar-forecast-agg" in datasets, "Plugin cannot list datasets"


# def test_dataset(plugin: IntakeDatasetProviderPlugin):
#     ds = plugin.get_dataset("ucar-forecast-agg")

#     assert isinstance(ds, xr.Dataset), "Plugin can return the dataset"


def test_datasets_endpoint(test_client: TestClient):
    response = test_client.get("/datasets")

    assert response.status_code == 200, "Response did not return successfully"

    content = response.json()

    assert "ucar-forecast-agg" in content, "Plugin isn't providing datasets to Xpublish"
