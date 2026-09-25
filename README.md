# Monitor de Erros de Lote

Script em Python para monitoramento de erros no processamento de lotes, com consulta ao MySQL e envio automático de alertas para o Microsoft Teams.

## Sobre

Os lotes precisam ser tratados rapidamente quando apresentam erros, pois uma demora na resolução pode impactar o andamento dos disparos para as operações.

Antes da automação, a identificação dependia de uma consulta manual em um site. O objetivo deste projeto foi deixar esse acompanhamento contínuo e avisar a equipe quando novos erros fossem identificados, sem a necessidade de consulta manual para identificar se tinha algum erro.

## Como funciona

O script:

- Consulta o banco de dados;
- Processa os resultados e calcula a quantidade total de erros;
- Compara o resultado com a consulta anterior;
- Envia uma notificação para o Microsoft Teams quando a quantidade de erros aumenta;
- Aguarda 30 segundos e realiza uma nova consulta.

A comparação com o resultado anterior evita o envio repetido da mesma ocorrência.

Exemplo:

0 → 2   alerta
2 → 2   sem alerta
2 → 4   alerta
4 → 4   sem alerta

## Tecnologias

- Python
- MySQL
- mysql.connector
- Requests
- API REST
- Microsoft Teams
- Adaptive Cards
- Anaconda

## Estrutura

A lógica principal do monitoramento é baseada em um loop contínuo:

![Fluxo do monitoramento](imagens/Fluxo_Alerta_Lote.png)

## Resultado

A automação reduziu significativamente a frequência de reclamações relacionadas à demora na identificação e resolução de erros de lote.

Com o monitoramento contínuo, novos erros passaram a gerar uma notificação automaticamente, deixando sem a dependência da verificação manual.

## Observação

Este projeto foi desenvolvido para utilização em ambiente interno.

Para disponibilização pública, informações como credenciais de banco de dados, URLs de webhook, endpoints internos e dados relacionados à operação devem ser removidas ou substituídas por configurações externas.

## Desenvolvimento

Projeto desenvolvido utilizando pesquisa, testes e documentação técnica, com auxílio de IA durante o processo de desenvolvimento e resolução de problemas.
