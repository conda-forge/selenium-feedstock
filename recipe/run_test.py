"""Verify hacks maintain upstream packaging intent."""
import unittest
from pathlib import Path


class Smoketest(unittest.TestCase):
    def test_manager_binary(self):
        """The `selenium-manager` binary should be found."""
        from selenium.webdriver.common.selenium_manager import SeleniumManager

        assert SeleniumManager._get_binary().exists(), "no manager binary"

    def test_remote_js(self):
        """MANIFEST.in/pyproject.toml/setup.py should create JS assets."""
        from selenium.webdriver.remote import webelement

        webelement._load_js()

    def test_ff_json(self):
        """MANIFEST.in/pyproject.toml/setup.py should create JSON assets."""
        from selenium.webdriver.firefox import firefox_profile

        ff_json = Path(firefox_profile.__file__).parent / firefox_profile.WEBDRIVER_PREFERENCES
        assert ff_json.exists(), "no firefox JSON found"

    def test_remote_cdp(self):
        """CDP should import."""
        from selenium.webdriver.remote import webdriver

        webdriver.import_cdp()

    def test_bidi_devtools(self):
        """Some versions of the devtools should be found/importable."""
        from selenium.webdriver.common import devtools

        vs = sorted(Path(devtools.__file__).parent.glob("v*/"))
        assert vs, "no versioned devtools found"
        from selenium.webdriver.common.bidi import cdp

        for v in vs:
            cdp.import_devtools(v.name[1:])


if __name__ == "__main__":
    unittest.main(verbosity=2)
