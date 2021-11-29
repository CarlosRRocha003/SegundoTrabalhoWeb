# Curriculos Org 
## Alunos:
  - Carlos Ribeiro da Rocha - 1720372
  - Leonardo Santos Abreu - 1720565
## Resumo:
Estamos planejando desenvolver um site para envio/consulta de currículos. O usuário vai ter a opção de entrar como Pessoa física e publicar/editar seu currículo ou como Empresa para consultar currículos de possíveis candidatos

## Implementações
 - Site implementado em Python+Django, HTML, CSS e Javascript
 - Quatro operações do CRUD (Criar/Ler/Atualizar/Deletar Candidatos e Empresas)
 - AJAX - Utilizado para garantir que as datas de nascimento inseridas pelo usuário na criação de Candidatos são realmente válidas, ou seja, são datas que ja passaram quando comparadas a data atual.
 - Login/Acesso/Ações selecionadas por usuário. Existem dois tipos de usuários, Candidatos e Empresas, cada tipo tem uma visão diferente do site. No caso de um candidato, ele pode Criar/Atualizar/Deletar seu currículo e ler a lista de empresas disponíveis para contato. Já no caso de uma empresa, o usuário pode Criar/Atualizar/Deletar as informaçoes de sua empresa e ler a lista de usuários disponíveis para contato.
 - Site [Curriculos Org](https://curriculos-org-trabalho-web.herokuapp.com/) publicado em Heroku!

## Como visitar o site
O site se encontra hospedado no Heroku. Para acessá-lo e testar todas as implementações mencionadas acima basta acessar o link abaixo
 - https://curriculos-org-trabalho-web.herokuapp.com

## Bugs conhecidos
 - Ao cadastrar um usuário com espaço no Username ("Leonardo Exemplo", por exemplo) não é posssível salvar o formulario dele no banco.

## Possíveis melhoras
 - Exisita a possibilidade de serem feitas muitas validações em campos no formulário, como País/Estado/Cidade por exemplo, mas por falta de tempo não conseguimos implementar.
 - Identidade visual no geral
 - O banco de dados poderia ter sido modelado de maneira mais eficiente
 - Planejavamos criar uma tela de Envio de proposta das empresas para os candidatos listados, mas não conseguimos tempo para implementar.