# Prompt para abrir uma conta nova

Cole o texto abaixo no primeiro chat de um projeto novo, na conta que vai produzir os vídeos.

---

Você vai assumir a produção dos vídeos do meu perfil @cobaia.dev (série "30 dias, 30 experimentos com Claude"). Outra conta do Claude produzia até agora, e tudo o que ela aprendeu está no meu repositório privado do GitHub `luisalves23/cobaia-producao`. Quero que você entregue exatamente o mesmo resultado que ela, sem eu ter que ensinar de novo.

Faça nesta ordem:

1. Conecte-se ao repositório `luisalves23/cobaia-producao` (adicione ao projeto, se puder) e clone.
2. Leia o `CLAUDE.md` inteiro e siga a ordem de leitura dele: `DOSSIE.md` (Dossiê Cobaia 2.0, a regra principal), `skill/SKILL.md` inteira, `CHANGELOG.md`, `skill/historico-pedidos.md`, `referencia/dia10-v3/` (assista o MP4 leve e leia o `d10.html`) e `motor/LEIAME.md`.
3. Prepare o ambiente e faça a verificação da seção "Verificar uma instalação nova" do `motor/LEIAME.md`: o quadro de 7,5 s que você renderizar tem que bater com o vídeo aprovado, e o `a10.py` tem que gerar 54,8 s de áudio. Me diga o resultado com números.
4. Instale a skill `cobaia-dev-videos` nesta conta com o conteúdo de `skill/SKILL.md` (veja `skill/COMO-INSTALAR.md`).
5. Me devolva um resumo curto, com suas palavras: o pipeline de um vídeo, as 10 regras que você considera mais importantes, o que fazer quando eu pedir uma mudança e quais temas e apps já foram usados.

Regras permanentes desta conta:
- Antes de cada produção ou mudança: `git pull` e leitura das entradas novas do `CHANGELOG.md`. A outra conta também trabalha neste repositório.
- Quando eu pedir qualquer mudança no jeito de produzir, siga a seção "Quando o Luis pedir uma mudança" do `CLAUDE.md`: atualize o arquivo certo, registre no `CHANGELOG.md`, faça commit e push no mesmo dia e atualize a skill instalada.
- Não use nada do repositório antigo `kit-edicao-`: é a identidade antiga e não vale mais.
- Nunca renderize sem roteiro e storyboard estático aprovados por mim.
- O `DOSSIE.md` vale por cima de qualquer regra antiga. Em toda entrega, me mostre o checklist da seção 11 dele preenchido.

Não comece nenhum vídeo ainda. Termine os 5 passos e espere o tema do próximo dia.
