# TechFlow Tasks

Sistema web de gerenciamento ágil de tarefas desenvolvido para uma startup fictícia de logística. O projeto atende ao desafio acadêmico de aplicar Engenharia de Software, GitHub Projects, controle de versão, testes automatizados, integração contínua e gestão de mudanças.

## Objetivo

Permitir que equipes de logística:

- cadastrem, consultem, editem e excluam tarefas;
- classifiquem tarefas por prioridade;
- acompanhem o fluxo em um quadro com “A Fazer”, “Em Progresso” e “Concluído”;
- definam responsável e prazo;
- visualizem indicadores resumidos no painel.

## Escopo inicial

O escopo inicial contempla um CRUD de tarefas com os campos título, descrição, prioridade, status, responsável e prazo. Os dados são persistidos em SQLite.

## Metodologia adotada

Foi adotado um modelo híbrido com **Kanban** para gestão visual do fluxo e práticas de **Scrum** para organização em entregas curtas. O GitHub Projects deve ser configurado com as colunas:

1. To Do / A Fazer
2. In Progress / Em Progresso
3. Done / Concluído

O backlog sugerido está em `docs/kanban.md`.

## Mudança de escopo simulada

Durante o desenvolvimento, o cliente solicitou a inclusão de **responsável e prazo de entrega** em cada tarefa. A mudança foi aceita porque melhora a rastreabilidade das atividades logísticas e reduz atrasos. Para gerenciá-la:

- foi criado um novo card no Kanban;
- o modelo de dados foi ampliado;
- o formulário e o painel foram atualizados;
- os testes passaram a validar a nova estrutura;
- a mudança foi registrada em commit próprio.

## Tecnologias

- Python 3.12
- Flask
- Flask-SQLAlchemy
- SQLite
- Tailwind CSS via CDN
- Pytest e pytest-cov
- Ruff
- GitHub Actions
- PyCharm

## Estrutura

```text
techflow_task_manager/
├── .github/workflows/ci.yml
├── docs/
│   ├── class-diagram.puml
│   ├── use-case-diagram.puml
│   ├── kanban.md
│   ├── theoretical-report.md
│   └── video-pitch.md
├── src/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── services.py
├── tests/
├── requirements.txt
└── run.py
```

## Execução no PyCharm

1. Abra o PyCharm e selecione **Open**.
2. Escolha a pasta `techflow_task_manager`.
3. Crie um ambiente virtual em **Settings > Project > Python Interpreter**.
4. No terminal do PyCharm, execute:

```bash
pip install -r requirements.txt
python run.py
```

5. Acesse `http://127.0.0.1:5000`.

## Testes e qualidade

```bash
pytest -v
pytest --cov=src
ruff check src tests
```

O workflow `.github/workflows/ci.yml` executa Ruff e Pytest automaticamente em pushes e pull requests.


## Beneficiários

Os principais beneficiários são gestores de logística, líderes de equipe e colaboradores operacionais. Gestores usam indicadores e prioridades; líderes acompanham o andamento; colaboradores consultam responsabilidades e atualizam o status das tarefas.

## Principais riscos e mitigação

Falhas em projetos ágeis normalmente surgem por requisitos vagos, comunicação insuficiente, excesso de trabalho em andamento e ausência de testes. GitHub Issues, Projects, commits, pull requests e Actions melhoram rastreabilidade, colaboração e controle de qualidade.

## Licença

Projeto acadêmico.
