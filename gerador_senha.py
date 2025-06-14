import tkinter as tk
from tkinter import messagebox, scrolledtext
import tldextract
import pyperclip

from tkinter import filedialog
from datetime import datetime

def gerar_senha():
    url = entrada_url.get().strip()

    if not url:
        messagebox.showwarning("Atenção", "Por favor, informe a URL ou nome do site.")
        return

    dominio = tldextract.extract(url).domain

    if not dominio:
        messagebox.showerror("Erro", "URL inválida! Tente novamente.")
        return

    senha = f"DECODE_bhdskf@{dominio.lower()}_041"

    resultado_senha.config(state="normal")
    resultado_senha.delete(0, tk.END)
    resultado_senha.insert(0, senha)
    resultado_senha.config(state="readonly")

    pyperclip.copy(senha)
    messagebox.showinfo("Senha Copiada", f"✅ Senha gerada e copiada:\n{senha}")

    # Adiciona no histórico
    historico_text.insert(tk.END, senha + '\n')
    historico_text.see(tk.END)  # Scroll automático

# == Limpar Histórico Antigo ==
#def limpar_historico():
#    historico_text.delete('1.0', tk.END)

# == Limpar Histórico ==
def limpa_historico():
    resposta = messagebox.askyesnocancel(
        "Confirmação",
        "Deseja salvar o histórico de senhas em um arquivo, antes de limpar?"
    )
    if resposta is None:
        # == cancelou a operação
        return
    elif resposta:
        # == gera o arquivo e salva antes de limpar
        # == pega o conteúdo do histórico
        conteudo = historico_text.get('1.0', tk.END).strip()
    if not conteudo:
        messagebox.showinfo("Aviso", "O histórico está vazio, nada a salvar.")
    else:
        # == abre o dialógo para escolher onde salvar
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt")],
            initialfile=f"historico_senhas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            title="Salvar Histórico como..."
        )
        if arquivo:
                try:
                    with open(arquivo, "w", encoding="utf-8") as f:
                        f.write(conteudo)
                    messagebox.showinfo("Sucesso", f"Histórico salvo em:\n{arquivo}")
                except  Exception as e:
                    messagebox.showerror("Erro", f"Falha ao salvar o arquivo:\n{e}")
                return # == Não limpa se falhar o salvamento
                historico_text.delete('1.0', tk.END)
        else:
        # == usuário não quer salvar, só limpa direto a informação
            historico_text.delete('1.0', tk.END)

# === Janela Principal ===
janela = tk.Tk()
janela.title("Gerador de Senhas Padrão DECODE")
janela.geometry("600x500")
janela.resizable(False, False)

# === Aplicação do Tema Dark ===
cor_fundo = "#121212"         # preto bem escuro
cor_texto = "#CCCCCC"         # cinza claro
cor_botao_bg = "#333333"      # cinza escuro botão normal
cor_botao_fg = "#FFFFFF"      # branco texto botão
cor_botao_gerar_bg = "#4CAF50" # verde botão gerar
cor_botao_limpar_bg = "#f44336" # vermelho botão limpar
cor_entrada_bg = "#1E1E1E"    # cinza escuro para entrada
cor_entrada_fg = "#FFFFFF"    # branco para texto entrada
cor_historico_bg = "#1E1E1E"  # cinza escuro para histórico
cor_historico_fg = "#FFFFFF" # branco para texto histórico

janela.configure(bg=cor_fundo)

# === Layout ===
titulo = tk.Label(
    janela, text="Gerador Automático de Senhas", font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

frame = tk.Frame(janela)
frame.pack(pady=5)

label_url = tk.Label(frame, text="URL ou nome do site:", font=("Arial", 12))
label_url.grid(row=0, column=0, padx=5, pady=5)

entrada_url = tk.Entry(frame, width=40, font=("Arial", 12))
entrada_url.grid(row=0, column=1, padx=5, pady=5)

btn_gerar = tk.Button(
    janela,
    text="Gerar Senha",
    command=gerar_senha,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    width=20,
)
btn_gerar.pack(pady=10)

label_resultado = tk.Label(janela, text="Senha Gerada:", font=("Arial", 12, "bold"))
label_resultado.pack()

resultado_senha = tk.Entry(
    janela, width=50, font=("Arial", 12), justify="center", state="readonly"
)
resultado_senha.pack(pady=5)

label_hist = tk.Label(
    janela, text="Histórico de Senhas Geradas:", font=("Arial", 12, "bold")
)
label_hist.pack(pady=10)

historico_text = scrolledtext.ScrolledText(
    janela, width=70, height=10, font=("Arial", 10)
)
historico_text.pack(pady=5)

btn_limpar = tk.Button(
    janela,
    text="Limpar Histórico",
    command=limpa_historico,
    font=("Arial", 10),
    bg="#f44336",
    fg="white",
    width=20,
)
btn_limpar.pack(pady=10)


# === Executa a Janela ===
janela.mainloop()
