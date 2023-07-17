import matplotlib.pyplot as plt
from tkinter import * # Dessa forma, não será necessário recrutar o tkinter cada vez que forem usadas suas ferramentas

# Início do programa

def tensao_eng():                                                     # Tensão de engenharia
    def calcular():
        forca_aplicada = float(entry_carga.get())
        area_transv = float(entry_area.get())
        tensao_engenharia = forca_aplicada / area_transv
        resultado_tensao.config(text = 'Tensão de engenharia: {:.2f} MPa'.format(tensao_engenharia))

    window_tensao_eng = Toplevel(window)                              # TopLevel cria uma janela secundária
    window_tensao_eng.title('Tensão de Engenharia')
    window_tensao_eng.geometry('250x160')

    # Campo de preenchimento
    lbl_carga = Label(window_tensao_eng, text = 'Carga instantânea aplicada [N]:')
    lbl_carga.pack()

    entry_carga = Entry(window_tensao_eng)
    entry_carga.pack()

    # Campo de preenchimento
    lbl_area = Label(window_tensao_eng, text = 'Área da seção transversal [m²]:')
    lbl_area.pack()

    entry_area = Entry(window_tensao_eng)
    entry_area.pack()

    btn_calcular = Button(window_tensao_eng, text = 'Calcular', command = calcular)
    btn_calcular.pack()

    resultado_tensao = Label(window_tensao_eng, text = '')           # Exibe o resultado gerado
    resultado_tensao.pack()

def def_eng():                                                       # Deformação de engenharia
    def calcular():
        var_comp = float(entry_var_comp.get())
        comp_orig = float(entry_comp_orig.get())
        def_engenharia = var_comp / comp_orig
        resultado_def.config(text = 'Deformação de Engenharia {:.4f}'.format(def_engenharia))

    window_def_eng = Toplevel(window)
    window_def_eng.title('Deformação de Engenharia')
    window_def_eng.geometry('250x160')
    
    # Campo de preenchimento
    lbl_var_comp = Label(window_def_eng, text = 'Variação do Comprimento [m]:')
    lbl_var_comp.pack()

    entry_var_comp = Entry(window_def_eng)
    entry_var_comp.pack()

    # Campo de preenchimento
    lbl_comp_orig = Label(window_def_eng, text = 'Comprimento Original [m]:')
    lbl_comp_orig.pack()

    entry_comp_orig = Entry(window_def_eng)
    entry_comp_orig.pack()

    btn_calcular = Button(window_def_eng, text = 'Calcular', command = calcular)
    btn_calcular.pack()

    resultado_def = Label(window_def_eng, text = "")
    resultado_def.place()

def plot_tensao_deformacao():                                        # Gráfico tensão-deformação
    def gerar_grafico():
        m_elasticidade = float(entry_mod_elast.get())
        deformacao_ultima = float(entry_def_ultima.get())
        plot_tensao = m_elasticidade * deformacao_ultima

        # Gerar eixos tensão e deformação
        deformacao = [0.0, deformacao_ultima]
        tensao = [0.0, plot_tensao]

        # Plotar gráfico tensão-deformação
        plt.plot(deformacao, tensao)
        plt.xlabel('Deformação [m]')
        plt.ylabel('Tensão [MPa]')
        plt.title('Tensão-Deformação')
        plt.grid(True)
        plt.show()

    window_plot = Toplevel(window)
    window_plot.title("Gráfico Tensão-Deformação")
    window_plot.geometry("340x200")

    lbl_mod_elast = Label(window_plot, text = 'Módulo de elasticidade [MPa]:')
    lbl_mod_elast.pack()

    entry_mod_elast = Entry(window_plot)
    entry_mod_elast.pack()

    lbl_def_ultima = Label(window_plot, text = 'Deformação mediante limite de proporcionalidade:')
    lbl_def_ultima.pack()

    entry_def_ultima = Entry(window_plot)
    entry_def_ultima.pack()

    btn_gerar = Button(window_plot, text = 'Gerar gráfico', command=gerar_grafico)
    btn_gerar.pack()

    lbl_nota = Label(window_plot, text = 'Esta é uma versão em desenvolvimento, atualizações em breve.')
    lbl_nota.place(y = 180, in_ = window_plot)

def quit():
    window.quit()
    window.destroy()

# Definindo a janela principal
window = Tk()                                                     # Código do tkinter que cria a janela
window.resizable(0,0)                                             # Isso impede o usuário de resimensionar a janela
window.title('Calculadora para ensaios tensão-deformação')
window.geometry('400x225')

title_search = Label(window, text = 'Olá, seja bem-vindo ao seu ambiente de manipulação de\ndados obtidos via ensaio tensão-deformação.\nSelecione a opção desejada:')
title_search.pack()

copyright = Label(window, text = 'Copyright (c) 2023 Caio Nicácio. All Rights Reserved.')
copyright.place(y = 205, in_ = window)

# Botão
btn1 = Button(window, text = 'Tensão de engenharia', command = tensao_eng)
btn1.pack()

btn2 = Button(window, text = 'Deformação de engenharia', command = def_eng)
btn2.pack()

btn3 = Button(window, text = 'Gráfico tensão-deformação', command = plot_tensao_deformacao)
btn3.pack()

btn_quit = Button(window, text = "Encerrar aplicação", bg = '#E32636', fg = 'white', command = window.quit)
btn_quit.pack()

window.mainloop()                                             # Para que a janela permaneça aberta durante a execução do código