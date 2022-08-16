# 0x0C. Web server

## Tasks

### 0. Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

Requirements:
- Accepts 4 parameters
- The path to the file to be transferred
- The IP of the server we want to transfer the file to
- The username `scp` connects with
- The path to the SSH private key that `scp` uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 4 parameters passed
- `scp` must transfer the file to the user home directory `~/`
Strict host key checking must be disabled when using `scp`

### 1. Install nginx web server
Requirements:
- Install `nginx` on your `web-01` server
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World`
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can’t use `systemctl` for restarting `nginx`

### 2. Setup a domain name
Provide the domain name in your answer file.

### 3. Redirection
Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:
- The redirection must be a “301 Moved Permanently”
- Your answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### 4. Not found page 404
Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.
