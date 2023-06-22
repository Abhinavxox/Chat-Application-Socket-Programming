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
