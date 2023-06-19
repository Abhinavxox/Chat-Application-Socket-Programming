
# One to One connection between server and client

A Simple TCP Client program that takes the hostname/IP of the server and port number of the Server as Command Line arguments and is able to send messages to that server and receive the response from the server back.

A Simple TCP Single-Client Server program that takes the port number as command-line argument and can listen and accept a client connection and interact with the client till it says "Bye" just like a simple chat application.

## How to run: 

```
gcc server.c -o server
```

```
gcc client.c -o client
```

```
./server 5000
```

```
./client 127.0.0.1 5000
```

## Screenshots

![image](https://github.com/Abhinavxox/Chat-Application-Socket-Programming/assets/72064600/5c4f7fe7-c2ef-47e3-aabf-a74c58c7df27)

![image](https://github.com/Abhinavxox/Chat-Application-Socket-Programming/assets/72064600/96ccdef2-fe38-4a3d-a2cb-ab6e8a3b8e1a)
