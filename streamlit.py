import streamlit as st
import pandas as pd
import time as t
from datetime import time
from matplotlib import pyplot as plt
import numpy as np
# streamlit run streamlit.py
x=np.linspace(0, 10, 100)
bar_x=np.array([1, 2, 3, 4, 5])
st.markdown("<h1 style='text-align: center;'>Streamlit</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("# Text sizes")
st.title("Title - Text sizes")
st.header("Header - Why use different text sizes?")
st.markdown("")
st.subheader("Subheader - 1. Looks clean")
st.markdown("")
st.text("Text - If you want to make you writing cooler and more appealing")
st.markdown("---")
st.markdown("# Markdowns")
st.markdown("*****Hello*****, I'm ***a*** *****************MARKDOWN!*****************, *****I***** *can* ********change******** ***Size***")
st.markdown("### WAIT, Don't forget me!!, I'm also a markdown, I can change size too but it's in a different way than you")
st.markdown("> Hey, I am also markdown")
st.markdown("[DSL Website](https://dsl10git.github.io/) Can you belive I'm a markdown!")
st.markdown("↓↓↓↓↓↓↓ **I'm acctally a markdown** ↓↓↓↓↓↓↓")
st.markdown("---")
st.markdown("# Math symbols")
st.latex(r'f(\relax{x}) = \int_{-\infty}^\infty f(\hat\xi\,e^{2 \pi i \xi x}\,)d\xi')
st.latex(r"""
\int_{\Gamma^+[-R,R]} f(z) e^{-2\pi i \xi z} \,dz =
\int_{-R}^{R} f(x) e^{-2\pi i \xi x} \,dx +
\int_{\Gamma} f(z) e^{-2\pi i \xi z} \,dz = 0
""")
st.caption("Hi, I'm this website's captions!")
st.markdown("---")
st.markdown("# Code")
json = {"welcomle message":"Hi, I'm a json file!", "Creator":"DSL", "date":"Unknown", "user":"Unknown", "creator_info":"Go to dsl10git.github.io to learn about me!"}
st.json(json)
st.markdown("Run this code on IDLE, VS code, and ect. Game: Cookie clicker | if you want the better version, go to dsl10git.github.io")
code="""
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


"""
st.code(code, language="python")
st.markdown("---")
st.markdown("# Some cool stuff")
st.write("# I'm like HTML")
st.write("## I'm like HTML")
st.write("### I'm like HTML")
st.write("#### I'm like HTML")
st.write("##### and so on...")
st.markdown("")
st.metric(label="Wind Speed(Go to dsl10git.github.io project weather app for the true weather and more!)", value="103ms⁻¹", delta="1.4ms⁻¹")
st.metric(label="Wind Speed(Go to dsl10git.github.io project weather app for the true weather and more!)", value="120ms⁻¹", delta="-1.4ms⁻¹")
table = pd.DataFrame(
    {
        "Column 1": [1, 2, 3, 4, 5, 6, 7],
        "Column 2": [11, 12, 13, 14, 15, 16, 17]
}
)
st.table(table)
st.dataframe(table)
st.markdown("---")
st.markdown("# Media Widgets")
st.image("simple_calculator.webp", caption="The calculator project", width=680)
st.markdown("")
st.audio("audio.mp3")
st.markdown("#### I'm smelly DAD")
st.markdown("")
st.video("cat.mp4")
st.markdown("#### Meow Meow CAT")
st.markdown("---")
st.markdown("# Interactive widgets")
state = st.checkbox("Checkbox", value=True)
if state:
    st.write("Hello user")
else:
    st.write("Bye user")
st.markdown("")
def change():
    print(st.session_state.checker)
state2 = st.checkbox("Checkbox2", value=True, on_change=change, key="checker")
if state2:
    st.write("Terminal - True")
else:
    st.write("Terminal - False")
st.markdown("")
radio_btn=st.radio("In which country do you live?", options=("US", "UK", "Canda", "China","South Korea", "Russia","Europe", "more"))
st.markdown("")
def btn_click():
    st.write("+1 Gold coin")
btn = st.button("Click ME!", on_click=btn_click)
select = st.selectbox("what is your favorite car?", options=("Audi", "BMW", "Ferreri", "Tesla", "lamborghini", "other"))
multi_select = st.multiselect("what is you favorite Tech Brand?", options=("Amazon", "Apple", "Adobe", "IBM", "Microsoft", "Nvidia", "Salesforce", "SAP", "Other"))
st.write(multi_select)
st.markdown("# Uploading files")
st.markdown("---")
image = st.file_uploader("Please a upload a image", type=["jpeg", "png", "tiff", "webp"])
if image is not None:
    for image in image:
        st.image(image)
video = st.file_uploader("Please a upload a video", type="mpv4")
if video is not None:
    st.video(video)
val = st.slider("I'm this website's slider!", min_value=50, max_value=150, value=70, )
print(val)
val2 = st.text_input("Enter your farvorite video", max_chars=100)
print(val2)
val3 = st.text_area("Favorite video description")
print(val3)
val4 = st.date_input("Enter today's Date")
print(val4)
val5 = st.time_input("Set timer")
print(val5)
st.markdown("---")
st.markdown("# Timer")
val6=st.time_input("Set timer", value=time(0, 0, 0))
def converter(value):
    m, s, mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s
if str(val6) == "00:00:00":
    st.write("Please set timer")
else:
    print(val6)
    sec=converter(str(val6))
    st.write("Preforming other function")
    vally = st.text_input("say perentage?(y/n)", max_chars=1)
    if vally == "n":
        per=sec/100
        bar=st.progress(0)
        for i in range(100):
            bar.progress(i+1)
            t.sleep(per)
    else:
        per=sec/100
        bar=st.progress(0)
        progress_status = st.empty()
        for i in range(100):
            bar.progress(i+1)
            progress_status.write(str(i+1)+"%")
            t.sleep(per)
    st.write("Done!")
st.markdown("---")
st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 2", clear_on_submit=True):
    col1, col2, col3=st.columns(3)
    f_name=col1.text_input("First name")
    m_name=col2.text_input("Middle name")
    l_name=col3.text_input("Last name")
    st.text_input("Email Address")
    col4, col5=st.columns(2)
    col4.text_input("Password password")
    col5.text_input("Comfirm password")
    day, month, year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and m_name == "" and l_name == "":
            st.warning("Please fill above the fields")
        else:
            st.success("Submitted Sucessfully")
st.markdown("# Sidebar & Graphs")
st.sidebar.write("# Sidebar & Graphs")
st.sidebar.write("Hello I'm this website's side bar")
opt = st.sidebar.radio("Select Any graph", options=("Line", "Bar", "H-bar"))
if opt=="Line":
    st.markdown("## Line chart")
    fig=plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/refs/heads/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    st.write(fig)
elif opt=="Bar":
    st.markdown("## Bar chart")
    fig=plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/refs/heads/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown("## H-Bar chart")
    fig=plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/refs/heads/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)