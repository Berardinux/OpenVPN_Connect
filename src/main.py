import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from load_css import LoadCSS
from window_components import WindowUIComponents
from profiles_window_components import ProfilesWindowUIComponents

def my_click_function(wedget):
    print("Hamburger Clicked!")

class MainGUI:
    def profiles_window(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()

        win_ui = WindowUIComponents()
        pro_ui = ProfilesWindowUIComponents()
        header_box = pro_ui.create_profiles_header_box(
                hamburger_button_clicked=pro_ui.toggle_sidebar, 
                list_button_clicked=my_click_function
                )
        body_box = pro_ui.create_profiles_body_box()
        footer_box = pro_ui.create_profiles_footer_box(callback=my_click_function)
        pro_ui.create_sidebar()
        win_ui.create_window(header_box, body_box, footer_box)
        win_ui.win.show_all()

    def settings_window(self):
        LoadCSS().load_styles_css()
        LoadCSS().load_theme_css()




MainGUI().profiles_window()
Gtk.main()
