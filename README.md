1. Inicie a aplicação localmente
Antes de usar o Postman, é necessário rodar a aplicação Flask no seu computador:
Abra o terminal na pasta do projeto.

Execute o comando:
bash

python app.py

Isso inicia o servidor Flask, que por padrão estará disponível em:

http://127.0.0.1:5000

Certifique-se de que o terminal mostra que o servidor está ativo (sem erros) antes de prosseguir.

2. Configure o Postman para testar os endpoints
Com o servidor rodando, abra o Postman e use as instruções abaixo para interagir com os endpoints da API:
Criar um pagamento
Método: POST

URL: http://127.0.0.1:5000/payments

Corpo (Body):
Selecione a opção raw no Postman e escolha o formato JSON.

Insira um exemplo como este:
json

{
  "value": 123.45,
  "expiration_date": "2025-05-30T12:00:00"
}

Ação: Clique em "Send".

Resposta esperada: O servidor retornará um JSON com os detalhes do pagamento criado, incluindo o id e possivelmente um qr_code.

Consultar um pagamento
Método: GET

URL: http://127.0.0.1:5000/payments/<id>
Substitua <id> pelo ID do pagamento que você deseja consultar (exemplo: http://127.0.0.1:5000/payments/1).

Corpo (Body): Não é necessário (deixe em branco).

Ação: Clique em "Send".

Resposta esperada: Um JSON com os detalhes do pagamento, como valor, data de expiração e status.

Confirmar um pagamento
Método: GET

URL: http://127.0.0.1:5000/confirm_payment/<id>
Substitua <id> pelo ID do pagamento (exemplo: http://127.0.0.1:5000/confirm_payment/1).

Corpo (Body): Não é necessário (deixe em branco).

Ação: Clique em "Send".

Resposta esperada: O servidor retorna uma página HTML com a confirmação do pagamento. No Postman, você verá o código HTML bruto. Para uma visualização formatada, é recomendado abrir essa URL diretamente em um navegador.

3. Dica extra: Visualização no navegador
Embora o foco seja o uso do Postman, a rota de confirmação (/confirm_payment/<id>) foi projetada para exibir uma página HTML. Para ver o resultado de forma mais amigável:
Abra um navegador e digite:

http://127.0.0.1:5000/confirm_payment/<id>

Substitua <id> pelo ID do pagamento. Isso mostrará a página de confirmação estilizada.

Resumo dos passos
Rodar o servidor: Use python app.py para iniciar a aplicação em http://127.0.0.1:5000.

Testar no Postman:
POST /payments: Criar um pagamento com JSON no corpo.

GET /payments/<id>: Consultar os dados de um pagamento.

GET /confirm_payment/<id>: Confirmar um pagamento (HTML retornado).

Opcional: Use o navegador para visualizar a página de confirmação.

Com isso, você consegue acessar e testar toda a funcionalidade da aplicação usando o Postman! Se houver dúvidas ou erros, verifique se o servidor está ativo e se os IDs usados nas URLs são válidos.

Obrigado!
