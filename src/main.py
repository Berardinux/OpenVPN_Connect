import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from window_components.window_components import WindowUIComponents
from window_components.profiles_window_components import ProfilesWindowUIComponents
from window_components.settings_window_components import SettingsWindowUIComponents
from window_components.logs_window_components import LogsWindowUIComponents
from window_components.import_profile_window_components import ImportProfileWindowUIComponents

def my_click_function(wedget):
    print("Hamburger Clicked!")

class MainGUI:
    def __init__(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()
        self.win_ui = WindowUIComponents()
        self.overlay, self.stack = self.win_ui.create_window()
 
    def init_profiles_window(self):
        self.settings_window()
        pro_ui = ProfilesWindowUIComponents()
        header_box = pro_ui.create_profiles_header_box(
                hamburger_button_clicked=pro_ui.open_sidebar, 
                list_button_clicked=self.logs_window
                )
        body_box = pro_ui.create_profiles_body_box()
        footer_box = pro_ui.create_profiles_footer_box(callback=self.import_profile_window)
        profiles_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        profiles_view.pack_start(header_box, False, False, 0)
        profiles_view.pack_start(body_box, True, True, 0)
        profiles_view.pack_start(footer_box, False, False, 0)
        if not self.stack.get_child_by_name("profiles"):
            self.stack.add_named(profiles_view, "profiles")
        self.stack.set_visible_child_name("profiles")
        pro_ui.create_sidebar(
                self.overlay,
                import_profile_callback=self.import_profile_window,
                settings_callback=self.settings_window
                )

    def profiles_window(self, button=None):
        self.win_ui.win.show_all()
        self.stack.set_visible_child_name("profiles")

    def init_settings_window(self):
        set_ui = SettingsWindowUIComponents()
        settings_header_box = set_ui.create_settings_header_box(callback=self.profiles_window)
        settings_body_box = set_ui.create_settings_body_box()
        settings_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        settings_view.pack_start(settings_header_box, False, False, 0)
        settings_view.pack_start(settings_body_box, True, True, 0)
        self.stack.add_named(settings_view, "settings")

    def settings_window(self, button=None):
        self.stack.set_visible_child_name("settings")
        self.win_ui.win.show_all()

    def init_logs_window(self):
        log_ui = LogsWindowUIComponents()
        logs_header_box = log_ui.create_logs_header_box(callback=self.profiles_window)
        logs_body_box = log_ui.create_logs_body_box()
        logs_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        logs_view.pack_start(logs_header_box, False, False, 0)
        logs_view.pack_start(logs_body_box, True, True, 0)
        self.stack.add_named(logs_view, "logs")

    def logs_window(self, button=None):
        self.stack.set_visible_child_name("logs")
        self.win_ui.win.show_all()

    def init_import_profile_window(self):
        imp_ui = ImportProfileWindowUIComponents()
        import_profile_header_box = imp_ui.create_import_profile_header_box(callback=self.profiles_window)
        import_profile_body_box = imp_ui.create_import_profile_body_box()
        import_profile_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        import_profile_view.pack_start(import_profile_header_box, False, False, 0)
        import_profile_view.pack_start(import_profile_body_box, True, True, 0)
        self.stack.add_named(import_profile_view, "import_profile")

    def import_profile_window(self, button=None):
        self.stack.set_visible_child_name("import_profile")
        self.win_ui.win.show_all()

if __name__ == "__main__":
    app = MainGUI()
    app.init_logs_window()
    app.init_import_profile_window()
    app.init_settings_window()
    app.init_profiles_window()
    app.profiles_window()
    Gtk.main()
