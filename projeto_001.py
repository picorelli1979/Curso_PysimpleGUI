import PySimpleGUI as sg 

# AQUI PASSAMOS O TAMANHO DA FONTE POR COMPLETO
sg.set_options(font= 'Arial 20')

# AQUI JÁ DECIDIMOS QUAL SERÁ O TEMA USADO NA TEMPLATE
sg.theme('topanga')

# AQUI DEFINIMOS OS CAMPOS : NESTE CASO CAMPOS DE TEXTO !!!!
coluna01 = [
        [sg.Text('NOME: ')],
        [sg.Text('BAIRRO:')],
        [sg.Text('CIDADE:')],
]

# AQUI DEFINIMOS CAMPOS : NESTE CASO CAMPOS DE INPUT QUE SERÃO PREENCHIDOS!!!!        
coluna02 = [
        [sg.Input('', key = '--NOME--')],
        [sg.Input('', key = '--BAIRRO--')],
        [sg.Input('', key = '--CIDADE--')],
] 
       
# AQUI DEFINIMOS A TELA EM SI :
  # 1 - CABEÇALHO DA TELA 
  # 2 - COLUNAS 
  # 3 - BOTÕES NA TELA          
tela = [
    
      [sg.Text('CADASTRO DE PESSOAS', size=(30,3), font= 'Arial 18', justification= 'center' )],
      
      [sg.Column(layout= coluna01, vertical_alignment= 'top'),
       sg.Column(layout= coluna02, vertical_alignment= 'top')],
       
      [sg.Button('CADASTRAR', key = '--CADASTRAR', size=(15,2))],
      [sg.Button('LIMPAR', key = '--LIMPAR--', size=(15,2))],
      [sg.Button('FECHAR', key = '--FECHAR--', size=(15,2))],
]


# AQUI ESTÁ AS ESPECIFICAÇÕES DA JANELA : TAMANHO / NOME / LAYOUT
janela = sg.Window('PRIMEIRA TELA', layout = tela, size=(500,500))


# TODA VEZ QUE QUISER RODAR UMA TELA PRECISA DE UM LOOP WHILE TRUE,
# DENTRO DELA TEM QUE TER UM EVENTO, VALORES SENDO IGUAL JANELA.READ()
# O EVENTO TEM QUE SER FECHADO COM O WIN_CLOSED
while True:
    
      evento, valores = janela.read()
      
      if evento == sg.WIN_CLOSED:
         break
      
      if evento == '--FECHAR--':
         break     
      
      if evento == '--LIMPAR--':
         janela['--NOME--'].update(' ')      
         janela['--BAIRRO--'].update(' ')
         janela['--CIDADE--'].update(' ')
          
      if evento == '--CADASTRAR--':
          sg.popup('CADASTRO FEITO COM SUCESSO')    

janela.close()
    
    
    







        