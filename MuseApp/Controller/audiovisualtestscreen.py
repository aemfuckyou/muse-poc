from View.AudioVisualTestScreen import AudioVisualTestPage

class AudioVisualTestController:

    def __init__(self, model):
        self.model = model
        self.view = AudioVisualTestPage(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def load_text(self):
        self.model.load_text()
