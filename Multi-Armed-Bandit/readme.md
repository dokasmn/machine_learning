## README para Algoritmo Multi-Armed Bandit

### Multi-Armed Bandit

**Descrição:**

O problema Multi-Armed Bandit é um clássico problema de otimização em que um jogador deve escolher entre várias opções (ou "bandidos") com recompensas desconhecidas e estocásticas. O objetivo é maximizar a recompensa total ao longo do tempo, explorando e explorando essas opções.

**Como Funciona:**

1. **Inicialização:**
   * Cada bandido tem uma estimativa inicial de recompensa, geralmente configurada como zero.
2. **Seleção de Ação:**
   * Usa uma estratégia de ε-greedy para selecionar a ação:
     * **Exploração** : Com probabilidade ε, escolhe um bandido aleatório.
     * **Exploração** : Com probabilidade 1 - ε, escolhe o bandido com a maior recompensa estimada.
3. **Atualização das Estimativas:**
   * Após a escolha de um bandido e a obtenção de uma recompensa, atualiza a estimativa da recompensa para esse bandido.

**Código Exemplo:**

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copiar código</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import numpy as np

# Parâmetros
num_bandidos = 5
num_rodadas = 1000
epsilon = 0.1

# Inicialização
recompensas_verdadeiras = np.random.randn(num_bandidos)
estimativas_recompensa = np.zeros(num_bandidos)
contadores = np.zeros(num_bandidos)

total_recompensa = 0

for _ in range(num_rodadas):
    if np.random.rand() < epsilon:
        acao = np.random.randint(num_bandidos)  # Exploração
    else:
        acao = np.argmax(estimativas_recompensa)  # Exploração

    recompensa = np.random.randn() + recompensas_verdadeiras[acao]
    contadores[acao] += 1
    estimativas_recompensa[acao] += (recompensa - estimativas_recompensa[acao]) / contadores[acao]
    total_recompensa += recompensa

print(f"Recompensas verdadeiras: {recompensas_verdadeiras}")
print(f"Estimativas de recompensa: {estimativas_recompensa}")
print(f"Total recompensa obtida: {total_recompensa}")
</code></div></div></pre>

**Explicação do Código:**

* Inicializa os parâmetros e as estimativas de recompensa.
* Usa uma estratégia ε-greedy para escolher entre diferentes bandidos.
* Atualiza as estimativas de recompensa com base nas recompensas obtidas.
* Calcula e imprime a recompensa total e as estimativas finais.
