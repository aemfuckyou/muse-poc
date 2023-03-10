
class ChooseTestModel:

    def __init__(self, user):
        self._observers = []
        self.user = user

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()