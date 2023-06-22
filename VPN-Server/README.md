## Step 1: Generate SSL/TLS Certificate and Key

- Install OpenSSL if it's not already installed on your system. You can download it from the OpenSSL website (https://www.openssl.org/).

- Open a terminal or command prompt and navigate to a directory where you want to generate the SSL/TLS certificate and key.

- Run the following command to generate the private key (server.key):

```
openssl genpkey -algorithm RSA -out server.key
```

- Next, generate the certificate signing request (CSR) file (server.csr):

```
openssl req -new -key server.key -out server.csr
```

- Finally, generate the self-signed SSL/TLS certificate (server.crt) using the CSR and private key:

```
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

![image](https://github.com/Abhinavxox/Socket-Programming/assets/72064600/f94215d8-a393-45c2-b914-802899e9aacc)

## Step 2: Set Up Python Environment

- Install the required Python packages by running the following command in the terminal:

```
pip install pyopenssl
```

## Step 4 : Run the following command to start the VPN server:

```
python server.py
```
