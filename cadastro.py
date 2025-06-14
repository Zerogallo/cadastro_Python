import tkinter as tk
from tkinter import messagebox



class AppLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("300x300")
        
        # Dados fictícios (substitua por um banco de dados)
        self.usuarios = {"admin": "123456"}
        
        self.criar_tela_login()
        

    def criar_tela_login(self):
        self.limpar_tela()
        
        tk.Label(self.root, text="Usuário:").pack(pady=5)
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack(pady=5)
        
        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack(pady=5)
        
        tk.Button(self.root, text="Login", command=self.verificar_login).pack(pady=10)
        tk.Button(self.root, text="Cadastrar", command=self.criar_tela_cadastro).pack(pady=5)

    def criar_tela_cadastro(self):
        self.limpar_tela()
        
        tk.Label(self.root, text="Novo Usuário:").pack(pady=5)
        self.entry_novo_usuario = tk.Entry(self.root)
        self.entry_novo_usuario.pack(pady=5)
        
        tk.Label(self.root, text="Nova Senha:").pack(pady=5)
        self.entry_nova_senha = tk.Entry(self.root, show="*")
        self.entry_nova_senha.pack(pady=5)
        
        tk.Label(self.root, text="Confirmar Senha:").pack(pady=5)
        self.entry_confirma_senha = tk.Entry(self.root, show="*")
        self.entry_confirma_senha.pack(pady=5)
        
        tk.Button(self.root, text="Salvar", command=self.salvar_cadastro).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.criar_tela_login).pack(pady=5)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if usuario in self.usuarios and self.usuarios[usuario] == senha:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def salvar_cadastro(self):
        novo_usuario = self.entry_novo_usuario.get()
        nova_senha = self.entry_nova_senha.get()
        confirma_senha = self.entry_confirma_senha.get()
        
        if nova_senha != confirma_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
        elif novo_usuario in self.usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
        else:
            self.usuarios[novo_usuario] = nova_senha
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.criar_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Configuração para Windows
if __name__ == "__main__":
    root = tk.Tk()
    app = AppLogin(root)
    root.mainloop()