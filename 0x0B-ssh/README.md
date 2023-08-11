# 0x0B. SSH

# Public Key authentication
The public key encryption algorithm work with two separate keys.These two keys form a pair that is specific to each user.
# Key pair - Public and Private
## ssh-keygen
Ssh-keygen is a tool for creating new authentication key pairs for SSH.Such key pairs are used for automating logins, single sign-on, and for authenticating hosts.
# Creating an SSH Key Pair for User Authentication
The simplest way to generate a key pair is run ssh-kegen without arguments.In this case it will prompt for the file in which to stores keys.
```bash
ssh-keygen Generating public/private rsa key pair
Enter the file in which to save the key(path/to/save/.ssh/id rsa)
Enter the passphrase
Your identification has been saved in path/to/save/.ssh/id_rsa
Your public key has been saved in   path/to/save.ssh/id rsa.pub
```

# Choosing an Algorithm key and Size
The algorith is selected using the -t option
```bash
ssh-keygen -t rsa -b 4096
ssh-keygen -t dsa
ssh-keygen -t ecdsa -b 521
ssh-keygen -t ed25519
```
# Specifying the File Name
Normally, the tool prompts for the file in which to store the key.However it can also be specified on the command line using the -f <filename> option.
```bash
ssh-keygen -f ~/my_key_pair -t rsa -b 4096
```
# Copying the Public Key to the Server
To use public key authentication, the public key must be copied to the server and installed in an `authorized_keys` file.This can be done using the `ssh_copy_id` tool.
```bash
ssh-copy-id -i ~/.ssh/my_key_pair user@host
```
Only the public key is copied to the server.The private key should never be copied to another machine
- ssh-copy-id uses the `SSH protocal` to connect to the target host and upload the SSH user key.
- The command edits the authorized_keys file on the server.
- It creates the .ssh directory if it doesn't exist.
- It create the authorized keys file if it doesn't exist.
- Effectively, ssh key copied to the server.
- It also checks if the key already exists on the server.
- Unless the -f option is given, each key is only added to the authorized keys file once.
# Test the new key
Once the key has been copied, it is best to test it.
```bash
ssh -i ~/.ssh/my_key_pair user@host
```
The login should now be complete without asking for a password.The command might ask for the passphrase you specified for the key

Once the public key has been configured on the server, the server will allow any connecting user that has the private key to log in.During the login process, the client proves possession of the private key by digitally signing the key exchange.

# Basic of SSH
The SSH protocal is based on server-client architechture.The "server" allows the "client" to be connected over a communication channel.This channel is encrypted and the exchange is governed by the use of public and private SSH keys.
- Client initiates the connection by contancting the server.
- The SSH Server sends server public key
- Negotiating parameters and open secure channel
- user login to server host operating system
# Checking the status of the server
```bash
service ssh status
#you may also use the systemd commands
sudo systemctl status ssh
#if the server is not running enable it
sudo systemctl enable --now ssh
# Allowing SSH through the firewall
sudo ufw allow ssh
# checking ufw status
sudo ufw status
```
At this time the SSH Server is up and running, just waiting for a connection from a client
# Connecting to the remote sytem from your local machine
```bash
sudo apt install openssh-client
# You need to know the IP address of the computer and use the ssh command like this
ssh username@address
```
# Managing multiple servers
The SSH config file allows you to create different profiles for different host configurations.When connecting to multiple servers creating SSH profiles is a good move.


## ssh single character flags
- '-p' Specifies the port number to use for the SSH connection.
`ssh -p 2222 user@hostname` would connect to the SSH server on port 2222
- '-i' Specifies the identity of the file to use for public key authentication.
`ssh -i ~/.ssh/my_key user@hostname` would use a private key located at `~/.ssh/my_key`
- '-l' specifies the login user name `ssh -l user hostname` would connect to the SSH server as the user 'user'
- -v verbose provide more detailed output about the SSH connection
# key pair generation
- ssh-keygen is used to generate the RSA key pair.
- -t rsa option specifies that an RSA key should be generated
- -b 4096 specifies the number of bits in the key.
- -f ~/.shh/school specifies the file name and location of the private eky
- -N betty set the passpharase to betty
# add another key pair
to add another key pair edit the file .ssh/authorized_keys paste the other persons public key and save changes.