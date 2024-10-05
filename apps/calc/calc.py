
"""
This module defines a simple calculator application using the Flet framework.
Functions:
    main(page: ft.Page):
        The main function that sets up the calculator UI and handles button click events.
        Args:
            page (ft.Page): The page object provided by Flet to build the UI.
        The function performs the following tasks:
            - Sets the title of the page to "Calculadora".
            - Configures the initial window size and centers it on the screen.
            - Sets the background color, padding, spacing, and vertical alignment of the page.
            - Defines the output field for displaying the result.
            - Defines the text style for the buttons.
            - Handles button click events to perform calculations or reset the output.
            - Creates and styles the calculator buttons, including numbers and operators.
            - Adds all components to the page.
"""
import flet as ft
from flet import TextStyle

def main(page: ft.Page):
    page.title = "Calculadora do Flet"
    
    # Tamanho da janela ao abrir
    page.window_width = 340
    page.window_height = 540
    # Centralizar a janela na tela
    page.window_center()
    
    page.bgcolor = ft.colors.BLACK  # Cor de fundo preta
    page.padding = 20
    page.spacing = 10
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Definir campo de saída (alinhado à direita)
    output = ft.Text(value="0", size=40, color="white", text_align="right")

    # Definir estilo de texto para os botões
    button_text_style = TextStyle(size=20, weight="bold")

    # Função para lidar com o clique dos botões
    def botao_click(e):
        if e.control.data == "=":
            try:
                output.value = str(eval(output.value))
            except:
                output.value = "Erro"
        elif e.control.data == "AC":
            output.value = "0"
        else:
            if output.value == "0":
                output.value = e.control.data
            else:
                output.value += e.control.data
        page.update()

    # Botões da calculadora
    botoes = [
        ["AC", "+/-", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
    ]

    # Cores para operadores e números
    cor_num = ft.colors.GREY
    cor_op = ft.colors.ORANGE

    grid = []
    for linha in botoes:
        linha_botoes = []
        for b in linha:
            # Determinar cor do botão
            cor_botao = cor_op if b in ["/", "*", "-", "+", "="] else cor_num
            botao = ft.ElevatedButton(
                text=b, 
                on_click=botao_click, 
                data=b,
                style=ft.ButtonStyle(text_style=button_text_style),
                bgcolor=cor_botao,
                color="white",
                width=70,
                height=70
            )
            linha_botoes.append(botao)
        grid.append(ft.Row(linha_botoes, alignment=ft.MainAxisAlignment.CENTER))

    # Linha final com botão 0 e botão =
    linha_final = [
        ft.ElevatedButton(text="0", on_click=botao_click, data="0", style=ft.ButtonStyle(text_style=button_text_style), bgcolor=cor_num, color="white", width=70, height=70),
        ft.ElevatedButton(text=".", on_click=botao_click, data=".", style=ft.ButtonStyle(text_style=button_text_style), bgcolor=cor_num, color="white", width=70, height=70),
        ft.ElevatedButton(text="=", on_click=botao_click, data="=", style=ft.ButtonStyle(text_style=button_text_style), bgcolor=cor_op, color="white", width=150, height=70)
    ]

    # Adicionar todos os componentes à página
    page.add(output, *grid, ft.Row(linha_final, alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
