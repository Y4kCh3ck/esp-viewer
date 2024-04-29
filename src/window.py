# window.py
#
# Copyright 2024 yakcheck
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

from .connect import ConnectDialog

@Gtk.Template(resource_path='/esp_viewer/yackcheck/io/ui/window.ui')
class EspViewerWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'EspViewerWindow'

    connection_button = Gtk.Template.Child()


    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.connection_button.connect("clicked", self.show_connect_dialog)

    def show_connect_dialog(self, button):
        connection_dialog = ConnectDialog()
        connection_dialog.present(self)
