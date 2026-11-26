# Guia do projeto: portfólio LR (base: template Kairo, ProfitizeBuild)

Portfólio feito sobre a template **Kairo** da ProfitizeBuild (licença: uso próprio e de clientes, não revender nem publicar o prompt).
Vite sem framework, GSAP, Anton, Caveat e Manrope pelo Fontsource. **O site se monta na frente de quem visita:** um enxame de cursores de editor multiplayer desenha cada bloco (caixa azul com medida → esboço → conteúdo), copia itens de lista, arrasta peças até encaixar e testa os componentes. O conteúdo é HTML de verdade desde o início; o enxame só lê atributos.

## Marca LR (já aplicada)
- Logo em vetor (L lavanda + R em degradê roxo `#9b7dff` → azul `#5b8dff` → verde-água `#36e6c8` + quadrado `#2ff0c8`) em três lugares: `src/sections/nav.html`, a função `intro` de `src/motion/enxame.js` e `public/favicon.svg`. O PNG original está em `fonte/logo-lr.png`.
- Paleta em `src/styles/tokens.css`. Os nomes `--vermelho*` ficaram da template, mas os valores agora vêm da logo: `--vermelho` `#6a5cff` (botões e blocos), `--vermelho-texto` `#3fe6cc` (números e palavras de destaque), `--ponto` `#2ff0c8` (o ponto final quadrado `.pq`), `--titulo-topo/meio/pe` (degradê do PORTFÓLIO), `--card-topo/pe` (card do Sobre), `--pagina` `#0c0b14`.
- Nenhuma cor solta nas seções: tudo sai dos tokens.

## Arquitetura
- Uma seção por arquivo: o `index.html` só tem `<!-- @secao nome -->`, e o plugin do `vite.config.js` troca pela `src/sections/<nome>.html`. CSS de cada seção importado em `src/main.js`.
- Escalas: hero em `--u` (1 px num quadro 1440 × 900); demais seções em `--su` (1 px a partir de 1280). Tamanhos saem dos tokens.
- Enxame (`src/motion/`): `data-camada` (`quadro`, `titulo`, `texto`, `bloco`, `foto`), `data-montagem`, `data-parte` (hero no celular), `data-reforco`, `data-duplica` (listas), `data-ajusta="dx,dy"`, `data-teste`, `data-fecho`/`data-alvo`.
- Imagens em `public/img/` (WebP): retrato recortado com alfa 900 px, telas 1280 × 800 em modo escuro, wireframe no mesmo enquadramento.

## Regras
- Toda peça nova que deva ser montada ganha `data-camada`; lista repetida ganha `data-duplica`. Elemento com `data-ajusta` não pode ser `inline`. Texto dentro de botão/link `flex` com `gap` vai num `<span>`.
- Telas de projeto em modo escuro (tela branca estoura ao gravar com o celular).
- Celular (corte em 760 px): nada rola para o lado, alvos de 44 px, campos com fonte 16 px, títulos em no máximo duas linhas.
- Nada de número, nota, cliente, projeto ou depoimento inventado: o que não foi informado fica `[preencher]` (nunca no título).

## O que muda e onde
| o quê | onde |
|---|---|
| Nome, `<title>`, `description` | `index.html`; `hero.html` (h1), `contato.html` (rodapé e card de replay); nome na nav em `nav.html` (`.nav__nome`, hoje removido) |
| Hero (cargo, texto, botão, local, números) | `src/sections/hero.html` |
| Foto do hero | removida a pedido (o hero fica só com o título PORTFÓLIO) |
| Projetos | `src/sections/projetos.html` (imagem, alt, etiqueta, número, nome, categoria/ano, `data-tipo`, `data-busca`) |
| Ferramentas | `.ferramentas__trilho` em `projetos.html`, "Ver todas (N)" e texto em `interface.js`; logos em `icones.html` |
| Comparador | segunda `<section>` de `projetos.html`; `proj-balcao.webp` + `wire-balcao.webp` |
| Sobre | `src/sections/sobre.html` |
| Trajetória | `src/sections/trajetoria.html` |
| Contato e formulário | `src/sections/contato.html`; e-mail do formulário em `src/motion/interface.js` (`formulario`) |

Receitas de imagem (prompts) e prints de referência da demo estão em `referencia/`.

## Como checar
1. `npm run dev` (porta 5300). Olhar a 1456 × 840 e a 390 × 844.
2. Com `?pronto`: página já montada. Sem: abertura com a logo e os cursores, hero em ~7 s.
3. Tour na barra do pé até o fim; velocidades 2×/4×; "montar de novo".
4. Filtro/busca, faixa de ferramentas, comparador, sanfona, formulário, replay.
5. Celular sem rolagem lateral; console sem erros; `npm run build` passa. O `dist/` sobe em qualquer hospedagem estática.
