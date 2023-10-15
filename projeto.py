import PySimpleGUI as sg 

sg.theme('topanga')

# TELA PRINCIPAL
tela= [  
         [sg.Text('CABEÇALHO', size = (20,3), font='Arial 20', justification = 'center')],
         [sg.Text('AULAS DE PySimpleGUI', size = (20,3), font='Arial')],
         [sg.Input('')]
       ]           

# JANELA COM LAYOUT 
janela = sg.Window('PRIMEIRA TELA', layout = tela, size =(500,500))    
    
# LOOP DA JANELA     
while True:
    evento, values = janela.read()
    
    if evento == sg.WIN_CLOSED:
        break    