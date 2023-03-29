# 0x0B. SSH
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