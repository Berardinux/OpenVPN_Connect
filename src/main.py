import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from window_components.window_components import WindowUIComponents
from window_components.profiles_window_components import ProfilesWindowUIComponents
from window_components.statistics_window_components import StatisticsWindowUIComponents
from window_components.settings_window_components import SettingsWindowUIComponents
from window_components.cert_and_tok_window_components import CertAndTokWindowUIComponents
from window_components.add_proxy_window_components import AddProxyWindowUIComponents
from window_components.proxies_window_components import ProxiesWindowUIComponents
from window_components.import_profile_window_components import ImportProfileWindowUIComponents
from window_components.logs_window_components import LogsWindowUIComponents

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
                proxies_callback=self.proxies_window,
                cert_and_tok_callback=self.cert_and_tok_window,
                settings_callback=self.settings_window,
                statistics_callback=self.statistics_window
                )

    def profiles_window(self, button=None):
        self.win_ui.win.show_all()
        self.stack.set_visible_child_name("profiles")

    def init_statistics_window(self):
        sta_ui = StatisticsWindowUIComponents()
        statistics_header_box = sta_ui.create_statistics_header_box(callback=self.profiles_window)
        statistics_body_box = sta_ui.create_statistics_body_box()
        statistics_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        statistics_view.pack_start(statistics_header_box, False, False, 0)
        statistics_view.pack_start(statistics_body_box, True, True, 0)
        self.stack.add_named(statistics_view, "statistics")

    def statistics_window(self, button=None):
        self.stack.set_visible_child_name("statistics")
        self.win_ui.win.show_all()

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

    def init_cert_and_tok_window(self):
        cer_ui = CertAndTokWindowUIComponents()
        cert_and_tok_header_box = cer_ui.create_cert_and_tok_header_box(callback=self.profiles_window)
        cert_and_tok_body_box = cer_ui.create_cert_and_tok_body_box()
        cert_and_tok_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cert_and_tok_view.pack_start(cert_and_tok_header_box, False, False, 0)
        cert_and_tok_view.pack_start(cert_and_tok_body_box, True, True, 0)
        self.stack.add_named(cert_and_tok_view, "cert_and_tok")

    def cert_and_tok_window(self, button=None):
        self.stack.set_visible_child_name("cert_and_tok")
        self.win_ui.win.show_all()

    def init_add_proxy_window(self):
        apr_ui = AddProxyWindowUIComponents()
        add_proxy_header_box = apr_ui.create_add_proxy_header_box(callback=self.proxies_window)
        add_proxy_body_box = apr_ui.create_add_proxy_body_box()
        add_proxy_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        add_proxy_view.pack_start(add_proxy_header_box, False, False, 0)
        add_proxy_view.pack_start(add_proxy_body_box, True, True, 0)
        self.stack.add_named(add_proxy_view, "add_proxy")

    def add_proxy_window(self, button=None):
        self.stack.set_visible_child_name("add_proxy")
        self.win_ui.win.show_all()

    def init_proxies_window(self):
        prx_ui = ProxiesWindowUIComponents()
        proxies_header_box = prx_ui.create_proxies_header_box(callback=self.profiles_window)
        proxies_body_box = prx_ui.create_proxies_body_box()
        proxies_footer_box = prx_ui.create_proxies_footer_box(callback=self.add_proxy_window)
        proxies_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        proxies_view.pack_start(proxies_header_box, False, False, 0)
        proxies_view.pack_start(proxies_body_box, True, True, 0)
        proxies_view.pack_start(proxies_footer_box, False, False, 0)
        self.stack.add_named(proxies_view, "proxies")

    def proxies_window(self, button=None):
        self.stack.set_visible_child_name("proxies")
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

if __name__ == "__main__":
    app = MainGUI()
    app.init_logs_window()
    app.init_import_profile_window()
    app.init_add_proxy_window()
    app.init_proxies_window()
    app.init_cert_and_tok_window()
    app.init_settings_window()
    app.init_statistics_window()
    app.init_profiles_window()
    app.profiles_window()
    Gtk.main()
