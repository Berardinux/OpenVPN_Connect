import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from components import UIComponents

def my_click_function(wedget):
    print("Hamburger Clicked!")

class MainGUI:
    def profiles_window(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()

        ui = UIComponents()
        ui.create_profiles_header_box(callback=my_click_function)
        ui.create_window()
        ui.win.show_all()


MainGUI().profiles_window()
Gtk.main()

