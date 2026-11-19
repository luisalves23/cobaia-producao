# Capas (identidade nova, 17/11/2026)

`capas.html` desenha a capa 1080×1920 de cada dia (`capa(n)`) e os destaques do Instagram (`destaque(kind)`).

- Dia novo: acrescente a entrada em `DAYS` (linha 1 em serif, linha 2 em Anton, palavra-chave `kw`) e a ilustração flat em `ILL`.
- Gerar: `DIAS=12 node shot_capas.cjs saida/` (vários: `DIAS=11,12`).
- `exemplos/`: capas dos Dias 1 a 10 já na identidade nova, para conferir a grade do perfil.
- A capa do Dia 11 (paleta GTA) está em `exemplos/dia11-paleta-gta/` e não é padrão.
