import os

# Função da Cifra de César
def caesar_cipher(text, shift):
    result = ""

    # Loop para cada letra no texto
    for i in range(len(text)):
        char = text[i]

        # Verifica se é uma letra maiúscula
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Verifica se é uma letra minúscula
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


# Usar o Zenity para pegar a entrada do usuário
text = os.popen('zenity --entry --title="Cifra de César" --text="Digite o texto para cifrar:\n Vamos codificar sua mensagem!" --width=400 --height=200').read().strip()

# Usar o Zenity para pegar o valor do deslocamento
shift = os.popen('zenity --entry --title="Cifra de César" --text="Digite o valor de deslocamento (número):" --width=400 --height=200').read().strip()

# Verificar se o valor de deslocamento é um número
if shift.isdigit():
    shift = int(shift)
    # Cifrar o texto e mostrar o resultado com Zenity
    encrypted_text = caesar_cipher(text, shift)
    os.popen(f'zenity --info --title="Texto Cifrado" --text="Texto Cifrado: {encrypted_text}" --width=400 --height=200')
else:
    os.popen('zenity --error --text="Erro: O valor de deslocamento deve ser um número." --width=400 --height=200')