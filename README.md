# projeto-alepe

- ## Descrição

    Esse projeto tem como intuito otimizar o gerenciamento do **Suporte**, setor da **STI** da **Assembleia  Legislativa de Pernambuco**, ao mesmo tempo que procura reduzir o uso de papéis, visando a digitalização do processo de organização de eventos promovidos pela Casa. 

- ## Configuração

    - ### Clonando o repositório

        Para começar, através de um termial, acesse o local de preferência para importar o repositório. Utilize o seguinte comando:

        ```
        git clone <code>
        ``` 

        #

    - ### Instalando o virtualenv

        Com o repositório em sua máquina, execute o comando a seguir para instalação do virtualenv.

        ```
        pip install virtualenv
        ```

        #

    - ### Criando o venv do projeto

        Em um terminal com permissões de administrador aberto na pasta do projeto, execute o comando:

        ```
        python -m virtualenv venv
        ```

        #

    - ### Ativando e desativando o venv

        Para ativar o venv, em um terminal aberto no repositório, execute:
    
        ```
        venv\Scripts\activate
        ```

        > **[ ! ] Será sempre necessário ativar o venv para manipulação do repositório.**

        Para desativar, apenas execute no terminal o comando abaixo.
        ```
        deactivate
        ``` 

        #

    - ### Instalando os requisitos

        Após seguir os passos anteriores, com o venv ativo, execute:

        ```
        pip install -r requirements.txt
        ```

        Para checar se tudo foi instalado corretamente, utilize:

        ```
        pip freeze
        ```

        O output deverá ser exatamente o que está escrito no arquivo de requisitos.

- ## Execução

    >**[ ! ] É importante que o terminal esteja aberto no repositório do projeto com o venv ativo para execução dos póroximos comandos.**

    - ### Localmente

        - ### Iniciando o banco de dados

            ```
            python manage.py migrate
            ```

            >**[ ! ] Esse comando só é necessário no primeiro contato com a aplicação.**

            #

        - ### Criando um administrador

            ```
            python manage.py createsuperuser
            ```

            >**[ ! ] Para acessar a página de administração, adicione /admin no link oferecido ao executar o comando abaixo e faça login com o administrador criado anteriormente.**

            #

        - ### Executando a aplicação

            ```
            python manage.py runserver
            ```

- ## Manipulação

    🚧 **WORK IN PROGRESS** 🚧

# Tutorial Git

> **[ ! ] Tenha certeza de que está executando os próximos comandos com o terminal aberto no repositório do projeto.**

- ## Pull

    - ### Atualizando o repositório 

        O comando a seguir busca por alterações no repositório.

        ```
        git pull
        ```

        Caso exista algum alteração, ele atualizará seu repositório, se não, você verá no terminal:

        ```
        Already up to date.
        ```

        > **[ ! ] É recomendado que você atualize seu repositório antes de fazer qualquer nova alteração e também garanta que não haja uma ou mais pessoas mexendo nos mesmos arquivos que você, para não gerar conflito no código.**

- ## Push

    - ### Fazendo um commit

        Após fazer alterações no repositório, antes do commit e push, não esqueça de adicionar as mudanças para staging.

        ```
        git add .
        ```

        Agora, escreva uma mensagem descrevendo brevemente sua contribuição.

        ```
        <ex.> git commit -m "Adição do modelo Evento em eventos"
        ```

        Pronto! Seu commit está pronto para ser enviado, utilize:

        ```
        git push
        ```

# Troubleshooting

- ## pip install

    Caso ocorra erro de permissão de rede, execute o seguinte comando:

    ```
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <flag> <package-name>         
    ```

- ## git push

    Caso ocorra algum erro, tente o comando a seguir antes de terntar fazer push novamente.
        
    ```
    git config --global --add safe.directory C:/<path>/projeto-alepe
    ```

# Glossário

- ## <>

    *Exemplificar; demonstrar.*

    >**[ ! ] Qualquer texto dentro dessa sinalização, incluindo ela mesma, deve ser desconsiderado ou substituído por algo, a depender do que estiver relacionda.**