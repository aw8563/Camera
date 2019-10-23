#include <unistd.h> 
#include <stdio.h> 
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <string.h> 

#define SIZE 10000

int main(void) {
    int s = socket(AF_INET, SOCK_STREAM, 0);
    char buffer[SIZE];

    if (!socket) {
        printf("FAILED TO CREATE SOCKET\n");
    }

    struct sockaddr_in address;
    
    address.sin_family = AF_INET;
    address.sin_port = htons(5000);
    if(inet_pton(AF_INET, "203.63.149.98", &address.sin_addr)<=0) { 
        printf("\nInvalid address/ Address not supported \n"); 
        return -1; 
    } 

    int connection = connect(s, (struct sockaddr *)&address, sizeof(address));
    if (connection < 0) {
        printf("FAILeD TO CONNECT\n");
    } 
    printf("SCUCESFULLY CONNECTED!\n");
    while(1) {
        read(s, buffer, SIZE);
        printf(">> %s\n", buffer);
    }

    return 0;
}