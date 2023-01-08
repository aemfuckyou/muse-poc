from View.ChooseResultScreen import ChooseResultPage

class ChooseResultController:

    def __init__(self, model):
        self.model = model
        self.view = ChooseResultPage(controller=self, model=self.model)

    def get_all_tests(self):
        self.model.get_all_tests()

    def get_screen(self):
        return self.view

    def load_text(self):
        self.model.load_text()
