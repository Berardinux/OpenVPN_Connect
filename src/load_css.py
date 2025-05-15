import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from error import ErrorCheck
from read_write_json import ReadWriteJSON

class LoadCSS:
    CSS_PROVIDER = Gtk.CssProvider()

    def __init__(self):
        self.config = ReadWriteJSON().read_config()
    
    def load_styles_css(self):
    
        css_path = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "css", "styles.css"
                    )
                )

        ErrorCheck().error_check_for_loading_css(LoadCSS.CSS_PROVIDER, css_path)

    def load_theme_css(self):
        theme = self.config.get("theme", "light")
        filename = f"{theme}.css"

        css_path = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "css", filename
                    )
                )

        ErrorCheck().error_check_for_loading_css(self.CSS_PROVIDER, css_path)


