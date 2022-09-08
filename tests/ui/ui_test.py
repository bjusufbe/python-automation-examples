import pytest
from lib.pages.navigation import Navigation

@pytest.mark.usefixtures("setup")
class TestExample:
    @pytest.mark.ui_set
    def test_ui_example(self):
        navigation = Navigation(self.driver)
        navigation.click(navigation.HOME)
        navigation.click(navigation.SERVICES["general"])
