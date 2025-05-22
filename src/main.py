import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from window_components import WindowUIComponents
from profiles_window_components import ProfilesWindowUIComponents
from settings_window_components import SettingsWindowUIComponents

def my_click_function(wedget):
    print("Hamburger Clicked!")

class MainGUI:
    def __init__(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()
        self.win_ui = WindowUIComponents()
        self.overlay, self.stack = self.win_ui.create_window()

    def profiles_window(self, button=None):

        pro_ui = ProfilesWindowUIComponents()

        header_box = pro_ui.create_profiles_header_box(
                hamburger_button_clicked=pro_ui.toggle_sidebar, 
                list_button_clicked=my_click_function
                )
        body_box = pro_ui.create_profiles_body_box()
        footer_box = pro_ui.create_profiles_footer_box(callback=my_click_function)

        profiles_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        profiles_view.pack_start(header_box, False, False, 0)
        profiles_view.pack_start(body_box, True, True, 0)
        profiles_view.pack_start(footer_box, False, False, 0)

        if not self.stack.get_child_by_name("profiles"):
            self.stack.add_named(profiles_view, "profiles")

        self.stack.set_visible_child_name("profiles")

        pro_ui.create_sidebar(self.overlay, settings_callback=self.settings_window)

        self.win_ui.win.show_all()

    def settings_window(self, button=None):
        set_ui = SettingsWindowUIComponents()

        header_box = set_ui.create_settings_header_box(callback=self.profiles_window)
        body_box = set_ui.create_settings_body_box()

        settings_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        settings_view.pack_start(header_box, False, False, 0)
        settings_view.pack_start(body_box, True, True, 0)

        if not self.stack.get_child_by_name("settings"):
            self.stack.add_named(settings_view, "settings")

        self.stack.set_visible_child_name("settings")

        self.win_ui.win.show_all()

MainGUI().profiles_window()
Gtk.main()
