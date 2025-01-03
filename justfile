default:
  @just --list

install:
  pip install --user -e . --break-system-packages
  cp -ur /tmp/pokedex-cli/pokedex/resources/* ~/.cache/pokedex/resources/
