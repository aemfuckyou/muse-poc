from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Controller.menuscreen import MenuScreenController
from Model.menuscreen import MenuScreenModel
from Utility.observer import Observer
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty

class EntryPage (MDScreen, Observer):

    users = []

    #<Controller.startscreen.StartScreenController object>
    controller = ObjectProperty()
    #<Model.startscreen.StartScreenModel object>
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer
        self.controller.get_all_users()

    def save_new_user(self):
        # add new user to db with user_name of text in textinputfield
        inputUser = self.ids.tfNewUser.text
        self.controller.new_user_name(inputUser)

    def model_is_changed(self):
        self.users = self.model.users
        self.ids.user_list.clear_widgets()
        for i in self.users:
            self.ids.user_list.add_widget(
                OneLineListItem(text=i, on_release=self.choose_user)
            )

    def choose_user(self, value):
        #route to new view with existing user in db
        self.change_scene_to_menu(value.text)

    def change_scene_to_menu(self, value):
        self.model = MenuScreenModel(value)
        self.controller = MenuScreenController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="left")


    Builder.load_file('View/startscreen.kv')
