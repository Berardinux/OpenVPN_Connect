import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class UIComponents:
    def __init__(self):
        self.header_box = None
        self.header_label = None
        self.main_box = None
        self.win = None

    def create_header_box(self):
        self.header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.header_box.set_size_request(500, 55)
        self.header_box.set_name("custom-header")
    
        # Centered container
        self.center_container = Gtk.Box()
        self.center_container.set_halign(Gtk.Align.CENTER)
        self.center_container.set_hexpand(True)
        self.header_box.pack_start(self.center_container, False, False, 0)
    
    def create_hamburger(self, callback):
        self.hamburger_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.hamburger_box.set_size_request(500, 55)

        # Hamburger
        self.hamburger_container = Gtk.Box()
        self.hamburger_box.pack_start(self.hamburger_container, False, False, 0)

        icon = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.BUTTON)
        icon.set_pixel_size(32)
        hamburger_button = Gtk.Button()
        hamburger_button.set_image(icon)
        hamburger_button.set_relief(Gtk.ReliefStyle.NONE)
        hamburger_button.get_style_context().add_class("hamburger-btn")
        hamburger_button.connect("clicked", callback)
        self.hamburger_container.pack_start(hamburger_button, False, False, 0)

    def create_header_label(self, text):
        self.header_label = Gtk.Label(label=text)
        self.header_label.set_halign(Gtk.Align.CENTER)
        self.header_label.get_style_context().add_class("header-title")
        self.center_container.pack_start(self.header_label, True, True, 0)

    def create_window(self):
        self.win = Gtk.Window()
        self.win.set_title("OpenVPN Connect")
        self.win.set_default_size(500, 800)
        self.win.set_resizable(False)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.main_box.pack_start(self.hamburger_box, False, False, 0)
        self.main_box.pack_start(self.header_box, False, False, 0)
        self.win.add(self.main_box)

