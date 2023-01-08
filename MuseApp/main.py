import threading
from kivymd.app import MDApp
from Controller.startscreen import StartScreenController
from Model.startscreen import StartScreenModel
from kivymd.uix.screenmanager import ScreenManager

class Main(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = StartScreenModel()
        self.controller = StartScreenController(self.model)
        self.sm = ScreenManager()
        self.sm.stop = threading.Event()

    def build(self):
        self.title = "Muse Test POC"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.sm.add_widget(self.controller.get_screen())
        return self.sm

    def on_stop(self):
        self.root.stop.set()

Main().run()
