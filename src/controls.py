from gi.repository import Adw
from gi.repository import Gtk

# import toml

class ControlsPageGenerator(Adw.PreferencesPage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def generate():

        sample = Adw.SwitchRow()
        sample.set_title("test")

        pins_group = Adw.PreferencesGroup()
        pins_group.add(sample)

        result_page = Adw.PreferencesPage()
        result_page.add(pins_group)

        return result_page
