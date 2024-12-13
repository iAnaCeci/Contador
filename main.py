import tkinter as tk


class ContadorApp:
    def __init__(self, root):
        self.valor = 0

        # Configuração da janela principal
        self.root = root
        self.root.iconbitmap("numeros.ico")
        self.root.title("Contador")

        # Label para exibir o valor (centralizado e ajustável)
        self.label = tk.Label(root, text="0", font=("Helvetica", 48))
        self.label.pack(pady=20, expand=True, fill="both")

        # Frame para os botões
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(side="bottom", fill="x")

        # Botões
        self.btn_incrementar = tk.Button(self.frame_botoes, text="Incrementar", command=self.incrementar, width=10)
        self.btn_incrementar.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        self.btn_decrementar = tk.Button(self.frame_botoes, text="Decrementar", command=self.decrementar, width=10)
        self.btn_decrementar.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        self.btn_zerar = tk.Button(self.frame_botoes, text="Zerar", command=self.zerar, width=10)
        self.btn_zerar.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def incrementar(self):
        self.valor += 1
        self.atualizar_label()

    def decrementar(self):
        self.valor -= 1
        self.atualizar_label()

    def zerar(self):
        self.valor = 0
        self.atualizar_label()

    def atualizar_label(self):
        self.label.config(text=str(self.valor))


# Inicializa a aplicação
root = tk.Tk()
app = ContadorApp(root)
root.mainloop()
