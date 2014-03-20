This is a small script that you can use to display [Maven] project information in your terminal prompt:

![Screenshot](//i.imgur.com/ON7CQPv.png)

Usage
=====

You need to have Python 3 installed (no extra packages required). Simply put `mvnps1.py` in your `$PATH` (or not) and
execute it in your `PS1`. For example, you could have this in your `~/.bash_profile`:

    export PS1='\w$(mvnps1.py)$ '

This will give you the current working directory (`\w`) plus the `artifactId` of the current project, if any. For more
sophisticated usage, check out `mvnps1.py --help`:

```
usage: mvnps1.py [-h] [--filename FILENAME] [--no-up] [--debug] [format]

Extract Maven project information for PS1

positional arguments:
  format                Format in which to output the information. Anything
                        between hash signs (#) gets replaced with the text of
                        the tag at that path. Note that Maven pom.xml files
                        have a namespace, so you need to specify that.
                        Default:
                        (#{http://maven.apache.org/POM/4.0.0}artifactId#)

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME, -f FILENAME
                        Project filename. Default: pom.xml
  --no-up               Look for project file only in the current folder, do
                        not search up the filesystem for one.
  --debug               Print debugging information.
```

[Maven]: http://maven.apache.org/
