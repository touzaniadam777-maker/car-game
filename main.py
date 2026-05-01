from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class StoreApp(App):
    def build(self):
        self.money = 100
        self.inventory = {}

        self.store = {
            "تفاح": 5,
            "خبز": 3,
            "حليب": 7,
            "شوكولا": 10
        }

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.money_label = Label(text=f"💰 فلوسك: {self.money}", font_size=24)
        self.layout.add_widget(self.money_label)

        self.info_label = Label(text="مرحبا في متجرك!", font_size=18)
        self.layout.add_widget(self.info_label)

        # أزرار الشراء
        for item, price in self.store.items():
            btn = Button(text=f"شراء {item} ({price})", size_hint=(1, 0.2))
            btn.bind(on_press=self.buy_item)
            self.layout.add_widget(btn)

        # زر عرض المخزون
        inv_btn = Button(text="📦 عرض المخزون", size_hint=(1, 0.2))
        inv_btn.bind(on_press=self.show_inventory)
        self.layout.add_widget(inv_btn)

        return self.layout

    def buy_item(self, instance):
        text = instance.text.split(" ")
        item = text[1]

        price = self.store[item]

        if self.money >= price:
            self.money -= price
            self.inventory[item] = self.inventory.get(item, 0) + 1
            self.info_label.text = f"✅ اشتريت {item}"
        else:
            self.info_label.text = "❌ ما عندك فلوس"

        self.update_money()

    def show_inventory(self, instance):
        if not self.inventory:
            self.info_label.text = "📦 المخزون فارغ"
        else:
            items = ", ".join([f"{k} x{v}" for k, v in self.inventory.items()])
            self.info_label.text = f"📦 {items}"

    def update_money(self):
        self.money_label.text = f"💰 فلوسك: {self.money}"


if __name__ == "__main__":
    StoreApp().run()
