import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class CarList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.load_cars()

    def load_cars(self):
        try:
            with open('cars.json', 'r') as f:
                cars = json.load(f)
        except FileNotFoundError:
            print("Error: cars.json file not found")
            return
        except json.JSONDecodeError:
            print("Error: cars.json file is malformed")
            return

        self.create_car_list(cars)

    def create_car_list(self, cars):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for car in cars:
            car_info = f"Nome: {car['name']}\nFabricante: {car['manufacturer']}\nVelocidade Máxima: {car['max_speed']}"
            label = Label(text=car_info, size_hint_y=None, height=100)
            layout.add_widget(label)

        scroll = ScrollView(size_hint=(1, None), size_hint_max_y=400)
        scroll.add_widget(layout)
        self.add_widget(scroll)

class RacingApp(App):
    def build(self):
        return CarList()

if __name__ == '__main__':
    RacingApp().run()