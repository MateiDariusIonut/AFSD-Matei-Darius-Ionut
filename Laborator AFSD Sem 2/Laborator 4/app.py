import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import json
import os

# Functie care verifica daca numele produsului este format doar din litere mari/mici si spatii
def verify_product_name(entry_vals):

    product_name = entry_vals["product_name_entry"].get().strip()

    for char in product_name:
        if not (char.isalpha() or char.isspace()):
            return "Numele poate fi format doar din litere și spații!"
    return None

# Functie care verifica daca cantitatea produsului este un numar intreg
def verify_product_quantity(entry_vals):

    product_quantity = entry_vals["product_quantity_entry"].get().strip()

    for char in product_quantity:
        if not char.isdigit():
            return "Cantitatea trebuie să fie un număr întreg!"
    return None

# Functie care verifica daca pretul produsului este un numar intreg
def verify_product_price(entry_vals):

    product_price = entry_vals["product_price_entry"].get().strip()

    for char in product_price:
        if not char.isdigit():
            return "Prețul trebuie să fie un număr întreg!"
    return None

# Functie care goleste toate campurile pentru nume, cantitate si pret
def empty_entry(entry_vals):

    entry_vals["product_name_entry"].delete(0, tk.END)
    entry_vals["product_quantity_entry"].delete(0, tk.END)
    entry_vals["product_price_entry"].delete(0, tk.END)

# Functie care adauga un nou produs in fisierul stock.json daca acesta respecta formatul pentru nume/cantitate/pret
# in caz contrar afiseaza erorile corespunzatoare
def create(entry_vals):

    name = entry_vals["product_name_entry"].get().strip()
    quantity = entry_vals["product_quantity_entry"].get().strip()
    price = entry_vals["product_price_entry"].get().strip()

    error = verify_product_name(entry_vals)
    if error:
        msgbox.showerror("Eroare", error)
        return
    error = verify_product_quantity(entry_vals)
    if error:
        msgbox.showerror("Eroare", error)
        return
    error = verify_product_price(entry_vals)
    if error:
        msgbox.showerror("Eroare", error)
        return
    if not name or not quantity or not price:
        msgbox.showerror("Eroare", "Toate câmpurile trebuie completate.")
        return

    quantity = int(quantity)
    price = int(price)

    data = {}
    if os.path.exists("stock.json"):
        with open("stock.json", "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}

    if name in data:
        msgbox.showwarning("Atenție", f"Produsul '{name}' există deja!")
        return

    data[name] = {"cantitate": quantity, "pret": price}

    with open("stock.json", "w") as f:
        json.dump(data, f, indent=4)

    msgbox.showinfo("Succes", f"Produsul '{name}' a fost adăugat cu succes!")

# Functie care afiseaza stocul conform fisierului stock.json, iar daca acesta este gol afiseaza eroare
def read(entry_vals):

    products_tree = entry_vals["products_tree"]

    for item in products_tree.get_children():
        products_tree.delete(item)

    if os.path.exists("stock.json"):
        with open("stock.json", "r") as f:
            try:
                data = json.load(f)
                if data == {}:
                    msgbox.showwarning("Atenție", "Nu există nimic în stoc!")
                    return
                for product_name, product_info in data.items():
                    products_tree.insert("", "end", values=(product_name, product_info["cantitate"], product_info["pret"]))
            except:
                msgbox.showwarning("Atenție", "Nu există nimic în stoc!")
                return

# Functie care actualizeaza produsul dorit de catre utilizator cu noi informatii, iar daca nu sunt respectate conditiile impuse
# afiseaza erorile aferente
def update(entry_vals):

    name = entry_vals["product_name_entry"].get().strip()
    quantity = entry_vals["product_quantity_entry"].get().strip()
    price = entry_vals["product_price_entry"].get().strip()

    data = {}
    if os.path.exists("stock.json"):
        with open("stock.json", "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}

    if not name:
        msgbox.showerror("Eroare", "Introduceți numele produsului pentru actualizare!")
        return

    if name not in data:
        msgbox.showwarning("Produs inexistent", f"Produsul '{name}' nu există în stoc!")
        return

    if quantity:
        if not quantity.isdigit():
            msgbox.showerror("Eroare", "Cantitatea trebuie să fie un număr întreg!")
            return
        quantity = int(quantity)
        data[name]["cantitate"] = quantity

    if price:
        if not price.isdigit():
            msgbox.showerror("Eroare", "Prețul trebuie să fie un număr întreg!")
            return
        price = int(price)
        data[name]["pret"] = price

    with open("stock.json", "w") as f:
        json.dump(data, f, indent=4)

    msgbox.showinfo("Actualizare", f"Produsul '{name}' a fost actualizat cu succes!")

# Functie care sterge produsul dorit de catre utilizator, iar daca nu sunt respectate conditiile impuse
# afiseaza erorile aferente
def delete(entry_vals):

    name = entry_vals["product_name_entry"].get().strip()

    data = {}
    if os.path.exists("stock.json"):
        with open("stock.json", "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}

    if not name:
        msgbox.showerror("Eroare", "Introduceți numele produsului pentru ștergere!")
        return

    if name not in data:
        msgbox.showwarning("Produs inexistent", f"Produsul '{name}' nu există în stoc!")
        return

    confirm = msgbox.askyesno("Confirmare ștergere", f"Sunteți sigur că doriți să ștergeți produsul '{name}' din stoc?")
    if not confirm:
        return
    else:
        data.pop(name, None)

    with open("stock.json", "w") as f:
        json.dump(data, f, indent=4)

    msgbox.showinfo("Ștergere", f"Produsul '{name}' a fost șters cu succes!")

# Functie care contine toate widget-urile si configuratia acestora folosite pentru interfata
def gui():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Gestionare inventar")

    frame1 = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    frame1.grid(row=0, column=0, padx=20, pady=20)
    create_button = ttk.Button(frame1, text="Creare", command=lambda: create(entry_vals))
    create_button.grid(row=0, column=0, pady=(10,0))
    read_button = ttk.Button(frame1, text="Citire", command=lambda: read(entry_vals))
    read_button.grid(row=1, column=0)
    update_button = ttk.Button(frame1, text="Actualizare", command=lambda: update(entry_vals))
    update_button.grid(row=2, column=0)
    delete_button = ttk.Button(frame1, text="Ștergere", command=lambda: delete(entry_vals))
    delete_button.grid(row=3, column=0)
    products_stoc_label = tk.Label(frame1, text="Stoc produse:")
    products_stoc_label.grid(row=4, column=0)

    columns = ("produs", "cantitate", "pret")
    products_tree = ttk.Treeview(frame1, columns=columns, show="headings", height=5)
    products_tree.grid(row=5, column=0, padx=10, pady=(0, 10))
    products_tree.heading("produs", text="Produs")
    products_tree.heading("cantitate", text="Cantitate")
    products_tree.heading("pret", text="Preț (RON)")
    products_tree.column("produs", anchor="w", width=200)
    products_tree.column("cantitate", anchor="center", width=80)
    products_tree.column("pret", anchor="center", width=80)

    frame2 = tk.Frame(root, highlightbackground="black", highlightthickness=1)
    frame2.grid(row=0, column=1, padx=20, pady=20)
    create_edit_label = tk.Label(frame2, text="Informații Adăugare/Editare/Ștergere")
    create_edit_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,0))
    product_name_label = tk.Label(frame2, text="Produs:")
    product_name_label.grid(row=1, column=0, pady=5, sticky="e")
    product_quantity_label = tk.Label(frame2, text="Cantitate:")
    product_quantity_label.grid(row=2, column=0, pady=5, sticky="e")
    product_price_label = tk.Label(frame2, text="Preț:")
    product_price_label.grid(row=3, column=0, pady=5, sticky="e")
    product_name_entry = ttk.Entry(frame2, width=20)
    product_name_entry.grid(row=1, column=1, sticky="w")
    product_quantity_entry = ttk.Entry(frame2, width=10)
    product_quantity_entry.grid(row=2, column=1, sticky="w")
    product_price_entry = ttk.Entry(frame2, width=10)
    product_price_entry.grid(row=3, column=1, sticky="w")
    reset_button = ttk.Button(frame2, text="Golire", command=lambda: empty_entry(entry_vals))
    reset_button.grid(row=4, column=0, columnspan=2, pady=10)

    entry_vals = {
        "product_name_entry": product_name_entry,
        "product_quantity_entry": product_quantity_entry,
        "product_price_entry": product_price_entry,
        "products_tree": products_tree,
    }

    root.mainloop()

if __name__ == "__main__":
    gui()