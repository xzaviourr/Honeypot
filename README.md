# Honeypot
Implementation of a basic honey pot, that binds itself with the telnet port and detects the presence of any attacks that the attacker might be trying on your system. Contains a debian fake file system to trap the attacker in the honey pot for as long as possible, while maintaining a proper log records for future analysis.

## To initiate the whole project and for repetitive builds
``` docker build -t myimage . ```

## To run the program
``` docker run -p 23:23 myimage ```

## Log file location
``` /var/lib/docker/containers/<container id>/<container id>-json.log ```

### You can check out the ppt presentation we made on this project [here](https://drive.google.com/file/d/1hBmEDj2MPR13lSb2BKT2xJi6MIWp8-8-/view?usp=sharing)
