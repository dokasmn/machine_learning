## README para Algoritmo de Q-Learning

### Q-Learning

**Descrição:**

Q-Learning é um algoritmo de aprendizado por reforço utilizado para encontrar a política ótima que maximiza a recompensa acumulada de um agente em um ambiente. O Q-Learning é um método off-policy, o que significa que ele aprende sobre a política ótima independentemente da política que está sendo seguida.

**Como Funciona:**

1. **Inicialização:**

   * Cria uma tabela Q (`Q_table`) onde cada entrada Q(s, a) representa o valor esperado de tomar a ação `a` no estado `s`.
2. **Exploração e Exploração:**

   * Utiliza uma estratégia ε-greedy para escolher ações:
     * **Exploração** : Com probabilidade ε, escolhe uma ação aleatória.
     * **Exploração** : Com probabilidade 1 - ε, escolhe a ação com o maior valor Q para o estado atual.
3. **Atualização da Tabela Q:**

   * Após a ação ser tomada e o novo estado ser alcançado, atualiza o valor Q usando a fórmula:
     Q(s,a)←Q(s,a)+α[r+γmax⁡a′Q(s′,a′)−Q(s,a)]Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]**Q**(**s**,**a**)**←**Q**(**s**,**a**)**+**α**[**r**+**γ**a**′**max****Q**(**s**′**,**a**′**)**−**Q**(**s**,**a**)**]**

   Onde:

   * `α` é a taxa de aprendizado.
   * `r` é a recompensa recebida.
   * `γ` é o fator de desconto.
   * `s'` é o novo estado.
   * `a'` são as ações no novo estado.
4. **Repetição:**

   * Repete o processo até que a política esteja suficientemente refinada, ou um critério de parada seja atingido.

**Código Exemplo:**

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copiar código</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import numpy as np
import gym

# Criação do ambiente
env = gym.make('FrozenLake-v1', is_slippery=False)

# Inicialização da tabela Q
Q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Parâmetros do algoritmo
num_episodes = 1000
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1

for episode in range(num_episodes):
    state = env.reset()
    done = False
    while not done:
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Exploração
        else:
            action = np.argmax(Q_table[state])  # Exploração
      
        new_state, reward, done, _ = env.step(action)
      
        Q_table[state, action] = Q_table[state, action] + learning_rate * (
            reward + discount_factor * np.max(Q_table[new_state]) - Q_table[state, action]
        )
      
        state = new_state

print("Tabela Q final:")
print(Q_table)
</code></div></div></pre>

**Explicação do Código:**

* Inicializa o ambiente e a tabela Q.
* Itera por vários episódios, ajustando a tabela Q com base na recompensa e no valor futuro esperado.
* O processo de exploração/exploração garante que o agente descubra novas estratégias e refine suas ações com o tempo.
