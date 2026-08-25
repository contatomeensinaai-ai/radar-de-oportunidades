---
name: rastrear-oportunidades
description: Use quando o usuário quiser localizar e qualificar empresas públicas com base em um Dossiê de Mercado, gerando relatório e CSV com evidências, sem contato automático. Não use para comprar listas, obter dados privados ou enviar prospecção.
---

# Rastrear oportunidades

Transforme a inteligência de mercado do usuário em uma lista revisável de empresas com aderência comercial. Trabalhe somente com dados comerciais públicos, preserve as fontes e deixe a decisão com a pessoa.

## Escolha o modo

### Modo VIP

Use como padrão quando houver um **Dossiê de Mercado** anexado, colado ou localizado no projeto.

1. Leia o dossiê completo.
2. Extraia nicho, regiões, perfil prioritário, dores, sinais de compra, exclusões e diferenciais.
3. Não repita a entrevista que já gerou o dossiê.
4. Pergunte somente por um dado realmente indispensável que não possa ser inferido nem marcado como `A CONFIRMAR`.

### Modo Comercial

Use quando o usuário não tiver dossiê. Faça uma coleta breve apenas dos itens necessários: oferta, região, perfil desejado, exclusões, objetivo da lista e quantidade aproximada. Marque lacunas como `A CONFIRMAR` e não invente critérios.

## Prepare a busca

Converta o contexto em critérios objetivos antes de navegar:

- quem entra e quem fica de fora;
- regiões permitidas;
- sinais públicos que indicam aderência;
- fontes aceitáveis;
- quantidade desejada;
- critério de prioridade.

Leia [critérios de qualificação](references/criterios-de-qualificacao.md) antes de pontuar empresas. Leia [navegação segura](references/navegacao-segura.md) quando for usar navegador, busca pública ou Browser Harness.

## Pesquise com evidências

Use os recursos de busca e navegador disponíveis no ambiente. Priorize Google Maps, pesquisa pública, site oficial da empresa, diretórios profissionais e perfis comerciais públicos no Instagram, Facebook ou LinkedIn.

Para cada empresa:

1. Confirme nome, categoria, região e URL principal.
2. Registre apenas dados comerciais anunciados publicamente.
3. Identifique sinais observáveis de aderência, necessidade ou oportunidade.
4. Guarde as URLs que sustentam cada conclusão.
5. Diferencie `CONFIRMADO`, `INFERIDO` e `NÃO ENCONTRADO`.
6. Elimine duplicatas por domínio, telefone comercial e combinação de nome com cidade.

Se uma plataforma exigir login, apresentar CAPTCHA ou bloquear a visualização pública, não contorne a proteção. Siga com outras fontes ou marque a informação como não encontrada.

## Qualifique

Pontue somente com base nos critérios extraídos do dossiê e nas evidências encontradas. Não trate a pontuação como verdade estatística. Ela é uma heurística para ordenar a revisão humana.

Empresas sem fonte verificável não podem receber prioridade máxima. Quando houver pouca evidência, reduza a confiança e explique por quê.

## Entrega

Produza dois arquivos:

1. `RADAR-DE-OPORTUNIDADES.md`, usando [o modelo de relatório](templates/RADAR-DE-OPORTUNIDADES.md).
2. `LEADS-QUALIFICADOS.csv`, usando [o cabeçalho do CSV](templates/LEADS-QUALIFICADOS.csv).

O relatório deve conter:

- critérios usados;
- data da pesquisa;
- fontes consultadas;
- resumo executivo;
- oportunidades priorizadas;
- limitações e itens a confirmar;
- próximos passos sugeridos, sem execução automática.

Ao terminar, execute `scripts/validate_radar_csv.py` quando o script estiver acessível. Corrija cabeçalhos, pontuações inválidas, duplicatas e evidências ausentes antes de entregar.

## Limites

- Trabalhe somente com dados comerciais públicos e necessários.
- Não colete dado pessoal oculto, sensível ou obtido por contorno técnico.
- Não faça login, não resolva CAPTCHA e não burle restrições de plataforma.
- **Não envie mensagens**, emails, DMs ou formulários.
- Não publique, não compre listas e não altere CRM sem autorização explícita.
- Não invente empresa, contato, review, dor, pontuação ou evidência.
- Uma abordagem sugerida é apenas rascunho para revisão humana.

## Próximo passo

Entregue a lista para revisão. Se o usuário quiser preparar contato, apresente rascunhos separados e obtenha aprovação explícita antes de qualquer envio.
