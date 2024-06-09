from gi.repository import Adw
from gi.repository import Gtk

class StackGenerator():

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate(self):
        stack = Adw.ViewStack()

        pref = Adw.StatusPage()
        pref.set_title("qqdw")
        pref.set_icon_name("open-menu-symbolic")
        pref.set_visible_child_name(pref)
        stack.add_titled_with_icon(pref, None, "Test", "open-menu-symbolic")

        return stack


