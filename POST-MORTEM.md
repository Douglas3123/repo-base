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
Não usamos rebase devido a forma que ele atua no histórico de commits: deletando a linha do tempo original e substituindo por uma nova.

## Onde usamos merge (e por quê)
Usamos o merge para atualizar a branch de desenvolvimento. Utilizamos ela devido a forma que ela atua: preservando o histório e dando continuidade a ele.

## O que faríamos diferente
Não perderiamos tanto tempo com essa caixa de seleção (perdemos mais de 1 hora).