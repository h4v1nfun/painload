#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE

os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
pidfile = "/tmp/krebs.stream.pid"
url_file = os.environ.get("STREAM_DB", "stream.db")
urls = []
#urls = [ url,f for (url,f) in open(url_file).readline() ]
for line in open(url_file):
    urls.append(line.split())
#print urls
mybin = sys.argv[0]
cmd = sys.argv[1] if len(sys.argv) > 1 else "you-are-made-of-stupid"
stream = sys.argv[2] if len(sys.argv) == 3 else "groove"


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def urlForStream(stream):
    for url, s in urls:
        if s == stream:
            return url


def start(stream):
    ret = running()
    if ret:
        print "!! Stream `%s` already running with pid `%s` !" % \
                (ret[1], ret[0])
    else:
        pipe_silent = open('/dev/null', 'w')
        url = urlForStream(stream)
        mpl = Popen(["mplayer", url],
                 stdout=pipe_silent, stderr=pipe_silent).pid
        print >> open(pidfile, "w+"), "%d %s" % (mpl, stream)


def stop():
    ret = running()
    if not ret:
        print "!! No Stream running!"
    else:
        pid, name = ret
        print "** Killing `%s` with pid %s" % (name, pid)
        os.kill(int(pid), 15)
        #if check_pid(int(pid)):
        #    print "!! trying harder to kill process"
        #    os.kill(int(pid), 9)
        os.remove(pidfile)


def running():
    try:
        pid, currstream = open(pidfile).read().split()
        if check_pid(int(pid)):
            return (pid, currstream)
        else:
            print "!! removing stale pidfile"
            os.remove(pidfile)
            raise Exception("Pidfile stale")
    except Exception as e:
        return ()


def slist():
    for url, name in urls:
        print "%s : %s" % (name, url)


def shorthelp():
    print "start|stop|restart|status|list [audio stream]"


def longhelp():
    print "Usage: %s" % mybin,
    shorthelp
    print """[32;1m get all available streams with [31;1;4m'/%(fil)s list'[m
    Examples:
    %(fil)s list
    %(fil)s start groove
    %(fil)s switch deepmix
    %(fil)s status
    %(fil)s stop""" % {'fil': mybin}

if cmd == "start":
    start(stream)
elif cmd == "stop":
    stop()
elif cmd == "switch" or cmd == "restart":
    stop()
    start(stream)
elif cmd == "status":
    ret = running()
    if not ret:
        print "** no stream running"  # , e
    else:
        print "%s is running(%s)" % (ret[1], urlForStream(ret[1]))
elif cmd == "list":
    slist()
elif cmd == "--help":
    longhelp()
elif cmd == "-h":
    shorthelp()
else:
    print "unknown command `%s`" % cmd
    print "try `%s` --help" % os.path.basename(mybin)
