import PySimpleGUI as sg 

# TEMA PRINCIPAL 
sg.theme('topanga')

# TELA PRINCIPAL
tela= [

[sg.Text('FICHA CADASTRAL', size=(50,3), font= 'Arial 20',justification= 'center')], 
[sg.Text('NOME:')],
[sg.Input('',key= '--TEXTO--')],         

[sg.Button('PLAY', key= '--CADASTRAR--', size=(10,2)),
 sg.Button('DELETAR', key= '--DELETAR--', size=(10,2))],

[sg.Text('ESCOLHA QUAL EMAIL VOCÊ QUER CADASTRAR ?')],

[sg.Checkbox('Gmail:'), sg.Checkbox('Hotmail:'), sg.Checkbox('Yahoo:')],

[sg.Text('QUAL LINGUAGEM VC DOMINA ?')],

[sg.Output(key = '--Caixa_Texto--',size=(30,20))],
   
]
# LAYOUT DA JANELA 
janela = sg.Window('TELA DE CADASTRO', layout= tela, size=(500,500))

# lOOP DA JANELA 
while True:
      evento, valores = janela.read() 
      
      if evento == sg.WIN_CLOSED:
          break
      
      if evento == '--CADASTRAR--':
         janela['--Caixa_Texto--'].update(valores['--TEXTO--'].values()) 
      
      if evento == '--DELETAR--':
          janela['--TEXTO--'].update('')