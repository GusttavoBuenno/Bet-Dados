 Relatório de Pagamentos de Afiliados<
Este programa foi desenvolvido para calcular os pagamentos de afiliados com base nas apostas dos clientes registradas em um banco de dados PostgreSQL e nos valores de pagamento fornecidos em um arquivo CSV. 
O resultado é apresentado em uma interface gráfica usando a biblioteca Tkinter.

Como o Código Funciona
O programa se conecta ao banco de dados PostgreSQL utilizando as credenciais fornecidas, incluindo o host, porta, usuário, senha e nome do banco de dados.

O programa lê o arquivo CSV fornecido, que contém informações sobre os pagamentos dos afiliados, incluindo o ID do afiliado e o valor do pagamento.

Para cada afiliado listado no arquivo CSV, o programa executa uma consulta SQL para somar as apostas dos clientes associados a esse afiliado no banco de dados. Isso é feito utilizando a tabela bets.

Cálculo do Pagamento Final: Com base nas somas das apostas dos clientes e nas informações da tabela limits, o programa determina a porcentagem de acréscimo aplicada ao pagamento final. 
Se não houver limite superior, é aplicada a porcentagem máxima de 50%. O pagamento final é então calculado como a porcentagem do pagamento do afiliado.

Interface Gráfica Tkinter: O programa cria uma janela Tkinter e exibe os resultados em uma tabela utilizando a biblioteca ttk. Cada linha da tabela corresponde a um resultado do cálculo dos pagamentos de afiliados.

Como Executar o Código
Para executar o código:

Certifique-se de ter instalado o Python em seu ambiente.
Instale as bibliotecas necessárias: psycopg2, tkinter, tabulate.
Certifique-se de ter acesso ao banco de dados PostgreSQL e que as credenciais fornecidas estão corretas.
Garanta que o arquivo CSV com os pagamentos dos afiliados esteja no diretório correto.
Execute o código em um ambiente Python compatível.
Melhorias Futuras
Implementar tratamento de erros mais robusto, incluindo gerenciamento de exceções para conexão ao banco de dados e leitura do arquivo CSV.
Adicionar funcionalidades para permitir a seleção de diferentes arquivos CSV e bancos de dados.
Aprimorar a interface gráfica com mais recursos de personalização e interação.



![image](https://github.com/GusttavoBuenno/Bet-Dados/assets/97835681/e2dc8cfc-7033-45a0-bc61-57e6ceb9c140)
