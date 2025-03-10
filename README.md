

Agência de Marketing Crew

Este é um projeto experimental para a criação de uma agência de publicidade utilizando CREW.io. O projeto está 100% funcional e pronto para uso.

Instalação

Certifique-se de ter o Python >= 3.10 e <= 3.13 instalado no seu sistema. Este projeto utiliza o Poetry para gerenciamento de dependências e pacotes, proporcionando uma experiência de configuração e execução simplificada.

Passo 1: Instalar o Poetry

Caso ainda não tenha o Poetry instalado, execute o seguinte comando:

pip install poetry

Passo 2: Instalar dependências do projeto

1. No diretório raiz do projeto, primeiro trave as dependências e depois instale-as:

poetry lock

poetry install



Configuração

Para personalizar sua agência de marketing baseada em CrewAI, siga os passos abaixo:

1. Adicione sua chave da OpenAI ao arquivo .env:

OPENAI_API_KEY=your_api_key_here


2. Configure os agentes editando o arquivo:

src/agencia_marketing/config/agents.yaml


3. Defina as tarefas no arquivo:

src/agencia_marketing/config/tasks.yaml


4. Personalize a lógica, ferramentas e argumentos no arquivo:

src/agencia_marketing/crew.py


5. Adapte as entradas para seus agentes e tarefas no arquivo:

src/agencia_marketing/main.py



Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, utilize o comando abaixo no diretório raiz do projeto:

poetry run agencia_marketing

Este comando inicializa a Agência de Marketing Crew, reunindo os agentes e atribuindo as tarefas conforme definido na configuração.

> Por padrão, o projeto gera um arquivo report.md na pasta raiz, contendo um relatório sobre pesquisa de Modelos de Linguagem (LLMs).



Estrutura da Agência de Marketing Crew

A Agência de Marketing Crew é composta por vários agentes de IA, cada um com funções, objetivos e ferramentas específicas. Eles trabalham de forma colaborativa em uma série de tarefas definidas no arquivo config/tasks.yaml, utilizando suas habilidades combinadas para alcançar objetivos complexos.

O arquivo config/agents.yaml define as configurações e capacidades de cada agente da equipe.

