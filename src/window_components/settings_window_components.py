import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf
from read_write_json import ReadWriteJSON
from load_css import ThemeManager
from gi.repository import GLib

class SettingsWindowUIComponents:
    def __init__(self, callback):
        self.callback = callback
        self.header_box = None
        self.header_label = None
        self.body_box = None
        self.theme_buttons = []
        self.config=ReadWriteJSON().read_config()
        self.theme = self.config.get("theme", "light")

    def create_settings_header_box(self, callback):
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
        self.header_label = Gtk.Label("Settings")
        self.header_label.set_halign(Gtk.Align.CENTER)
        self.header_label.get_style_context().add_class("Settings")
        self.header_box.pack_start(self.header_label, True, True, 0)

        # Spacer
        spacer = Gtk.Box()
        spacer.set_size_request(80, -1)
        self.header_box.pack_start(spacer, False, False, 0)

        return self.header_box

    def create_settings_body_box(self):
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_hexpand(True)
        scroll.set_vexpand(False)
        scroll.set_name("custom-body-scroll")

        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        container.set_margin_top(20)
        container.set_margin_bottom(20)
        container.set_margin_left(20)
        container.set_margin_right(20)

        # Theme section {
        theme_title = Gtk.Label(label="Theme")
        theme_title.get_style_context().add_class("h5")
        theme_title.get_style_context().add_class("color3")
        theme_title.set_halign(Gtk.Align.START)
        
        theme_desc = Gtk.Label(label="Choose application color theme")
        theme_desc.get_style_context().add_class("h6")
        theme_desc.get_style_context().add_class("color0")
        theme_desc.set_halign(Gtk.Align.START)
        theme_desc.set_valign(Gtk.Align.START)
        theme_desc.set_line_wrap(True)

        theme_button_box = Gtk.Box(spacing=10)
        theme_button_box.set_halign(Gtk.Align.START)

        themes = [("Light", "light"), ("Dark", "dark")]

        for label_text, theme_value in themes:
            btn = Gtk.Button(label=label_text.upper())
            btn.set_name("settings-toggle-btn")
            btn.connect("clicked", self.on_theme_clicked, theme_value)
            if theme_value == self.theme:
                btn.get_style_context().add_class("theme-selected")
            self.theme_buttons.append(btn)
            theme_button_box.pack_start(btn, False, False, 0)

        container.pack_start(theme_title, False, False, 0)
        container.pack_start(theme_desc, False, False, 0)
        container.pack_start(theme_button_box, False, False, 0)
        # }


        scroll.add(container)
        self.body_box = scroll
        return self.body_box

    def on_theme_clicked(self, button, theme_value):
        print(f"Theme selected: {theme_value}")
        self.config["theme"] = theme_value
        ReadWriteJSON().write_config(self.config)

        for btn in self.theme_buttons:
            btn.get_style_context().remove_class("theme-selected")

        button.get_style_context().add_class("theme-selected")

        ThemeManager().apply_theme(theme_value)

        GLib.idle_add(self.callback.reload_theme_dependent_pages, theme_value)  

        
