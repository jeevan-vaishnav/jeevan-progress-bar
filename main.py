from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar

Builder.load_file('main.kv')


class MyLayout(Widget):
    def press_it(self):
        # Grab the current progress bar value
        current = self.ids.my_profress_bar.value

        # If statement to start voer after 100

        if current == 1:
            current = 0

        # Increment value by .25
        current += .25
        # Update the progress bar
        self.ids.my_profress_bar.value = current

        # Update the label
        self.ids.my_label.text = f"{int(current*100)}% Progress"


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
