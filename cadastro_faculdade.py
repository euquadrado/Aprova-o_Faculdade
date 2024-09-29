import tkinter as tk
from tkinter import messagebox

cursos_por_campus = {
    "São Paulo": {
        "Engenharia da Computação": 700,
        "Ciência da Computação": 680,
        "Direito": 650
    },
    "Ribeirão": {
        "Administração": 600,
        "Engenharia Civil": 660,
        "Arquitetura": 640
    },
    "Americana": {
        "Medicina": 760,
        "Enfermagem": 620,
        "Biomedicina": 630
    },
    "Campinas": {
        "Engenharia de Software": 680,
        "Sistemas de Informação": 670,
        "Gestão de TI": 620
    }
}

def atualizar_cursos(*args):
    campus_selecionado = campus_var.get()
    cursos_menu['menu'].delete(0, 'end')
    if campus_selecionado in cursos_por_campus:
        for curso in cursos_por_campus[campus_selecionado]:
            cursos_menu['menu'].add_command(label=curso, command=tk._setit(curso_var, curso))
        curso_var.set(list(cursos_por_campus[campus_selecionado].keys())[0])

def verificar_aprovacao():
    nome = entry_nome.get()
    try:
        nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma nota válida.")
        return

    curso = curso_var.get()
    campus = campus_var.get()

    if not nome or not nota or not curso or not campus:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    nota_de_corte = cursos_por_campus[campus][curso]

    if nota >= nota_de_corte:
        messagebox.showinfo("Aprovado", f"Parabéns, {nome}! Você foi aprovado no curso de {curso} no campus de {campus}.")
    else:
        sugestoes = [outro_curso for outro_curso, corte in cursos_por_campus[campus].items() if outro_curso != curso and nota >= corte]
        if sugestoes:
            sugestao_texto = "\n".join(sugestoes)
            messagebox.showinfo("Reprovado", f"Infelizmente, você não tem nota suficiente para {curso}. Mas você pode se inscrever nos seguintes cursos:\n{sugestao_texto}")
        else:
            messagebox.showinfo("Reprovado", f"Infelizmente, sua nota não é suficiente para {curso} e nenhum outro curso no campus de {campus}.")

root = tk.Tk()
root.title("Tela de Cadastro da Faculdade")
root.geometry("400x500")

label_nome = tk.Label(root, text="Nome Completo:")
label_nome.pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_nota = tk.Label(root, text="Nota do Vestibular:")
label_nota.pack(pady=5)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

label_campus = tk.Label(root, text="Selecione o Campus:")
label_campus.pack(pady=5)

campus_var = tk.StringVar()
campus_var.set("Selecione")

campus_opcoes = ["São Paulo", "Ribeirão", "Americana", "Campinas"]
campus_menu = tk.OptionMenu(root, campus_var, *campus_opcoes, command=atualizar_cursos)
campus_menu.pack(pady=5)

label_curso = tk.Label(root, text="Selecione o Curso:")
label_curso.pack(pady=5)

curso_var = tk.StringVar()
curso_var.set("Escolha um campus")

cursos_menu = tk.OptionMenu(root, curso_var, "")
cursos_menu.pack(pady=5)

botao_verificar = tk.Button(root, text="Verificar Aprovação", command=verificar_aprovacao)
botao_verificar.pack(pady=20)

root.mainloop()
