# project-smart_house-python_oo-rria
Projeto feito como avaliação parcial da disciplina de Python (Orientação a Objetos) da Pós Graduação em Robótica e Inteligência Artificial do CIn-UFPE | Softex

## Visão Geral do Projeto
O projeto consiste de uma representação simplificada de um sistema de gerenciamento de **Casa Inteligente**. O sistema suporta três tipos de dispositivo [Luz](src/dispositivos/luz.py), [Termostato](src/dispositivos/termostato.py) e [Sistema de Segurança](src/dispositivos/sistema_seguranca.py). Cada dispositivo possui uma máquina de estados que descreve o comportamento do dispositivo, e controla suas mudanças de estado. O sistema também suporta a adição e remoção de dispositivos dinamicamente.
Além disso, o sistema implementa os padrões de projeto _Singleton_ (tanto na classe `Main` que implementa a interface de linha de comando, quanto na `CasaInteligente`, que gerencia os dispositivos), _Factory_ (na classe `DispositivoFactory` para a criação das instâncias dos dispositivos na casa) e _Observer_ (entre os dispositivos inteligentes, que herdam da classe `Observable Device` e os dispositivos que herdam de `Observer` que foram implementados somente como simplificações de `Celular` e `EMail`), e aplica técnicas de programação funcional, como compreensões de listas, `map`, `filter`, e `reduce` para lidar com os dispostivos adicionados na casa.
Vale ressaltar que o sistema foi implementado com a biblioteca `transitions` para gerenciar as máquinas de estados dos dispositivos. E algumas das decisões de implementação foram tomadas para exercitar os conceitos vistos em sala de aula, e não necessariamente representam a melhor solução para um sistema de casa inteligente real.

## Executando o Projeto Localmente:
Para executar o projeto localmente, siga os passos abaixo:
**1. Crie um ambiente virtual com `venv`:**

_Bash_
```bash
python3 -m venv venv
```

_PowerShell_
```powershell
python -m venv venv
```

**2. Ative o ambiente virtual:**

_Bash_
```bash
source venv/bin/activate
```

_PowerShell_
```powershell
.\venv\Scripts\Activate.ps1
```

**3. Instale as dependências do projeto:**

_Bash ou Powershell_
```bash
pip install -r requirements.txt
```

**4. Execute o projeto:**

_Bash_
```bash
python3 main.py
```

_PowerShell_
```powershell
python .\src\main.py
```

Por padrão, a casa inteligente é inicializada com um limite de 5 dispositivos. Para alterar o limite de dispositivos, use o argumento `-m` ou `--max-devices`:

_Bash_
```bash
python3 .\src\main.py -m 10
```

_PowerShell_
```powershell
python .\src\main.py --max-devices 10
```

**5. Não esqueça de desativar o ambiente virutal:**

_Bash ou PowerShell_
```bash
deactivate
```

## Principais Componentes e Padrões de Design Utilizados:

| Componente | Padrão de Projeto | Descrição |
|------------|-------------------|-----------|
| `Dispositivo` | - | Classe abstrata que define a interface para os dispositivos da casa inteligente. |
| `ObservableDevice` | Observer | Classe que notifica mudanças de estado para os observadores. |
| `Luz`, `Termostato`, `SistemaSeguranca` | - | Classes concretas que implementam a interface `ObservableDevice`. |
| `Celular`, `EMail` | Observer | Classes que observam mudanças de estado nos dispositivos. |
| `DispositivoFactory` | Factory | Classe que cria instâncias de diferentes dispositivos. |
| `CasaInteligente` | Singleton | Classe que gerencia os dispositivos da casa inteligente. |
| `Main` | Singleton | Classe que implementa a interface de linha de comando para interação com o sistema. |

## Exemplos de Uso da CLI:
Ao executar o projeto, a CLI exibe um menu com as opções disponíveis.

```output
== CONTROLE: Casa Inteligente ==
[1] - ADICIONAR DISPOSITIVO
[2] - LISTAR DISPOSITIVOS
[3] - STATUS DOS DISPOSITIVOS
[4] - LIGAR TODAS AS LUZES
[5] - DESLIGAR TODAS AS LUZES
[6] - EXIBIR LUZES ACESAS
[7] - CONTROLAR DISPOSITIVO INDIVIDUAL
[8] - REMOVER DISPOSITIVO
[9] - ADICIONAR CELULAR
[10] - ADICIONAR E-MAIL
[0] - SAIR
```

As opções entre colchetes `[ ]` representam os números que devem ser digitados para selecionar a opção desejada.

### [1] - Adicionar Dispositivo:
Ao selecionar a opção `ADICIONAR DISPOSITIVO`, a CLI exibe as opções de dispositivos disponíveis para adicionar.

```output
[1] - LUZ
[2] - TERMOSTATO
[3] - SISTEMA_SEGURANCA
```

Depois de selecionar o tipo de dispositivo, a CLI solicita um nome para o dispositivo, adicionando-o à casa inteligente e retornando ao menu inicial.

### [2] - Listar Dispositivos:
A opção `LISTAR DISPOSITIVOS` exibe uma lista de todos os dispositivos na casa inteligente e seus respectivos nomes, retornando ao menu inicial em seguida.

```output
Device: Termo Friozão
Device: Luz da Sala
Device: Luz da Cozinha
Device: Sistema Segurão
```

### [3] - Status dos Dispositivos:
A opção `STATUS DOS DISPOSITIVOS` exibe o status atual de todos os dispositivos na casa inteligente, retornando ao menu inicial em seguida.

```output
Termo Friozão            DESLIGADO
Luz da Sala              DESLIGADA
Luz da Cozinha           DESLIGADA
Sistema Segurão          DESARMADO
```

### [4] - Ligar Todas as Luzes:
A opção `LIGAR TODAS AS LUZES` liga todas as luzes na casa inteligente, retornando ao menu inicial em seguida. Nenhuma saída é exibida, mas é possível verificar o status das luzes com a opção `STATUS DOS DISPOSITIVOS`.

### [5] - Desligar Todas as Luzes:
A opção `DESLIGAR TODAS AS LUZES` desliga todas as luzes na casa inteligente, retornando ao menu inicial em seguida. Nenhuma saída é exibida, mas é possível verificar o status das luzes com a opção `STATUS DOS DISPOSITIVOS`.

### [6] - Exibir Luzes Acesas:
A opção `EXIBIR LUZES ACESAS` exibe uma lista de todas as luzes que estão ligadas na casa inteligente, retornando ao menu inicial em seguida.

```output
Luz da Sala              LIGADA
Luz da Cozinha           LIGADA
```

### [7] - Controlar Dispositivo Individual:
A opção `CONTROLAR DISPOSITIVO INDIVIDUAL` exibe a lista de todos os dispositivos na casa inteligente, conforme a função `LISTAR DISPOSITIVOS` e solicita o nome do dispositivo que deseja controlar. Depois de selecionar o dispositivo, a CLI exibe as opções de controle referentes ao dispositivo selecionado.

```output
>> Termo Friozão

[1] - AQUECER
[2] - ESFRIAR
[3] - DESLIGAR
```

Depois de selecionar a opção de controle, a CLI executa a ação correspondente e retorna ao menu inicial.

Ao vincular dispositívos de `Celular` ou `EMail` como observadores, quando um dispositivo vinculado muda de estado, o observador é notificado.

```output
Qual dispositivo deseja controlar?
Device: Termo Friozão
Device: Luz da Sala
Device: Sistema Segurão

>> Sistema Segurão
[1] - ARMAR_COM_GENTE
[2] - ARMAR_SEM_NINGUEM
[3] - DESARMAR

>> 2
CELULAR 9090-9090: Notificado () {'state': <SisSegState.ARMADO_SEM_NINGUEM: 'armado_sem_ninguem'>}
E-Mail observador@email.com: Notificado () {'state': <SisSegState.ARMADO_SEM_NINGUEM: 'armado_sem_ninguem'>}
```

### [8] - Remover Dispositivo:
A opção `REMOVER DISPOSITIVO` exibe a lista de todos os dispositivos na casa inteligente, conforme a função `LISTAR DISPOSITIVOS` e solicita o nome do dispositivo que deseja remover. Depois de selecionar o dispositivo, a CLI remove o dispositivo da casa inteligente e retorna ao menu inicial.

### [9] - Adicionar Celular:
A opção `ADICIONAR CELULAR` adiciona um celular como observador de um dos dispositivos na casa inteligente, retornando ao menu inicial em seguida. O usuário é solicitado a selecionar o dispositivo que deseja observar e a informar o número do celular.

```output
Adicionando um Celular
Digite o número do celular a ser cadastrado.
>> 9090-9090
Escolha o dispositivo a ser vinculado com o celular
Device: Termo Friozão
Device: Luz da Sala
Device: Sistema Segurão

>> Sistema Segurão
```

Essa função permite que o dispostivo seja notificado de quaisquer mudanças de estado no dispositivo selecionado.

### [10] - Adicionar E-Mail:
A opção `ADICIONAR E-MAIL` adiciona um e-mail como observador de um dos dispositivos na casa inteligente, retornando ao menu inicial em seguida. O usuário é solicitado a selecionar o dispositivo que deseja observar e a informar o endereço de e-mail.

```output
Adicione um e-mail para receber notificações:
>> observador@email.com
Escolha o dispositivo a ser vinculado com o e-mail
Device: Termo Friozão
Device: Luz da Sala
Device: Sistema Segurão

>> Sistema Segurão
```

Essa função permite que o dispostivo seja notificado de quaisquer mudanças de estado no dispositivo selecionado.

### [0] - Sair:
A opção `SAIR` encerra a execução do programa.

## Demonstração do Projeto:
TO-DO

## Enunciado - Projeto: Sistema de Casa Inteligente

### Objetivo
O objetivo deste projeto é projetar e implementar um sistema de casa inteligente abrangente que integra vários conceitos vistos durante a disciplina, como programação orientada a objetos, padrões de projeto, máquinas de estados usando a biblioteca `transitions`, e conceitos de programação funcional, como compreensões de listas e funções como `map`, `filter` e `reduce`, além de argumentos de linha de comando.

### Visão Geral do Projeto
Você irá criar um sistema de casa inteligente que gerencia vários dispositivos, incluindo pelo menos luzes, termostatos e sistemas de segurança, mas pode incluir mais tipos de dispositivos à vontade. O sistema incluirá na implementação:
1. Classes de dispositivos com máquinas de estados. Cada dispositivo tem a sua própria máquina de estados que descreve o comportamento do dispositivo.
2. Integração de padrões de projeto: _Singleton_, _Factory_ e _Observer_.
3. Aplicação de técnicas de programação funcional, como compreensões de listas, `map`, `filter`, e `reduce`.
4. Uma interface de linha de comando para interação do usuário e configuração do limite de dispositivos.

## Passos para Implementar o Projeto

### 1. Definir as Classes de Dispositivos
Crie uma classe base `Dispositivo`, que deve ser definida como uma classe abstrata que tem um método abstrato para retornar o status atual do dispositivo. A partir desta superclasse é possível criar classes derivadas, como `Luz`, `Termostato`, `SistemaSeguranca`, e outros dispositivos que deseje implementar. 

Cada classe concreta de dispositivo deve:
- Usar a biblioteca `transitions` para gerenciar estados e transições.
- Implementar o método para retornar o status atual do dispositivo.

### 2. Implementar Máquinas de Estados
Para cada classe de dispositivo, use a biblioteca `transitions` para definir estados e transições.

**Exemplos de Estados e Transições**:
- **Luz**:
  - Estados: `desligada`, `ligada`
  - Transições: `ligar`, `desligar`
- **Termostato**:
  - Estados: `desligado`, `aquecendo`, `esfriando`
  - Transições: `aquecer`, `esfriar`, `desligar`
- **Sistema de Segurança**:
  - Estados: `desarmado`, `armado_com_gente_em_casa`, `armado_sem_ninguem_em_casa`
  - Transições: `armar_com_gente_em_casa`, `armar_sem_gente_em_casa`, `desarmar`

### 3. Integrar Padrões de Projeto
Integre os seguintes padrões de projeto:

1. **Padrão Singleton**:
   - Aplique o padrão Singleton à classe `CasaInteligente` para garantir que exista apenas uma instância do sistema de casa inteligente.
   
2. **Padrão Factory**:
   - Implemente uma classe `DispositivoFactory` para criar instâncias de diferentes dispositivos (`Luz`, `Termostato`, `SistemaSeguranca`).

3. **Padrão Observer**:
   - Implemente o padrão Observer para notificar mudanças nos estados dos dispositivos. Crie uma classe `Observer` e uma lista de observadores para gerenciar múltiplos observadores.

### 4. Aplicar Técnicas de Programação Funcional
Use compreensões de listas, `map`, `filter` e `reduce` no seu projeto. Aqui estão alguns exemplos de como essas técnicas podem ser integradas, pode criar mais funções, estes são apenas alguns casos.

1. **Compreensões de Listas**:
   - Use compreensões de listas para obter o status de todos os dispositivos no sistema de casa inteligente.

2. **Map**:
   - Use a função `map` para aplicar um método a todos os dispositivos em uma lista, como desligar todas as luzes.

3. **Filter**:
   - Use a função `filter` para filtrar dispositivos com base no seu estado atual, como obter todos os dispositivos que estão `on`.

4. **Reduce**:
   - Use a função `reduce` para agregar dados de dispositivos, como calcular o número total de dispositivos que estão `on`.

### 5. Adicionar uma Interface de Linha de Comando
Implemente uma interface de linha de comando (CLI) para permitir que os usuários interajam com o sistema de casa inteligente. A CLI deve fornecer opções para:
- Ver os status dos dispositivos.
- Controlar dispositivos individuais (ligar/desligar luzes, configurar modos do termostato, armar/desarmar o sistema de segurança).
- Adicionar e remover dispositivos dinamicamente.
- Permita que o limite de dispositivos que a casa inteligente pode receber seja configurado através de argumentos de linha de comando.

## Entregáveis

1. **Código Fonte**:
   - Envie todos os arquivos de código fonte, garantindo que o código esteja bem documentado.

2. **Documentação**:
   - Forneça um arquivo README detalhado que inclua:
     - Uma visão geral do projeto.
     - Instruções para configurar e executar o projeto.
     - Descrições dos principais componentes e padrões de design utilizados.
     - Exemplos de como usar a CLI.

3. **Demonstração**:
   - Prepare um vídeo curto (até 5 minutos) para mostrar a funcionalidade do seu sistema de casa inteligente. Explique e destaque as principais funcionalidade, padrões de projeto e como as técnicas de programação vistas em sala foram aplicadas.
