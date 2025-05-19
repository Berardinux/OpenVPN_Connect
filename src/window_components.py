import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class WindowUIComponents:
    def __init__(self):
        self.main_box = None
        self.win = None

    def create_window(self, header_box, body_box, footer_box):
        self.win = Gtk.Window()
        self.win.set_title("OpenVPN Connect")
        self.win.set_default_size(500, 800)
        self.win.set_resizable(False)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.main_box.pack_start(header_box, False, False, 0)
        self.main_box.pack_start(body_box, True, True, 0)
        self.main_box.pack_start(footer_box, False, False, 0)
        self.win.add(self.main_box)
