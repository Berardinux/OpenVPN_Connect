import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from window_components.profiles_window_components import ProfilesWindowUIComponents
from window_components.statistics_window_components import StatisticsWindowUIComponents
from window_components.settings_window_components import SettingsWindowUIComponents
from window_components.cert_and_tok_window_components import CertAndTokWindowUIComponents
from window_components.add_proxy_window_components import AddProxyWindowUIComponents
from window_components.proxies_window_components import ProxiesWindowUIComponents
from window_components.import_profile_window_components import ImportProfileWindowUIComponents
from window_components.logs_window_components import LogsWindowUIComponents

class WindowUIComponents:
    def __init__(self):
        self.win = None
        self.stack = None
        self.overlay = None

    def create_window(self):
        self.win = Gtk.Window()
        self.win.set_title("Linux OVPN")
        self.win.set_default_size(500, 800)
        self.win.set_resizable(False)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)
        self.win.set_keep_above(True)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.NONE)
        self.stack.set_transition_duration(0)

        screen = Gdk.Screen.get_default()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.win.set_visual(visual)

        self.win.set_app_paintable(True)
        self.win.connect("draw", self.on_draw_background)

        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.NONE)
        frame.set_name("main-frame")
        frame.add(self.stack)


        self.overlay = Gtk.Overlay()
        self.overlay.add(frame)

        self.win.add(self.overlay)
        return self.overlay, self.stack
        
    def on_draw_background(self, widget, cr):
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)
        return False

class InitWindows:
    def __init__(self, callback):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()
        self.callback = callback
        self.win_ui = WindowUIComponents()
        self.overlay, self.stack = self.win_ui.create_window()

    def init_profiles_window(self):
        pro_ui = ProfilesWindowUIComponents()
        header_box = pro_ui.create_profiles_header_box(
                hamburger_button_clicked=pro_ui.open_sidebar, 
                list_button_clicked=self.callback.logs_window
                )
        body_box = pro_ui.create_profiles_body_box()
        footer_box = pro_ui.create_profiles_footer_box(callback=self.callback.import_profile_window)
        profiles_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        profiles_view.pack_start(header_box, False, False, 0)
        profiles_view.pack_start(body_box, True, True, 0)
        profiles_view.pack_start(footer_box, False, False, 0)

        profiles_overlay = Gtk.Overlay()
        profiles_overlay.add(profiles_view)

        self.profiles_dimmer = Gtk.EventBox()
        self.profiles_dimmer.set_visible_window(True)
        self.profiles_dimmer.override_background_color(
                Gtk.StateFlags.NORMAL,
                Gdk.RGBA(0, 0, 0, 0.5)
                )

        self.profiles_dimmer.set_halign(Gtk.Align.FILL)
        self.profiles_dimmer.set_valign(Gtk.Align.FILL)
        self.profiles_dimmer.set_hexpand(True)
        self.profiles_dimmer.set_vexpand(True)
        self.profiles_dimmer.set_no_show_all(True)
        self.profiles_dimmer.hide()

        profiles_overlay.add_overlay(self.profiles_dimmer)

        self.stack.add_named(profiles_overlay, "profiles")

        self.stack.set_visible_child_name("profiles")
        pro_ui.create_sidebar(
                self.overlay,
                import_profile_callback=self.callback.import_profile_window,
                proxies_callback=self.callback.proxies_window,
                cert_and_tok_callback=self.callback.cert_and_tok_window,
                settings_callback=self.callback.settings_window,
                statistics_callback=self.callback.statistics_window,
                dimmer=self.profiles_dimmer
                )

    def init_statistics_window(self):
        sta_ui = StatisticsWindowUIComponents()
        statistics_header_box = sta_ui.create_statistics_header_box(callback=self.callback.profiles_window)
        statistics_body_box = sta_ui.create_statistics_body_box()
        statistics_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        statistics_view.pack_start(statistics_header_box, False, False, 0)
        statistics_view.pack_start(statistics_body_box, True, True, 0)
        self.stack.add_named(statistics_view, "statistics")

    def init_settings_window(self, callback):
        set_ui = SettingsWindowUIComponents(callback)
        settings_header_box = set_ui.create_settings_header_box(callback=self.callback.profiles_window)
        settings_body_box = set_ui.create_settings_body_box()
        settings_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        settings_view.pack_start(settings_header_box, False, False, 0)
        settings_view.pack_start(settings_body_box, True, True, 0)
        self.stack.add_named(settings_view, "settings")

    def init_cert_and_tok_window(self):
        cer_ui = CertAndTokWindowUIComponents()
        cert_and_tok_header_box = cer_ui.create_cert_and_tok_header_box(callback=self.callback.profiles_window)
        cert_and_tok_body_box = cer_ui.create_cert_and_tok_body_box()
        cert_and_tok_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cert_and_tok_view.pack_start(cert_and_tok_header_box, False, False, 0)
        cert_and_tok_view.pack_start(cert_and_tok_body_box, True, True, 0)
        self.stack.add_named(cert_and_tok_view, "cert_and_tok")

    def init_add_proxy_window(self):
        apr_ui = AddProxyWindowUIComponents()
        add_proxy_header_box = apr_ui.create_add_proxy_header_box(callback=self.callback.proxies_window)
        add_proxy_body_box = apr_ui.create_add_proxy_body_box()
        add_proxy_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        add_proxy_view.pack_start(add_proxy_header_box, False, False, 0)
        add_proxy_view.pack_start(add_proxy_body_box, True, True, 0)
        self.stack.add_named(add_proxy_view, "add_proxy")

    def init_proxies_window(self):
        prx_ui = ProxiesWindowUIComponents()
        proxies_header_box = prx_ui.create_proxies_header_box(callback=self.callback.profiles_window)
        proxies_body_box = prx_ui.create_proxies_body_box()
        proxies_footer_box = prx_ui.create_proxies_footer_box(callback=self.callback.add_proxy_window)
        proxies_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        proxies_view.pack_start(proxies_header_box, False, False, 0)
        proxies_view.pack_start(proxies_body_box, True, True, 0)
        proxies_view.pack_start(proxies_footer_box, False, False, 0)
        self.stack.add_named(proxies_view, "proxies")

    def init_import_profile_window(self):
        imp_ui = ImportProfileWindowUIComponents()
        import_profile_header_box = imp_ui.create_import_profile_header_box(callback=self.callback.profiles_window)
        import_profile_body_box = imp_ui.create_import_profile_body_box()
        import_profile_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        import_profile_view.pack_start(import_profile_header_box, False, False, 0)
        import_profile_view.pack_start(import_profile_body_box, True, True, 0)
        self.stack.add_named(import_profile_view, "import_profile")

    def init_logs_window(self):
        log_ui = LogsWindowUIComponents()
        logs_header_box = log_ui.create_logs_header_box(callback=self.callback.profiles_window)
        logs_body_box = log_ui.create_logs_body_box()
        logs_view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        logs_view.pack_start(logs_header_box, False, False, 0)
        logs_view.pack_start(logs_body_box, True, True, 0)
        self.stack.add_named(logs_view, "logs")
