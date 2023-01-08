from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

class ScrollableLabel(ScrollView):
    text = StringProperty('')

    Builder.load_file('View/scrollablelabel.kv')