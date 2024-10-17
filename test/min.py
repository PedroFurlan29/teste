import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label  # Importing Label

class TuningMenu(BoxLayout):
    def _init_(self, **kwargs):
        super(TuningMenu, self)._init_(**kwargs)
        self.orientation = 'vertical'

        self.title_label = Label(text='Tuning Menu', font_size=30, font_name='Arial')
        self.add_widget(self.title_label)

        self.button_grid = GridLayout(cols=2, spacing=10, padding=20)
        self.add_widget(self.button_grid)

        self.stage1_button = Button(text='Stage 1: Filtro de ar Sport', font_size=18, size_hint=(0.4, 0.2))
        self.stage1_button.bind(on_press=self.stage1_selected)
        self.button_grid.add_widget(self.stage1_button)

        self.stage2_button = Button(text='Stage 2: Filtro de ar + Escape Sport', font_size=18, size_hint=(0.4, 0.2))
        self.stage2_button.bind(on_press=self.stage2_selected)
        self.button_grid.add_widget(self.stage2_button)

        self.stage3_button = Button(text='Stage 3: Filtro de ar + Escape Sport + Turbo', font_size=18, size_hint=(0.4, 0.2))
        self.stage3_button.bind(on_press=self.stage3_selected)
        self.button_grid.add_widget(self.stage3_button)

        self.stage4_button = Button(text='Stage 4: Eixo de comando + Pistões + Anteriores', font_size=18, size_hint=(0.4, 0.2))
        self.stage4_button.bind(on_press=self.stage4_selected)
        self.button_grid.add_widget(self.stage4_button)

        # Label para exibir o aumento de potência
        self.power_label = Label(text='', font_size=20)
        self.add_widget(self.power_label)

        # Label para exibir o valor do tuning
        self.valor_label = Label(text='', font_size=20)
        self.add_widget(self.valor_label)

    def stage1_selected(self, instance):
        self.valor_label.text = 'Valor para a instalação: R$ 1.000,00'
        self.power_label.text = 'Potência incrementada: 30 CV' 
        print('Stage 1 selected: Filtro de ar Sport')

    def stage2_selected(self, instance):
        self.valor_label.text = 'Valor para a instalação: R$ 7.000,00'
        self.power_label.text = 'Potência incrementada: 50 CV'
        print('Stage 2 selected: Filtro de ar + Escape Sport')

    def stage3_selected(self, instance):
        self.valor_label.text = 'Valor para a instalação: R$ 15.000,00'
        self.power_label.text = 'Potência incrementada: 100 CV'
        print('Stage 3 selected: Filtro de ar + Escape Sport + Turbo')

    def stage4_selected(self, instance):
        self.valor_label.text = 'Valor para a instalação: R$ 25.000,00'
        self.power_label.text = 'Potência incrementada: 180 CV'
        print('Stage 4 selected: Eixo de comando + Pistões + Anteriores')

class MeuApp(App):
    def build(self):
        return TuningMenu()

if __name__ == "__main__":
    MeuApp().run()