# -- WHERE ARE THE MONKEYS? --

### Search your 42 friends
By using the 42 API you can check whether your friends are online or offline on your campus, and even where they are actually logged in. 
First you need to create an app on the intra, for more information, read the docs [here](https://api.intra.42.fr/apidoc/guides/getting_started).

Once you have both your UID and Secret ID, put it into the _"config.yml"_ file.

Then add all the logins of your _"monkey friends"_ to the _"monkeys"_ file, each separated by a new line, here is a example:
```
login1
login2
login3
```

You can easily do that by executing:
```bash
echo "login" >> monkeys
```

Finally, you should be able to execute the program:
```
./wherearethemonkeys
```
