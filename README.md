# Trabalho de LFA

Automatos para linha de produção

## Install

    git clone <repo>


## Utilização

versão python: 3.7.5rc1 (Windows x64)

```bash
python principal.py
```

## Sobre
    Implementação de Threads para controlar as instâncias dos maquinários.
    Fita geral compartilhada, das quais cada maquinário faz sua interseção para interpretá-la.
    Buffers servem apenas para consulta, não atuando no posicionamento de componentes.

##Automatos

![controle]()
![estoque]()
![esteira]()
![torno]()
![qualidade]()
![parafusadeira](https://github.com/Draylon/LFA-Trabalho/blob/master/automatos/parafusadeira.png)

##Comandos

    peca1,peca2,shut

peca1: produzir peça 1
peca2: produzir peça 2
shut:  encerrar a produção


## bugs conhecidos

#Graves/sem solução conhecida:>
    - Torno dessincronizado ( rever Threads )
    - Demora muito para fazer 2 pecas simultaneas, devido às interseções das fitas
    - Exibição no terminal dessincronizada
    - Buffers sempre vazios após primeira peça feita

#Médios/resolvíveis:>
    - Multiplos estados finais alterando a fita simultaneamente
    - Parafusadeira ocasionalmente dessincronizada ( não deve interferir no comportamento )