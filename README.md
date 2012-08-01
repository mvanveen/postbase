postbase
========

SQLite-hosted HTTP Request Logging for Whoever™

![A Post Bin Diagram](https://github.com/mvanveen/postbase/blob/master/ABW.gif?raw=true)
![Usage diagram for a post base](https://github.com/mvanveen/postbase/blob/master/ABW-2.gif?raw=true)

[Source](http://evstudio.com/simpson-strong-tie-will-replace-commonly-specified-ab-and-abe-standoff-post-bases-with-the-abw-in-2012/)

# Introduction

# Usage


Default logging behavior works on port 80 and logs to `requests.sql`.  All logging goes to standard output by default.

```bash
$ python postbase -h
usage: postbase [-h] [--port p] [--filename f] [--hostname HOSTNAME]

SQLite-hosted HTTP Request Logging for Whoever™

optional arguments:
  -h, --help           show this help message and exit
  --port p             Port number to listen on
  --filename f         filename of the database to write to
  --hostname HOSTNAME  Hostname to listen on
```
