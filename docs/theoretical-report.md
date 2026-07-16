# Parte Teórica — TechFlow Tasks

## 1. Descrição do projeto e escopo inicial

O TechFlow Tasks é um sistema web básico criado para organizar atividades de uma startup de logística. Seu escopo inicial compreende o cadastro, consulta, edição e exclusão de tarefas, além da classificação por prioridade e do acompanhamento por status.

## 2. Metodologia ágil

Foi escolhida uma abordagem híbrida. O Kanban organiza visualmente as tarefas em A Fazer, Em Progresso e Concluído, enquanto práticas do Scrum orientam entregas pequenas, revisão frequente e adaptação do backlog.

## 3. Importância da modelagem

A modelagem reduz ambiguidades antes da implementação. O diagrama de casos de uso esclarece quem utiliza o sistema e quais operações estão disponíveis. O diagrama de classes representa a estrutura do software, as entidades e as dependências entre aplicação, rotas, serviços e banco de dados.

## 4. Diagrama de casos de uso

Arquivo: `docs/use-case-diagram.puml`.

O gestor cadastra, edita, exclui, prioriza e acompanha indicadores. O colaborador consulta o painel e atualiza o status das tarefas.

## 5. Diagrama de classes

Arquivo: `docs/class-diagram.puml`.

A classe `Task` representa a entidade principal. As rotas recebem as requisições HTTP, o serviço valida os dados e o Flask cria e configura a aplicação.

## 6. Mudança de escopo

A mudança simulada foi a inclusão dos campos responsável e prazo. Ela foi justificada pela necessidade de melhorar o acompanhamento das entregas. O impacto foi controlado com novo card no Kanban, alteração do modelo, atualização das telas, testes e documentação.

## 7. Testes automatizados

Foram implementados testes unitários para validação de entrada e testes de integração das rotas principais. O Pytest verifica carregamento do painel, criação de tarefas e rejeição de dados inválidos. A cobertura pode ser medida com `pytest --cov=src`.

## 8. GitHub Actions

O pipeline é acionado em push e pull request. Ele instala as dependências, executa Ruff para qualidade do código e Pytest para garantir que as funcionalidades continuem operando.

## 9. Falhas em projetos ágeis e mitigação

As principais causas são requisitos pouco claros, comunicação deficiente, falta de priorização, mudanças sem registro e ausência de testes. O GitHub reduz esses riscos por meio de Issues, Projects, pull requests, histórico de commits e Actions.