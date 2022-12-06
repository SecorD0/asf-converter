<h1><p align="center">ASF converter</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker](#Docker)
    - [Source code](#Source-code)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀This program allows you to create ASF configs according to a configured sample for the specified accounts.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[ASF converter](https://github.com/SecorD0/asf-converter)

⠀[ASF official repository](https://github.com/JustArchiNET/ArchiSteamFarm)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `config` — a directory with ready configs and found maFiles, which you can put in the ASF;
- `maFiles` — a directory with maFiles from accounts;
- `accounts.txt` — a text file with logins and passwords to be processed;
- `asf-converter.exe` / `app.py` — an executable file that runs the program;
- `errors.log` — a log file with errors that occurred during the work;
- `log.log` — a log file with the history of processed accounts;
- `sample_config.json` — the sample config you set up, which will be applied when the program runs.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/asf-converter/releases);
2. Create a folder and put the EXE file in it;
3. Run the program the first time to create necessary files;
4. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
5. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones;
6. Run the program;
7. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[X]` — a config was created, but maFile wasn't found;
   - `[!]` — something went wrong that caused the config not to be created.
8. Copy the `config` directory to ASF directory;
9. Run the ASF.



<h2><p align="center">Docker</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
cd; git clone https://github.com/SecorD0/asf-converter
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
7. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones;
8. Run the program:
```sh
docker run -it --rm -v $HOME/asf-converter/:/program --name asf-converter asf-converter
```
9. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[X]` — a config was created, but maFile wasn't found;
   - `[!]` — something went wrong that caused the config not to be created.
10. Copy the `config` directory to ASF directory;
11. Run the ASF.

<h2><p align="center">Source code</p></h2>

1. Install [Python](https://www.python.org/downloads/);
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/asf-converter
```
3. Set up an environment;
4. Install requirements:
```sh
pip install -r requirements.txt
```
5. Run the `app.py` the first time to create necessary files;
6. Insert account logins and passwords in one of the following formats into the `accounts.txt` file:
```
login_TAB  password
login2;password
```
7. Copy the maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones;
8. Run the program;
9. You can see the following account statuses:
   - `[V]` — a config was created and maFile was found;
   - `[X]` — a config was created, but maFile wasn't found;
   - `[!]` — something went wrong that caused the config not to be created.
10. Copy the `config` directory to ASF directory;
11. Run the ASF.

⠀If you want to build the EXE file by yourself, use the command:
```sh
pyinstaller app.py -Fn asf-converter -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/asf-converter/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`