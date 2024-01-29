# ALEPE Demandas

# INSTALAÇÃO:

Para instalar o projeto na sua maquina:

Crie uma pasta do projeto com o nome do projeto

Na pasta de um clone dos arquivos:
git clone https://github.com/Warpedro1/projeto-alepe.git

Quando clonado os arquivos set os ambientes da venv:
```
 (TRUSTED HOST) pip install virtualenv
``` 
Caso ocorra erro de permissão de rede:
```
  pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>
 
```
Instalar o ambiente virtual:
 
```
(ADMNISTRADOR) python -m virtualenv venv
 
```
Depois entre na sua venv:
 
```
 venv\Scripts\activate
 
```

No ultimo passo baixe os arquivos requirements:

```
 (TRUSTED HOST) pip install -r requirements.txt
 
```
Caso ocorra erro de permissão de rede:
 
```
  pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>
```

# COMEÇAR A TRABALHAR:

```
- git pull ( vai puxar as alterações do repositório online)
```

# FINALIZAR TRABALHO:

```
-git add . ( coloca suas altercação em staged)

-git commit -m “nome do commit” ( commita as alterações)

-git push
```
 caso ocorra erro na hora do push (fatal: detected dubious ownership in repository at...):
 
 use o comando:
  
```
 git config --global --add safe.directory C:/Users/<seu_usuario>/pull/projeto-alepe
 
```
#venv/lib/site-packages/django/contrib/admin/templates/sites.py