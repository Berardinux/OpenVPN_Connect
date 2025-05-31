import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf
from read_write_json import ReadWriteJSON

class ImportProfileWindowUIComponents:
    def __init__(self):
        self.header_box = None
        self.header_label = None
        self.body_box = None
        self.config=ReadWriteJSON().read_config()
        self.theme = self.config.get("theme", "light")

    def create_import_profile_header_box(self, callback):
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
        self.header_label = Gtk.Label("Import Profile")
        self.header_label.set_halign(Gtk.Align.CENTER)
        self.header_label.get_style_context().add_class("ImportProfile")
        self.header_box.pack_start(self.header_label, True, True, 0)

        # Spacer
        spacer = Gtk.Box()
        spacer.set_size_request(80, -1)
        self.header_box.pack_start(spacer, False, False, 0)

        return self.header_box

    def create_import_profile_body_box(self):
        self.body_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.body_box.set_name("custom-body")

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.NONE)
        self.stack.set_vexpand(True)
        self.stack.set_hexpand(True)

        via_url = self.create_url_stack()
        upload_file = self.create_file_stack()

        self.stack.add_named(via_url, "url")
        self.stack.add_named(upload_file, "file")

        self.tab_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        self.tab_box.set_halign(Gtk.Align.CENTER)
        self.tab_box.set_margin_top(10)

        self.via_url_btn = Gtk.Button(label="VIA URL")
        self.via_url_btn.set_size_request(200, -1)
        self.via_url_btn.get_style_context().add_class("body-stack-toggle-btn")
        self.upload_file_btn = Gtk.Button(label="UPLOAD FILE")
        self.upload_file_btn.set_size_request(200, -1)
        self.upload_file_btn.get_style_context().add_class("body-stack-toggle-btn")

        self.via_url_btn.connect("clicked", lambda btn: self.switch_tab("url"))
        self.upload_file_btn.connect("clicked", lambda btn: self.switch_tab("file"))

        self.tab_box.pack_start(self.via_url_btn, False, False, 0)
        self.tab_box.pack_start(self.upload_file_btn, False, False, 0)

        self.body_box.pack_start(self.tab_box, False, False, 10)
        self.body_box.pack_start(self.stack, True, True, 10)

        self.switch_tab("url")

        return self.body_box

    def switch_tab(self, tab_name):
        self.stack.set_visible_child_name(tab_name)
        self.via_url_btn.get_style_context().remove_class("selected")
        self.upload_file_btn.get_style_context().remove_class("selected")
        if tab_name == "url":
            self.via_url_btn.get_style_context().add_class("selected")
        else:
            self.upload_file_btn.get_style_context().add_class("selected")

    def create_url_stack(self):
        outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        inner_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        inner_box.set_valign(Gtk.Align.CENTER)
        inner_box.set_halign(Gtk.Align.CENTER)

        
        # Footer button
        footer_box = Gtk.Box()
        footer_box.set_size_request(-1, 40)
        footer_box.set_valign(Gtk.Align.END)
        footer_box.set_halign(Gtk.Align.CENTER)

        button = Gtk.Button(label="NEXT")
        button.get_style_context().add_class("add-wide-footer-btn")
        button.set_margin_bottom(20)
        
        footer_box.pack_start(button, False, False, 0)
        outer_box.pack_start(inner_box, True, True, 0)
        outer_box.pack_start(footer_box, False, False, 0)

        return outer_box

    def create_file_stack(self):
        outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        inner_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        inner_box.set_valign(Gtk.Align.CENTER)
        inner_box.set_halign(Gtk.Align.CENTER)

        footer_box = Gtk.Box()
        footer_box.set_size_request(-1, 40)
        footer_box.set_valign(Gtk.Align.END)
        footer_box.set_halign(Gtk.Align.CENTER)

        outer_box.pack_start(inner_box, True, True, 0)
        outer_box.pack_start(footer_box, False, False, 0)

        return outer_box
