import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from error import Error

def load_css():

    css_provider = Gtk.CssProvider()
    css_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..", "css", "styles.css"
                )
            )

    if not os.path.exists(css_path):
        Error().show_error_dialog(f"CSS file not found:\n{css_path}")

    try:
        css_provider.load_from_path(css_path)
        screen = Gdk.Screen.get_default()
        Gtk.StyleContext.add_provider_for_screen(
                screen,
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                )

    except Exception as e:
        Error().show_error_dialog(f"Failed to load CSS:\n{e}")

class MainGUI:
    def ProfilesWindow(self):
        
        load_css()

        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
