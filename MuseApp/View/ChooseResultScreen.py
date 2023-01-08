import Controller as c
import Model as m
from Model.plottestscreen import PlotTestModel
from Controller.plottestscreen import PlotTestController
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem


class ChooseResultPage (MDScreen, Observer):

    #<Controller.chooseresultscreen.ChooseResultController object>
    controller = ObjectProperty()
    #<Model.chooseresultscreen.ChooseResultModel object>
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer
        self.controller.get_all_tests()

    def model_is_changed(self):
        self.tests = self.model.tests
        self.ids.test_list.clear_widgets()
        for idx, test in enumerate(self.tests):
            self.ids.test_list.add_widget(
                OneLineListItem(text=f'Test No. {idx+1} at {test.start_time.strftime("%d-%m-%Y, %H:%M:%S")}',
                                on_release=self.choose_test, id=str(idx))
            )

    def back_to_menu(self):
        self.model = m.menuscreen.MenuScreenModel(self.model.user.user_name)
        self.controller = c.menuscreen.MenuScreenController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="right")

    def choose_test(self, instance):
        self.model = PlotTestModel(self.tests[int(instance.id)])
        self.controller = PlotTestController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")

    Builder.load_file('View/chooseresultscreen.kv')
