# Podcast Jesus vs. Diabo — produção 3D cinematográfica

Vídeos no formato "podcast" entre Jesus e o Diabo, em estilo **3D de longa-metragem de animação** (cinematográfico). O vídeo de referência usa traço simples em preto e branco; aqui o objetivo é outro nível visual.

## Arquivos
| Arquivo | Conteúdo |
|---------|----------|
| [`PERSONAGENS.md`](PERSONAGENS.md) | Ficha visual fixa + prompts de imagem de Jesus, do Diabo e do plano duplo |
| [`CENAS.md`](CENAS.md) | 13 planos de câmera com prompts de movimento (imagem → vídeo), dicas de som |
| [`ROTEIRO-EP01.md`](ROTEIRO-EP01.md) | Roteiro completo do episódio 1, marcado com os planos |

## Fluxo de produção
1. **Personagens:** gerar os retratos (Prompt 1) de cada personagem → escolher o melhor → usar como referência fixa.
2. **Cenas:** gerar as imagens de cada plano de `CENAS.md`, sempre com a referência do personagem.
3. **Animação:** cada imagem → vídeo de 5–10 s com o prompt de movimento correspondente.
4. **Voz:** gravar ou gerar as falas do roteiro (duas vozes bem diferentes).
5. **Edição:** montar seguindo o roteiro, com trilha, foley e legendas animadas.

## Chave de API
Nunca coloque a chave no código nem no repositório. Use variável de ambiente:
```bash
export HYPER3D_API_KEY="sua-chave"
```
