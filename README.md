## Xpublish-Intake-Provider

Xpublish-Intake-Provider allows serving datasets with Xpublish specified by Intake catalogs.

### Installation

For `conda` users you can

```shell
conda install --channel conda-forge xpublish_intake_provider
```

or, if you are a `pip` users

```shell
pip install xpublish_intake_provider
```

### Example

Currently this package includes one plugin which can load an
Intake catalog and serve it's datasets via `/datasets/{dataset_id}`.

You can register the plugin multiple times in order to serve
multiple catalogs as long as each gets its own name.

```python
from xpublish_intake_provider import IntakeDatasetProviderPlugin

rest = xpublish.Rest({})

rest.register_plugin(
    IntakeDatasetProviderPlugin(
        name="gfs-datasets",
        uri="https://raw.githubusercontent.com/axiom-data-science/mc-goods/main/mc_goods/gfs-1-4deg.yaml"
    )
)
rest.register_plugin(
    IntakeDatasetProviderPlugin(
        name="gomofs-datasets",
        uri="https://raw.githubusercontent.com/axiom-data-science/mc-goods/main/mc_goods/gomofs.yaml"
    )
)
```

## Get in touch

Report bugs, suggest features or view the source code on [GitHub](https://github.com/ioos/xpublish_intake_provider/issues).


## License and copyright

xpublish_intake_provider is licensed under BSD 3-Clause "New" or "Revised" License (BSD-3-Clause).

Development occurs on GitHub at <https://github.com/ioos/xpublish_intake_provider>.
