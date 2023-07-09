<h1><p align="center">asf-converter</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
  - [Windows](#Windows)
  - [Docker (image)](#Docker-image)
  - [Docker (building)](#Docker-building)
  - [Source code](#Source-code)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
    - [General](#General)
    - [Breaking](#Breaking)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to create ASF configs according to a configured sample for the specified accounts.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[asf-converter](https://github.com/SecorD0/asf-converter)

⠀[ASF official repository](https://github.com/JustArchiNET/ArchiSteamFarm)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `config` — a directory with ready configs and found maFiles, which you can put in the ASF;
  - `maFiles` — a directory with maFiles from accounts;
  - `accounts.txt` — a text file with logins and passwords to be processed;
  - `errors.log` — a log file with errors that occurred during the work;
  - `log.log` — a log file with the history of the program working;
  - `sample_config.json` — the sample config you set up, which will be applied when the program runs.
- `asf-converter.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/asf-converter/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time to create necessary files.
4. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
5. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
6. Run the program.
7. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[!]` — a config was created, but maFile wasn't found;
   - `[X]` — something went wrong that caused the config not to be created.
8. Copy the `config` directory to the ASF directory.
9. Run the ASF.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/asf-converter/files:/program/files --name asf-converter ghcr.io/secord0/asf-converter:main
```
3. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
4. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
5. Run the program again:
```sh
docker run -it --rm -v $HOME/asf-converter/files:/program/files --name asf-converter ghcr.io/secord0/asf-converter:main
```
6. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[!]` — a config was created, but maFile wasn't found;
   - `[X]` — something went wrong that caused the config not to be created.
7. Copy the `config` directory to the ASF directory.
8. Run the ASF.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/asf-converter
```
3. Go to the repository:
```sh
cd asf-converter
```
4. Build an image:
```sh
docker build -t asf-converter .
```
5. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```
6. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
7. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
8. Run the program again:
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```
9. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[!]` — a config was created, but maFile wasn't found;
   - `[X]` — something went wrong that caused the config not to be created.
10. Copy the `config` directory to the ASF directory.
11. Run the ASF.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/asf-converter
```
3. Go to the repository:
```sh
cd asf-converter
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time to create necessary files.
7. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
8. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
9. Run the `app.py` again.
10. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[!]` — a config was created, but maFile wasn't found;
   - `[X]` — something went wrong that caused the config not to be created.
11. Copy the `config` directory to the ASF directory.
12. Run the ASF.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn asf-converter -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/asf-converter/releases) and replace the old one with it.
2. Run the EXE file of the new version.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop asf-converter
```
2. Remove the container:
```sh
docker rm asf-converter
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/asf-converter:main
```
4. Run the program:
```sh
docker run -it --rm -v $HOME/asf-converter/files:/program/files --name asf-converter ghcr.io/secord0/asf-converter:main
```


<h2><p align="center">Self-built image</p></h2>

<h3><p align="center">General</p></h3>

1. Go to the repository:
```sh
cd asf-converter
```
2. Update the local files:
```sh
git pull
```
3. Run the program:
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```

<h3><p align="center">Breaking</p></h3>

⠀In addition to the general steps, follow the steps below if the software developer has notified that changes have been made to the project libraries.

1. Stop the container:
```sh
docker stop asf-converter
```
2. Remove the container:
```sh
docker rm asf-converter
```
3. Go to the repository:
```sh
cd asf-converter
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t asf-converter .
```
6. Run the program:
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd asf-converter
```
2. Update the local files:
```sh
git pull
```
3. Run the `app.py`.



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/asf-converter/files:/program/files --name asf-converter ghcr.io/secord0/asf-converter:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```

⠀To remove the container:
```sh
docker stop asf-converter; docker rm asf-converter
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/asf-converter/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
