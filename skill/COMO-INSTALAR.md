# Como instalar a skill numa conta do Claude

A skill `cobaia-dev-videos` mora em `skill/SKILL.md`. Ela precisa estar instalada em cada conta que produz vídeos, e as cópias são mantidas iguais ao arquivo deste repositório.

## Primeira vez
- No claude.ai: Configurações → Capacidades → Skills → criar skill e colar o conteúdo de `skill/SKILL.md` (com o cabeçalho `name` e `description`). Ou peça ao próprio Claude: "instale como skill o arquivo skill/SKILL.md do repositório cobaia-producao", e aprove o cartão que ele mostrar.

## Depois de cada mudança
1. `git pull`.
2. Se o `CHANGELOG.md` mostra mudança na skill, peça ao Claude da sua conta para atualizar a skill instalada com o `skill/SKILL.md` atual.
3. Se a mudança foi feita na sua conta, o Claude edita `skill/SKILL.md`, registra no CHANGELOG, faz push e atualiza a skill instalada.

Os caminhos citados na skill são relativos à raiz deste repositório.
