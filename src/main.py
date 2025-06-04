import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from read_write_json import ReadWriteJSON
from window_components.window_components import WindowUIComponents
from window_components.window_components import InitWindows

class MainGUI:
    def __init__(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()
        self.win_ui = WindowUIComponents()
        self.overlay, self.stack = self.win_ui.create_window()

        self.init = InitWindows(callback=self)
        self.overlay, self.stack = self.init.overlay, self.init.stack
        self.win_ui = self.init.win_ui

        self.init.init_logs_window()
        self.init.init_import_profile_window()
        self.init.init_add_proxy_window()
        self.init.init_proxies_window()
        self.init.init_cert_and_tok_window()
        self.init.init_settings_window(callback=self)
        self.init.init_statistics_window()
        self.init.init_profiles_window()
        self.profiles_window()
 
    def profiles_window(self, button=None):
        self.win_ui.win.show_all()
        self.stack.set_visible_child_name("profiles")

    def statistics_window(self, button=None):
        self.stack.set_visible_child_name("statistics")
        self.win_ui.win.show_all()

    def settings_window(self, button=None):
        self.stack.set_visible_child_name("settings")
        self.win_ui.win.show_all()

    def cert_and_tok_window(self, button=None):
        self.stack.set_visible_child_name("cert_and_tok")
        self.win_ui.win.show_all()

    def add_proxy_window(self, button=None):
        self.stack.set_visible_child_name("add_proxy")
        self.win_ui.win.show_all()

    def proxies_window(self, button=None):
        self.stack.set_visible_child_name("proxies")
        self.win_ui.win.show_all()

    def import_profile_window(self, button=None):
        self.stack.set_visible_child_name("import_profile")
        self.win_ui.win.show_all()

    def logs_window(self, button=None):
        self.stack.set_visible_child_name("logs")
        self.win_ui.win.show_all()

    def reload_theme_dependent_pages(self, theme_value):
        cert_widget = self.stack.get_child_by_name("cert_and_tok")
        if cert_widget:
            self.stack.remove(cert_widget)
        proxies_widget = self.stack.get_child_by_name("proxies")
        if proxies_widget:
            self.stack.remove(proxies_widget)
        import_widget = self.stack.get_child_by_name("import_profile")
        if import_widget:
            self.stack.remove(import_widget)

        self.init.init_cert_and_tok_window()
        self.init.init_proxies_window()
        self.init.init_import_profile_window()


if __name__ == "__main__":
    app = MainGUI()
    Gtk.main()
