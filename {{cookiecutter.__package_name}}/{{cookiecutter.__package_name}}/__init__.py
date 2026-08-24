# see license/LICENSE.rst
import os
from pathlib import Path

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

import swxsoc
from swxsoc import print_config  # noqa: E402

# Force the mission environment variable and reconfigure regardless of import order
os.environ["SWXSOC_MISSION"] = "{{ cookiecutter.mission_name }}"
swxsoc.reconfigure()

# Load user configuration
config = swxsoc.config

log = swxsoc.log

# Then you can be explicit to control what ends up in the namespace,
__all__ = ["config", "print_config"]

_package_directory = Path(__file__).parent
_data_directory = _package_directory / "data"
_test_files_directory = _package_directory / "data" / "test"

log.debug(
    f"{{  cookiecutter.__package_name }} version: {__version__}"
)

MISSION_NAME = "{{ cookiecutter.mission_name }}"
INSTRUMENT_NAME = "{{cookiecutter.instr_name}}"
