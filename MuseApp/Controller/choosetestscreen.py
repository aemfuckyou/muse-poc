from View.ChooseTestScreen import ChooseTestPage

class ChooseTestController:

    def __init__(self, model):
        self.model = model
        self.view = ChooseTestPage(controller=self, model=self.model)

    def get_screen(self):
        return self.view
