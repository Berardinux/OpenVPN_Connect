import g
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

def load_css():
    css_provider = Gtk.CssProvider()

    css_path = "css/styles.css"


class MainGUI:
    def ProfilesWindow(self):

        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
