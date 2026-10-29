import turtle
import webbrowser

# Configuração da Janela
screen = turtle.Screen()
screen.title("Portal Informativo - Luiz Inácio Lula da Silva")
screen.bgcolor("#0F172A")
screen.setup(width=850, height=650)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

aba_atual = "trajetoria"

def desenhar_card():
    pen.goto(-380, 260)
    pen.color("#047857")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(760)
        pen.right(90)
        pen.forward(520)
        pen.left(90)
    pen.end_fill()

    pen.color("#FACC15")
    pen.pensize(3)
    pen.pendown()
    for _ in range(2):
        pen.forward(760)
        pen.right(90)
        pen.forward(520)
        pen.left(90)
    pen.penup()

def desenhar_botao(x, y, largura, altura, texto, ativo):
    pen.goto(x, y)
    pen.color("#FACC15" if ativo else "#065F46")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(largura)
        pen.right(90)
        pen.forward(altura)
        pen.left(90)
    pen.end_fill()

    pen.color("#FFFFFF" if ativo else "#10B981")
    pen.pensize(2)
    pen.pendown()
    for _ in range(2):
        pen.forward(largura)
        pen.right(90)
        pen.forward(altura)
        pen.left(90)
    pen.penup()

    pen.goto(x + largura / 2, y - altura / 2 - 6)
    pen.color("#000000" if ativo else "#FFFFFF")
    pen.write(texto, align="center", font=("Arial", 9, "bold"))

def desenhar_secao(x, y, titulo, textos):
    pen.goto(x, y)
    pen.color("#FACC15")
    pen.write(titulo, align="left", font=("Arial", 11, "bold"))
    
    y_text = y - 22
    pen.color("#FFFFFF")
    for linha in textos:
        pen.goto(x, y_text)
        pen.write(linha, align="left", font=("Arial", 9, "normal"))
        y_text -= 18
    return y_text

def atualizar_tela():
    pen.clear()
    desenhar_card()

    pen.goto(0, 215)
    pen.color("#FACC15")
    pen.write("PORTAL INFORMATIVO: LUIZ INÁCIO LULA DA SILVA", align="center", font=("Arial", 14, "bold"))

    desenhar_botao(-350, 190, 220, 32, "1. TRAJETÓRIA", aba_atual == "trajetoria")
    desenhar_botao(-110, 190, 220, 32, "2. REALIZAÇÕES", aba_atual == "realizacoes")
    desenhar_botao(130, 190, 220, 32, "3. SITES E FONTES", aba_atual == "links")

    if aba_atual == "trajetoria":
        y = desenhar_secao(
            -350, 130, 
            "Origem e Início Político", 
            [
                "• Nasceu em Caetés (PE) em 1945 e mudou-se para São Paulo na infância.",
                "• Trabalhou como torneiro mecânico e liderou o Sindicato dos Metalúrgicos.",
                "• Fundou o Partido dos Trabalhadores (PT) em 1980 durante o regime militar."
            ]
        )
        y = desenhar_secao(
            -350, y - 10, 
            "Mandatos Presidenciais", 
            [
                "• 1º e 2º Mandatos (2003–2010): Foco em programas sociais e estabilidade.",
                "• 3º Mandato (2023–Presente): Reconstrução de políticas públicas e transição ecológica."
            ]
        )
    elif aba_atual == "realizacoes":
        y = desenhar_secao(
            -350, 130, 
            "Programas Sociais e Educação", 
            [
                "• Bolsa Família: Criação e expansão da transferência de renda no país.",
                "• Expansão Universitária: Criação de Universidades Federais e Institutos (IFs).",
                "• Prouni e FIES: Ampliação do acesso de jovens de baixa renda ao ensino superior."
            ]
        )
        y = desenhar_secao(
            -350, y - 10, 
            "Economia e Conquistas", 
            [
                "• Saída do Brasil do Mapa da Fome da ONU em 2014.",
                "• Política de valorização constante do salário mínimo acima da inflação."
            ]
        )
    else:
        pen.goto(-350, 130)
        pen.color("#FACC15")
        pen.write("Acesse Fontes Oficiais no Navegador:", align="left", font=("Arial", 11, "bold"))
        
        pen.goto(-350, 90)
        pen.color("#6EE7B7")
        pen.write("👉 Clique no botão abaixo para abrir o Portal do Governo Federal", align="left", font=("Arial", 10, "normal"))
        
        desenhar_botao(-350, 50, 320, 40, "ABRIR SITE OFICIAL DO GOVERNO", False)

    pen.goto(0, -230)
    pen.color("#CBD5E1")
    pen.write("Clique nos botões amarelos no topo para alternar as informações", align="center", font=("Arial", 9, "bold"))
    
    screen.update()

def checar_clique(x, y):
    global aba_atual
    if -350 <= x <= -130 and 158 <= y <= 190:
        if aba_atual != "trajetoria":
            aba_atual = "trajetoria"
            atualizar_tela()
    elif -110 <= x <= 110 and 158 <= y <= 190:
        if aba_atual != "realizacoes":
            aba_atual = "realizacoes"
            atualizar_tela()
    elif 130 <= x <= 350 and 158 <= y <= 190:
        if aba_atual != "links":
            aba_atual = "links"
            atualizar_tela()
    elif aba_atual == "links":
        if -350 <= x <= -30 and 10 <= y <= 50:
            webbrowser.open("https://www.gov.br/planalto/pt-br")

screen.onclick(checar_clique)
atualizar_tela()
screen.mainloop()