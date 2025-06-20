
# Documentação de Decisões Técnicas do Projeto Client Favorites API

## Introdução

Este documento visa apresentar as principais decisões arquiteturais e tecnológicas adotadas no desenvolvimento da API Client Favorites. O objetivo é explicitar os tradeoffs, pontos positivos e negativos, e justificar as escolhas técnicas frente a alternativas comuns no ecossistema Python e backend moderno.

## Escolha do Framework Web: FastAPI

Inicialmente, eu iria escolher o Flask, por ser mais simples e mais fácil de desenvolveer. Porém, pensando em performance, concorrência, escalabilidade e validação de dados, optei pelo FastAPI.

### Pontos positivos do FastAPI:

- **Alto desempenho:** graças ao Starlette e Uvicorn, o FastAPI entrega alta performance comparável a frameworks baseados em asyncio. O Flask, por outro lado, possuí menor foco em async, o que limita a escalabilidade em I/O-bound.
- **Validação automática:** a integração com Pydantic para validação e serialização dos dados traz segurança e agilidade na construção das rotas. Se tivesse optado pelo uso do Flask, teria que adicionar complementos externos, pois a tipagem não é integrada.
- **Documentação automática:** gera automaticamente documentação interativa via Swagger e Redoc, facilitando testes e entendimento da API.
- **Tipagem Python:** código mais claro, menos erros e melhor suporte a IDEs.

### Tradeoffs

- **Curva de aprendizado:** para equipes não acostumadas com Python assíncrono e Pydantic, o FastAPI pode ser mais complexo que frameworks tradicionais. Nesse ponto, o Flask é mais fácil de aprender e possui uma vasta comunidade.
- **Ecossistema menor que Flask:** Flask possui uma comunidade maior e mais plugins disponíveis, com mais tempo de mercado.
- **Menos flexível para casos específicos:** FastAPI é excelente para APIs, mas Flask pode ser mais flexível para apps web complexos, com múltiplas camadas de templates e estados.

## Escolha do ORM: SQLAlchemy Async

### Por que SQLAlchemy?

Usei ORM, pois é uma prática muito comum em API Restful. Eles facilitam a manipulação e leitura de dados.
Optei pelo SQLAlchemy, pois é um ORM popular e maduro do ecossistema Python. 

- **Flexibilidade:** permite escrever queries tanto em ORM quanto SQL puro.
- **Suporte à múltiplos bancos:** abstração bem feita para diversos bancos relacionais.
- **Comunidade ativa:** documentação robusta, inúmeros exemplos e ferramentas.

### Por que usar SQLAlchemy Async?

Confesso que antes desse desafio, eu havia apenas usado o SQLAlchemy na sua forma síncrona. Foi interessante ver que existe a sua forma Async, o que ajuda a otimizar as chamadas de I/O, melhorando performance e escalabilidade em operações concorrentes.

### Tradeoffs e pontos negativos

O SQLAlchemy é um ORM complexo, o que pode aumentar a curva de aprendizado. Além disso, tive dificuldades com partes async, pois nem todas as features do SQLAlchemy estão 100% para async. A principal dificuldade foi na hora de criar e rodar testes, pois haviam muitas questões envolvendo concorrencia no banco de dados.


## Banco de Dados: PostgreSQL

A ideia de um banco de dados relacional foi por conta das domínios e relações que existiam na aplicação (clientes e lista de favoritos). Escolhi PostgreSQL por ser um banco relacional robusto, open-source, com suporte avançado a tipos e extensões, além de excelente compatibilidade com SQLAlchemy.

### Tradeoffs

- **Complexidade de setup:** mais complexo que bancos NoSQL, exige modelagem e manutenção.
- **Escalabilidade vertical:** para alta escala horizontal, soluções NoSQL ou específicas podem ser mais indicadas.

## Autenticação e Segurança

Implementei autenticação via JWT, garantindo que cada cliente só acesse seus próprios dados de favoritos, sem necessidade de sessão ou estado server-side.

### Tradeoffs

- JWT facilita escalabilidade, mas requer atenção para expiração, renovação e revogação.
- Alternativa seria usar OAuth2 completo, mas complexidade maior e necessidade de provedor externo.

## Docker e DevOps

Uso Docker Compose para orquestrar containers da API e banco, facilitando desenvolvimento e deploy.

### Tradeoffs

- Facilita replicação do ambiente, porém adiciona uma camada de complexidade para quem não está familiarizado.
- Alternativa seria deploy direto no host, menos portável.

## Testes

Infelizmente, tive dificuldades com as configurações do ambiente de testes com a combinação FastAPI + SQLAlchemy Async. Tive problemas de configuração de um banco separado para os testes, a concorrencia na hora de fazer requisições ao banco. Caso queiram olhar, é só ir para a branch chore/tests e lá é possível conferir o setup do pytest.

## Melhorias futuras

Para o futuro, além dos testes unitários e de integração, eu adicionaria logs em pontos críticos, principalmente em fluxos de erros, para facilitar o debug no ambiente de produção. Um ponto que eu estudaria, seria adição de Cache, principalmente para as rotas de obter os dados do cliente e seus favoritos, para evitar requisições ao banco toda hora que é requisitado.

## Conclusão

Minhas escolhas priorizaram a escalabilidade, desempenho e modernidade da aplicação, com foco em boas práticas de desenvolvimento. Ao mesmo tempo, reconheço que cada decisão carrega complexidades e tradeoffs que devem ser bem compreendidos para garantir manutenção e evolução saudáveis do projeto.
