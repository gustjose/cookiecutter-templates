# Meus Templates de Projetos (Cookiecutter)

Este repositório centraliza meus modelos de projeto (scaffolding). Utiliza o [Cookiecutter](https://github.com/cookiecutter/cookiecutter) para gerar estruturas de pastas, configurações iniciais e automações.

## Pré-requisitos

Certifique-se de ter o `uv` instalado. Em seguida, instale o Cookiecutter como uma ferramenta global:

```bash
# Instala o cookiecutter em um ambiente isolado
uv tool install cookiecutter
```

## Como Usar

Como este é um "monorepo" (vários templates em um só lugar), é obrigatório usar a flag --directory para especificar qual template você quer usar.

### Sintaxe Básica

```bash
cookiecutter [https://github.com/gustjose/cookiecutter-templates](https://github.com/gustjose/cookiecutter-templates) --directory="pasta"
```