import tkinter as tk
from tkinter import ttk

cookies = 0
cookiesPerClick = 1
cookiesPerSecond = 0

upgrades = [
    {"name": "Cookie Baker", "cost": 100, "cps": 1, "cpc": 1, "count": 0},
    {"name": "Oven", "cost": 500, "cps": 5, "cpc": 2, "count": 0},
    {"name": "Bakery", "cost": 2000, "cps": 20, "cpc": 5, "count": 0},
    {"name": "Cookie Factory", "cost": 10000, "cps": 100, "cpc": 10, "count": 0},
    {"name": "Cookie Empire", "cost": 50000, "cps": 500, "cpc": 20, "count": 0}
]

def update_cookies():
    cookie_label.config(text=f"Cookies: {cookies}")
    cps_label.config(text=f"Cookies per second: {cookiesPerSecond}")
    cpc_label.config(text=f"Cookies per click: {cookiesPerClick}")
    update_buttons()

def update_buttons():
    """Enable or disable upgrade buttons based on current cookies."""
    for i, upgrade in enumerate(upgrades):
        if cookies >= upgrade["cost"]:
            upgrade_buttons[i].config(state=tk.NORMAL)
        else:
            upgrade_buttons[i].config(state=tk.DISABLED)

def click_cookie():
    global cookies
    cookies += cookiesPerClick
    update_cookies()

def buy_upgrade(index):
    global cookies, cookiesPerSecond, cookiesPerClick
    upgrade = upgrades[index]
    if cookies >= upgrade["cost"]:
        cookies -= upgrade["cost"]
        cookiesPerSecond += upgrade["cps"]
        cookiesPerClick += upgrade["cpc"]
        upgrade["count"] += 1
        # Increase cost for next purchase
        upgrade["cost"] = int(upgrade["cost"] * 1.15)
        update_cookies()
        update_shop()
    else:
        alert_label.config(text="Not enough cookies!", fg="red")
        root.after(2000, lambda: alert_label.config(text=""))  # Clear alert after 2s

def auto_cookie():
    global cookies
    cookies += cookiesPerSecond
    update_cookies()
    root.after(1000, auto_cookie)

root = tk.Tk()
root.title("Cookie Clicker")

notebook = ttk.Notebook(root)
clicker_tab = ttk.Frame(notebook)
shop_tab = ttk.Frame(notebook)
notebook.add(clicker_tab, text="Cookie Clicker")
notebook.add(shop_tab, text="Shop")
notebook.pack(expand=True, fill="both")

# Cookie Clicker Tab
cookie_button = tk.Button(clicker_tab, text="Click Cookie", command=click_cookie)
cookie_button.pack()

cookie_label = tk.Label(clicker_tab, text=f"Cookies: {cookies}")
cookie_label.pack()

cps_label = tk.Label(clicker_tab, text=f"Cookies per second: {cookiesPerSecond}")
cps_label.pack()

cpc_label = tk.Label(clicker_tab, text=f"Cookies per click: {cookiesPerClick}")
cpc_label.pack()

alert_label = tk.Label(clicker_tab, text="")
alert_label.pack()

# Shop Tab
shop_label = tk.Label(shop_tab, text="Shop - Buy upgrades to improve your cookie production!")
shop_label.pack()

upgrade_buttons = []
def update_shop():
    for widget in shop_tab.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()
    for i, upgrade in enumerate(upgrades):
        btn = tk.Button(shop_tab, text=f"{upgrade['name']} - Cost: {upgrade['cost']} cookies\nAdds {upgrade['cps']} CPS & {upgrade['cpc']} CPC",
                        command=lambda i=i: buy_upgrade(i))
        btn.pack()
        upgrade_buttons.append(btn)
    update_buttons()

update_shop()
root.after(1000, auto_cookie)
root.mainloop()
