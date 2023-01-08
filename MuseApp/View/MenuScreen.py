from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
import Controller as c
import Model as m
from Model.choosetestscreen import ChooseTestModel
from Controller.choosetestscreen import ChooseTestController
from Model.chooseresultscreen import ChooseResultModel
from Controller.chooseresultscreen import ChooseResultController

class MenuPage (MDScreen, Observer):

    #<Controller.menuscreen.MenuScreenController object>
    controller = ObjectProperty()
    #<Model.menuscreen.MenuScreenModel object>
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer

    def model_is_changed(self):
        pass

    def route_tests(self):
        self.model = ChooseTestModel(self.model.user)
        self.controller = ChooseTestController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")

    def back_to_start(self):
        self.model = m.startscreen.StartScreenModel()
        self.controller = c.startscreen.StartScreenController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="right")

    def route_results(self):
        self.model = ChooseResultModel(self.model.user)
        self.controller = ChooseResultController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")


    Builder.load_file('View/menuscreen.kv')
