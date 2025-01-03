default:
  @just --list

install:
  pip install --user -e . --break-system-packages
  mkdir -p ~/.cache/pokedex/resources/
  cp -ur ./pokedex/resources/* ~/.cache/pokedex/resources/
