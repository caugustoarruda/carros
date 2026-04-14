
# **`Documentação do projeto Carros`**

# Funcionalidades do projeto
- `Funcionalidade 1`: Gerenciamento de Carros | CRUD completo
- `Funcionalidade 2`: Gerenciamento de Acessos, criação e acesso com login

<!-- # 📁 Acesso ao projeto
**Indique como é possível baixar ou acessar o código fonte do projeto, seja projeto inicial ou final** -->

# 🛠️ Abrir e rodar o projeto
**Instruções necessárias executar o projeto**

#### Partindo do pressuposto que já tenha o Python instalado e um terminal para executar os comandos
1. Clone the repo  
```bash 
git clone https://github.com/caugustoarruda/carros 
```
2. Ative ou Crie seu ambiente virtual
```bash 
python -m venv env ou source/bin/activate para ativar um ambiente virtual ja existente
```
3. Instale as dependencias  
```bash 
pip install -r requirements.txt
```
4. Tenha um gerenciador de banco de dados instalado ou utilize o sqlite, banco padrão adotado pelo Django

5. O próximo passo será definir qual sera o banco de dados utilizado, alterando uma simples configuração no `settings` do projeto 

   - vá na pasta app do projeto e procure por `settings.py`
   - procure onde está a definição de banco de dados `DATABASES`
   - e ai agora é so configurar com seu banco preferido seguindo os exemplos abaixo:

   sqlite
   ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
   ```
   postgres
   ```py
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'NOME DO SEU BANCO',
          'USER': 'USUARIO DO BANCO',
          'PASSWORD': 'SENHA',
          'HOST': 'localhost',
          'PORT': '5432'
      }
    }
   ```
6. Seguindo, será necessário executar o comando migrate do Django, para que seja criado as tabelas necessárias para que a aplicação rode
```py
   python manage.py migrate
```
7. Se chegou até aqui, agora é so executar o comando para disponibilizar o projeto localmente
```py
   python manage.py runserver
```
se tudo ocorreu bem, você verá uma mensagem no terminal igual a mensagem abaixo

![alt text](media/image.png)

Pronto! Agora você já pode acessar a aplicação digitando o endereço informado no termial após executar o comando runserver
`127.0.0.1:8000/cars`

![alt text](media/tela_app.png)

Agora você já pode se logar ou se cadastrar pela interface do navegador, basta preencher os dados e pronto!

![alt text](media/tela_login.png)

Quando você se logar, terá como opção cadastrar novos veículos, mas para isso ser possível você terá que cadastrar a marca do veículo e isso só é possível com superuser
1. Para criar um super user, basta executar o comando abaixo e seguir os passos solicitados:
```py
   python manage.py createsuperuser
```
![alt text](media/cadastro_super.png)


