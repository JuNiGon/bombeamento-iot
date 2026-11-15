# Bombeamento com telemetria IoT degradada: custo energético e margem adaptativa de pressão

Estudo em simulação (sem testes físicos) sobre estações de bombeamento com inversor de frequência cujo controle depende de medições recebidas por telemetria.

## Pergunta de pesquisa

Qual é o custo energético (kWh/m³ e R$) da degradação da telemetria (atraso, perda de pacotes, ruído, período de amostragem e dados falsos) em uma estação de bombeamento com inversor, e quanto desse custo pode ser recuperado ao tornar a folga de pressão uma função da idade e da confiabilidade da informação, sem aumentar a violação da pressão mínima?

### Perguntas secundárias

1. A partir de que atraso, taxa de perda ou nível de ruído o MPC deixa de superar o PID com setpoint compensado?
2. Um soft sensor de vazão baseado em potência, velocidade e altura manométrica mantém a malha utilizável quando o pacote de vazão se perde?
3. O resíduo entre a vazão estimada e a medida detecta dados falsos sem gerar alarmes em excesso?

## Hipóteses

| ID | Hipótese | Como pode ser refutada | Teste principal |
| --- | --- | --- | --- |
| H1 | A margem adaptativa reduz kWh/m³ em relação à margem fixa de pior caso, com a mesma taxa de violação da pressão mínima | Diferença não significativa, ou violação maior | Wilcoxon de postos sinalizados pareado por semente; cobertura empírica contra ε |
| H2 | O ganho do MPC sobre o PID com setpoint compensado diminui com o atraso e a perda, existindo um limiar em que a ordem se inverte | Nenhum cruzamento nas condições varridas | Diferença pareada de kWh/m³ por condição, com intervalo bootstrap |
| H3 | O soft sensor com calibração RLS reduz o tempo com pressão abaixo do mínimo durante quedas de telemetria de vazão | Nenhuma redução frente a manter a última amostra | Wilcoxon pareado |
| H4 | O resíduo de consistência física detecta injeção de dados falsos acima de certa magnitude, com falso alarme controlado | Curva ROC próxima do acaso | AUC com intervalo bootstrap; atraso de detecção |

Se uma hipótese for refutada, o resultado continua válido: mostra onde a complexidade não compensa.

## Regras do estudo

- Desfechos primários, testes e limiares são definidos e datados em `docs/plano_de_analise.md` **antes** de qualquer experimento.
- Parâmetros do supervisor e da margem são ajustados só em sementes de treino; a avaliação usa sementes de teste distintas.
- Correção de Holm sobre a família de testes primários; intervalos por bootstrap; tamanho de efeito reportado.
- Todo resultado vale para o **modelo**, não para uma estação específica.

## Estrutura do repositório

```
planta/        # modelo reduzido (bomba, coluna de água, inversor) e testes
rede/          # sensores, atraso, perda, ataque, vigia de dado velho
controle/      # B0, C1, C2, C3 (MPC), supervisor, soft sensor, RLS
cenarios/      # demandas, desgaste, ataques (arquivos de configuração)
experimentos/  # orquestrador, sementes, planos de análise
analise/       # estatística e figuras
docker/        # compose do modo de fidelidade (MQTT)
docs/          # plano de análise datado, relatório de validação
```

## Validação do simulador (antes de qualquer resultado)

1. Regime permanente do modelo reduzido contra o WNTR (tolerância inicial de 2%).
2. Reprodução do exemplo de economia do inversor do Doc 4 (62%, 44% e 23% para altura estática de 0, 20 e 40 m).
3. Convergência ao reduzir o passo de tempo.
4. Equivalência entre o modo rápido (fila em memória) e o modo MQTT.

## Limitações conhecidas

Sem dados de estação real; o controlador e a planta podem compartilhar o mesmo modelo (descasamento deve ser introduzido); rede emulada estatisticamente; planta sem golpe de aríete, bombas em paralelo e reservatório. Detalhes e agenda futura no estudo completo.

## Como rodar

A preencher quando o ambiente estiver montado (instalação, testes e execução de um experimento).

## Licença

A definir.