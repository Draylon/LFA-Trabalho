#include <iostream>
#include <thread>

#include "esteira.cpp"

//using namespace std;

void processo_update(std::string processo){
    
}


int main(int argc, char *argv[]){
    std::string processo = "lmao";
    std::cout << processo << std::endl;

    std::thread t( Esteira( &processo ) );
    processo = "yeet";
    

    //funcao_main_do_torno.join();
    return 0;
}

/*

http://www.cplusplus.com/reference/thread/thread/
https://www.geeksforgeeks.org/multithreading-in-cpp/

*/