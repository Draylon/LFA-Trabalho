#include <peca>

class Esteira{
    public: 
        Peca pecas[3];
        boolean mov;

    void aguarda_peca(){
        /* estado de atividade diferente de parado, em que a máquina está aguardando a peça chegar no sensor */
    }

    void pega_peca(){
        /* alguma peça chegou no sensor
        parar a esteira
        olhar qual peça é
        pegar peca e colocar dentro do torno, caso for a correspondente */
    }

    void processa_peca(){
        /*
            torno trabalhando na peça, vai retornar assíncrono para a string na main quando tiver pronta
            começar a colocar na esteira
        */
    }

    void coloca_na_esteira(){
        /* parar a esteira
        colocar peça na esteira desde que não tenha nada impedindo */
    }
}


void main(int argc, char *argv[]){
    cout << "Esteira";
}