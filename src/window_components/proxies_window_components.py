import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf
from read_write_json import ReadWriteJSON

class ProxiesWindowUIComponents:
    def __init__(self):
        self.header_box = None
        self.header_label = None
        self.body_box = None
        self.config=ReadWriteJSON().read_config()
        self.theme = self.config.get("theme", "light")

    def create_proxies_header_box(self, callback):
        self.header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.header_box.set_size_request(500, 55)
        self.header_box.set_name("custom-header")
      
        # Back button
        path = "../images/" + self.theme + "/ovpn_arrow.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                path, 32, 32,
                preserve_aspect_ratio=True
                )
        view_icon = Gtk.Image.new_from_pixbuf(pixbuf)
        back_button = Gtk.Button()
        back_button.set_image(view_icon)
        back_button.set_relief(Gtk.ReliefStyle.NONE)
        back_button.get_style_context().add_class("back-btn")
        back_button.connect("clicked", callback)
        self.header_box.pack_start(back_button, False, False, 0)

        # Header label
        self.header_label = Gtk.Label("Proxies")
        self.header_label.set_halign(Gtk.Align.CENTER)
        self.header_label.get_style_context().add_class("Proxies")
        self.header_box.pack_start(self.header_label, True, True, 0)

        # Spacer
        spacer = Gtk.Box()
        spacer.set_size_request(80, -1)
        self.header_box.pack_start(spacer, False, False, 0)

        return self.header_box

    def create_proxies_body_box(self):
        self.body_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.body_box.set_name("custom-body")
        
        # You have no proxies added yet body box
        self.body_box.set_valign(Gtk.Align.CENTER)
        self.body_box.set_halign(Gtk.Align.CENTER)
        path = "../images/" + self.theme + "/ovpn_proxies.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                path, 200, 200,
                preserve_aspect_ratio=True
                )
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        label = Gtk.Label(label="You have no proxies added yet")
        label.set_margin_top(30)
        label.set_justify(Gtk.Justification.CENTER)
        label.get_style_context().add_class("label")
        label.get_style_context().add_class("color0")

        self.body_box.pack_start(image, False, False, 0)
        self.body_box.pack_start(label, False, False, 0)


        return self.body_box

    def create_proxies_footer_box(self, callback):
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
        add_proxy_button = Gtk.Button()
        add_proxy_button.set_image(view_icon)
        add_proxy_button.set_relief(Gtk.ReliefStyle.NONE)
        add_proxy_button.get_style_context().add_class("add_proxy_btn")
        add_proxy_button.connect("clicked", callback)
        self.footer_box.pack_start(add_proxy_button, False, False, 0)

        return self.footer_box
