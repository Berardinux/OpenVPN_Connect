import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf
from read_write_json import ReadWriteJSON

class SettingsWindowUIComponents:
    def __init__(self):
        self.header_box = None
        self.header_label = None
        self.body_box = None
        self.footer_box = None
        self.config=ReadWriteJSON().read_config()
        self.theme = self.config.get("theme", "light")

    def create_settings_header_box(self, callback):
        self.header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.header_box.set_size_request(500, 55)
        self.header_box.set_name("custom-header")
       
        # Hamburger button
        icon = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.BUTTON)
        icon.set_pixel_size(32)
        hamburger_button = Gtk.Button()
        hamburger_button.set_image(icon)
        hamburger_button.set_relief(Gtk.ReliefStyle.NONE)
        hamburger_button.get_style_context().add_class("hamburger-btn")
        hamburger_button.connect("clicked", callback)
        self.header_box.pack_start(hamburger_button, False, False, 0)

        # Header label
        self.header_label = Gtk.Label("Profiles")
        self.header_label.set_halign(Gtk.Align.CENTER)
        self.header_label.get_style_context().add_class("Profiles")
        self.header_box.pack_start(self.header_label, True, True, 0)

        # Scroll button
        path = "../images/" + self.theme + "/ovpn_scroll.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                path , 32, 32,
                preserve_aspect_ratio=True
                )
        view_icon = Gtk.Image.new_from_pixbuf(pixbuf)
        list_button = Gtk.Button()
        list_button.set_image(view_icon)
        list_button.set_relief(Gtk.ReliefStyle.NONE)
        list_button.get_style_context().add_class("list-btn")
        list_button.connect("clicked", callback)
        self.header_box.pack_start(list_button, False, False, 0)

        return self.header_box

    def create_settings_body_box(self):
        self.body_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.body_box.set_name("custom-body")
        return self.body_box

    def create_settings_footer_box(self, callback):
        self.footer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.footer_box.set_size_request(500, 100)
        self.footer_box.set_name("custom-footer")

        self.footer_box.pack_start(Gtk.Box(), True, True, 0)

        # Import profile button
        path = "../images/" + self.theme + "/ovpn_plus.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                path, 60, 60,
                preserve_aspect_ratio=True
                )
        view_icon = Gtk.Image.new_from_pixbuf(pixbuf)
        import_profile_button = Gtk.Button()
        import_profile_button.set_image(view_icon)
        import_profile_button.set_relief(Gtk.ReliefStyle.NONE)
        import_profile_button.get_style_context().add_class("import_profile_btn")
        import_profile_button.connect("clicked", callback)
        self.footer_box.pack_start(import_profile_button, False, False, 0)

        return self.footer_box
