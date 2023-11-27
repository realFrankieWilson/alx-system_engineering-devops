## 0x0B. SSH

---

#### Overview:
This project deals with How ssh keys can be generated and used to connect to a [server](https://intranet.alxswe.com/rltoken/dkgW9lKiBRiUZHfq0MDJuw).

--

##### General points are:
*	What server is.
*	Where server lives.
*	What SSH is.
*	How to create an SSH RSA key pair
*	How to connect to a remote host using an SSH RSA key pair
*	The advantage of using #!/usr/bin/env over /bin/bash

---

#### Tasks:
*	0-use\_a\_private\_key
A Bash script that connects my ubuntu server using a private key in ~/.ssh/school

*	1-create\_ssh\_key\_pair
A Bash script that creates an RSA key pair.
	Name of the created private key is "school"
	Number of bits key created is 4096
	The created key has a passpharse.

*	2-ssh\_config
This deals with configuration:
	The aim is to configure the ssh client so it can connect to a server
Without having to type in password. (Check 2-ssh\_config file for details)

*	The task 3 deals with issuing a connection using a pub key to give
Give access to the owner of the private key.

*	100-puppet\_ssh\_confi.pp
We use puppet to make changes to our configuration file
We set ssh client configuration to use the private key ~/.ssh/school
The ssh client config must refuse to authenticate using password.

---

#### USAGE/REQUIREMENTS.
All the files are tested using Ubuntu 20.04.
The files can be executed directly using "./example.file"

---

#### Author:
Frank Williams Ugwu
[frankuwill101@gmail.com]()
