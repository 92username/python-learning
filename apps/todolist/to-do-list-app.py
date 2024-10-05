import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.window_width = 400
    page.window_height = 600
    page.window_center()

    # Personalização de cores
    cor_fundo = "#FFDEAD"  # Alterar a cor de fundo aqui (hex ou nome)
    cor_texto = "#000000"  # Cor do texto (preto)
    cor_botao_fundo = "#DEB887"  # Cor de fundo do botão
    cor_botao_texto = "#8B4513"  # Cor do texto do botão
    cor_checkbox = "#DEB887"  # Cor do checkbox
    cor_icone_lixeira = "#FF6347"  # Cor do ícone de lixeira
    cor_tarefa = "#8B4513"  # Cor do texto da tarefa (label do checkbox)
    cor_borda_input = "#8B4513"  # Cor da borda do campo de texto

    # Definir as cores no layout
    page.bgcolor = cor_fundo  # Cor de fundo da página
    page.padding = 20
    page.spacing = 10

    # Campo para adicionar tarefas
    tarefa_input = ft.TextField(
        label="Digite uma nova tarefa", 
        expand=True, 
        text_style=ft.TextStyle(color=cor_texto),
        border_color=cor_borda_input,  # Cor da borda do campo de texto
        on_submit=lambda e: adicionar_tarefa(None)  # Adicionar tarefa ao apertar "Enter"
    )

    # Lista para armazenar as tarefas
    lista_tarefas = ft.Column()

    # Função para adicionar tarefas
    def adicionar_tarefa(e):
        if tarefa_input.value:
            # Criar uma linha para a tarefa com checkbox e botão de remover
            nova_tarefa = ft.Row([
                ft.Checkbox(label=tarefa_input.value, 
                            on_change=marcar_concluida, 
                            check_color=cor_checkbox, 
                            label_style=ft.TextStyle(color=cor_tarefa)),  # Cor da tarefa
                ft.IconButton(icon=ft.icons.DELETE, on_click=remover_tarefa, icon_color=cor_icone_lixeira)
            ])
            # Adicionar a nova tarefa à lista
            lista_tarefas.controls.append(nova_tarefa)
            tarefa_input.value = ""
            page.update()

    # Função para marcar a tarefa como concluída
    def marcar_concluida(e):
        checkbox = e.control
        if checkbox.value:
            checkbox.label = f"[Concluída] {checkbox.label}"
        else:
            checkbox.label = checkbox.label.replace("[Concluída] ", "")
        page.update()

    # Função para remover tarefa
    def remover_tarefa(e):
        lista_tarefas.controls.remove(e.control.parent)
        page.update()

    # Botão para adicionar tarefa
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar", 
        on_click=adicionar_tarefa, 
        bgcolor=cor_botao_fundo, 
        color=cor_botao_texto
    )

    # Organizar a interface
    page.add(
        ft.Row([tarefa_input, botao_adicionar]),
        lista_tarefas
    )

ft.app(target=main)
