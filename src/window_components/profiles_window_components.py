import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf
from read_write_json import ReadWriteJSON

class ProfilesWindowUIComponents:
    def __init__(self):
        self.header_box = None
        self.header_label = None
        self.body_box = None
        self.footer_box = None
        self.revealer = None
        self.config=ReadWriteJSON().read_config()
        self.theme = self.config.get("theme", "light")

    def create_profiles_header_box(self, hamburger_button_clicked, list_button_clicked):
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
        hamburger_button.connect("clicked", hamburger_button_clicked)
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
        list_button.connect("clicked", list_button_clicked)
        self.header_box.pack_start(list_button, False, False, 0)

        return self.header_box

    def create_profiles_body_box(self):
        self.body_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.body_box.set_name("custom-body")
        return self.body_box

    def create_profiles_footer_box(self, callback):
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

    def create_sidebar(
            self, overlay,
            import_profile_callback=None,
            proxies_callback=None,
            cert_and_tok_callback = None,
            settings_callback=None,
            statistics_callback=None,
            dimmer=None
            ):
        self.profiles_dimmer = dimmer
        self.import_profile_callback = import_profile_callback
        self.proxies_callback = proxies_callback
        self.cert_and_tok_callback = cert_and_tok_callback
        self.settings_callback = settings_callback
        self.statistics_callback = statistics_callback

        self.revealer = Gtk.Revealer()
        self.revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_RIGHT)
        self.revealer.set_transition_duration(300)

        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        sidebar.set_size_request(250, -1)
        sidebar.set_name("sidebar")
        sidebar.get_style_context().add_class("sidebar")

        # Spacer
        spacer = Gtk.Box()
        spacer.set_size_request(-1, 40)
        sidebar.pack_start(spacer, False, False, 0)

        buttons = {
                "Import Profile": lambda btn: (self.close_sidebar(), self.import_profile_callback(btn)),
                "Proxies": lambda btn: (self.close_sidebar(), self.proxies_callback(btn)),
                "Certificates & Tokens": lambda btn: (self.close_sidebar(), self.cert_and_tok_callback(btn)),
                "Settings": lambda btn: (self.close_sidebar(), self.settings_callback(btn)),
                "Statistics": lambda btn: (self.close_sidebar(), self.statistics_callback(btn))
                }

        for label, handler in buttons.items():
            button = Gtk.Button(label=label)
            button.set_margin_left(20)
            button.set_margin_right(20)
            button.connect("clicked", handler)
            sidebar.pack_start(button, False, False, 0)

        self.revealer.add(sidebar)
        self.revealer.set_reveal_child(False)
        self.revealer.set_halign(Gtk.Align.START)
        self.revealer.set_valign(Gtk.Align.FILL)
        overlay.add_overlay(self.revealer)

        self.click_catcher = Gtk.EventBox()
        self.click_catcher.set_visible_window(True)
        self.click_catcher.set_above_child(True)
        self.click_catcher.connect("button-press-event", self._on_click_outside)

        click_area = Gtk.Box()
        click_area.set_size_request(1, 1)
        self.click_catcher.add(click_area)
        
        self.click_catcher.set_margin_left(250)
        self.click_catcher.set_hexpand(True)
        self.click_catcher.set_vexpand(True)
        self.click_catcher.set_valign(Gtk.Align.FILL)
        self.click_catcher.set_halign(Gtk.Align.FILL)
        overlay.add_overlay(self.click_catcher)
        self.click_catcher.set_no_show_all(True)
        self.click_catcher.hide()

    def open_sidebar(self, button=None):
        self.revealer.set_reveal_child(True)
        if self.click_catcher:
            self.profiles_dimmer.show()
            self.click_catcher.show()

    def close_sidebar(self):
        self.revealer.set_reveal_child(False)
        if self.click_catcher:
            self.click_catcher.hide()
            self.profiles_dimmer.hide()

    def _on_click_outside(self, widget, event):
        self.close_sidebar()
        return True
