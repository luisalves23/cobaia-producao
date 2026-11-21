# Histórico dos pedidos do Luis

Tudo o que o Luis pediu para mudar na produção, em ordem, de 01/11/2026 até a criação deste repositório. Serve para entender **por que** cada regra da skill existe.

> **Dossiê Cobaia 2.0 (21/11/2026):** o `DOSSIE.md` revogou parte destes pedidos (vinheta "Dia N de trinta" depois do gancho, gancho palavra por palavra, gancho em pergunta, palavras grandes no lugar da legenda, telas sempre simuladas, canal sem rosto, ensino por conceito). Este arquivo fica como histórico; o que vale está no dossiê e na skill.

**Como ler:**
- A `skill/SKILL.md` já incorpora tudo o que continua valendo. Em conflito, a skill vence este arquivo.
- Até 15/11 o canal usava a identidade antiga (biblioteca `telas/`, Liquid Glass nos cartões, legenda pequena, câmera lateral, HyperFrames, "constituição"). A partir de 16/11 vale a estética de motion aprovada, e o padrão final é o Dia 10 v3 (18/11). Pedidos antigos sobre visual e ferramenta foram substituídos; pedidos sobre roteiro, canal, aprovação, voz, chamada e post continuam valendo como estão na skill.
- Mudanças depois de 19/11 ficam no `CHANGELOG.md` da raiz, não aqui.

## 01/11 a 11/11 (identidade antiga)

- **2026-11-01, formato:** voz só do Luis e vídeo 100% gerado pelo Claude, cena a cena. Exemplos reais, nunca inventados. Motions, efeitos e música de bancos gratuitos populares, nada "padrão do Claude". Roteiro com cara de gente, só o texto que ele lê. Cortar os espaços vazios do áudio.
- **2026-11-01, marca:** @cobaia.dev em preto, off-white e vermelho. Mascote rato de laboratório branco de brinquedo (impresso em 3D, 4 cores, estilo desenho antigo). Sem Star Wars ou marcas registradas. Não expor cenário falso.
- **2026-11-02, série:** de "30 aulas" para "30 dias, 30 experimentos com Claude". Conteúdo viral e atual, não curso. Final com pergunta aberta, nunca sim/não (ex.: "O que vai acontecer com os editores de vídeo?").
- **2026-11-02, post:** depois de todo roteiro, legendas para Instagram, TikTok e Shorts. Barra de progresso dopaminérgica (rápida no começo, devagar depois). Grão/chiado bem mais leve.
- **2026-11-02, área útil:** respeitar a UI do TikTok e do Instagram. Glassmorphism sutil e jateado. Variar fontes. Mostrar as cenas para aprovação antes do vídeo, exceto se o Luis estiver ausente.
- **2026-11-02, liquid glass:** cartões menos foscos, com refração nas bordas estilo Apple. Legendas mais sutis. Barra de progresso não pode estourar à direita no último frame. CTA no estilo visual do TikTok com as cores da marca, com animação de alguém comentando. Ícone oficial do app do Claude (liquid glass) quando ele for citado. Logos oficiais das ferramentas citadas.
- **2026-11-02, Dia 1 refeito:** música bem mais animada, efeitos chamativos ("chuva de dopamina") e áudio pode ser acelerado.
- **2026-11-02, Dia 2:**
  - Jogo próprio do rato fugindo do cientista maluco, com fases difíceis e cores da marca.
  - Simular o Claude Code digitando e o jogo abrindo ao lado, com gameplay de verdade.
  - Telas tombando em 3D com zoom sem perder qualidade. Telas sempre simuladas.
  - Cada vídeo supera o anterior.
  - CTA de palavra-chave ("comenta JOGO que eu te mando o passo a passo grátis...") para entrega de PDF por direct.
- **2026-11-02, Dia 1 v4:**
  - **Regra prioritária: nada sobrepõe nada.** Cabeçalho com margem própria. Barra 2× mais alta (12 px). Legenda mais baixa (top 1452).
  - Calendário completo exatamente no "trinta". Corte de silêncios tátil (agarrar, esticar, cortar, reagrupar).
  - Ícone do Claude só quando falado, tombando no carimbo. Carimbo com desgaste real.
  - Transições de câmera da esquerda para a direita, sem tela parada.
  - "Guia do perfil" com negrito só nas palavras-chave, e liquid glass no cartão e nas cores (estilo ícone de app).
  - Texto lido como retângulos-palavra.
  - CTA: avatar centralizado com "+", fogos e ✓, coração que explode e só o campo de comentário digitando. Sem réplica da tela do TikTok e só o que está sendo falado.
- **2026-11-02, revisão interna do Dia 1 v4:**
  - Etapas da cena de silêncio viraram uma faixa rígida deslizante (a miniatura não cobre mais a onda).
  - O contador conta já ao aparecer.
  - Conversa do chat maior e centralizada, com palavras-chave em vermelho.
  - Confete do envio não cobre mais a pergunta.
  - O cartão de música mostra a faixa real usada.
- **2026-11-02, nota:** o Dia 1 v4 e o Dia 2 saíram com a barra de progresso linear, por regressão. A regra correta é a curva ^0.55 (seção 4).
- **2026-11-02, skill:** o Luis aprovou o Dia 1 v4 e o Dia 2 como "impecáveis" e pediu esta skill. Toda alteração futura deve ser registrada aqui.
- **2026-11-02, barra dinâmica:** o Luis pediu uma barra não literal: a primeira metade bem rápida (~5%/s), depois ~2%/s e, no fim, quase parando (~0,2%/s), porque no final a pessoa já está presa. A curva exponencial da seção 4 substitui a curva ^0.55. Os vídeos dos Dias 1 e 2 ficam como estão, por decisão do Luis; a nova barra vale a partir do Dia 3.
- **2026-11-02, plano novo dos 30 dias:** o Luis não gostou de parte dos temas e pediu temas virais e chamativos como os Dias 1 e 2, sem repetição. O Dia 3 é a skill que edita os vídeos, com "comenta SKILL" (manual grátis pra criar skills). Os Dias 4 a 30 foram refeitos com pesquisa do que mais viraliza sobre o Claude; a tabela fica no Doc.
- **2026-11-02, um roteiro por vez:** o Luis pediu o roteiro completo só do Dia 3, "viral e cheio de gatilhos e ganchos". Os próximos são escritos um a um, depois de cada gravação (seção 8).
- **2026-11-02, Dia 3 v2 (roteiro):** o Luis achou o gancho "Um arquivo de texto editou esse vídeo" repetitivo com o Dia 1 e pediu:
  - Explicar o que é skill construindo o hype ("uma habilidade que o Claude tem") e depois quebrando (é um arquivo de texto), com os ajustes dos Dias 1 e 2 como exemplo.
  - Manter o loop "o truque que esse vídeo tá usando em você".
  - Tom de senioridade: "você não precisa escrever, o Claude escreve a sua", nunca "eu não escrevi".
  - Mostrar o valor do perfil (curso pago contra um minuto aqui) e pensar o motion junto com o roteiro.
  - Nunca expor código na tela nem revelar estratégias como a barra dinâmica.
  - Teaser mais absurdo e grave, e no fim "comenta EU QUERO" pra liberar o jogo do Dia 2.
  - Regras novas nas seções 2 (10 e 11), 7, 8 e 11.
- **2026-11-02, propósito do canal e Dia 3 v3:** o Luis achou o roteiro v2 engessado e raso sobre skills. Ele pediu:
  - Nenhuma palavra repetida na frase ("todo mundo" 2×, "trinta" 3×) e nada de "truque" em todo vídeo: estrutura dinâmica, sem fórmula.
  - Explicar skill de verdade e tirar o pedido do jogo ("EU QUERO") pra ganhar tempo.
  - O canal ensina o Claude (skills, conectores, MCP, Cowork, Claude Desktop), de forma lúdica e com exemplos da vida real como o do pão de queijo. Ferramentas de fora só quando ajudam a explicar o Claude. O Luis também quer aprender.
  - Telas do Claude sempre simuladas e zoom de janela: a janela inteira cresce até a área útil, com o conteúdo junto, como uma pinça.
  - Refazer os 30 dias com os principais recursos do Claude e conceitos difíceis explicados de forma simples. O plano novo está no Doc.
  - Regras novas nas seções 1, 5, 7, 8 e 11.
- **2026-11-02, pasta por vídeo e PDF sob pedido:** o Luis pediu que cada vídeo seja entregue numa pasta própria com vídeo, legendas das 3 redes, capa e o resto do material, também para os Dias 1 e 2. O PDF/ebook de cada vídeo só é feito quando ele pedir, porque ele ainda pode pedir mudanças. Ele pediu o material do Dia 2 (JOGO). As legendas seguem o formato da agência. Regras novas nas seções 7, 8, 10 e 11.
- **2026-11-02, Dia 3 (áudio e vídeo):** o Luis gravou o Dia 3 e pediu: "edita, faça as correções e depois produz o vídeo porque vou estar ausente", e depois "faça tudo mas faça o melhor, dê o seu máximo". O vídeo saiu direto, sem prévia (regra dos 30 min). Regras novas:
  - Marcador "corrigindo" na gravação e correção da transcrição pelo roteiro (seção 9).
  - Música recortada no beat (seção 9).
  - Partículas atrás da câmera e selo ✕ ao lado, nunca por cima (seção 5). Carimbo `.ink` sobre papel (seção 3).
  - Legendas sem piscadas: faixas escondidas terminando no bloco seguinte e nenhum bloco curto demais (seções 4 e 11).
  - Versão leve com bitrate pela duração para ficar abaixo de 25 MB; render final completo (seções 10, 11 e 12).
  - Cenas do Dia 3 na biblioteca (seção 6), ainda sem o retorno do Luis. Fonte completa do Dia 3 em `videos/fonte/dia03/` (seção 12).
- **2026-11-02, cópia no PC:** o Luis pediu que, ao finalizar cada conteúdo, a versão na qualidade recomendada para as redes (a HQ) seja copiada para a pasta do dia em `C:\Users\usuário\cobaia\diaNN\`, até o fim dos 30 dias. Regra nova na seção 10, passo 9. Se não houver ferramenta de transferência na sessão, o Luis baixa da Biblioteca.
- **2026-11-08, Dia 4 v3:** HyperFrames mantendo a identidade; Humanizer nos roteiros; vida real e resultado na tela em vez de conceito; surgimento de texto mais orgânico; aprovação só por frames estáticos; tags do ElevenLabs animadas. Lições pendentes dos Dias 4 e 5 em `skill/licoes-pendentes-dia04.md`.
- **2026-11-09, Dia 4 v4:** tela sem moldura com zoom inclinado no ponto do clique; cursor branco guiando a fala; tela inteira só para visão geral; desfoque rápido e sutil; contador gigante para números exagerados; grátis em verde com caixa registradora; chamada final sempre igual à do Dia 3; vídeo em loop; canal dark sem nome ou dado do Luis. Código base movido para `skill/codigo-base.md`.
- **2026-11-09, Liquid Glass do site:** o Luis aprovou o vidro da barra do topo do site e pediu o mesmo nível em todos os cartões, modais e caixas, inclusive nos vídeos. Código em `skill/liquid-glass.md`.
- **2026-11-09, site junto com o vídeo:** o Luis aprovou o site cobaia-dev.vercel.app e pediu que todo vídeo criado ou editado atualize também a página dele no site.
- **2026-11-09, Dia 5 v2:** telas em perspectiva 3D, mockups genéricos de UI, música contínua do começo ao fim e trilha que acompanha a narrativa; voz alinhada pelo texto quando o whisper está bloqueado (`skill/padroes-dia05-v2.md`).
- **2026-11-10, revisão da skill e biblioteca única:** o Luis pediu uma análise da skill (pontos fortes, fracos e melhorias), disse que o Dia 5 não seguiu HyperFrames, a biblioteca de áudios e a identidade dos 30 dias, e pediu "faça as melhorias e correções", com tudo o que puder ser reaproveitado vindo sempre da biblioteca. Mudou:
  - Regra "biblioteca primeiro" (seção 0). Biblioteca `telas/` ganhou o kit de identidade (`kit/`), o áudio (`audio/`, 31 efeitos, 2 músicas, créditos), os scripts (`scripts/`), CATALOGO.md e catalogo.jpg.
  - Modelo novo `videos/template/` em HyperFrames ligado ao kit; o antigo virou `videos/template-antigo/`. Render só pelo `hyperframes render`, checagem pelo `hyperframes check`.
  - Decisões do Luis nos cartões: render só com roteiro e storyboard aprovados, salvo aviso de ausência (sai a regra dos 30 min); vinheta logo depois do gancho; gancho sempre do banco de virais, trocando se a estrutura lembrar um dia anterior; material de quem comenta pela página do site com link enviado à mão, sem automação de DM e sem agência; voz gravada ou de IA, escolhida por vídeo.
  - Incorporadas as lições pendentes dos Dias 4 e 5 e os padrões do Dia 5 v2. Regras novas: laranja só no Claude, legenda escondida em título falado, nenhuma tela quase igual por mais de ~2,5 s, música sem repetir a dos três dias anteriores, sons só da biblioteca.
  - Changelog saiu da skill e fica só neste arquivo.
- 2026-11-10 (Dia 5 aprovado): o Luis definiu que "o vídeo tem que ter 60 segundos... regra pétrea... registrada na skill", recusou a voz a 1,13x e pediu para desacelerar, mandou "nunca deixe passar essa CTA" e vetou tags e cochicho na voz de IA. Mudou: 60 s vira teto duro nas Regras invioláveis (vídeo inteiro, com chamada e loop; meta perto de 60 sem passar); atempo ~1,03 a 1,05, cortando um exemplo inteiro em vez de acelerar; chamada "Segue o cobaia, curte e comenta PALAVRA" obrigatória, com emenda de vídeo anterior se a gravação vier sem ela; voz de IA sem tags e sem cochicho; QA compara o último frame com o primeiro; entrega em videos/diaNN/<versão>/postar/ e carrossel antigo marcado como "não combina" se o tema mudar.

- **2026-11-11, zoom na ênfase e reação real.** O Luis pediu zooms onde ele dá ênfase ou mostra algo, zoom leve acompanhando o mouse nas telas simuladas, a reação gravada dele cortada curta dentro do vídeo e liberou acelerar o vídeo se precisar. Mudou: seção 5 (zoom leve que segue o cursor e o ponto enfatizado na fala; reação real do Luis curta, até ~3 s, acelerada até 1,15x, com dados sensíveis borrados).
- **2026-11-11, músicas e efeitos novos.** O Luis pediu: "Pode baixar outras músicas, efeitos visuais, deixa global, põe na constituição e na skill onde encontrar", efeitos "que não sejam tão óbvios", trilha que se adapta à emoção e barra de progresso também no render. Mudou: regra 3 e seção 9 da skill (fontes Mixkit por ID, medir-musica.py, sintetizar-sfx2.py, trilha por segmentos no mix.py, efeitos menos batidos); constituição Art. 7 e Art. 8 §5.

## 16/11 a 17/11 (estética nova)


Última mudança: **2026-11-17, correções do Dia 09.** O Luis revisou o primeiro take do Dia 09 segundo a segundo e pediu que a skill passasse a fazer assim (sem refazer o vídeo): gancho de 3 s mais denso, a coisa real na tela em flat (prova, calendário, mapa, professor, lista de exercícios), elemento vermelho como guia que se transforma, contorno em leque de 3 vermelhos com quebra no canto inferior esquerdo, alternar janela e cena, logos oficiais (Claude sempre que falado, GitHub), verde para o positivo, duas fontes por frase e animação por fonte, desfoque de lente fora da área segura e nova chamada final (foto de perfil + @cobaia.dev, seguir, curtir, comentar digitando, 2 s roxos sem fala e loop). Mudou: regras 5, 12, 14 e 15 da seção 2, seção 5.0 e seção 7.

Mudança anterior à última: **2026-11-16, estética de motion aprovada.** O Luis aprovou o teste "07 · Síntese" como a estética de todos os vídeos daqui pra frente, pediu vídeos de no máximo 60 segundos e a chamada final na tela roxa com "comenta PALAVRA" em neon. Mudou: seção 5.0 nova, seção 7 (chamada final), regra 14 (cores) e seção 8 (duração).




## 18/11: Dia 10 v3 aprovado e identidade nova

O Luis aprovou a v3 do Dia 10 ("quem tá roubando seu Wi-Fi?") como padrão, pediu para levar à skill tudo o que pediu nele, com o som do movimento do elemento vermelho 30% mais baixo, e aprovou a identidade nova das capas e do site. Pedidos do Dia 10 que viraram regra:
- Um único elemento vermelho do começo ao fim: "o elemento de destaque da cena anterior é deformado e comprimido até virar uma bola, e dessa bola ele se transforma no próximo elemento, sempre de forma orgânica." Nunca animação padrão ou engessada. A bola deixa o lugar vazio, viaja em arco com uma voltinha e a cena se monta em volta dela.
- Antes do storyboard, escrever a corrente "veio de → vira" batida por batida.
- A palavra "Claude" se transforma, girando, na logo laranja (~0,1 s depois da fala, ~0,28 s de transformação); palavra e logo nunca competem. "Toda vez que 'Claude' é falado, a logo aparece."
- Outras ferramentas com a cara oficial delas (GitHub com estrelas amarelo-ouro etc.).
- Foto de perfil do canal em todos os vídeos, capas e site, com "@cobaia.dev" logo abaixo; "+" por cima da moldura.
- DM com o link sozinho numa linha; o Luis manda à mão.
- Capas na identidade nova (DIA NN em Anton vermelho, gancho em duas linhas, cartão com leque e ilustração flat, rodapé com foto e "comenta PALAVRA").
Mudou na skill: regras 5 e 12 da seção 2, seção 5.0, seção 6, seção 7, seção 9 (som) e seção 10 (capa e site).

## 18/11: Dia 11 (exceção)

Vídeo especial do GTA VI com paleta própria (violeta, magenta, coral, laranja, amarelo) e música enviada pelo Luis. **Não é padrão.** Fica em `exemplos/dia11-paleta-gta/` só como exemplo de troca de paleta e de remontagem de música.

## 19/11: repositório compartilhado

O Luis pediu este repositório para que uma segunda conta do Claude produza com o mesmo resultado, e para as duas contas se manterem sincronizadas: `git pull` antes de cada produção e commit com entrada no `CHANGELOG.md` depois de cada melhoria. Vídeos com o rosto do Luis vão entrar depois, em `formatos/face-cam/`, com regras que ele vai escrever.
