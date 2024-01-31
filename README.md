# projeto-alepe

- ## Importando o repositório

    Para começar, através de um termial, acesse o local de preferência para clonar o repositório.

    ```
    git clone <code>
    ``` 

    Quando terminado, o output deverá ser algo como:

    ```
    Resolving deltas: 100% (x/y), done.
    ```

- ## Configurando o virtualenv

    Execute o seguinte comando para instalação do virtualenv via pip

    ```
    pip install virtualenv
    ``` 

    Caso ocorra algum erro de permissão de rede, execute o seguinte comando:

    ```
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org virtualenv
    ```

- ## Criação do venv do projeto

    Abra um terminal como administrador no repositório do projeto e execute o comando:

    ```
    python -m virtualenv venv
    ```

    Em seguida, ative o venv:
 
    ```
    venv\Scripts\activate
    ```

    Antes do path do seu terminal, deve aparecer "**(venv)**", sinalizando que ele está ativo. 

    > **[ ! ] Será sempre necessário ativar o venv para manipulação do repositório.**

- ## Instalando os requisitos

    Com o terminal aberto no repositório e com o venv ativo, execute o comando:

    ```
    pip install -r requirements.txt
    ```

    Caso ocorra algum erro de permissão de rede novamente, execute o seguinte comando:
 
    ```
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
    ```

# tutorial-git

> **[ ! ] Tenha certeza de que está executando os próximos comandos com o terminal na mesma pasta do repositório do projeto.**

- ## Procurar por alterações e atualizar o repositório 

    Apenas um comando é necessário para ambas situações:

    ```
    git pull
    ```

    Caso exista algum alteração, ele vai atualizar seu repositório, se não, já está atualizado e você verá no terminal:

    ```
    Already up to date.
    ```

    > **[ ! ] É recomendado que você atualize seu repositório antes de fazer qualquer nova alteração e também garanta que não haja duas ou mais pessoas mexendo nos mesmos arquivos que você, para não gerar conflito no código.**

- ## Fazendo um commit

    Após fazer alterações no repositório, antes do commit, adicione as mudanças para staging.

    ```
    git add .
    ```

    Agora, escreva uma mensagem descrevendo brevemente o que contém no seu commit.

    ```
    <ex.> git commit -m "Adição do modelo Evento em eventos"
    ```

    Agora seu commit está pronto para ser enviado.

    ```
    git push
    ```

    Caso ocorra algum erro ao executar o push, utilize o seguinte comando antes de terntar fazer push novamente.

    ```
    git config --global --add safe.directory C:/<path>/projeto-alepe
    ```

# glossário

- ## <>

    *Exemplificar; demonstrar.*

    >**[!] Qualquer texto dentro dessa sinalização, incluindo ela mesma, deve ser desconsiderado ou substituído por algo.**