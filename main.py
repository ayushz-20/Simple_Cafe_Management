import tkinter as tk
from tkinter import messagebox

class CafeApp:
    def __init__(self, root):
        self.menu = {
            'Pizza': 40,
            'Pasta': 50,
            'Burger': 60,
            'Sandwich': 70,
            'Salad': 80,
            'Coffee': 90,
            'Tea': 100,
            'Juice': 110,
            'Water': 20,
        }
        self.order_total = 0

        self.root = root
        self.root.title("Ayush's Cafe")

        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Ayush's Cafe", font=('Helvetica', 16, 'bold')).pack(pady=10)

        menu_text = self.get_menu_text()
        tk.Label(self.root, text=menu_text, justify=tk.LEFT, font=('Helvetica', 12)).pack(pady=10)

        self.item_entry_label = tk.Label(self.root, text="Enter the item you want to order:")
        self.item_entry_label.pack(pady=5)
        
        self.item_entry = tk.Entry(self.root)
        self.item_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add to Order", command=self.add_to_order)
        self.add_button.pack(pady=5)

        self.another_order_label = tk.Label(self.root, text="Say Yes To Get the Total Amount? (Yes):")
        self.another_order_label.pack(pady=5)

        self.another_order_entry = tk.Entry(self.root)
        self.another_order_entry.pack(pady=5)
        
        self.check_button = tk.Button(self.root, text="Check Order", command=self.check_another_order)
        self.check_button.pack(pady=5)
        
        self.total_label = tk.Label(self.root, text="The total amount for your order is: Rs0", font=('Helvetica', 12, 'bold'))
        self.total_label.pack(pady=10)

    def get_menu_text(self):
        return "\n".join([f"{item}: Rs{price}" for item, price in self.menu.items()])

    def add_to_order(self):
        item = self.item_entry.get().capitalize()
        if item in self.menu:
            self.order_total += self.menu[item]
            messagebox.showinfo("Order Update", f"Your item '{item}' has been added to your order.")
        else:
            messagebox.showwarning("Order Update", f"Ordered item '{item}' is not available yet!!")
        self.item_entry.delete(0, tk.END)

    def check_another_order(self):
        another_order = self.another_order_entry.get().lower()
        if another_order == "yes":
            self.item_entry_label.config(text="Enter the next item you want to order:")
        else:
            self.total_label.config(text=f"The total amount for your order is: Rs{self.order_total}")
            self.disable_ordering()
        self.another_order_entry.delete(0, tk.END)

    def disable_ordering(self):
        self.item_entry.config(state=tk.DISABLED)
        self.add_button.config(state=tk.DISABLED)
        self.another_order_entry.config(state=tk.DISABLED)
        self.check_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeApp(root)
    root.mainloop()
