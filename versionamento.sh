#!/bin/bash

# Nome do arquivo de versão
arquivo_json="./version.json"

# Verificar se o arquivo existe
if [[ ! -f $arquivo_json ]]; then
  echo "Arquivo $arquivo_json não encontrado!"
  exit 1
fi

# Ler a versão atual do JSON usando jq
app_version=$(jq -r '.version' $arquivo_json)
echo ">>> VERSIONAMENTO SEMANTICO <<<"
echo "Última versão: $app_version"

# Separando os componentes da versão
IFS='.' read -r major minor patch <<< "$app_version"

# Tipo do pull request (recebido como argumento)
pr_branch=$1
echo "pr_branch: $pr_branch"

# Verificando se o PR é "fix/" ou "feature/" ou "breaking-change/"
if [[ $pr_branch == breaking-change/* ]]; then
    major=$((major + 1))
elif [[ $pr_branch == feature/* ]]; then
    minor=$((minor + 1))
elif [[ $pr_branch == fix/* ]]; then
    patch=$((patch + 1))
else
    echo "Tipo de branch não identificado. Use 'fix/', 'feature/' ou 'breaking-change/'."
    exit 1
fi

# Gerando a nova versão
nova_versao="${major}.${minor}.${patch}"
echo ">>> Nova versão: $nova_versao <<<"

# Atualizando o arquivo JSON
jq --arg nv "$nova_versao" '.version = $nv' $arquivo_json > tmp.$$.json && mv tmp.$$.json $arquivo_json

# Exibir o conteúdo atualizado
cat $arquivo_json