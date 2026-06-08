# Post-Mortem — Missão de Release

## Time
- Tech Lead: Douglas
- Dev A: Felipe de Freitas
- Dev B: Silvio
- QA/Release: Wagner Junior

---

## O que funcionou bem
As ferramentas do GitHub para verificar a criação/atualização/merge das braches.

## O que deu errado ou foi difícil
Devido a falta de costume em utilizar essa aplicação (ainda mais em grupo), perdemos muito tempo devido a uma caixa de seleção que estava fazendo os nossos pull requests serem enviados para o repositório original (e não o forkado).

## Onde usamos rebase (e por quê)
Usamos o rebase  nas branches de feature para deixar o histórico mais limpo (reescrevendo sobre o antigo histórico).

## Onde usamos merge (e por quê)
Usamos o merge para atualizar a branch de desenvolvimento. Utilizamos ela devido a forma que ela atua: preservando o histório e dando continuidade a ele.

## O que faríamos diferente
Não perderiamos tanto tempo com essa caixa de seleção (perdemos mais de 1 hora).
Dificuldade inicial para visualizar o merge do hotfix no develop. Tivemos que forçar um merge explícito para deixar o commit visível.
Entender o fluxo completo: feature → develop → release → main + hotfix paralelo.