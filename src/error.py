import os
import gi
import sys
gi.require_version("Gtk", "3.0")
import os
from gi.repository import Gtk, Gdk

class Error:
    def show_error_dialog(self, message):
        dialog = Gtk.MessageDialog (
            transient_for = None,
            flags = 0,
            message_type = Gtk.MessageType.ERROR,
            buttons = Gtk.ButtonsType.CLOSE,
            text = "OpenVPN_Connect Error",
        )
    
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()

class ErrorCheck:
    def error_check_for_loading_css(self, css_provider, css_path):
        if not os.path.exists(css_path):
            Error().show_error_dialog(f"CSS file not found:\n{css_path}")
            sys.exit(1)
            Gtk.main_quit()

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
            sys.exit(1)
            Gtk.main_quit()

    def error_check_for_loading_config(self, config_path):
        if not os.path.exists(config_path):
            Error().show_error_dialog(f"Config file not found:\n{config_path}")
            sys.exit(1)
            Gtk.main_quit()

    def error_check_for_drag_and_drop_ovpn_profile(self, path):
        name, ext = os.path.splitext(path)
        if ext.lower() != ".ovpn":
            Error().show_error_dialog(
                    f"Failed to import profile\nWe do not support this type of files"
                    )
            return 1
        else:
            return 0
        
