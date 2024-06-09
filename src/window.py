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
from .stackgenerator import StackGenerator
from .configparser import ConfigParser

import toml
import os
import requests
# import cv2

@Gtk.Template(resource_path='/esp_viewer/yackcheck/io/ui/window.ui')
class EspViewerWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'EspViewerWindow'

    connection_button: Gtk.Button = Gtk.Template.Child()
    view_switcher: Adw.ViewSwitcher = Gtk.Template.Child()
    disconnected_stack: Adw.ViewStack = Gtk.Template.Child()
    controls_page: Adw.PreferencesPage = Gtk.Template.Child()
    camera_page: Gtk.ScrolledWindow = Gtk.Template.Child()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.connection_button.connect("clicked", self.show_connect_dialog)

    def show_connect_dialog(self, button):
        self.switch_stack()

        self.generate_camera_content()

        self.connection_dialog = ConnectDialog()
        self.connection_dialog.present(self)

    def connection_established_callback(self):
        # ns = generate_stack()
        pass

    def switch_stack(self):
        new_stack = Adw.ViewStack()

        pref = Adw.StatusPage()
        pref.set_title("Controls")
        pref.set_icon_name("open-menu-symbolic")
        self.generate_controls_content()

        pass

    def pin_change_callback(self, switch: Adw.SwitchRow, arg2):
        pin_state = "false" if switch.props.active == 0 else "true"
        pin_id =  switch.props.title

        print(f"PS: {pin_state} PI {pin_id}")
        self.connection_dialog.post_digital_pin_state(pin_id, pin_state)

        pass

    def generate_controls_content(self):
        pg = Adw.PreferencesGroup()
        pg.set_title("Digital I/O")

        digital_pins = ConfigParser.read_config_pins()
        print(digital_pins)

        for pin_id, pin_description in digital_pins.items():
            pin_entry = PinEntryFactory.create_pin_entry(pin_id, pin_description, self.pin_change_callback)
            pg.add(pin_entry)

            self.controls_page.add(pg)

    def generate_camera_content(self):

        print("getting image")
        url = "http://192.168.4.1:81/stream"

        capture_path = os.environ.get('XDG_CONFIG_HOME') + "/capture.jpg"

        def get_image(image_url):
            response = requests.get(image_url)


            if response.status_code == 200:

                with open(capture_path, 'wb') as file:
                    file.write(response.content)
                print("Image successfully saved!")
            else:
                print(f"Failed to retrieve the image. Status code: {response.status_code}")

        def get_stream(stream_url):
            cap = cv2.VideoCapture(stream_url)

            if not cap.isOpened():
                print("Error: Could not open video stream.")
            else:
                ret, frame = cap.read()

                if ret:

                    filename = capture_path
                    cv2.imwrite(filename, frame)
                    print(f"Frame saved as {filename}")
                    cv2.waitKey(0)
                else:
                    print("Error: Can't receive frame (stream end?).")

                cap.release()


        # get_stream(url)
        def detection_image_frame(  ):
            button_wraper = Gtk.Button()

            d_frame = Gtk.Frame()
            d_frame.set_valign(Gtk.Align.FILL)

            d_frame.set_margin_start(10)
            d_frame.set_margin_end(10)
            d_frame.set_margin_top(10)
            d_frame.set_margin_bottom(10)

            content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            v_clamp = Adw.Clamp()
            v_clamp.set_maximum_size(300)
            v_clamp.set_child(content)


            label = Gtk.Label()
            label.set_label(f"ESP-CAM")
            label.set_margin_top(10)
            label.set_justify(Gtk.Justification.CENTER)

            pic = Gtk.Image()
            pic.set_from_file("capture.jpg")
            pic.set_pixel_size(256)
            # button_wraper.connect("clicked", self.open_image_viewer, "./images/icon.png")
            # image_path = "./cache/images/" + image_data['filename']
            # button_wraper.connect("clicked", lambda button, path=image_path: self.open_image_viewer(path))

            content.append(pic)
            content.append(label)
            button_wraper.set_child(v_clamp)
            d_frame.set_child(button_wraper)

            h_clamp = Adw.Clamp()
            h_clamp.set_maximum_size(350)
            h_clamp.set_child(d_frame)

            return d_frame


        self.camera_page.set_child(detection_image_frame())

class PinEntryFactory:
    @staticmethod
    def create_pin_entry(pin_id, pin_description, callback):
        pin_entry = Adw.SwitchRow()
        pin_entry.set_title(pin_description)
        pin_entry.set_subtitle(pin_id)
        pin_entry.connect('notify::active', callback)
        return pin_entry
