# project-smart_house-python_oo-rria
Projeto feito como avaliação parcial da disciplina de Python (Orientação a Objetos) da Pós Graduação em Robótica e Inteligência Artificial do CIn-UFPE | Softex

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
python main.py
```

**5. Não esqueça de desativar o ambiente virutal:**

_Bash ou PowerShell_
```bash
deactivate
```

## Projeto: Sistema de Casa Inteligente

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
