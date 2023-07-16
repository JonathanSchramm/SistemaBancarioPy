import tkinter as tk
from tkinter import messagebox

saldo_valor = 500
arquivo_dados = "dados.txt"

def carregar_dados():
    global saldo_valor
    try:
        with open(arquivo_dados, "r") as arquivo:
            saldo_valor = float(arquivo.read())
    except FileNotFoundError:
        salvar_dados()

def salvar_dados():
    global saldo_valor
    with open(arquivo_dados, "w") as arquivo:
        arquivo.write(str(saldo_valor))

def saldo():
    global saldo_valor

    Swindow = tk.Toplevel()
    Swindow.title("Saldo")
    Swindow.geometry("300x160")

    titulo_label1 = tk.Label(Swindow, text="Visualize aqui seu saldo!")
    titulo_label1.pack(pady=10,)

    titulo_label = tk.Label(Swindow, text=f"Seu saldo é de: {saldo_valor}")
    titulo_label.pack(pady=10,)

    saldo_button = tk.Button(Swindow, text="Voltar ao menu", command=lambda: (menu_principal(), Swindow.destroy()))
    saldo_button.pack(pady=5)
    saldo_button.config(width=20)

def sacar():
    global saldo_valor
    saque_valor = float(saque_entry.get())
    if saque_valor <= saldo_valor:
        saldo_valor -= saque_valor
        messagebox.showinfo("Saque", f"Saque no valor de: {saque_valor} realizado com sucesso!")
        opt = messagebox.askquestion("Novo Saldo", "Deseja ver seu novo saldo?")
        if opt == "yes":
            saldo()
        else:
            menu_principal()
    else:
        messagebox.showerror("Saldo Insuficiente", "Saldo insuficiente, digite um valor válido!")

def depositar():
    global saldo_valor
    deposito_valor = float(deposito_entry.get())
    saldo_valor += deposito_valor
    messagebox.showinfo("Depósito", f"Depósito no valor de: {deposito_valor} realizado com sucesso!")
    opt = messagebox.askquestion("Novo Saldo", "Deseja ver seu novo saldo?")
    if opt == "yes":
        saldo()
    else:
        menu_principal()
    salvar_dados()

def destroy():
    window = tk.Tk()
    window.withdraw()
    saldo()

def menu_principal():
    window = tk.Tk()
    window.title("Banco")
    window.geometry("300x300")

    titulo_label = tk.Label(window, text="Bem-vindo ao nosso banco!")
    titulo_label.pack(pady=10,)
    titulo_label.config(width=100)

    saldo_button = tk.Button(window, text="Saldo", command=lambda: (saldo(), window.destroy()))
    saldo_button.pack(pady=5)
    saldo_button.config(width=20)


    saque_button = tk.Button(window, text="Sacar", command=sacar)
    saque_button.pack(pady=5)
    saque_button.config(width=20)

    deposito_button = tk.Button(window, text="Depositar", command=depositar)
    deposito_button.pack(pady=5)
    deposito_button.config(width=20)

    sair_button = tk.Button(window, text="Sair", command=window.quit)
    sair_button.pack(pady=5)
    sair_button.config(width=20)

    window.mainloop()

carregar_dados()
menu_principal()
