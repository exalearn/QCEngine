"""
A set of scripts to setup testing
"""

import pytest
import os


def _plugin_import(plug):
    """
    Tests to see if a module is available
    """
    import sys
    if sys.version_info >= (3, 4):
        from importlib import util
        plug_spec = util.find_spec(plug)
    else:
        import pkgutil
        plug_spec = pkgutil.find_loader(plug)
    if plug_spec is None:
        return False
    else:
        return True


# Modify paths for testing
os.environ["DQM_CONFIG_PATH"] = os.path.dirname(os.path.abspath(__file__))
os.environ["TMPDIR"] = "/tmp/"

# Add flags
using_psi4 = pytest.mark.skipif(
    _plugin_import("psi4") is False, reason="could not find psi4. please install the package to enable tests")
using_rdkit = pytest.mark.skipif(
    _plugin_import("rdkit") is False, reason="could not find rdkit. please install the package to enable tests")

test_mols = {
    "water": {
        "geometry": [
            0.0, 0.0, -0.1294769411935893, 0.0, -1.494187339479985, 1.0274465079245698, 0.0, 1.494187339479985,
            1.0274465079245698
        ],
        "symbols": ["O", "H", "H"]
    }
}
