import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS

class MainGUI:
    def __init__(self):
        self.win = Gtk.Window()
        self.win.set_title("OpenVPN Connect")
        self.win.set_default_size(500, 800)
        self.win.set_resizable(False)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)

        main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        header_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
        header_box.set_size_request(500, 100)

        header_box.set_name("custom-header")
        self.header_label = Gtk.Label()
        header_box.pack_start(self.header_label, True, True, 0)
       
        main_box.pack_start(header_box,False, False, 0)
        self.win.add(main_box)

    def profiles_window(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()
        self.header_label.set_text("Profiles")
        self.win.show_all()

MainGUI().profiles_window()
Gtk.main()

