from gi.repository import Adw
from gi.repository import Gtk

#

import requests

@Gtk.Template(resource_path='/esp_viewer/yackcheck/io/ui/connect_dialog.ui')
class ConnectDialog(Adw.Dialog):
    __gtype_name__ = 'connect_dialog'

    connect_button: Gtk.Button = Gtk.Template.Child()
    ip_address_entry: Adw.EntryRow = Gtk.Template.Child()
    port_entry: Adw.EntryRow = Gtk.Template.Child()

    # stack: Adw.ViewStack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect_button.connect("clicked", self.on_button_clicked)

    def on_button_clicked(self, widget):
        input_ip_address = self.ip_address_entry.get_text()
        input_port = self.port_entry.get_text()

        if( input_ip_address != "" ):
            if( input_port != "" ):
                self.establish_connection(input_ip_address, input_port)
            else:
                self.establish_connection(input_ip_address)
        else:
            self.establish_connection()

        self.close()

    def establish_connection(self, ip_addr="192.168.4.1", port="80"):

        self.id_addr = ip_addr
        self.port = port

        url = "http://" + ip_addr + ":" + port
        print("ip: " + ip_addr)
        print("port: " + port)

        def check_webpage(url):
            try:
                response = requests.get(url, timeout=1.5)
                # Check if the status code is in the 200 range
                if response.status_code // 100 == 2:
                    return True, f"The webpage {url} is alive."
                else:
                    return False, f"The webpage {url} returned status code: {response.status_code}"
            except requests.exceptions.RequestException as e:
                return False, f"An error occurred: {e}"

        is_alive, message = check_webpage(url)
        print(message)

    @classmethod
    def post_digital_pin_state(cls, pin_id, pin_state ):
        payload = {
           "pin_id": pin_id,
           "state": pin_state
        }

        url = "http://" + cls.ip_addr + ":" + cls.port

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print("POST request successful")
            print("Response:", response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST request: {e}")

