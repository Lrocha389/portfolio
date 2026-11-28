# Portfólio do Leonardo

No ar em **https://lrocha389.github.io/portfolio/**.

Portfólio de desenvolvedor full-stack com dois trabalhos reais: BarberGest (Barbearia VIP) e Gorillaz BJJ Manager. A página se monta na frente de quem visita: um enxame de cursores, como num editor multiplayer, desenha cada bloco, copia itens de lista e encaixa as peças.

Feito em Vite sem framework, com GSAP e as fontes Anton, Caveat e Manrope (Fontsource). Base: template Kairo, da ProfitizeBuild.

## Rodar no computador

```bash
npm ci
npm run dev        # http://localhost:5300
```

Com `?pronto` no fim do endereço, a página abre já montada.

## Publicar

Cada envio para a `main` dispara a automação em `.github/workflows/pages.yml`, que faz o build e publica no GitHub Pages. No repositório, **Settings → Pages → Source** fica em **GitHub Actions**.

## Onde mudar o quê

- Textos de cada seção: `src/sections/*.html` (hero, projetos, sobre, trajetória, contato).
- Cores: `src/styles/tokens.css`.
- Imagens: `public/img/`. A imagem de compartilhamento é `public/og.jpg`, gerada por `fonte/og.py`.
- O hero não tem foto (a foto de perfil foi retirada).
