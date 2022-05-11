#!/bin/env python

from argparse import ArgumentParser
from pathlib import Path
from shutil import copy2


def main():
  parser = ArgumentParser(description='Multiply files X_n_m.*')
  parser.add_argument('dir', help='Files directory')
  parser.add_argument('-d', '--deler', default='_')
  parser.add_argument('-t', '--tim', default=2, type=int)
  args = parser.parse_args()

  dirpath = Path(args.dir)

  if not dirpath.is_dir():
    raise RuntimeError(f'{dirpath} is not a directory')

  groups = {}

  for filepath in dirpath.iterdir():
    if not filepath.suffix in groups:
      groups[filepath.suffix] = {}
    parts = filepath.name.split(args.deler)
    name = parts[0]
    if not name in groups[filepath.suffix]:
      groups[filepath.suffix][name] = []
    groups[filepath.suffix][name].append(filepath.name)

  for sfx, group in groups.items():
    for name, fnames in group.items():
      for fname in fnames:
        for cx in range(1, args.tim + 1):
          parts = fname.split(args.deler)
          count = str(int(parts[-2]) + args.tim * cx)
          parts[-2] = count
          dname = args.deler.join(parts)
          copy2(fname, dname)


if '__main__' == __name__:
  main()
