---
name: gerador-de-senhas
description: Use when developing, maintaining, redesigning, modernizing or extending the Gerador de Senhas project, a personal Python application for generating unique passwords based on a site or service name and maintaining a history of generated passwords.
---

# Gerador de Senhas

## Objetivo

Este projeto é um gerador de senhas desenvolvido em Python para facilitar a criação de senhas diferentes para sites e sistemas.

A aplicação atual permite:

- Informar a URL ou nome de um site/serviço.
- Gerar uma senha automaticamente.
- Exibir a senha gerada.
- Manter um histórico das senhas geradas.
- Limpar o histórico manualmente.

O objetivo principal é tornar a geração de senhas rápida, simples e prática.

---

## Arquivos atuais

O repositório possui atualmente:

```text
Gerador-de-Senhas/
├── gerador_senha.py
├── README.md
└── SKILL.md
```

O arquivo principal da aplicação é:

```text
gerador_senha.py
```

Antes de alterar qualquer comportamento, o agente deve analisar o código existente.

O código atual é a fonte de verdade sobre a implementação.

---

## Tecnologia

A aplicação atual é desenvolvida em:

- Python
- Interface gráfica desktop

Não assumir React, Node.js, Flask, Django ou outra tecnologia web.

Não migrar o projeto para outra tecnologia sem solicitação explícita do usuário.

---

## Fluxo principal

O fluxo esperado da aplicação é:

```text
Nome ou URL do site
        ↓
   Gerar Senha
        ↓
   Senha Gerada
        ↓
 Histórico de Senhas
```

A interface deve continuar simples e objetiva.

---

## Entrada do usuário

O usuário pode informar:

- URL.
- Domínio.
- Nome de site.
- Nome de sistema.
- Nome de serviço.

Exemplos:

```text
github.com
LinkedIn
Gmail
Sistema ERP
Meu Sistema
```

Não exigir que a entrada seja uma URL válida se o projeto permitir nomes de serviços.

Tratar entrada vazia de forma clara.

Remover espaços desnecessários quando apropriado.

---

## Geração de senha

Ao clicar em:

```text
Gerar Senha
```

a aplicação deve gerar uma nova senha.

A senha deve priorizar:

- comprimento adequado;
- variedade de caracteres;
- aleatoriedade;
- ausência de padrões previsíveis.

Para novas implementações de geração de senha em Python, preferir o módulo:

```python
secrets
```

em vez de:

```python
random
```

quando o objetivo for segurança criptográfica.

Não afirmar que uma senha é "100% segura".

Não afirmar que o gerador é criptograficamente seguro sem verificar a implementação.

---

## Histórico

A interface possui:

```text
Histórico de Senhas Geradas
```

O histórico deve manter a associação entre o site/serviço e a senha quando essa informação fizer parte da implementação atual.

A ação:

```text
Limpar Histórico
```

deve continuar sendo explícita.

Não apagar o histórico automaticamente após gerar uma nova senha.

Antes de alterar o armazenamento do histórico, verificar como o código atual funciona.

Não assumir que o histórico é persistido entre execuções.

---

## Segurança

Este projeto trabalha com senhas e deve ser tratado como sensível.

Nunca:

- colocar senhas reais no código;
- colocar credenciais reais no GitHub;
- registrar senhas em logs;
- enviar senhas para APIs externas sem solicitação explícita;
- expor senhas em mensagens de erro;
- expor senhas em screenshots públicos;
- criar telemetria que capture senhas.

Se o histórico passar a ser persistente, avaliar cuidadosamente o risco de armazenar senhas em texto puro.

Não implementar uma falsa camada de criptografia apenas para afirmar que os dados estão protegidos.

---

## Clipboard

Se for adicionada uma funcionalidade de copiar senha:

- copiar somente a senha atualmente selecionada/gerada;
- não copiar o histórico inteiro;
- informar visualmente que a cópia foi realizada;
- considerar limpeza automática do clipboard após determinado período;
- nunca registrar o conteúdo copiado em logs.

---

## Interface

A interface deve priorizar:

1. Simplicidade.
2. Rapidez.
3. Clareza.
4. Segurança.
5. Facilidade de uso.

A tela principal deve deixar evidente:

- onde informar o site;
- como gerar a senha;
- qual senha foi gerada;
- onde consultar o histórico;
- como limpar o histórico.

Evitar excesso de elementos visuais.

---

## Modernização

Se o usuário solicitar uma modernização visual:

- preservar o fluxo atual;
- preservar a lógica de geração;
- preservar o histórico;
- melhorar hierarquia visual;
- melhorar espaçamento;
- melhorar tipografia;
- melhorar feedback das ações.

Não reescrever toda a aplicação sem necessidade.

---

## Uso com Lovable

Se este projeto for levado para o Lovable, não simplesmente converter o Python para React sem analisar a arquitetura.

O Lovable deve:

1. Entender o funcionamento atual.
2. Preservar as regras de negócio.
3. Preservar o fluxo de geração.
4. Preservar o conceito de histórico.
5. Separar interface e lógica de geração.
6. Evitar enviar senhas para um servidor sem necessidade.
7. Considerar geração local no navegador quando apropriado.
8. Usar uma fonte de aleatoriedade adequada para geração segura.
9. Não inventar funcionalidades inexistentes.

Uma possível arquitetura web seria:

```text
Usuário
   ↓
Interface Web
   ↓
Gerador de Senhas
   ↓
Fonte aleatória segura
   ↓
Senha gerada
   ↓
Histórico local opcional
```

Para uma versão web simples, não assumir que um backend é necessário.

---

## Persistência

Antes de implementar persistência, verificar a necessidade.

Para uma aplicação simples, possíveis alternativas são:

- JSON local;
- SQLite;
- armazenamento local do navegador em uma versão web.

Para senhas reais, considerar que armazenar histórico em texto puro aumenta o risco de exposição.

Uma versão mais segura pode utilizar:

- histórico desativado por padrão;
- armazenamento local protegido;
- criptografia apropriada;
- desbloqueio por senha mestre;
- expiração do histórico.

Não implementar criptografia sem uma implementação tecnicamente adequada.

---

## Validação

Tratar corretamente:

- entrada vazia;
- nomes longos;
- espaços;
- caracteres especiais;
- múltiplas gerações;
- limpeza do histórico;
- falhas de armazenamento.

Nunca exibir uma exceção técnica diretamente para o usuário final quando uma mensagem amigável for suficiente.

---

## Testes

Ao modificar o gerador, verificar:

### Geração

- uma senha é criada;
- a senha não é vazia;
- o tamanho atende à configuração;
- gerações consecutivas normalmente produzem resultados diferentes.

### Caracteres

Quando configurado:

- letras maiúsculas;
- letras minúsculas;
- números;
- caracteres especiais.

### Entrada

- campo vazio;
- nome de site;
- URL;
- caracteres especiais;
- nomes longos.

### Histórico

- registro da senha;
- associação com o site;
- múltiplos registros;
- limpeza explícita;
- geração continua funcionando depois de limpar.

---

## Regras para alteração do código

Antes de implementar uma mudança:

1. Ler o código existente.
2. Identificar onde a funcionalidade está implementada.
3. Fazer a menor alteração necessária.
4. Preservar funcionalidades existentes.
5. Evitar refatorações não relacionadas.
6. Evitar novas dependências sem necessidade.
7. Testar o comportamento afetado.

Não substituir uma implementação funcional apenas porque existe uma abordagem tecnicamente diferente.

---

## Segurança durante desenvolvimento

Nunca assumir propriedades de segurança apenas pelo nome do projeto ou pelo README.

Antes de afirmar que o projeto possui:

- aleatoriedade criptográfica;
- criptografia;
- armazenamento seguro;
- proteção de clipboard;
- proteção do histórico;

verificar o código.

A implementação é a fonte de verdade.

---

## Quando o requisito for ambíguo

Se uma solicitação puder alterar significativamente a segurança ou a arquitetura, preservar o comportamento atual e esclarecer a mudança necessária.

Exemplos:

- armazenar histórico permanentemente;
- sincronizar senhas com a nuvem;
- criar conta de usuário;
- adicionar backend;
- adicionar senha mestre;
- criptografar histórico;
- transformar a aplicação em SaaS.

Não implementar automaticamente uma dessas mudanças.

---

## Princípios para agentes de IA

Ao trabalhar neste projeto:

- Não inventar funcionalidades.
- Não remover funcionalidades existentes.
- Não expor senhas.
- Não adicionar dependências desnecessárias.
- Não migrar tecnologia sem autorização.
- Não afirmar segurança sem verificar a implementação.
- Não armazenar senhas remotamente sem necessidade.
- Priorizar mudanças pequenas e testáveis.

---

## Definition of Done

Uma alteração está concluída quando:

- a funcionalidade solicitada funciona;
- a geração existente continua funcionando;
- o histórico continua funcionando;
- nenhuma senha é exposta acidentalmente;
- não foram adicionadas dependências desnecessárias;
- a interface continua simples;
- os impactos de segurança foram considerados;
- o comportamento foi testado.

---

## Princípio principal

O projeto deve continuar sendo uma ferramenta simples, rápida e útil para geração de senhas.

A prioridade é:

**Segurança → Simplicidade → Usabilidade → Aparência**

Evitar complexidade que não gere benefício concreto para o usuário.
