import requests
import tkinter as tk
from tkinter import ttk

def get_exchange_rates(api_key):
    url = f"http://data.fixer.io/api/latest?access_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['rates']
    else:
        print("Error:", response.status_code)
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    return amount * (rates[to_currency] / rates[from_currency])

def on_convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        result = convert_currency(amount, from_currency, to_currency, rates)
        result_label.config(text=f"תוצאה: {result:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="אנא הזן סכום תקין.")

api_key = "20f0ca845931db98df9ac1d190806979"
rates = get_exchange_rates(api_key)

window = tk.Tk()
window.title("ממיר מטבעות")
window.geometry("350x250")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 12), background="#4a7ab7", foreground="white")
style.configure("TEntry", font=("Helvetica", 14), background="white")
style.configure("TMenubutton", font=("Helvetica", 12))

window.configure(background="#f0f0f0")

ttk.Label(window, text="סכום:", background="#f0f0f0").pack(pady=5)
amount_entry = ttk.Entry(window)
amount_entry.pack()

ttk.Label(window, text="ממטבע:", background="#f0f0f0").pack(pady=5)
from_currency_var = tk.StringVar(window)
from_currency_var.set("USD")
from_currency_menu = ttk.OptionMenu(window, from_currency_var, "USD", *rates.keys())
from_currency_menu.pack()

ttk.Label(window, text="למטבע:", background="#f0f0f0").pack(pady=5)
to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR")
to_currency_menu = ttk.OptionMenu(window, to_currency_var, "EUR", *rates.keys())
to_currency_menu.pack()

convert_button = ttk.Button(window, text="המר", command=on_convert)
convert_button.pack(pady=10)

result_label = ttk.Label(window, text="תוצאה: ", background="#f0f0f0")
result_label.pack()

window.mainloop()
