default:
  @just --list

install:
  pip install --user -e . --break-system-packages
