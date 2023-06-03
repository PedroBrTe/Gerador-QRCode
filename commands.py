from tkinter.filedialog import askopenfilename
import ttkbootstrap as ttk
from PIL import Image
import qrcode
from tkinter.messagebox import askyesno


def selecionar_arquivo():
    global botao_imagem
    global caminho_arquivo

    caminho_arquivo = askopenfilename(title="Selecione o Arquivo de Moeda")
    if caminho_arquivo:
        nome_arquivo = caminho_arquivo.split('/')[-1]
        botao_imagem = ttk.Button(bootstyle='success', text=f"{nome_arquivo}", command=selecionar_arquivo)
        botao_imagem.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')


def criar_qrcode(link: str):
    nome_arquivo = link.replace(' ', '_')
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(link)
        qrcode_image = qr.make_image(fill_color='black', back_color='white')

        logo = Image.open(caminho_arquivo)
        logo = logo.resize((80, 80))
        largura_imagem, altura_imagem = logo.size
        largura_qr, altura_qr = qrcode_image.size
        posicao_x = int((largura_qr - largura_imagem) / 2)
        posicao_y = int((altura_qr - altura_imagem) / 2)

        qrcode_image.paste(logo, (posicao_x, posicao_y))
        arquivo = f"{nome_arquivo}.png"
        qrcode_image.save(arquivo)
        img = Image.open(arquivo)
        img.show()
    except:
        print(link)
        qr = qrcode.QRCode(version=1, box_size=6, border=4)
        qr.add_data(link)
        qrcode_image = qr.make_image(fill_color='black', back_color='white')
        resposta = askyesno(title='Confirmação', message='Certeza que deseja criar o qrcode?')
        if resposta:
            arquivo = f"{nome_arquivo}.png"
            qrcode_image.save(arquivo)
            img = Image.open(arquivo)
            img.show()

        else:
            pass
