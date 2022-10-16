
# Project Title

This project is for Japanese Anime lovers to easily download Animes without interuption e.g ads


## Installation

Clone my project from the repo

```bash
  git clone https://github.com/devoply-dev/cmdanime

  cd cmdanime
```
Driver Installation
--------------------

1. open cmd in Administrator mode and copy and paste the following:
```bash
  @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

2. For WindowsPowerShell Installation, open WindowsPowerShell in Administrator mode and paste the following:
```bash
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Then you can use these commands to install the drivers:
```bash
  choco install chromedriver
```

## Appendix
How to use the script
----------------

1. just follow the prompts

2. make sure to enter correct info on any prompt

3. read thru the information printed out after any prompt
## Authors

- [@haxsys](https://github.com/devoply-dev)
