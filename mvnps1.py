#!/usr/bin/env python3

from argparse import ArgumentParser
import os
import os.path
import logging
import re
import xml.etree.ElementTree as ET

DEFAULT_FORMAT = ' (#{http://maven.apache.org/POM/4.0.0}artifactId#)'

parser = ArgumentParser(description="Extract Maven project information for PS1")
parser.add_argument("format", type=str, action="store", nargs='?', default=DEFAULT_FORMAT,
                    help="Format in which to output the information. Anything between hash signs (#) gets replaced " +
                    "with the text of the tag at that path. Note that Maven pom.xml files have a namespace, so you " +
                    "need to specify that. Default: " + DEFAULT_FORMAT)
parser.add_argument("--filename", "-f", dest="filename", action="store", default="pom.xml", type=str,
                    help="Project filename. Default: pom.xml")
parser.add_argument("--no-up", dest="no_up", action="store_true", help="Look for project file only in the current " +
                    "folder, do not search up the filesystem for one.")
parser.add_argument("--debug", dest="debug", action="store_true", help="Print debugging information.")

args = parser.parse_args()

if args.debug:
  logging.getLogger().setLevel(logging.DEBUG)

filename = args.filename
format = args.format

# Locate project file
path = os.path.abspath('.')

if not args.no_up:
  while not os.path.isfile(os.path.join(path, filename)) and not os.path.ismount(path):
      path = os.path.abspath(os.path.join(path, '..'))

fpath = os.path.join(path, filename)
if os.path.isfile(fpath):
    logging.debug("Found project file at: " + fpath)
    tree = ET.parse(fpath)
    regex = re.compile("#(.*)#")
    output = format
    match = regex.search(output)
    while match:
      output = output[:match.start()] + tree.findtext(match.group(1)) + output[match.end():]
      match = regex.search(output)
    print(output, end='')
else:
    logging.debug("Reached " + path + ", no project file found")
