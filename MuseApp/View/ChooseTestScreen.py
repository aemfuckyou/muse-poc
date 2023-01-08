from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
import Controller as c
import Model as m
from Controller.audiovisualtestscreen import AudioVisualTestController
from Model.audiovisualtestscreen import AudioVisualTestModel
from Controller.visualtestscreen import VisualTestController
from Model.visualtestscreen import VisualTestModel

class ChooseTestPage (MDScreen, Observer):

    #<Controller.choosetestscreen.ChooseTestController object>
    controller = ObjectProperty()
    #<Model.choosetestscreen.ChooseTestModel object>
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer

    def model_is_changed(self):
        pass
    
    def back_to_menu(self):
        self.model = m.menuscreen.MenuScreenModel(self.model.user.user_name)
        self.controller = c.menuscreen.MenuScreenController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="right")


    def start_visual_test(self):
        self.model = VisualTestModel(self.model.user)
        self.controller = VisualTestController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")

    def start_audio_visual_test(self):
        self.model = AudioVisualTestModel(self.model.user)
        self.controller = AudioVisualTestController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")


    Builder.load_file('View/choosetestscreen.kv')
