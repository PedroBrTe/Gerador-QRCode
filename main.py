import ttkbootstrap as ttk
import commands


def criar_qrcode():
    commands.criar_qrcode(entry_link.get())


janela = ttk.Window()
janela.title('Criar QRCode')

label_titulo = ttk.Label(bootstyle='inverse-primary', text=f"{' ' * 65}Criar QRCode customizado", borderwidth=8)
label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_link = ttk.Label(text="Selecione o texto que deseja usar no QRCode")
label_link.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

entry_link = ttk.Entry(bootstyle='secondary')
entry_link.grid(row=1, column=2, padx=20, pady=10, sticky='nswe')

label_image = ttk.Label(text="Selecione a imagem que deseja usar no QRCode (opcional)")
label_image.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

botao_imagem = ttk.Button(bootstyle='secondary', text="Selecione o Arquivo", command=commands.selecionar_arquivo)
botao_imagem.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

try:
    botao_confirmar = ttk.Button(bootstyle='info', text="Confirmar", command=criar_qrcode)
    botao_confirmar.grid(row=3, column=1, padx=10, pady=10, sticky='nswe')
except NameError as ne:
    label_error = ttk.Label(bootstyle='warning', text=ne)

if __name__ == '__main__':
    janela.mainloop()
