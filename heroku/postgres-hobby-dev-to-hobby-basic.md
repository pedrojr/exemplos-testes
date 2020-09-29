## Alterar plano do postgres de hobby-dev para hobby-basic

### Instalar o heroku cli
[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Criar um novo banco na versão para a sua aplicação
```
heroku addons:create heroku-postgresql:hobby-basic --version 11 --app APP_NAME
```

### Atribuir modo de manutenção para on
```
heroku maintenance:on --app APP_NAME
```

### Copiar banco existente para o novo banco
```
heroku pg:copy OLD_DB NEW_DB --app APP_NAME
```

### Relacionar o novo banco para a aplicação
```
heroku pg:promote NEW_DB --app APP_NAME
```

### Atribuir modo de manutenção para off
```
heroku maintenance:off --app APP_NAME
```
