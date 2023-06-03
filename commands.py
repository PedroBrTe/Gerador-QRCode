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
        logo = Image.open(caminho_arquivo)
        largura = 100

        lporcent = (largura/float(logo.size[0]))
        altura = int((float(logo.size[1])*float(lporcent)))

        logo = logo.resize((largura, altura), Image.ANTIALIAS)
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

        qr.add_data(link)
        qr.make()

        qrcode_image = qr.make_image(fill_color='black', back_color='white').convert('RGB')
        pos = ((qrcode_image.size[0] - logo.size[0]) // 2,
               (qrcode_image.size[1] - logo.size[1]) // 2)

        qrcode_image.paste(logo, pos)
        resposta = askyesno(title='Confirmação', message='Certeza que deseja criar o qrcode?')
        if resposta:
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
