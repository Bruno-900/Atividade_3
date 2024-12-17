import os
import tkinter as tk
from tkinter import messagebox, Label
import json

Lista = []

# Funções
def adicionar_tarefas():
    nova_tarefa = entry.get()
    if nova_tarefa:
        Lista.append({"tarefa": nova_tarefa, "concluida": False})
        entry.delete(0, tk.END)
        atualizar_lista()

def editar_tarefas():
    selecionado = listbox.curselection()
    if selecionado:
        indice = selecionado[0]
        nova_descricao = entry.get()
        if nova_descricao:
            Lista[indice]["tarefa"] = nova_descricao
            entry.delete(0, tk.END)
            atualizar_lista()

def excluir_tarefas():
    selecionado = listbox.curselection()
    if selecionado:
        indice = selecionado[0]
        Lista.pop(indice)
        atualizar_lista()

def marcar_concluida_tarefas():
    selecionado = listbox.curselection()
    if selecionado:
        indice = selecionado[0]
        Lista[indice]["concluida"] = True
        atualizar_lista()

def atualizar_lista():
    listbox.delete(0, tk.END)
    for tarefa in Lista:
        status = "Concluída" if tarefa["concluida"] else "Não Concluída"
        listbox.insert(tk.END, f"{tarefa['tarefa']} - {status}")

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo:
        json.dump(Lista, arquivo)

def carregar_tarefas():
    global Lista
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            Lista = json.load(arquivo)
        atualizar_lista()

# Janela principal
janela = tk.Tk() 
janela.title("Gerenciador de Tarefas") 
janela.geometry("400x600")

# Widgets de entrada e listbox
entry = tk.Entry(janela, width=170)
entry.place(x=360, y=100)

label_tarefa = Label(janela, text="Tarefa:") 
label_tarefa.place(x=300, y=100)

#caixa de tarefas
listbox = tk.Listbox(janela, width=180, height=23)
listbox.place(x=300, y=150)

# Botões com comandos corretos
botao_adicionar = tk.Button(janela, text="Adicionar", width=20, command=adicionar_tarefas)
botao_adicionar.place(x=20, y=100)

botao_editar = tk.Button(janela, text="Editar", width=20, command=editar_tarefas)
botao_editar.place(x=20, y=200)

botao_excluir = tk.Button(janela, text="Excluir", width=20, command=excluir_tarefas)
botao_excluir.place(x=20, y=300)

botao_marcar = tk.Button(janela, text="Marcar Concluída", width=20, command=marcar_concluida_tarefas)
botao_marcar.place(x=20, y=400)

botao_fechar = tk.Button(janela, text="SAIR", command=janela.destroy, width=20)
botao_fechar.place(x=20, y=500)

# Carregar tarefas ao iniciar
carregar_tarefas()

# Iniciar o loop principal
janela.mainloop()