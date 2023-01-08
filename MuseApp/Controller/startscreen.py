from View.StartScreen import EntryPage

class StartScreenController:

    def __init__(self, model):
        self.model = model
        self.view = EntryPage(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def get_all_users(self):
        self.model.get_all_users()

    def new_user_name(self, value):
        self.model.new_user_name(value)

