import gi
gi.require_version("Gtk", "3.0")
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
        Gtk.main.quit()


