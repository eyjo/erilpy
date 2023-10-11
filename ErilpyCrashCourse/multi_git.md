# Margir notenda aðgangar að git
Til að aðgreina notenda aðgang á milli vinnu og einka er hægt að skilgreina alias í ssh stillingum og merkja svo aðganginn í viðkomandi git repo.

## 1. Stilla ssh alias:
Bæta í ssh stillingaskrá (`~/.ssh/config`) eftirfarandi texta:
```bash
# Github account private
Host github-privat
    HostName github.com
    IdentifyFile ~/.ssh/id_ed25519
    User git
    IdentitiesOnly yes
```

## 2. Sækja í tölvu git repo:
```bash
git clone git@github-private:eyjo/erilpy.git
```

## 3. Stilla viðkomandi git repo á réttan notanda:
Vera staðsett í git repo, þ.e. það folder þar sem git repóið er vistað (er með `.git` möppu).
```bash
cd erilpy
```
Til þess að gá hvað það er stillt á nú þegar er hægt
að (i) kalla eftir því:
```bash
git config --get user.name
git config --get user.email
```
eða (ii) skoða það í stillingaskrá:
```bash
cat .git/config
```

Til að stilla viðkomandi repo á réttan notanda eru skipanirar:
```bash
git config user.username "eyjo"
git config user.email "eyjolfurs@gmail.com"

# Til að gá hvort það hafi heppnast rétt:
git config --get user.name
git config --get user.email
# eða
cat .git/config
```

Þetta er frábrugðið 'global' git stillingunum, þ.a. ef maður er ekki staðsettur í viðkomandi repo möppu ætti default gildin að vera virk.

# Samantekt:

```bash
echo "
# Github account private
Host github-privat
    HostName github.com
    IdentifyFile ~/.ssh/id_ed25519
    User git
    IdentitiesOnly yes
" >> ~/.ssh/config
git clone git@github-private:eyjo/erilpy.git
cd erilpy
git config user.username "eyjo"
git config user.email "eyjolfurs@gmail.com"
```


