# Pokédex CLI

The Pocket Monster Index, now in your terminal!

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgments](#acknowledgments)

## Installation

```
git clone https://github.com/calacuda/pokedex-cli.git
cd pokedex-cli/
pip install -e .
```

For the best output quality, please adjust the vertical line spacing in your
terminal emulator until the block characters connect.

## Supported Python Versions:
- 3.8
- 3.10
- newer then 3.6 (probably)


## Things That Don't Work

"-f page" doesn't work. but it didn't work in the original, so I have no way of knowing
how it is supposed to work.


## Usage

```
$ pokedex --help
Usage: main.py [OPTIONS] POKEMON

  Command-line interface for a quick Pokédex reference.

  Positional argument POKEMON can be either an id or a name, which has to be
  specified in the configured language.

Options:
  -s, --shiny                     Show shiny version of the Pokémon.
  -m, --mega                      Show Mega Evolution(s) if available.
  -l, --language LANGUAGE         Pokédex language to use.
  -pv, --pokedex-version VERSION  Pokédex version to use.
  -f, --format FORMAT             Output format (can be card, json, simple,
                                  line, page).
  --help                          Show this message and exit.
```

## Screenshots

![charzard.png](/screen-shots/charzard.png?raw=true "charzard")
![swampert.png](/screen-shots/swampert.png?raw=true "swampert")
![torterra.png](/screen-shots/torterra.png?raw=true "torterra")

## Acknowledgments

- Database fetched at runtime from [Veekun](http://veekun.com/dex/downloads)
- Icons adapted from [Pikachumazzinga on DeviantArt](http://pikachumazzinga.deviantart.com/art/Pokemon-Essentials-Icon-Pack-ORAS-UPDATE-424114559)
- origianl code by [Tenchi2xh](https://github.com/Tenchi2xh/pokedex-cli)

Pokémon © 2002-2016 Pokémon. © 1995-2016 Nintendo/Creatures Inc./GAME FREAK inc.
TM, ® and Pokémon character names are trademarks of Nintendo.

No copyright or trademark infringement is intended in using Pokémon content in
this project.
