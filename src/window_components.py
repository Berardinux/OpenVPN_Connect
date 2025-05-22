import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class WindowUIComponents:
    def __init__(self):
        self.win = None
        self.stack = None
        self.overlay = None

    def create_window(self):
        self.win = Gtk.Window()
        self.win.set_title("OpenVPN Connect")
        self.win.set_default_size(500, 800)
        self.win.set_resizable(False)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(300)


        self.overlay = Gtk.Overlay()
        self.overlay.add(self.stack)

        self.win.add(self.overlay)
        return self.overlay, self.stack


