r"""Wrapper for stdc-predef.h

Generated with:
./run.py -llibc.so.6 /usr/include/stdc-predef.h /usr/include/stdint.h /usr/include/stdio.h /usr/include/stdio_ext.h /usr/include/stdlib.h /usr/include/x86_64-linux-gnu/a.out.h /usr/include/x86_64-linux-gnu/expat_config.h /usr/include/x86_64-linux-gnu/fpu_control.h /usr/include/x86_64-linux-gnu/ieee754.h /usr/include/x86_64-linux-gnu/sys/acct.h /usr/include/x86_64-linux-gnu/sys/auxv.h /usr/include/x86_64-linux-gnu/sys/bitypes.h /usr/include/x86_64-linux-gnu/sys/cdefs.h /usr/include/x86_64-linux-gnu/sys/debugreg.h /usr/include/x86_64-linux-gnu/sys/dir.h /usr/include/x86_64-linux-gnu/sys/elf.h /usr/include/x86_64-linux-gnu/sys/epoll.h /usr/include/x86_64-linux-gnu/sys/errno.h /usr/include/x86_64-linux-gnu/sys/eventfd.h /usr/include/x86_64-linux-gnu/sys/fanotify.h /usr/include/x86_64-linux-gnu/sys/fcntl.h /usr/include/x86_64-linux-gnu/sys/file.h /usr/include/x86_64-linux-gnu/sys/fsuid.h /usr/include/x86_64-linux-gnu/sys/gmon.h /usr/include/x86_64-linux-gnu/sys/gmon_out.h /usr/include/x86_64-linux-gnu/sys/inotify.h /usr/include/x86_64-linux-gnu/sys/io.h /usr/include/x86_64-linux-gnu/sys/ioctl.h /usr/include/x86_64-linux-gnu/sys/ipc.h /usr/include/x86_64-linux-gnu/sys/kd.h /usr/include/x86_64-linux-gnu/sys/klog.h /usr/include/x86_64-linux-gnu/sys/mman.h /usr/include/x86_64-linux-gnu/sys/mount.h /usr/include/x86_64-linux-gnu/sys/msg.h /usr/include/x86_64-linux-gnu/sys/mtio.h /usr/include/x86_64-linux-gnu/sys/param.h /usr/include/x86_64-linux-gnu/sys/pci.h /usr/include/x86_64-linux-gnu/sys/perm.h /usr/include/x86_64-linux-gnu/sys/personality.h /usr/include/x86_64-linux-gnu/sys/poll.h /usr/include/x86_64-linux-gnu/sys/prctl.h /usr/include/x86_64-linux-gnu/sys/procfs.h /usr/include/x86_64-linux-gnu/sys/profil.h /usr/include/x86_64-linux-gnu/sys/ptrace.h /usr/include/x86_64-linux-gnu/sys/queue.h /usr/include/x86_64-linux-gnu/sys/quota.h /usr/include/x86_64-linux-gnu/sys/random.h /usr/include/x86_64-linux-gnu/sys/raw.h /usr/include/x86_64-linux-gnu/sys/reboot.h /usr/include/x86_64-linux-gnu/sys/reg.h /usr/include/x86_64-linux-gnu/sys/resource.h /usr/include/x86_64-linux-gnu/sys/select.h /usr/include/x86_64-linux-gnu/sys/sem.h /usr/include/x86_64-linux-gnu/sys/sendfile.h /usr/include/x86_64-linux-gnu/sys/shm.h /usr/include/x86_64-linux-gnu/sys/signal.h /usr/include/x86_64-linux-gnu/sys/signalfd.h /usr/include/x86_64-linux-gnu/sys/socket.h /usr/include/x86_64-linux-gnu/sys/socketvar.h /usr/include/x86_64-linux-gnu/sys/soundcard.h /usr/include/x86_64-linux-gnu/sys/stat.h /usr/include/x86_64-linux-gnu/sys/statfs.h /usr/include/x86_64-linux-gnu/sys/statvfs.h /usr/include/x86_64-linux-gnu/sys/swap.h /usr/include/x86_64-linux-gnu/sys/syscall.h /usr/include/x86_64-linux-gnu/sys/sysctl.h /usr/include/x86_64-linux-gnu/sys/sysinfo.h /usr/include/x86_64-linux-gnu/sys/syslog.h /usr/include/x86_64-linux-gnu/sys/sysmacros.h /usr/include/x86_64-linux-gnu/sys/termios.h /usr/include/x86_64-linux-gnu/sys/time.h /usr/include/x86_64-linux-gnu/sys/timeb.h /usr/include/x86_64-linux-gnu/sys/timerfd.h /usr/include/x86_64-linux-gnu/sys/times.h /usr/include/x86_64-linux-gnu/sys/timex.h /usr/include/x86_64-linux-gnu/sys/ttychars.h /usr/include/x86_64-linux-gnu/sys/ttydefaults.h /usr/include/x86_64-linux-gnu/sys/types.h /usr/include/x86_64-linux-gnu/sys/ucontext.h /usr/include/x86_64-linux-gnu/sys/uio.h /usr/include/x86_64-linux-gnu/sys/un.h /usr/include/x86_64-linux-gnu/sys/unistd.h /usr/include/x86_64-linux-gnu/sys/user.h /usr/include/x86_64-linux-gnu/sys/utsname.h /usr/include/x86_64-linux-gnu/sys/vfs.h /usr/include/x86_64-linux-gnu/sys/vlimit.h /usr/include/x86_64-linux-gnu/sys/vm86.h /usr/include/x86_64-linux-gnu/sys/vt.h /usr/include/x86_64-linux-gnu/sys/vtimes.h /usr/include/x86_64-linux-gnu/sys/wait.h /usr/include/x86_64-linux-gnu/sys/xattr.h -o /home/tz-wsl1-2004/py_inotify/linux_libc.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libc.so.6"] = load_library("libc.so.6")

# 1 libraries
# End libraries

# No modules

__u_char = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 31

__u_short = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 32

__u_int = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 33

__u_long = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 34

__int8_t = c_char# /usr/include/x86_64-linux-gnu/bits/types.h: 37

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__int16_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 39

__uint16_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__int32_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 41

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__int64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 44

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

__int_least8_t = __int8_t# /usr/include/x86_64-linux-gnu/bits/types.h: 52

__uint_least8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/types.h: 53

__int_least16_t = __int16_t# /usr/include/x86_64-linux-gnu/bits/types.h: 54

__uint_least16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/types.h: 55

__int_least32_t = __int32_t# /usr/include/x86_64-linux-gnu/bits/types.h: 56

__uint_least32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/types.h: 57

__int_least64_t = __int64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 58

__uint_least64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 59

__quad_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 63

__u_quad_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 64

__intmax_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 72

__uintmax_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 73

__dev_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 145

__uid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 146

__gid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 147

__ino_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 148

__ino64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 149

__mode_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 150

__nlink_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 151

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__pid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 154

# /usr/include/x86_64-linux-gnu/bits/types.h: 155
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_1# /usr/include/x86_64-linux-gnu/bits/types.h: 155

__clock_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 156

__rlim_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 157

__rlim64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 158

__id_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 159

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

__useconds_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 161

__suseconds_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 162

__daddr_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 164

__key_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 165

__clockid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 168

__timer_t = POINTER(None)# /usr/include/x86_64-linux-gnu/bits/types.h: 171

__blksize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 174

__blkcnt_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 179

__blkcnt64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 180

__fsblkcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 183

__fsblkcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 184

__fsfilcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 187

__fsfilcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 188

__fsword_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 191

__ssize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 193

__syscall_slong_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 196

__syscall_ulong_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 198

__loff_t = __off64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 202

__caddr_t = String# /usr/include/x86_64-linux-gnu/bits/types.h: 203

__intptr_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 206

__socklen_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 209

__sig_atomic_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 214

int_least8_t = __int_least8_t# /usr/include/stdint.h: 43

int_least16_t = __int_least16_t# /usr/include/stdint.h: 44

int_least32_t = __int_least32_t# /usr/include/stdint.h: 45

int_least64_t = __int_least64_t# /usr/include/stdint.h: 46

uint_least8_t = __uint_least8_t# /usr/include/stdint.h: 49

uint_least16_t = __uint_least16_t# /usr/include/stdint.h: 50

uint_least32_t = __uint_least32_t# /usr/include/stdint.h: 51

uint_least64_t = __uint_least64_t# /usr/include/stdint.h: 52

int_fast8_t = c_char# /usr/include/stdint.h: 58

int_fast16_t = c_long# /usr/include/stdint.h: 60

int_fast32_t = c_long# /usr/include/stdint.h: 61

int_fast64_t = c_long# /usr/include/stdint.h: 62

uint_fast8_t = c_ubyte# /usr/include/stdint.h: 71

uint_fast16_t = c_ulong# /usr/include/stdint.h: 73

uint_fast32_t = c_ulong# /usr/include/stdint.h: 74

uint_fast64_t = c_ulong# /usr/include/stdint.h: 75

intptr_t = c_long# /usr/include/stdint.h: 87

uintptr_t = c_ulong# /usr/include/stdint.h: 90

intmax_t = __intmax_t# /usr/include/stdint.h: 101

uintmax_t = __uintmax_t# /usr/include/stdint.h: 102

# /usr/include/x86_64-linux-gnu/bits/types/__mbstate_t.h: 16
class union_anon_2(Union):
    pass

union_anon_2.__slots__ = [
    '__wch',
    '__wchb',
]
union_anon_2._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * int(4)),
]

# /usr/include/x86_64-linux-gnu/bits/types/__mbstate_t.h: 21
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    '__count',
    '__value',
]
struct_anon_3._fields_ = [
    ('__count', c_int),
    ('__value', union_anon_2),
]

__mbstate_t = struct_anon_3# /usr/include/x86_64-linux-gnu/bits/types/__mbstate_t.h: 21

# /usr/include/x86_64-linux-gnu/bits/types/__fpos_t.h: 14
class struct__G_fpos_t(Structure):
    pass

struct__G_fpos_t.__slots__ = [
    '__pos',
    '__state',
]
struct__G_fpos_t._fields_ = [
    ('__pos', __off_t),
    ('__state', __mbstate_t),
]

__fpos_t = struct__G_fpos_t# /usr/include/x86_64-linux-gnu/bits/types/__fpos_t.h: 14

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 49
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE# /usr/include/x86_64-linux-gnu/bits/types/FILE.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 36
class struct__IO_marker(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 37
class struct__IO_codecvt(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 38
class struct__IO_wide_data(Structure):
    pass

_IO_lock_t = None# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 43

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '_codecvt',
    '_wide_data',
    '_freeres_list',
    '_freeres_buf',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * int(1)),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('_codecvt', POINTER(struct__IO_codecvt)),
    ('_wide_data', POINTER(struct__IO_wide_data)),
    ('_freeres_list', POINTER(struct__IO_FILE)),
    ('_freeres_buf', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * int((((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t)))),
]

off_t = __off_t# /usr/include/stdio.h: 63

ssize_t = __ssize_t# /usr/include/stdio.h: 77

fpos_t = __fpos_t# /usr/include/stdio.h: 84

# /usr/include/stdio.h: 137
try:
    stdin = (POINTER(FILE)).in_dll(_libs["libc.so.6"], "stdin")
except:
    pass

# /usr/include/stdio.h: 138
try:
    stdout = (POINTER(FILE)).in_dll(_libs["libc.so.6"], "stdout")
except:
    pass

# /usr/include/stdio.h: 139
try:
    stderr = (POINTER(FILE)).in_dll(_libs["libc.so.6"], "stderr")
except:
    pass

# /usr/include/stdio.h: 146
if _libs["libc.so.6"].has("remove", "cdecl"):
    remove = _libs["libc.so.6"].get("remove", "cdecl")
    remove.argtypes = [String]
    remove.restype = c_int

# /usr/include/stdio.h: 148
if _libs["libc.so.6"].has("rename", "cdecl"):
    rename = _libs["libc.so.6"].get("rename", "cdecl")
    rename.argtypes = [String, String]
    rename.restype = c_int

# /usr/include/stdio.h: 152
if _libs["libc.so.6"].has("renameat", "cdecl"):
    renameat = _libs["libc.so.6"].get("renameat", "cdecl")
    renameat.argtypes = [c_int, String, c_int, String]
    renameat.restype = c_int

# /usr/include/stdio.h: 173
if _libs["libc.so.6"].has("tmpfile", "cdecl"):
    tmpfile = _libs["libc.so.6"].get("tmpfile", "cdecl")
    tmpfile.argtypes = []
    tmpfile.restype = POINTER(FILE)

# /usr/include/stdio.h: 187
if _libs["libc.so.6"].has("tmpnam", "cdecl"):
    tmpnam = _libs["libc.so.6"].get("tmpnam", "cdecl")
    tmpnam.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        tmpnam.restype = ReturnString
    else:
        tmpnam.restype = String
        tmpnam.errcheck = ReturnString

# /usr/include/stdio.h: 192
if _libs["libc.so.6"].has("tmpnam_r", "cdecl"):
    tmpnam_r = _libs["libc.so.6"].get("tmpnam_r", "cdecl")
    tmpnam_r.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        tmpnam_r.restype = ReturnString
    else:
        tmpnam_r.restype = String
        tmpnam_r.errcheck = ReturnString

# /usr/include/stdio.h: 204
if _libs["libc.so.6"].has("tempnam", "cdecl"):
    tempnam = _libs["libc.so.6"].get("tempnam", "cdecl")
    tempnam.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        tempnam.restype = ReturnString
    else:
        tempnam.restype = String
        tempnam.errcheck = ReturnString

# /usr/include/stdio.h: 213
if _libs["libc.so.6"].has("fclose", "cdecl"):
    fclose = _libs["libc.so.6"].get("fclose", "cdecl")
    fclose.argtypes = [POINTER(FILE)]
    fclose.restype = c_int

# /usr/include/stdio.h: 218
if _libs["libc.so.6"].has("fflush", "cdecl"):
    fflush = _libs["libc.so.6"].get("fflush", "cdecl")
    fflush.argtypes = [POINTER(FILE)]
    fflush.restype = c_int

# /usr/include/stdio.h: 227
if _libs["libc.so.6"].has("fflush_unlocked", "cdecl"):
    fflush_unlocked = _libs["libc.so.6"].get("fflush_unlocked", "cdecl")
    fflush_unlocked.argtypes = [POINTER(FILE)]
    fflush_unlocked.restype = c_int

# /usr/include/stdio.h: 246
if _libs["libc.so.6"].has("fopen", "cdecl"):
    fopen = _libs["libc.so.6"].get("fopen", "cdecl")
    fopen.argtypes = [String, String]
    fopen.restype = POINTER(FILE)

# /usr/include/stdio.h: 252
if _libs["libc.so.6"].has("freopen", "cdecl"):
    freopen = _libs["libc.so.6"].get("freopen", "cdecl")
    freopen.argtypes = [String, String, POINTER(FILE)]
    freopen.restype = POINTER(FILE)

# /usr/include/stdio.h: 279
if _libs["libc.so.6"].has("fdopen", "cdecl"):
    fdopen = _libs["libc.so.6"].get("fdopen", "cdecl")
    fdopen.argtypes = [c_int, String]
    fdopen.restype = POINTER(FILE)

# /usr/include/stdio.h: 292
if _libs["libc.so.6"].has("fmemopen", "cdecl"):
    fmemopen = _libs["libc.so.6"].get("fmemopen", "cdecl")
    fmemopen.argtypes = [POINTER(None), c_size_t, String]
    fmemopen.restype = POINTER(FILE)

# /usr/include/stdio.h: 298
if _libs["libc.so.6"].has("open_memstream", "cdecl"):
    open_memstream = _libs["libc.so.6"].get("open_memstream", "cdecl")
    open_memstream.argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t)]
    open_memstream.restype = POINTER(FILE)

# /usr/include/stdio.h: 304
if _libs["libc.so.6"].has("setbuf", "cdecl"):
    setbuf = _libs["libc.so.6"].get("setbuf", "cdecl")
    setbuf.argtypes = [POINTER(FILE), String]
    setbuf.restype = None

# /usr/include/stdio.h: 308
if _libs["libc.so.6"].has("setvbuf", "cdecl"):
    setvbuf = _libs["libc.so.6"].get("setvbuf", "cdecl")
    setvbuf.argtypes = [POINTER(FILE), String, c_int, c_size_t]
    setvbuf.restype = c_int

# /usr/include/stdio.h: 314
if _libs["libc.so.6"].has("setbuffer", "cdecl"):
    setbuffer = _libs["libc.so.6"].get("setbuffer", "cdecl")
    setbuffer.argtypes = [POINTER(FILE), String, c_size_t]
    setbuffer.restype = None

# /usr/include/stdio.h: 318
if _libs["libc.so.6"].has("setlinebuf", "cdecl"):
    setlinebuf = _libs["libc.so.6"].get("setlinebuf", "cdecl")
    setlinebuf.argtypes = [POINTER(FILE)]
    setlinebuf.restype = None

# /usr/include/stdio.h: 326
if _libs["libc.so.6"].has("fprintf", "cdecl"):
    _func = _libs["libc.so.6"].get("fprintf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(FILE), String]
    fprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 332
if _libs["libc.so.6"].has("printf", "cdecl"):
    _func = _libs["libc.so.6"].get("printf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String]
    printf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 334
if _libs["libc.so.6"].has("sprintf", "cdecl"):
    _func = _libs["libc.so.6"].get("sprintf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    sprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 354
if _libs["libc.so.6"].has("snprintf", "cdecl"):
    _func = _libs["libc.so.6"].get("snprintf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, c_size_t, String]
    snprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 382
if _libs["libc.so.6"].has("dprintf", "cdecl"):
    _func = _libs["libc.so.6"].get("dprintf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int, String]
    dprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 391
if _libs["libc.so.6"].has("fscanf", "cdecl"):
    _func = _libs["libc.so.6"].get("fscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(FILE), String]
    fscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 397
if _libs["libc.so.6"].has("scanf", "cdecl"):
    _func = _libs["libc.so.6"].get("scanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String]
    scanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 399
if _libs["libc.so.6"].has("sscanf", "cdecl"):
    _func = _libs["libc.so.6"].get("sscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    sscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 416
if _libs["libc.so.6"].has("__isoc99_fscanf", "cdecl"):
    _func = _libs["libc.so.6"].get("__isoc99_fscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(FILE), String]
    __isoc99_fscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 418
if _libs["libc.so.6"].has("__isoc99_scanf", "cdecl"):
    _func = _libs["libc.so.6"].get("__isoc99_scanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String]
    __isoc99_scanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 419
if _libs["libc.so.6"].has("__isoc99_sscanf", "cdecl"):
    _func = _libs["libc.so.6"].get("__isoc99_sscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    __isoc99_sscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/stdio.h: 485
if _libs["libc.so.6"].has("fgetc", "cdecl"):
    fgetc = _libs["libc.so.6"].get("fgetc", "cdecl")
    fgetc.argtypes = [POINTER(FILE)]
    fgetc.restype = c_int

# /usr/include/stdio.h: 486
if _libs["libc.so.6"].has("getc", "cdecl"):
    getc = _libs["libc.so.6"].get("getc", "cdecl")
    getc.argtypes = [POINTER(FILE)]
    getc.restype = c_int

# /usr/include/stdio.h: 492
if _libs["libc.so.6"].has("getchar", "cdecl"):
    getchar = _libs["libc.so.6"].get("getchar", "cdecl")
    getchar.argtypes = []
    getchar.restype = c_int

# /usr/include/stdio.h: 499
if _libs["libc.so.6"].has("getc_unlocked", "cdecl"):
    getc_unlocked = _libs["libc.so.6"].get("getc_unlocked", "cdecl")
    getc_unlocked.argtypes = [POINTER(FILE)]
    getc_unlocked.restype = c_int

# /usr/include/stdio.h: 500
if _libs["libc.so.6"].has("getchar_unlocked", "cdecl"):
    getchar_unlocked = _libs["libc.so.6"].get("getchar_unlocked", "cdecl")
    getchar_unlocked.argtypes = []
    getchar_unlocked.restype = c_int

# /usr/include/stdio.h: 510
if _libs["libc.so.6"].has("fgetc_unlocked", "cdecl"):
    fgetc_unlocked = _libs["libc.so.6"].get("fgetc_unlocked", "cdecl")
    fgetc_unlocked.argtypes = [POINTER(FILE)]
    fgetc_unlocked.restype = c_int

# /usr/include/stdio.h: 521
if _libs["libc.so.6"].has("fputc", "cdecl"):
    fputc = _libs["libc.so.6"].get("fputc", "cdecl")
    fputc.argtypes = [c_int, POINTER(FILE)]
    fputc.restype = c_int

# /usr/include/stdio.h: 522
if _libs["libc.so.6"].has("putc", "cdecl"):
    putc = _libs["libc.so.6"].get("putc", "cdecl")
    putc.argtypes = [c_int, POINTER(FILE)]
    putc.restype = c_int

# /usr/include/stdio.h: 528
if _libs["libc.so.6"].has("putchar", "cdecl"):
    putchar = _libs["libc.so.6"].get("putchar", "cdecl")
    putchar.argtypes = [c_int]
    putchar.restype = c_int

# /usr/include/stdio.h: 537
if _libs["libc.so.6"].has("fputc_unlocked", "cdecl"):
    fputc_unlocked = _libs["libc.so.6"].get("fputc_unlocked", "cdecl")
    fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
    fputc_unlocked.restype = c_int

# /usr/include/stdio.h: 545
if _libs["libc.so.6"].has("putc_unlocked", "cdecl"):
    putc_unlocked = _libs["libc.so.6"].get("putc_unlocked", "cdecl")
    putc_unlocked.argtypes = [c_int, POINTER(FILE)]
    putc_unlocked.restype = c_int

# /usr/include/stdio.h: 546
if _libs["libc.so.6"].has("putchar_unlocked", "cdecl"):
    putchar_unlocked = _libs["libc.so.6"].get("putchar_unlocked", "cdecl")
    putchar_unlocked.argtypes = [c_int]
    putchar_unlocked.restype = c_int

# /usr/include/stdio.h: 553
if _libs["libc.so.6"].has("getw", "cdecl"):
    getw = _libs["libc.so.6"].get("getw", "cdecl")
    getw.argtypes = [POINTER(FILE)]
    getw.restype = c_int

# /usr/include/stdio.h: 556
if _libs["libc.so.6"].has("putw", "cdecl"):
    putw = _libs["libc.so.6"].get("putw", "cdecl")
    putw.argtypes = [c_int, POINTER(FILE)]
    putw.restype = c_int

# /usr/include/stdio.h: 564
if _libs["libc.so.6"].has("fgets", "cdecl"):
    fgets = _libs["libc.so.6"].get("fgets", "cdecl")
    fgets.argtypes = [String, c_int, POINTER(FILE)]
    if sizeof(c_int) == sizeof(c_void_p):
        fgets.restype = ReturnString
    else:
        fgets.restype = String
        fgets.errcheck = ReturnString

# /usr/include/stdio.h: 603
if _libs["libc.so.6"].has("__getdelim", "cdecl"):
    __getdelim = _libs["libc.so.6"].get("__getdelim", "cdecl")
    __getdelim.argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), c_int, POINTER(FILE)]
    __getdelim.restype = __ssize_t

# /usr/include/stdio.h: 606
if _libs["libc.so.6"].has("getdelim", "cdecl"):
    getdelim = _libs["libc.so.6"].get("getdelim", "cdecl")
    getdelim.argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), c_int, POINTER(FILE)]
    getdelim.restype = __ssize_t

# /usr/include/stdio.h: 616
if _libs["libc.so.6"].has("getline", "cdecl"):
    getline = _libs["libc.so.6"].get("getline", "cdecl")
    getline.argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), POINTER(FILE)]
    getline.restype = __ssize_t

# /usr/include/stdio.h: 626
if _libs["libc.so.6"].has("fputs", "cdecl"):
    fputs = _libs["libc.so.6"].get("fputs", "cdecl")
    fputs.argtypes = [String, POINTER(FILE)]
    fputs.restype = c_int

# /usr/include/stdio.h: 632
if _libs["libc.so.6"].has("puts", "cdecl"):
    puts = _libs["libc.so.6"].get("puts", "cdecl")
    puts.argtypes = [String]
    puts.restype = c_int

# /usr/include/stdio.h: 639
if _libs["libc.so.6"].has("ungetc", "cdecl"):
    ungetc = _libs["libc.so.6"].get("ungetc", "cdecl")
    ungetc.argtypes = [c_int, POINTER(FILE)]
    ungetc.restype = c_int

# /usr/include/stdio.h: 646
if _libs["libc.so.6"].has("fread", "cdecl"):
    fread = _libs["libc.so.6"].get("fread", "cdecl")
    fread.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
    fread.restype = c_size_t

# /usr/include/stdio.h: 652
if _libs["libc.so.6"].has("fwrite", "cdecl"):
    fwrite = _libs["libc.so.6"].get("fwrite", "cdecl")
    fwrite.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
    fwrite.restype = c_size_t

# /usr/include/stdio.h: 673
if _libs["libc.so.6"].has("fread_unlocked", "cdecl"):
    fread_unlocked = _libs["libc.so.6"].get("fread_unlocked", "cdecl")
    fread_unlocked.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
    fread_unlocked.restype = c_size_t

# /usr/include/stdio.h: 675
if _libs["libc.so.6"].has("fwrite_unlocked", "cdecl"):
    fwrite_unlocked = _libs["libc.so.6"].get("fwrite_unlocked", "cdecl")
    fwrite_unlocked.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
    fwrite_unlocked.restype = c_size_t

# /usr/include/stdio.h: 684
if _libs["libc.so.6"].has("fseek", "cdecl"):
    fseek = _libs["libc.so.6"].get("fseek", "cdecl")
    fseek.argtypes = [POINTER(FILE), c_long, c_int]
    fseek.restype = c_int

# /usr/include/stdio.h: 689
if _libs["libc.so.6"].has("ftell", "cdecl"):
    ftell = _libs["libc.so.6"].get("ftell", "cdecl")
    ftell.argtypes = [POINTER(FILE)]
    ftell.restype = c_long

# /usr/include/stdio.h: 694
if _libs["libc.so.6"].has("rewind", "cdecl"):
    rewind = _libs["libc.so.6"].get("rewind", "cdecl")
    rewind.argtypes = [POINTER(FILE)]
    rewind.restype = None

# /usr/include/stdio.h: 707
if _libs["libc.so.6"].has("fseeko", "cdecl"):
    fseeko = _libs["libc.so.6"].get("fseeko", "cdecl")
    fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
    fseeko.restype = c_int

# /usr/include/stdio.h: 712
if _libs["libc.so.6"].has("ftello", "cdecl"):
    ftello = _libs["libc.so.6"].get("ftello", "cdecl")
    ftello.argtypes = [POINTER(FILE)]
    ftello.restype = __off_t

# /usr/include/stdio.h: 731
if _libs["libc.so.6"].has("fgetpos", "cdecl"):
    fgetpos = _libs["libc.so.6"].get("fgetpos", "cdecl")
    fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
    fgetpos.restype = c_int

# /usr/include/stdio.h: 736
if _libs["libc.so.6"].has("fsetpos", "cdecl"):
    fsetpos = _libs["libc.so.6"].get("fsetpos", "cdecl")
    fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
    fsetpos.restype = c_int

# /usr/include/stdio.h: 757
if _libs["libc.so.6"].has("clearerr", "cdecl"):
    clearerr = _libs["libc.so.6"].get("clearerr", "cdecl")
    clearerr.argtypes = [POINTER(FILE)]
    clearerr.restype = None

# /usr/include/stdio.h: 759
if _libs["libc.so.6"].has("feof", "cdecl"):
    feof = _libs["libc.so.6"].get("feof", "cdecl")
    feof.argtypes = [POINTER(FILE)]
    feof.restype = c_int

# /usr/include/stdio.h: 761
if _libs["libc.so.6"].has("ferror", "cdecl"):
    ferror = _libs["libc.so.6"].get("ferror", "cdecl")
    ferror.argtypes = [POINTER(FILE)]
    ferror.restype = c_int

# /usr/include/stdio.h: 765
if _libs["libc.so.6"].has("clearerr_unlocked", "cdecl"):
    clearerr_unlocked = _libs["libc.so.6"].get("clearerr_unlocked", "cdecl")
    clearerr_unlocked.argtypes = [POINTER(FILE)]
    clearerr_unlocked.restype = None

# /usr/include/stdio.h: 766
if _libs["libc.so.6"].has("feof_unlocked", "cdecl"):
    feof_unlocked = _libs["libc.so.6"].get("feof_unlocked", "cdecl")
    feof_unlocked.argtypes = [POINTER(FILE)]
    feof_unlocked.restype = c_int

# /usr/include/stdio.h: 767
if _libs["libc.so.6"].has("ferror_unlocked", "cdecl"):
    ferror_unlocked = _libs["libc.so.6"].get("ferror_unlocked", "cdecl")
    ferror_unlocked.argtypes = [POINTER(FILE)]
    ferror_unlocked.restype = c_int

# /usr/include/stdio.h: 775
if _libs["libc.so.6"].has("perror", "cdecl"):
    perror = _libs["libc.so.6"].get("perror", "cdecl")
    perror.argtypes = [String]
    perror.restype = None

# /usr/include/stdio.h: 786
if _libs["libc.so.6"].has("fileno", "cdecl"):
    fileno = _libs["libc.so.6"].get("fileno", "cdecl")
    fileno.argtypes = [POINTER(FILE)]
    fileno.restype = c_int

# /usr/include/stdio.h: 791
if _libs["libc.so.6"].has("fileno_unlocked", "cdecl"):
    fileno_unlocked = _libs["libc.so.6"].get("fileno_unlocked", "cdecl")
    fileno_unlocked.argtypes = [POINTER(FILE)]
    fileno_unlocked.restype = c_int

# /usr/include/stdio.h: 800
if _libs["libc.so.6"].has("popen", "cdecl"):
    popen = _libs["libc.so.6"].get("popen", "cdecl")
    popen.argtypes = [String, String]
    popen.restype = POINTER(FILE)

# /usr/include/stdio.h: 806
if _libs["libc.so.6"].has("pclose", "cdecl"):
    pclose = _libs["libc.so.6"].get("pclose", "cdecl")
    pclose.argtypes = [POINTER(FILE)]
    pclose.restype = c_int

# /usr/include/stdio.h: 812
if _libs["libc.so.6"].has("ctermid", "cdecl"):
    ctermid = _libs["libc.so.6"].get("ctermid", "cdecl")
    ctermid.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        ctermid.restype = ReturnString
    else:
        ctermid.restype = String
        ctermid.errcheck = ReturnString

# /usr/include/stdio.h: 840
if _libs["libc.so.6"].has("flockfile", "cdecl"):
    flockfile = _libs["libc.so.6"].get("flockfile", "cdecl")
    flockfile.argtypes = [POINTER(FILE)]
    flockfile.restype = None

# /usr/include/stdio.h: 844
if _libs["libc.so.6"].has("ftrylockfile", "cdecl"):
    ftrylockfile = _libs["libc.so.6"].get("ftrylockfile", "cdecl")
    ftrylockfile.argtypes = [POINTER(FILE)]
    ftrylockfile.restype = c_int

# /usr/include/stdio.h: 847
if _libs["libc.so.6"].has("funlockfile", "cdecl"):
    funlockfile = _libs["libc.so.6"].get("funlockfile", "cdecl")
    funlockfile.argtypes = [POINTER(FILE)]
    funlockfile.restype = None

# /usr/include/stdio.h: 858
if _libs["libc.so.6"].has("__uflow", "cdecl"):
    __uflow = _libs["libc.so.6"].get("__uflow", "cdecl")
    __uflow.argtypes = [POINTER(FILE)]
    __uflow.restype = c_int

# /usr/include/stdio.h: 859
if _libs["libc.so.6"].has("__overflow", "cdecl"):
    __overflow = _libs["libc.so.6"].get("__overflow", "cdecl")
    __overflow.argtypes = [POINTER(FILE), c_int]
    __overflow.restype = c_int

enum_anon_4 = c_int# /usr/include/stdio_ext.h: 27

FSETLOCKING_QUERY = 0# /usr/include/stdio_ext.h: 27

FSETLOCKING_INTERNAL = (FSETLOCKING_QUERY + 1)# /usr/include/stdio_ext.h: 27

FSETLOCKING_BYCALLER = (FSETLOCKING_INTERNAL + 1)# /usr/include/stdio_ext.h: 27

# /usr/include/stdio_ext.h: 46
if _libs["libc.so.6"].has("__fbufsize", "cdecl"):
    __fbufsize = _libs["libc.so.6"].get("__fbufsize", "cdecl")
    __fbufsize.argtypes = [POINTER(FILE)]
    __fbufsize.restype = c_size_t

# /usr/include/stdio_ext.h: 51
if _libs["libc.so.6"].has("__freading", "cdecl"):
    __freading = _libs["libc.so.6"].get("__freading", "cdecl")
    __freading.argtypes = [POINTER(FILE)]
    __freading.restype = c_int

# /usr/include/stdio_ext.h: 56
if _libs["libc.so.6"].has("__fwriting", "cdecl"):
    __fwriting = _libs["libc.so.6"].get("__fwriting", "cdecl")
    __fwriting.argtypes = [POINTER(FILE)]
    __fwriting.restype = c_int

# /usr/include/stdio_ext.h: 61
if _libs["libc.so.6"].has("__freadable", "cdecl"):
    __freadable = _libs["libc.so.6"].get("__freadable", "cdecl")
    __freadable.argtypes = [POINTER(FILE)]
    __freadable.restype = c_int

# /usr/include/stdio_ext.h: 64
if _libs["libc.so.6"].has("__fwritable", "cdecl"):
    __fwritable = _libs["libc.so.6"].get("__fwritable", "cdecl")
    __fwritable.argtypes = [POINTER(FILE)]
    __fwritable.restype = c_int

# /usr/include/stdio_ext.h: 68
if _libs["libc.so.6"].has("__flbf", "cdecl"):
    __flbf = _libs["libc.so.6"].get("__flbf", "cdecl")
    __flbf.argtypes = [POINTER(FILE)]
    __flbf.restype = c_int

# /usr/include/stdio_ext.h: 72
if _libs["libc.so.6"].has("__fpurge", "cdecl"):
    __fpurge = _libs["libc.so.6"].get("__fpurge", "cdecl")
    __fpurge.argtypes = [POINTER(FILE)]
    __fpurge.restype = None

# /usr/include/stdio_ext.h: 75
if _libs["libc.so.6"].has("__fpending", "cdecl"):
    __fpending = _libs["libc.so.6"].get("__fpending", "cdecl")
    __fpending.argtypes = [POINTER(FILE)]
    __fpending.restype = c_size_t

# /usr/include/stdio_ext.h: 78
if _libs["libc.so.6"].has("_flushlbf", "cdecl"):
    _flushlbf = _libs["libc.so.6"].get("_flushlbf", "cdecl")
    _flushlbf.argtypes = []
    _flushlbf.restype = None

# /usr/include/stdio_ext.h: 82
if _libs["libc.so.6"].has("__fsetlocking", "cdecl"):
    __fsetlocking = _libs["libc.so.6"].get("__fsetlocking", "cdecl")
    __fsetlocking.argtypes = [POINTER(FILE), c_int]
    __fsetlocking.restype = c_int

enum_anon_5 = c_int# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 57

idtype_t = enum_anon_5# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 57

# /usr/include/stdlib.h: 62
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'quot',
    'rem',
]
struct_anon_6._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]

div_t = struct_anon_6# /usr/include/stdlib.h: 62

# /usr/include/stdlib.h: 70
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'quot',
    'rem',
]
struct_anon_7._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]

ldiv_t = struct_anon_7# /usr/include/stdlib.h: 70

# /usr/include/stdlib.h: 80
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'quot',
    'rem',
]
struct_anon_8._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]

lldiv_t = struct_anon_8# /usr/include/stdlib.h: 80

# /usr/include/stdlib.h: 97
if _libs["libc.so.6"].has("__ctype_get_mb_cur_max", "cdecl"):
    __ctype_get_mb_cur_max = _libs["libc.so.6"].get("__ctype_get_mb_cur_max", "cdecl")
    __ctype_get_mb_cur_max.argtypes = []
    __ctype_get_mb_cur_max.restype = c_size_t

# /usr/include/stdlib.h: 101
if _libs["libc.so.6"].has("atof", "cdecl"):
    atof = _libs["libc.so.6"].get("atof", "cdecl")
    atof.argtypes = [String]
    atof.restype = c_double

# /usr/include/stdlib.h: 104
if _libs["libc.so.6"].has("atoi", "cdecl"):
    atoi = _libs["libc.so.6"].get("atoi", "cdecl")
    atoi.argtypes = [String]
    atoi.restype = c_int

# /usr/include/stdlib.h: 107
if _libs["libc.so.6"].has("atol", "cdecl"):
    atol = _libs["libc.so.6"].get("atol", "cdecl")
    atol.argtypes = [String]
    atol.restype = c_long

# /usr/include/stdlib.h: 112
if _libs["libc.so.6"].has("atoll", "cdecl"):
    atoll = _libs["libc.so.6"].get("atoll", "cdecl")
    atoll.argtypes = [String]
    atoll.restype = c_longlong

# /usr/include/stdlib.h: 117
if _libs["libc.so.6"].has("strtod", "cdecl"):
    strtod = _libs["libc.so.6"].get("strtod", "cdecl")
    strtod.argtypes = [String, POINTER(POINTER(c_char))]
    strtod.restype = c_double

# /usr/include/stdlib.h: 123
if _libs["libc.so.6"].has("strtof", "cdecl"):
    strtof = _libs["libc.so.6"].get("strtof", "cdecl")
    strtof.argtypes = [String, POINTER(POINTER(c_char))]
    strtof.restype = c_float

# /usr/include/stdlib.h: 126
if _libs["libc.so.6"].has("strtold", "cdecl"):
    strtold = _libs["libc.so.6"].get("strtold", "cdecl")
    strtold.argtypes = [String, POINTER(POINTER(c_char))]
    strtold.restype = c_longdouble

# /usr/include/stdlib.h: 176
if _libs["libc.so.6"].has("strtol", "cdecl"):
    strtol = _libs["libc.so.6"].get("strtol", "cdecl")
    strtol.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtol.restype = c_long

# /usr/include/stdlib.h: 180
if _libs["libc.so.6"].has("strtoul", "cdecl"):
    strtoul = _libs["libc.so.6"].get("strtoul", "cdecl")
    strtoul.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoul.restype = c_ulong

# /usr/include/stdlib.h: 187
if _libs["libc.so.6"].has("strtoq", "cdecl"):
    strtoq = _libs["libc.so.6"].get("strtoq", "cdecl")
    strtoq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoq.restype = c_longlong

# /usr/include/stdlib.h: 192
if _libs["libc.so.6"].has("strtouq", "cdecl"):
    strtouq = _libs["libc.so.6"].get("strtouq", "cdecl")
    strtouq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtouq.restype = c_ulonglong

# /usr/include/stdlib.h: 200
if _libs["libc.so.6"].has("strtoll", "cdecl"):
    strtoll = _libs["libc.so.6"].get("strtoll", "cdecl")
    strtoll.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoll.restype = c_longlong

# /usr/include/stdlib.h: 205
if _libs["libc.so.6"].has("strtoull", "cdecl"):
    strtoull = _libs["libc.so.6"].get("strtoull", "cdecl")
    strtoull.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoull.restype = c_ulonglong

# /usr/include/stdlib.h: 385
if _libs["libc.so.6"].has("l64a", "cdecl"):
    l64a = _libs["libc.so.6"].get("l64a", "cdecl")
    l64a.argtypes = [c_long]
    if sizeof(c_int) == sizeof(c_void_p):
        l64a.restype = ReturnString
    else:
        l64a.restype = String
        l64a.errcheck = ReturnString

# /usr/include/stdlib.h: 388
if _libs["libc.so.6"].has("a64l", "cdecl"):
    a64l = _libs["libc.so.6"].get("a64l", "cdecl")
    a64l.argtypes = [String]
    a64l.restype = c_long

u_char = __u_char# /usr/include/x86_64-linux-gnu/sys/types.h: 33

u_short = __u_short# /usr/include/x86_64-linux-gnu/sys/types.h: 34

u_int = __u_int# /usr/include/x86_64-linux-gnu/sys/types.h: 35

u_long = __u_long# /usr/include/x86_64-linux-gnu/sys/types.h: 36

quad_t = __quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 37

u_quad_t = __u_quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 38

fsid_t = __fsid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 39

loff_t = __loff_t# /usr/include/x86_64-linux-gnu/sys/types.h: 42

ino_t = __ino_t# /usr/include/x86_64-linux-gnu/sys/types.h: 47

dev_t = __dev_t# /usr/include/x86_64-linux-gnu/sys/types.h: 59

gid_t = __gid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 64

mode_t = __mode_t# /usr/include/x86_64-linux-gnu/sys/types.h: 69

nlink_t = __nlink_t# /usr/include/x86_64-linux-gnu/sys/types.h: 74

uid_t = __uid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 79

pid_t = __pid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 97

id_t = __id_t# /usr/include/x86_64-linux-gnu/sys/types.h: 103

daddr_t = __daddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 114

caddr_t = __caddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 115

key_t = __key_t# /usr/include/x86_64-linux-gnu/sys/types.h: 121

clock_t = __clock_t# /usr/include/x86_64-linux-gnu/bits/types/clock_t.h: 7

clockid_t = __clockid_t# /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h: 7

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 7

timer_t = __timer_t# /usr/include/x86_64-linux-gnu/bits/types/timer_t.h: 7

ulong = c_ulong# /usr/include/x86_64-linux-gnu/sys/types.h: 148

ushort = c_uint# /usr/include/x86_64-linux-gnu/sys/types.h: 149

uint = c_uint# /usr/include/x86_64-linux-gnu/sys/types.h: 150

u_int8_t = __uint8_t# /usr/include/x86_64-linux-gnu/sys/types.h: 158

u_int16_t = __uint16_t# /usr/include/x86_64-linux-gnu/sys/types.h: 159

u_int32_t = __uint32_t# /usr/include/x86_64-linux-gnu/sys/types.h: 160

u_int64_t = __uint64_t# /usr/include/x86_64-linux-gnu/sys/types.h: 161

register_t = c_int# /usr/include/x86_64-linux-gnu/sys/types.h: 166

# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    '__val',
]
struct_anon_9._fields_ = [
    ('__val', c_ulong * int((1024 / (8 * sizeof(c_ulong))))),
]

__sigset_t = struct_anon_9# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8

sigset_t = __sigset_t# /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 10
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

suseconds_t = __suseconds_t# /usr/include/x86_64-linux-gnu/sys/select.h: 43

__fd_mask = c_long# /usr/include/x86_64-linux-gnu/sys/select.h: 49

# /usr/include/x86_64-linux-gnu/sys/select.h: 70
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    '__fds_bits',
]
struct_anon_10._fields_ = [
    ('__fds_bits', __fd_mask * int((1024 / (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)))),
]

fd_set = struct_anon_10# /usr/include/x86_64-linux-gnu/sys/select.h: 70

fd_mask = __fd_mask# /usr/include/x86_64-linux-gnu/sys/select.h: 77

# /usr/include/x86_64-linux-gnu/sys/select.h: 101
if _libs["libc.so.6"].has("select", "cdecl"):
    select = _libs["libc.so.6"].get("select", "cdecl")
    select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timeval)]
    select.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/select.h: 113
if _libs["libc.so.6"].has("pselect", "cdecl"):
    pselect = _libs["libc.so.6"].get("pselect", "cdecl")
    pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timespec), POINTER(__sigset_t)]
    pselect.restype = c_int

blksize_t = __blksize_t# /usr/include/x86_64-linux-gnu/sys/types.h: 185

blkcnt_t = __blkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 192

fsblkcnt_t = __fsblkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 196

fsfilcnt_t = __fsfilcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 200

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 56
class union_pthread_attr_t(Union):
    pass

union_pthread_attr_t.__slots__ = [
    '__size',
    '__align',
]
union_pthread_attr_t._fields_ = [
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_attr_t = union_pthread_attr_t# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 62

# /usr/include/stdlib.h: 401
if _libs["libc.so.6"].has("random", "cdecl"):
    random = _libs["libc.so.6"].get("random", "cdecl")
    random.argtypes = []
    random.restype = c_long

# /usr/include/stdlib.h: 404
if _libs["libc.so.6"].has("srandom", "cdecl"):
    srandom = _libs["libc.so.6"].get("srandom", "cdecl")
    srandom.argtypes = [c_uint]
    srandom.restype = None

# /usr/include/stdlib.h: 410
if _libs["libc.so.6"].has("initstate", "cdecl"):
    initstate = _libs["libc.so.6"].get("initstate", "cdecl")
    initstate.argtypes = [c_uint, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        initstate.restype = ReturnString
    else:
        initstate.restype = String
        initstate.errcheck = ReturnString

# /usr/include/stdlib.h: 415
if _libs["libc.so.6"].has("setstate", "cdecl"):
    setstate = _libs["libc.so.6"].get("setstate", "cdecl")
    setstate.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        setstate.restype = ReturnString
    else:
        setstate.restype = String
        setstate.errcheck = ReturnString

# /usr/include/stdlib.h: 423
class struct_random_data(Structure):
    pass

struct_random_data.__slots__ = [
    'fptr',
    'rptr',
    'state',
    'rand_type',
    'rand_deg',
    'rand_sep',
    'end_ptr',
]
struct_random_data._fields_ = [
    ('fptr', POINTER(c_int32)),
    ('rptr', POINTER(c_int32)),
    ('state', POINTER(c_int32)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(c_int32)),
]

# /usr/include/stdlib.h: 434
if _libs["libc.so.6"].has("random_r", "cdecl"):
    random_r = _libs["libc.so.6"].get("random_r", "cdecl")
    random_r.argtypes = [POINTER(struct_random_data), POINTER(c_int32)]
    random_r.restype = c_int

# /usr/include/stdlib.h: 437
if _libs["libc.so.6"].has("srandom_r", "cdecl"):
    srandom_r = _libs["libc.so.6"].get("srandom_r", "cdecl")
    srandom_r.argtypes = [c_uint, POINTER(struct_random_data)]
    srandom_r.restype = c_int

# /usr/include/stdlib.h: 440
if _libs["libc.so.6"].has("initstate_r", "cdecl"):
    initstate_r = _libs["libc.so.6"].get("initstate_r", "cdecl")
    initstate_r.argtypes = [c_uint, String, c_size_t, POINTER(struct_random_data)]
    initstate_r.restype = c_int

# /usr/include/stdlib.h: 445
if _libs["libc.so.6"].has("setstate_r", "cdecl"):
    setstate_r = _libs["libc.so.6"].get("setstate_r", "cdecl")
    setstate_r.argtypes = [String, POINTER(struct_random_data)]
    setstate_r.restype = c_int

# /usr/include/stdlib.h: 453
if _libs["libc.so.6"].has("rand", "cdecl"):
    rand = _libs["libc.so.6"].get("rand", "cdecl")
    rand.argtypes = []
    rand.restype = c_int

# /usr/include/stdlib.h: 455
if _libs["libc.so.6"].has("srand", "cdecl"):
    srand = _libs["libc.so.6"].get("srand", "cdecl")
    srand.argtypes = [c_uint]
    srand.restype = None

# /usr/include/stdlib.h: 459
if _libs["libc.so.6"].has("rand_r", "cdecl"):
    rand_r = _libs["libc.so.6"].get("rand_r", "cdecl")
    rand_r.argtypes = [POINTER(c_uint)]
    rand_r.restype = c_int

# /usr/include/stdlib.h: 467
if _libs["libc.so.6"].has("drand48", "cdecl"):
    drand48 = _libs["libc.so.6"].get("drand48", "cdecl")
    drand48.argtypes = []
    drand48.restype = c_double

# /usr/include/stdlib.h: 468
if _libs["libc.so.6"].has("erand48", "cdecl"):
    erand48 = _libs["libc.so.6"].get("erand48", "cdecl")
    erand48.argtypes = [c_uint * int(3)]
    erand48.restype = c_double

# /usr/include/stdlib.h: 471
if _libs["libc.so.6"].has("lrand48", "cdecl"):
    lrand48 = _libs["libc.so.6"].get("lrand48", "cdecl")
    lrand48.argtypes = []
    lrand48.restype = c_long

# /usr/include/stdlib.h: 472
if _libs["libc.so.6"].has("nrand48", "cdecl"):
    nrand48 = _libs["libc.so.6"].get("nrand48", "cdecl")
    nrand48.argtypes = [c_uint * int(3)]
    nrand48.restype = c_long

# /usr/include/stdlib.h: 476
if _libs["libc.so.6"].has("mrand48", "cdecl"):
    mrand48 = _libs["libc.so.6"].get("mrand48", "cdecl")
    mrand48.argtypes = []
    mrand48.restype = c_long

# /usr/include/stdlib.h: 477
if _libs["libc.so.6"].has("jrand48", "cdecl"):
    jrand48 = _libs["libc.so.6"].get("jrand48", "cdecl")
    jrand48.argtypes = [c_uint * int(3)]
    jrand48.restype = c_long

# /usr/include/stdlib.h: 481
if _libs["libc.so.6"].has("srand48", "cdecl"):
    srand48 = _libs["libc.so.6"].get("srand48", "cdecl")
    srand48.argtypes = [c_long]
    srand48.restype = None

# /usr/include/stdlib.h: 482
if _libs["libc.so.6"].has("seed48", "cdecl"):
    seed48 = _libs["libc.so.6"].get("seed48", "cdecl")
    seed48.argtypes = [c_uint * int(3)]
    seed48.restype = POINTER(c_uint)

# /usr/include/stdlib.h: 484
if _libs["libc.so.6"].has("lcong48", "cdecl"):
    lcong48 = _libs["libc.so.6"].get("lcong48", "cdecl")
    lcong48.argtypes = [c_uint * int(7)]
    lcong48.restype = None

# /usr/include/stdlib.h: 490
class struct_drand48_data(Structure):
    pass

struct_drand48_data.__slots__ = [
    '__x',
    '__old_x',
    '__c',
    '__init',
    '__a',
]
struct_drand48_data._fields_ = [
    ('__x', c_uint * int(3)),
    ('__old_x', c_uint * int(3)),
    ('__c', c_uint),
    ('__init', c_uint),
    ('__a', c_ulonglong),
]

# /usr/include/stdlib.h: 501
if _libs["libc.so.6"].has("drand48_r", "cdecl"):
    drand48_r = _libs["libc.so.6"].get("drand48_r", "cdecl")
    drand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_double)]
    drand48_r.restype = c_int

# /usr/include/stdlib.h: 503
if _libs["libc.so.6"].has("erand48_r", "cdecl"):
    erand48_r = _libs["libc.so.6"].get("erand48_r", "cdecl")
    erand48_r.argtypes = [c_uint * int(3), POINTER(struct_drand48_data), POINTER(c_double)]
    erand48_r.restype = c_int

# /usr/include/stdlib.h: 508
if _libs["libc.so.6"].has("lrand48_r", "cdecl"):
    lrand48_r = _libs["libc.so.6"].get("lrand48_r", "cdecl")
    lrand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_long)]
    lrand48_r.restype = c_int

# /usr/include/stdlib.h: 511
if _libs["libc.so.6"].has("nrand48_r", "cdecl"):
    nrand48_r = _libs["libc.so.6"].get("nrand48_r", "cdecl")
    nrand48_r.argtypes = [c_uint * int(3), POINTER(struct_drand48_data), POINTER(c_long)]
    nrand48_r.restype = c_int

# /usr/include/stdlib.h: 517
if _libs["libc.so.6"].has("mrand48_r", "cdecl"):
    mrand48_r = _libs["libc.so.6"].get("mrand48_r", "cdecl")
    mrand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_long)]
    mrand48_r.restype = c_int

# /usr/include/stdlib.h: 520
if _libs["libc.so.6"].has("jrand48_r", "cdecl"):
    jrand48_r = _libs["libc.so.6"].get("jrand48_r", "cdecl")
    jrand48_r.argtypes = [c_uint * int(3), POINTER(struct_drand48_data), POINTER(c_long)]
    jrand48_r.restype = c_int

# /usr/include/stdlib.h: 526
if _libs["libc.so.6"].has("srand48_r", "cdecl"):
    srand48_r = _libs["libc.so.6"].get("srand48_r", "cdecl")
    srand48_r.argtypes = [c_long, POINTER(struct_drand48_data)]
    srand48_r.restype = c_int

# /usr/include/stdlib.h: 529
if _libs["libc.so.6"].has("seed48_r", "cdecl"):
    seed48_r = _libs["libc.so.6"].get("seed48_r", "cdecl")
    seed48_r.argtypes = [c_uint * int(3), POINTER(struct_drand48_data)]
    seed48_r.restype = c_int

# /usr/include/stdlib.h: 532
if _libs["libc.so.6"].has("lcong48_r", "cdecl"):
    lcong48_r = _libs["libc.so.6"].get("lcong48_r", "cdecl")
    lcong48_r.argtypes = [c_uint * int(7), POINTER(struct_drand48_data)]
    lcong48_r.restype = c_int

# /usr/include/stdlib.h: 539
if _libs["libc.so.6"].has("malloc", "cdecl"):
    malloc = _libs["libc.so.6"].get("malloc", "cdecl")
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(c_ubyte)
    malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 542
if _libs["libc.so.6"].has("calloc", "cdecl"):
    calloc = _libs["libc.so.6"].get("calloc", "cdecl")
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(c_ubyte)
    calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 550
if _libs["libc.so.6"].has("realloc", "cdecl"):
    realloc = _libs["libc.so.6"].get("realloc", "cdecl")
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(c_ubyte)
    realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 559
if _libs["libc.so.6"].has("reallocarray", "cdecl"):
    reallocarray = _libs["libc.so.6"].get("reallocarray", "cdecl")
    reallocarray.argtypes = [POINTER(None), c_size_t, c_size_t]
    reallocarray.restype = POINTER(c_ubyte)
    reallocarray.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 565
if _libs["libc.so.6"].has("free", "cdecl"):
    free = _libs["libc.so.6"].get("free", "cdecl")
    free.argtypes = [POINTER(None)]
    free.restype = None

# /usr/include/stdlib.h: 574
if _libs["libc.so.6"].has("valloc", "cdecl"):
    valloc = _libs["libc.so.6"].get("valloc", "cdecl")
    valloc.argtypes = [c_size_t]
    valloc.restype = POINTER(c_ubyte)
    valloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 580
if _libs["libc.so.6"].has("posix_memalign", "cdecl"):
    posix_memalign = _libs["libc.so.6"].get("posix_memalign", "cdecl")
    posix_memalign.argtypes = [POINTER(POINTER(None)), c_size_t, c_size_t]
    posix_memalign.restype = c_int

# /usr/include/stdlib.h: 586
if _libs["libc.so.6"].has("aligned_alloc", "cdecl"):
    aligned_alloc = _libs["libc.so.6"].get("aligned_alloc", "cdecl")
    aligned_alloc.argtypes = [c_size_t, c_size_t]
    aligned_alloc.restype = POINTER(c_ubyte)
    aligned_alloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 591
if _libs["libc.so.6"].has("abort", "cdecl"):
    abort = _libs["libc.so.6"].get("abort", "cdecl")
    abort.argtypes = []
    abort.restype = None

# /usr/include/stdlib.h: 595
for _lib in _libs.values():
    if not _lib.has("atexit", "cdecl"):
        continue
    atexit = _lib.get("atexit", "cdecl")
    atexit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    atexit.restype = c_int
    break

# /usr/include/stdlib.h: 603
for _lib in _libs.values():
    if not _lib.has("at_quick_exit", "cdecl"):
        continue
    at_quick_exit = _lib.get("at_quick_exit", "cdecl")
    at_quick_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    at_quick_exit.restype = c_int
    break

# /usr/include/stdlib.h: 610
if _libs["libc.so.6"].has("on_exit", "cdecl"):
    on_exit = _libs["libc.so.6"].get("on_exit", "cdecl")
    on_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None)), POINTER(None)]
    on_exit.restype = c_int

# /usr/include/stdlib.h: 617
if _libs["libc.so.6"].has("exit", "cdecl"):
    exit = _libs["libc.so.6"].get("exit", "cdecl")
    exit.argtypes = [c_int]
    exit.restype = None

# /usr/include/stdlib.h: 623
if _libs["libc.so.6"].has("quick_exit", "cdecl"):
    quick_exit = _libs["libc.so.6"].get("quick_exit", "cdecl")
    quick_exit.argtypes = [c_int]
    quick_exit.restype = None

# /usr/include/stdlib.h: 629
if _libs["libc.so.6"].has("_Exit", "cdecl"):
    _Exit = _libs["libc.so.6"].get("_Exit", "cdecl")
    _Exit.argtypes = [c_int]
    _Exit.restype = None

# /usr/include/stdlib.h: 634
if _libs["libc.so.6"].has("getenv", "cdecl"):
    getenv = _libs["libc.so.6"].get("getenv", "cdecl")
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString

# /usr/include/stdlib.h: 647
if _libs["libc.so.6"].has("putenv", "cdecl"):
    putenv = _libs["libc.so.6"].get("putenv", "cdecl")
    putenv.argtypes = [String]
    putenv.restype = c_int

# /usr/include/stdlib.h: 653
if _libs["libc.so.6"].has("setenv", "cdecl"):
    setenv = _libs["libc.so.6"].get("setenv", "cdecl")
    setenv.argtypes = [String, String, c_int]
    setenv.restype = c_int

# /usr/include/stdlib.h: 657
if _libs["libc.so.6"].has("unsetenv", "cdecl"):
    unsetenv = _libs["libc.so.6"].get("unsetenv", "cdecl")
    unsetenv.argtypes = [String]
    unsetenv.restype = c_int

# /usr/include/stdlib.h: 664
if _libs["libc.so.6"].has("clearenv", "cdecl"):
    clearenv = _libs["libc.so.6"].get("clearenv", "cdecl")
    clearenv.argtypes = []
    clearenv.restype = c_int

# /usr/include/stdlib.h: 675
if _libs["libc.so.6"].has("mktemp", "cdecl"):
    mktemp = _libs["libc.so.6"].get("mktemp", "cdecl")
    mktemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mktemp.restype = ReturnString
    else:
        mktemp.restype = String
        mktemp.errcheck = ReturnString

# /usr/include/stdlib.h: 688
if _libs["libc.so.6"].has("mkstemp", "cdecl"):
    mkstemp = _libs["libc.so.6"].get("mkstemp", "cdecl")
    mkstemp.argtypes = [String]
    mkstemp.restype = c_int

# /usr/include/stdlib.h: 710
if _libs["libc.so.6"].has("mkstemps", "cdecl"):
    mkstemps = _libs["libc.so.6"].get("mkstemps", "cdecl")
    mkstemps.argtypes = [String, c_int]
    mkstemps.restype = c_int

# /usr/include/stdlib.h: 731
if _libs["libc.so.6"].has("mkdtemp", "cdecl"):
    mkdtemp = _libs["libc.so.6"].get("mkdtemp", "cdecl")
    mkdtemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mkdtemp.restype = ReturnString
    else:
        mkdtemp.restype = String
        mkdtemp.errcheck = ReturnString

# /usr/include/stdlib.h: 784
if _libs["libc.so.6"].has("system", "cdecl"):
    system = _libs["libc.so.6"].get("system", "cdecl")
    system.argtypes = [String]
    system.restype = c_int

# /usr/include/stdlib.h: 800
if _libs["libc.so.6"].has("realpath", "cdecl"):
    realpath = _libs["libc.so.6"].get("realpath", "cdecl")
    realpath.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        realpath.restype = ReturnString
    else:
        realpath.restype = String
        realpath.errcheck = ReturnString

__compar_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))# /usr/include/stdlib.h: 808

# /usr/include/stdlib.h: 820
if _libs["libc.so.6"].has("bsearch", "cdecl"):
    bsearch = _libs["libc.so.6"].get("bsearch", "cdecl")
    bsearch.argtypes = [POINTER(None), POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    bsearch.restype = POINTER(c_ubyte)
    bsearch.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 830
if _libs["libc.so.6"].has("qsort", "cdecl"):
    qsort = _libs["libc.so.6"].get("qsort", "cdecl")
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    qsort.restype = None

# /usr/include/stdlib.h: 840
if _libs["libc.so.6"].has("abs", "cdecl"):
    abs = _libs["libc.so.6"].get("abs", "cdecl")
    abs.argtypes = [c_int]
    abs.restype = c_int

# /usr/include/stdlib.h: 841
if _libs["libc.so.6"].has("labs", "cdecl"):
    labs = _libs["libc.so.6"].get("labs", "cdecl")
    labs.argtypes = [c_long]
    labs.restype = c_long

# /usr/include/stdlib.h: 844
if _libs["libc.so.6"].has("llabs", "cdecl"):
    llabs = _libs["libc.so.6"].get("llabs", "cdecl")
    llabs.argtypes = [c_longlong]
    llabs.restype = c_longlong

# /usr/include/stdlib.h: 852
if _libs["libc.so.6"].has("div", "cdecl"):
    div = _libs["libc.so.6"].get("div", "cdecl")
    div.argtypes = [c_int, c_int]
    div.restype = div_t

# /usr/include/stdlib.h: 854
if _libs["libc.so.6"].has("ldiv", "cdecl"):
    ldiv = _libs["libc.so.6"].get("ldiv", "cdecl")
    ldiv.argtypes = [c_long, c_long]
    ldiv.restype = ldiv_t

# /usr/include/stdlib.h: 858
if _libs["libc.so.6"].has("lldiv", "cdecl"):
    lldiv = _libs["libc.so.6"].get("lldiv", "cdecl")
    lldiv.argtypes = [c_longlong, c_longlong]
    lldiv.restype = lldiv_t

# /usr/include/stdlib.h: 872
if _libs["libc.so.6"].has("ecvt", "cdecl"):
    ecvt = _libs["libc.so.6"].get("ecvt", "cdecl")
    ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecvt.restype = ReturnString
    else:
        ecvt.restype = String
        ecvt.errcheck = ReturnString

# /usr/include/stdlib.h: 878
if _libs["libc.so.6"].has("fcvt", "cdecl"):
    fcvt = _libs["libc.so.6"].get("fcvt", "cdecl")
    fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        fcvt.restype = ReturnString
    else:
        fcvt.restype = String
        fcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 884
if _libs["libc.so.6"].has("gcvt", "cdecl"):
    gcvt = _libs["libc.so.6"].get("gcvt", "cdecl")
    gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        gcvt.restype = ReturnString
    else:
        gcvt.restype = String
        gcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 890
if _libs["libc.so.6"].has("qecvt", "cdecl"):
    qecvt = _libs["libc.so.6"].get("qecvt", "cdecl")
    qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        qecvt.restype = ReturnString
    else:
        qecvt.restype = String
        qecvt.errcheck = ReturnString

# /usr/include/stdlib.h: 893
if _libs["libc.so.6"].has("qfcvt", "cdecl"):
    qfcvt = _libs["libc.so.6"].get("qfcvt", "cdecl")
    qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        qfcvt.restype = ReturnString
    else:
        qfcvt.restype = String
        qfcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 896
if _libs["libc.so.6"].has("qgcvt", "cdecl"):
    qgcvt = _libs["libc.so.6"].get("qgcvt", "cdecl")
    qgcvt.argtypes = [c_longdouble, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        qgcvt.restype = ReturnString
    else:
        qgcvt.restype = String
        qgcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 902
if _libs["libc.so.6"].has("ecvt_r", "cdecl"):
    ecvt_r = _libs["libc.so.6"].get("ecvt_r", "cdecl")
    ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    ecvt_r.restype = c_int

# /usr/include/stdlib.h: 905
if _libs["libc.so.6"].has("fcvt_r", "cdecl"):
    fcvt_r = _libs["libc.so.6"].get("fcvt_r", "cdecl")
    fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    fcvt_r.restype = c_int

# /usr/include/stdlib.h: 909
if _libs["libc.so.6"].has("qecvt_r", "cdecl"):
    qecvt_r = _libs["libc.so.6"].get("qecvt_r", "cdecl")
    qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    qecvt_r.restype = c_int

# /usr/include/stdlib.h: 913
if _libs["libc.so.6"].has("qfcvt_r", "cdecl"):
    qfcvt_r = _libs["libc.so.6"].get("qfcvt_r", "cdecl")
    qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    qfcvt_r.restype = c_int

# /usr/include/stdlib.h: 922
if _libs["libc.so.6"].has("mblen", "cdecl"):
    mblen = _libs["libc.so.6"].get("mblen", "cdecl")
    mblen.argtypes = [String, c_size_t]
    mblen.restype = c_int

# /usr/include/stdlib.h: 925
if _libs["libc.so.6"].has("mbtowc", "cdecl"):
    mbtowc = _libs["libc.so.6"].get("mbtowc", "cdecl")
    mbtowc.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbtowc.restype = c_int

# /usr/include/stdlib.h: 929
if _libs["libc.so.6"].has("wctomb", "cdecl"):
    wctomb = _libs["libc.so.6"].get("wctomb", "cdecl")
    wctomb.argtypes = [String, c_wchar]
    wctomb.restype = c_int

# /usr/include/stdlib.h: 933
if _libs["libc.so.6"].has("mbstowcs", "cdecl"):
    mbstowcs = _libs["libc.so.6"].get("mbstowcs", "cdecl")
    mbstowcs.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbstowcs.restype = c_size_t

# /usr/include/stdlib.h: 936
if _libs["libc.so.6"].has("wcstombs", "cdecl"):
    wcstombs = _libs["libc.so.6"].get("wcstombs", "cdecl")
    wcstombs.argtypes = [String, POINTER(c_wchar), c_size_t]
    wcstombs.restype = c_size_t

# /usr/include/stdlib.h: 946
if _libs["libc.so.6"].has("rpmatch", "cdecl"):
    rpmatch = _libs["libc.so.6"].get("rpmatch", "cdecl")
    rpmatch.argtypes = [String]
    rpmatch.restype = c_int

# /usr/include/stdlib.h: 957
if _libs["libc.so.6"].has("getsubopt", "cdecl"):
    getsubopt = _libs["libc.so.6"].get("getsubopt", "cdecl")
    getsubopt.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    getsubopt.restype = c_int

# /usr/include/stdlib.h: 1003
if _libs["libc.so.6"].has("getloadavg", "cdecl"):
    getloadavg = _libs["libc.so.6"].get("getloadavg", "cdecl")
    getloadavg.argtypes = [POINTER(c_double), c_int]
    getloadavg.restype = c_int

# /usr/include/x86_64-linux-gnu/a.out.h: 8
class struct_exec(Structure):
    pass

struct_exec.__slots__ = [
    'a_info',
    'a_text',
    'a_data',
    'a_bss',
    'a_syms',
    'a_entry',
    'a_trsize',
    'a_drsize',
]
struct_exec._fields_ = [
    ('a_info', c_ulong),
    ('a_text', c_uint),
    ('a_data', c_uint),
    ('a_bss', c_uint),
    ('a_syms', c_uint),
    ('a_entry', c_uint),
    ('a_trsize', c_uint),
    ('a_drsize', c_uint),
]

enum_machine_type = c_int# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_OLDSUN2 = 0# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_68010 = 1# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_68020 = 2# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_SPARC = 3# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_386 = 100# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_MIPS1 = 151# /usr/include/x86_64-linux-gnu/a.out.h: 20

M_MIPS2 = 152# /usr/include/x86_64-linux-gnu/a.out.h: 20

# /usr/include/x86_64-linux-gnu/a.out.h: 90
class struct_nlist(Structure):
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 92
class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    'n_name',
    'n_next',
    'n_strx',
]
union_anon_23._fields_ = [
    ('n_name', String),
    ('n_next', POINTER(struct_nlist)),
    ('n_strx', c_long),
]

struct_nlist.__slots__ = [
    'n_un',
    'n_type',
    'n_other',
    'n_desc',
    'n_value',
]
struct_nlist._fields_ = [
    ('n_un', union_anon_23),
    ('n_type', c_ubyte),
    ('n_other', c_char),
    ('n_desc', c_short),
    ('n_value', c_ulong),
]

# /usr/include/x86_64-linux-gnu/a.out.h: 127
class struct_relocation_info(Structure):
    pass

struct_relocation_info.__slots__ = [
    'r_address',
    'r_symbolnum',
    'r_pcrel',
    'r_length',
    'r_extern',
    'r_pad',
]
struct_relocation_info._fields_ = [
    ('r_address', c_int),
    ('r_symbolnum', c_uint, 24),
    ('r_pcrel', c_uint, 1),
    ('r_length', c_uint, 2),
    ('r_extern', c_uint, 1),
    ('r_pad', c_uint, 4),
]

fpu_control_t = c_uint# /usr/include/x86_64-linux-gnu/fpu_control.h: 91

# /usr/include/x86_64-linux-gnu/fpu_control.h: 107
try:
    __fpu_control = (fpu_control_t).in_dll(_libs["libc.so.6"], "__fpu_control")
except:
    pass

# /usr/include/x86_64-linux-gnu/ieee754.h: 32
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'mantissa',
    'exponent',
    'negative',
]
struct_anon_24._fields_ = [
    ('mantissa', c_uint, 23),
    ('exponent', c_uint, 8),
    ('negative', c_uint, 1),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 47
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'mantissa',
    'quiet_nan',
    'exponent',
    'negative',
]
struct_anon_25._fields_ = [
    ('mantissa', c_uint, 22),
    ('quiet_nan', c_uint, 1),
    ('exponent', c_uint, 8),
    ('negative', c_uint, 1),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 27
class union_ieee754_float(Union):
    pass

union_ieee754_float.__slots__ = [
    'f',
    'ieee',
    'ieee_nan',
]
union_ieee754_float._fields_ = [
    ('f', c_float),
    ('ieee', struct_anon_24),
    ('ieee_nan', struct_anon_25),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 72
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'mantissa1',
    'mantissa0',
    'exponent',
    'negative',
]
struct_anon_26._fields_ = [
    ('mantissa1', c_uint, 32),
    ('mantissa0', c_uint, 20),
    ('exponent', c_uint, 11),
    ('negative', c_uint, 1),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 98
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'mantissa1',
    'mantissa0',
    'quiet_nan',
    'exponent',
    'negative',
]
struct_anon_27._fields_ = [
    ('mantissa1', c_uint, 32),
    ('mantissa0', c_uint, 19),
    ('quiet_nan', c_uint, 1),
    ('exponent', c_uint, 11),
    ('negative', c_uint, 1),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 67
class union_ieee754_double(Union):
    pass

union_ieee754_double.__slots__ = [
    'd',
    'ieee',
    'ieee_nan',
]
union_ieee754_double._fields_ = [
    ('d', c_double),
    ('ieee', struct_anon_26),
    ('ieee_nan', struct_anon_27),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 134
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'mantissa1',
    'mantissa0',
    'exponent',
    'negative',
    'empty',
]
struct_anon_28._fields_ = [
    ('mantissa1', c_uint, 32),
    ('mantissa0', c_uint, 32),
    ('exponent', c_uint, 15),
    ('negative', c_uint, 1),
    ('empty', c_uint, 16),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 161
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'mantissa1',
    'mantissa0',
    'quiet_nan',
    'one',
    'exponent',
    'negative',
    'empty',
]
struct_anon_29._fields_ = [
    ('mantissa1', c_uint, 32),
    ('mantissa0', c_uint, 30),
    ('quiet_nan', c_uint, 1),
    ('one', c_uint, 1),
    ('exponent', c_uint, 15),
    ('negative', c_uint, 1),
    ('empty', c_uint, 16),
]

# /usr/include/x86_64-linux-gnu/ieee754.h: 129
class union_ieee854_long_double(Union):
    pass

union_ieee854_long_double.__slots__ = [
    'd',
    'ieee',
    'ieee_nan',
]
union_ieee854_long_double._fields_ = [
    ('d', c_longdouble),
    ('ieee', struct_anon_28),
    ('ieee_nan', struct_anon_29),
]

comp_t = c_uint16# /usr/include/x86_64-linux-gnu/sys/acct.h: 36

# /usr/include/x86_64-linux-gnu/sys/acct.h: 38
class struct_acct(Structure):
    pass

struct_acct.__slots__ = [
    'ac_flag',
    'ac_uid',
    'ac_gid',
    'ac_tty',
    'ac_btime',
    'ac_utime',
    'ac_stime',
    'ac_etime',
    'ac_mem',
    'ac_io',
    'ac_rw',
    'ac_minflt',
    'ac_majflt',
    'ac_swaps',
    'ac_exitcode',
    'ac_comm',
    'ac_pad',
]
struct_acct._fields_ = [
    ('ac_flag', c_char),
    ('ac_uid', c_uint16),
    ('ac_gid', c_uint16),
    ('ac_tty', c_uint16),
    ('ac_btime', c_uint32),
    ('ac_utime', comp_t),
    ('ac_stime', comp_t),
    ('ac_etime', comp_t),
    ('ac_mem', comp_t),
    ('ac_io', comp_t),
    ('ac_rw', comp_t),
    ('ac_minflt', comp_t),
    ('ac_majflt', comp_t),
    ('ac_swaps', comp_t),
    ('ac_exitcode', c_uint32),
    ('ac_comm', c_char * int((16 + 1))),
    ('ac_pad', c_char * int(10)),
]

# /usr/include/x86_64-linux-gnu/sys/acct.h: 60
class struct_acct_v3(Structure):
    pass

struct_acct_v3.__slots__ = [
    'ac_flag',
    'ac_version',
    'ac_tty',
    'ac_exitcode',
    'ac_uid',
    'ac_gid',
    'ac_pid',
    'ac_ppid',
    'ac_btime',
    'ac_etime',
    'ac_utime',
    'ac_stime',
    'ac_mem',
    'ac_io',
    'ac_rw',
    'ac_minflt',
    'ac_majflt',
    'ac_swaps',
    'ac_comm',
]
struct_acct_v3._fields_ = [
    ('ac_flag', c_char),
    ('ac_version', c_char),
    ('ac_tty', c_uint16),
    ('ac_exitcode', c_uint32),
    ('ac_uid', c_uint32),
    ('ac_gid', c_uint32),
    ('ac_pid', c_uint32),
    ('ac_ppid', c_uint32),
    ('ac_btime', c_uint32),
    ('ac_etime', c_float),
    ('ac_utime', comp_t),
    ('ac_stime', comp_t),
    ('ac_mem', comp_t),
    ('ac_io', comp_t),
    ('ac_rw', comp_t),
    ('ac_minflt', comp_t),
    ('ac_majflt', comp_t),
    ('ac_swaps', comp_t),
    ('ac_comm', c_char * int(16)),
]

enum_anon_30 = c_int# /usr/include/x86_64-linux-gnu/sys/acct.h: 84

AFORK = 0x01# /usr/include/x86_64-linux-gnu/sys/acct.h: 84

ASU = 0x02# /usr/include/x86_64-linux-gnu/sys/acct.h: 84

ACORE = 0x08# /usr/include/x86_64-linux-gnu/sys/acct.h: 84

AXSIG = 0x10# /usr/include/x86_64-linux-gnu/sys/acct.h: 84

# /usr/include/x86_64-linux-gnu/sys/acct.h: 102
if _libs["libc.so.6"].has("acct", "cdecl"):
    acct = _libs["libc.so.6"].get("acct", "cdecl")
    acct.argtypes = [String]
    acct.restype = c_int

Elf32_Half = c_uint16# /usr/include/elf.h: 31

Elf64_Half = c_uint16# /usr/include/elf.h: 32

Elf32_Word = c_uint32# /usr/include/elf.h: 35

Elf32_Sword = c_int32# /usr/include/elf.h: 36

Elf64_Word = c_uint32# /usr/include/elf.h: 37

Elf64_Sword = c_int32# /usr/include/elf.h: 38

Elf32_Xword = c_uint64# /usr/include/elf.h: 41

Elf32_Sxword = c_int64# /usr/include/elf.h: 42

Elf64_Xword = c_uint64# /usr/include/elf.h: 43

Elf64_Sxword = c_int64# /usr/include/elf.h: 44

Elf32_Addr = c_uint32# /usr/include/elf.h: 47

Elf64_Addr = c_uint64# /usr/include/elf.h: 48

Elf32_Off = c_uint32# /usr/include/elf.h: 51

Elf64_Off = c_uint64# /usr/include/elf.h: 52

Elf32_Section = c_uint16# /usr/include/elf.h: 55

Elf64_Section = c_uint16# /usr/include/elf.h: 56

Elf32_Versym = Elf32_Half# /usr/include/elf.h: 59

Elf64_Versym = Elf64_Half# /usr/include/elf.h: 60

# /usr/include/elf.h: 83
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'e_ident',
    'e_type',
    'e_machine',
    'e_version',
    'e_entry',
    'e_phoff',
    'e_shoff',
    'e_flags',
    'e_ehsize',
    'e_phentsize',
    'e_phnum',
    'e_shentsize',
    'e_shnum',
    'e_shstrndx',
]
struct_anon_31._fields_ = [
    ('e_ident', c_ubyte * int(16)),
    ('e_type', Elf32_Half),
    ('e_machine', Elf32_Half),
    ('e_version', Elf32_Word),
    ('e_entry', Elf32_Addr),
    ('e_phoff', Elf32_Off),
    ('e_shoff', Elf32_Off),
    ('e_flags', Elf32_Word),
    ('e_ehsize', Elf32_Half),
    ('e_phentsize', Elf32_Half),
    ('e_phnum', Elf32_Half),
    ('e_shentsize', Elf32_Half),
    ('e_shnum', Elf32_Half),
    ('e_shstrndx', Elf32_Half),
]

Elf32_Ehdr = struct_anon_31# /usr/include/elf.h: 83

# /usr/include/elf.h: 101
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'e_ident',
    'e_type',
    'e_machine',
    'e_version',
    'e_entry',
    'e_phoff',
    'e_shoff',
    'e_flags',
    'e_ehsize',
    'e_phentsize',
    'e_phnum',
    'e_shentsize',
    'e_shnum',
    'e_shstrndx',
]
struct_anon_32._fields_ = [
    ('e_ident', c_ubyte * int(16)),
    ('e_type', Elf64_Half),
    ('e_machine', Elf64_Half),
    ('e_version', Elf64_Word),
    ('e_entry', Elf64_Addr),
    ('e_phoff', Elf64_Off),
    ('e_shoff', Elf64_Off),
    ('e_flags', Elf64_Word),
    ('e_ehsize', Elf64_Half),
    ('e_phentsize', Elf64_Half),
    ('e_phnum', Elf64_Half),
    ('e_shentsize', Elf64_Half),
    ('e_shnum', Elf64_Half),
    ('e_shstrndx', Elf64_Half),
]

Elf64_Ehdr = struct_anon_32# /usr/include/elf.h: 101

# /usr/include/elf.h: 397
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'sh_name',
    'sh_type',
    'sh_flags',
    'sh_addr',
    'sh_offset',
    'sh_size',
    'sh_link',
    'sh_info',
    'sh_addralign',
    'sh_entsize',
]
struct_anon_33._fields_ = [
    ('sh_name', Elf32_Word),
    ('sh_type', Elf32_Word),
    ('sh_flags', Elf32_Word),
    ('sh_addr', Elf32_Addr),
    ('sh_offset', Elf32_Off),
    ('sh_size', Elf32_Word),
    ('sh_link', Elf32_Word),
    ('sh_info', Elf32_Word),
    ('sh_addralign', Elf32_Word),
    ('sh_entsize', Elf32_Word),
]

Elf32_Shdr = struct_anon_33# /usr/include/elf.h: 397

# /usr/include/elf.h: 411
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'sh_name',
    'sh_type',
    'sh_flags',
    'sh_addr',
    'sh_offset',
    'sh_size',
    'sh_link',
    'sh_info',
    'sh_addralign',
    'sh_entsize',
]
struct_anon_34._fields_ = [
    ('sh_name', Elf64_Word),
    ('sh_type', Elf64_Word),
    ('sh_flags', Elf64_Xword),
    ('sh_addr', Elf64_Addr),
    ('sh_offset', Elf64_Off),
    ('sh_size', Elf64_Xword),
    ('sh_link', Elf64_Word),
    ('sh_info', Elf64_Word),
    ('sh_addralign', Elf64_Xword),
    ('sh_entsize', Elf64_Xword),
]

Elf64_Shdr = struct_anon_34# /usr/include/elf.h: 411

# /usr/include/elf.h: 497
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'ch_type',
    'ch_size',
    'ch_addralign',
]
struct_anon_35._fields_ = [
    ('ch_type', Elf32_Word),
    ('ch_size', Elf32_Word),
    ('ch_addralign', Elf32_Word),
]

Elf32_Chdr = struct_anon_35# /usr/include/elf.h: 497

# /usr/include/elf.h: 505
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'ch_type',
    'ch_reserved',
    'ch_size',
    'ch_addralign',
]
struct_anon_36._fields_ = [
    ('ch_type', Elf64_Word),
    ('ch_reserved', Elf64_Word),
    ('ch_size', Elf64_Xword),
    ('ch_addralign', Elf64_Xword),
]

Elf64_Chdr = struct_anon_36# /usr/include/elf.h: 505

# /usr/include/elf.h: 527
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'st_name',
    'st_value',
    'st_size',
    'st_info',
    'st_other',
    'st_shndx',
]
struct_anon_37._fields_ = [
    ('st_name', Elf32_Word),
    ('st_value', Elf32_Addr),
    ('st_size', Elf32_Word),
    ('st_info', c_ubyte),
    ('st_other', c_ubyte),
    ('st_shndx', Elf32_Section),
]

Elf32_Sym = struct_anon_37# /usr/include/elf.h: 527

# /usr/include/elf.h: 537
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'st_name',
    'st_info',
    'st_other',
    'st_shndx',
    'st_value',
    'st_size',
]
struct_anon_38._fields_ = [
    ('st_name', Elf64_Word),
    ('st_info', c_ubyte),
    ('st_other', c_ubyte),
    ('st_shndx', Elf64_Section),
    ('st_value', Elf64_Addr),
    ('st_size', Elf64_Xword),
]

Elf64_Sym = struct_anon_38# /usr/include/elf.h: 537

# /usr/include/elf.h: 546
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'si_boundto',
    'si_flags',
]
struct_anon_39._fields_ = [
    ('si_boundto', Elf32_Half),
    ('si_flags', Elf32_Half),
]

Elf32_Syminfo = struct_anon_39# /usr/include/elf.h: 546

# /usr/include/elf.h: 552
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'si_boundto',
    'si_flags',
]
struct_anon_40._fields_ = [
    ('si_boundto', Elf64_Half),
    ('si_flags', Elf64_Half),
]

Elf64_Syminfo = struct_anon_40# /usr/include/elf.h: 552

# /usr/include/elf.h: 638
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'r_offset',
    'r_info',
]
struct_anon_41._fields_ = [
    ('r_offset', Elf32_Addr),
    ('r_info', Elf32_Word),
]

Elf32_Rel = struct_anon_41# /usr/include/elf.h: 638

# /usr/include/elf.h: 649
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'r_offset',
    'r_info',
]
struct_anon_42._fields_ = [
    ('r_offset', Elf64_Addr),
    ('r_info', Elf64_Xword),
]

Elf64_Rel = struct_anon_42# /usr/include/elf.h: 649

# /usr/include/elf.h: 658
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'r_offset',
    'r_info',
    'r_addend',
]
struct_anon_43._fields_ = [
    ('r_offset', Elf32_Addr),
    ('r_info', Elf32_Word),
    ('r_addend', Elf32_Sword),
]

Elf32_Rela = struct_anon_43# /usr/include/elf.h: 658

# /usr/include/elf.h: 665
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'r_offset',
    'r_info',
    'r_addend',
]
struct_anon_44._fields_ = [
    ('r_offset', Elf64_Addr),
    ('r_info', Elf64_Xword),
    ('r_addend', Elf64_Sxword),
]

Elf64_Rela = struct_anon_44# /usr/include/elf.h: 665

# /usr/include/elf.h: 689
class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'p_type',
    'p_offset',
    'p_vaddr',
    'p_paddr',
    'p_filesz',
    'p_memsz',
    'p_flags',
    'p_align',
]
struct_anon_45._fields_ = [
    ('p_type', Elf32_Word),
    ('p_offset', Elf32_Off),
    ('p_vaddr', Elf32_Addr),
    ('p_paddr', Elf32_Addr),
    ('p_filesz', Elf32_Word),
    ('p_memsz', Elf32_Word),
    ('p_flags', Elf32_Word),
    ('p_align', Elf32_Word),
]

Elf32_Phdr = struct_anon_45# /usr/include/elf.h: 689

# /usr/include/elf.h: 701
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'p_type',
    'p_flags',
    'p_offset',
    'p_vaddr',
    'p_paddr',
    'p_filesz',
    'p_memsz',
    'p_align',
]
struct_anon_46._fields_ = [
    ('p_type', Elf64_Word),
    ('p_flags', Elf64_Word),
    ('p_offset', Elf64_Off),
    ('p_vaddr', Elf64_Addr),
    ('p_paddr', Elf64_Addr),
    ('p_filesz', Elf64_Xword),
    ('p_memsz', Elf64_Xword),
    ('p_align', Elf64_Xword),
]

Elf64_Phdr = struct_anon_46# /usr/include/elf.h: 701

# /usr/include/elf.h: 833
class union_anon_47(Union):
    pass

union_anon_47.__slots__ = [
    'd_val',
    'd_ptr',
]
union_anon_47._fields_ = [
    ('d_val', Elf32_Word),
    ('d_ptr', Elf32_Addr),
]

# /usr/include/elf.h: 838
class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    'd_tag',
    'd_un',
]
struct_anon_48._fields_ = [
    ('d_tag', Elf32_Sword),
    ('d_un', union_anon_47),
]

Elf32_Dyn = struct_anon_48# /usr/include/elf.h: 838

# /usr/include/elf.h: 843
class union_anon_49(Union):
    pass

union_anon_49.__slots__ = [
    'd_val',
    'd_ptr',
]
union_anon_49._fields_ = [
    ('d_val', Elf64_Xword),
    ('d_ptr', Elf64_Addr),
]

# /usr/include/elf.h: 848
class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    'd_tag',
    'd_un',
]
struct_anon_50._fields_ = [
    ('d_tag', Elf64_Sxword),
    ('d_un', union_anon_49),
]

Elf64_Dyn = struct_anon_50# /usr/include/elf.h: 848

# /usr/include/elf.h: 1022
class struct_anon_51(Structure):
    pass

struct_anon_51.__slots__ = [
    'vd_version',
    'vd_flags',
    'vd_ndx',
    'vd_cnt',
    'vd_hash',
    'vd_aux',
    'vd_next',
]
struct_anon_51._fields_ = [
    ('vd_version', Elf32_Half),
    ('vd_flags', Elf32_Half),
    ('vd_ndx', Elf32_Half),
    ('vd_cnt', Elf32_Half),
    ('vd_hash', Elf32_Word),
    ('vd_aux', Elf32_Word),
    ('vd_next', Elf32_Word),
]

Elf32_Verdef = struct_anon_51# /usr/include/elf.h: 1022

# /usr/include/elf.h: 1034
class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    'vd_version',
    'vd_flags',
    'vd_ndx',
    'vd_cnt',
    'vd_hash',
    'vd_aux',
    'vd_next',
]
struct_anon_52._fields_ = [
    ('vd_version', Elf64_Half),
    ('vd_flags', Elf64_Half),
    ('vd_ndx', Elf64_Half),
    ('vd_cnt', Elf64_Half),
    ('vd_hash', Elf64_Word),
    ('vd_aux', Elf64_Word),
    ('vd_next', Elf64_Word),
]

Elf64_Verdef = struct_anon_52# /usr/include/elf.h: 1034

# /usr/include/elf.h: 1059
class struct_anon_53(Structure):
    pass

struct_anon_53.__slots__ = [
    'vda_name',
    'vda_next',
]
struct_anon_53._fields_ = [
    ('vda_name', Elf32_Word),
    ('vda_next', Elf32_Word),
]

Elf32_Verdaux = struct_anon_53# /usr/include/elf.h: 1059

# /usr/include/elf.h: 1066
class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    'vda_name',
    'vda_next',
]
struct_anon_54._fields_ = [
    ('vda_name', Elf64_Word),
    ('vda_next', Elf64_Word),
]

Elf64_Verdaux = struct_anon_54# /usr/include/elf.h: 1066

# /usr/include/elf.h: 1080
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'vn_version',
    'vn_cnt',
    'vn_file',
    'vn_aux',
    'vn_next',
]
struct_anon_55._fields_ = [
    ('vn_version', Elf32_Half),
    ('vn_cnt', Elf32_Half),
    ('vn_file', Elf32_Word),
    ('vn_aux', Elf32_Word),
    ('vn_next', Elf32_Word),
]

Elf32_Verneed = struct_anon_55# /usr/include/elf.h: 1080

# /usr/include/elf.h: 1091
class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'vn_version',
    'vn_cnt',
    'vn_file',
    'vn_aux',
    'vn_next',
]
struct_anon_56._fields_ = [
    ('vn_version', Elf64_Half),
    ('vn_cnt', Elf64_Half),
    ('vn_file', Elf64_Word),
    ('vn_aux', Elf64_Word),
    ('vn_next', Elf64_Word),
]

Elf64_Verneed = struct_anon_56# /usr/include/elf.h: 1091

# /usr/include/elf.h: 1109
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    'vna_hash',
    'vna_flags',
    'vna_other',
    'vna_name',
    'vna_next',
]
struct_anon_57._fields_ = [
    ('vna_hash', Elf32_Word),
    ('vna_flags', Elf32_Half),
    ('vna_other', Elf32_Half),
    ('vna_name', Elf32_Word),
    ('vna_next', Elf32_Word),
]

Elf32_Vernaux = struct_anon_57# /usr/include/elf.h: 1109

# /usr/include/elf.h: 1119
class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'vna_hash',
    'vna_flags',
    'vna_other',
    'vna_name',
    'vna_next',
]
struct_anon_58._fields_ = [
    ('vna_hash', Elf64_Word),
    ('vna_flags', Elf64_Half),
    ('vna_other', Elf64_Half),
    ('vna_name', Elf64_Word),
    ('vna_next', Elf64_Word),
]

Elf64_Vernaux = struct_anon_58# /usr/include/elf.h: 1119

# /usr/include/elf.h: 1138
class union_anon_59(Union):
    pass

union_anon_59.__slots__ = [
    'a_val',
]
union_anon_59._fields_ = [
    ('a_val', c_uint32),
]

# /usr/include/elf.h: 1145
class struct_anon_60(Structure):
    pass

struct_anon_60.__slots__ = [
    'a_type',
    'a_un',
]
struct_anon_60._fields_ = [
    ('a_type', c_uint32),
    ('a_un', union_anon_59),
]

Elf32_auxv_t = struct_anon_60# /usr/include/elf.h: 1145

# /usr/include/elf.h: 1150
class union_anon_61(Union):
    pass

union_anon_61.__slots__ = [
    'a_val',
]
union_anon_61._fields_ = [
    ('a_val', c_uint64),
]

# /usr/include/elf.h: 1157
class struct_anon_62(Structure):
    pass

struct_anon_62.__slots__ = [
    'a_type',
    'a_un',
]
struct_anon_62._fields_ = [
    ('a_type', c_uint64),
    ('a_un', union_anon_61),
]

Elf64_auxv_t = struct_anon_62# /usr/include/elf.h: 1157

# /usr/include/elf.h: 1168
class struct_anon_63(Structure):
    pass

struct_anon_63.__slots__ = [
    'n_namesz',
    'n_descsz',
    'n_type',
]
struct_anon_63._fields_ = [
    ('n_namesz', Elf32_Word),
    ('n_descsz', Elf32_Word),
    ('n_type', Elf32_Word),
]

Elf32_Nhdr = struct_anon_63# /usr/include/elf.h: 1168

# /usr/include/elf.h: 1175
class struct_anon_64(Structure):
    pass

struct_anon_64.__slots__ = [
    'n_namesz',
    'n_descsz',
    'n_type',
]
struct_anon_64._fields_ = [
    ('n_namesz', Elf64_Word),
    ('n_descsz', Elf64_Word),
    ('n_type', Elf64_Word),
]

Elf64_Nhdr = struct_anon_64# /usr/include/elf.h: 1175

# /usr/include/elf.h: 1290
class struct_anon_65(Structure):
    pass

struct_anon_65.__slots__ = [
    'm_value',
    'm_info',
    'm_poffset',
    'm_repeat',
    'm_stride',
]
struct_anon_65._fields_ = [
    ('m_value', Elf32_Xword),
    ('m_info', Elf32_Word),
    ('m_poffset', Elf32_Word),
    ('m_repeat', Elf32_Half),
    ('m_stride', Elf32_Half),
]

Elf32_Move = struct_anon_65# /usr/include/elf.h: 1290

# /usr/include/elf.h: 1299
class struct_anon_66(Structure):
    pass

struct_anon_66.__slots__ = [
    'm_value',
    'm_info',
    'm_poffset',
    'm_repeat',
    'm_stride',
]
struct_anon_66._fields_ = [
    ('m_value', Elf64_Xword),
    ('m_info', Elf64_Xword),
    ('m_poffset', Elf64_Xword),
    ('m_repeat', Elf64_Half),
    ('m_stride', Elf64_Half),
]

Elf64_Move = struct_anon_66# /usr/include/elf.h: 1299

# /usr/include/elf.h: 1675
class struct_anon_67(Structure):
    pass

struct_anon_67.__slots__ = [
    'gt_current_g_value',
    'gt_unused',
]
struct_anon_67._fields_ = [
    ('gt_current_g_value', Elf32_Word),
    ('gt_unused', Elf32_Word),
]

# /usr/include/elf.h: 1680
class struct_anon_68(Structure):
    pass

struct_anon_68.__slots__ = [
    'gt_g_value',
    'gt_bytes',
]
struct_anon_68._fields_ = [
    ('gt_g_value', Elf32_Word),
    ('gt_bytes', Elf32_Word),
]

# /usr/include/elf.h: 1685
class union_anon_69(Union):
    pass

union_anon_69.__slots__ = [
    'gt_header',
    'gt_entry',
]
union_anon_69._fields_ = [
    ('gt_header', struct_anon_67),
    ('gt_entry', struct_anon_68),
]

Elf32_gptab = union_anon_69# /usr/include/elf.h: 1685

# /usr/include/elf.h: 1694
class struct_anon_70(Structure):
    pass

struct_anon_70.__slots__ = [
    'ri_gprmask',
    'ri_cprmask',
    'ri_gp_value',
]
struct_anon_70._fields_ = [
    ('ri_gprmask', Elf32_Word),
    ('ri_cprmask', Elf32_Word * int(4)),
    ('ri_gp_value', Elf32_Sword),
]

Elf32_RegInfo = struct_anon_70# /usr/include/elf.h: 1694

# /usr/include/elf.h: 1706
class struct_anon_71(Structure):
    pass

struct_anon_71.__slots__ = [
    'kind',
    'size',
    'section',
    'info',
]
struct_anon_71._fields_ = [
    ('kind', c_ubyte),
    ('size', c_ubyte),
    ('section', Elf32_Section),
    ('info', Elf32_Word),
]

Elf_Options = struct_anon_71# /usr/include/elf.h: 1706

# /usr/include/elf.h: 1753
class struct_anon_72(Structure):
    pass

struct_anon_72.__slots__ = [
    'hwp_flags1',
    'hwp_flags2',
]
struct_anon_72._fields_ = [
    ('hwp_flags1', Elf32_Word),
    ('hwp_flags2', Elf32_Word),
]

Elf_Options_Hw = struct_anon_72# /usr/include/elf.h: 1753

# /usr/include/elf.h: 1924
class struct_anon_73(Structure):
    pass

struct_anon_73.__slots__ = [
    'l_name',
    'l_time_stamp',
    'l_checksum',
    'l_version',
    'l_flags',
]
struct_anon_73._fields_ = [
    ('l_name', Elf32_Word),
    ('l_time_stamp', Elf32_Word),
    ('l_checksum', Elf32_Word),
    ('l_version', Elf32_Word),
    ('l_flags', Elf32_Word),
]

Elf32_Lib = struct_anon_73# /usr/include/elf.h: 1924

# /usr/include/elf.h: 1933
class struct_anon_74(Structure):
    pass

struct_anon_74.__slots__ = [
    'l_name',
    'l_time_stamp',
    'l_checksum',
    'l_version',
    'l_flags',
]
struct_anon_74._fields_ = [
    ('l_name', Elf64_Word),
    ('l_time_stamp', Elf64_Word),
    ('l_checksum', Elf64_Word),
    ('l_version', Elf64_Word),
    ('l_flags', Elf64_Word),
]

Elf64_Lib = struct_anon_74# /usr/include/elf.h: 1933

Elf32_Conflict = Elf32_Addr# /usr/include/elf.h: 1948

# /usr/include/elf.h: 1973
class struct_anon_75(Structure):
    pass

struct_anon_75.__slots__ = [
    'version',
    'isa_level',
    'isa_rev',
    'gpr_size',
    'cpr1_size',
    'cpr2_size',
    'fp_abi',
    'isa_ext',
    'ases',
    'flags1',
    'flags2',
]
struct_anon_75._fields_ = [
    ('version', Elf32_Half),
    ('isa_level', c_ubyte),
    ('isa_rev', c_ubyte),
    ('gpr_size', c_ubyte),
    ('cpr1_size', c_ubyte),
    ('cpr2_size', c_ubyte),
    ('fp_abi', c_ubyte),
    ('isa_ext', Elf32_Word),
    ('ases', Elf32_Word),
    ('flags1', Elf32_Word),
    ('flags2', Elf32_Word),
]

Elf_MIPS_ABIFlags_v0 = struct_anon_75# /usr/include/elf.h: 1973

enum_anon_76 = c_int# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_ANY = 0# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_DOUBLE = 1# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_SINGLE = 2# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_SOFT = 3# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_OLD_64 = 4# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_XX = 5# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_64 = 6# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_64A = 7# /usr/include/elf.h: 2024

Val_GNU_MIPS_ABI_FP_MAX = 7# /usr/include/elf.h: 2024

# /usr/include/x86_64-linux-gnu/sys/auxv.h: 32
if _libs["libc.so.6"].has("getauxval", "cdecl"):
    getauxval = _libs["libc.so.6"].get("getauxval", "cdecl")
    getauxval.argtypes = [c_ulong]
    getauxval.restype = c_ulong

enum_anon_78 = c_int# /usr/include/x86_64-linux-gnu/bits/epoll.h: 23

EPOLL_CLOEXEC = 0o2000000# /usr/include/x86_64-linux-gnu/bits/epoll.h: 23

enum_EPOLL_EVENTS = c_int# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLIN = 0x001# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLPRI = 0x002# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLOUT = 0x004# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLRDNORM = 0x040# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLRDBAND = 0x080# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLWRNORM = 0x100# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLWRBAND = 0x200# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLMSG = 0x400# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLERR = 0x008# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLHUP = 0x010# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLRDHUP = 0x2000# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLEXCLUSIVE = (1 << 28)# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLWAKEUP = (1 << 29)# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLONESHOT = (1 << 30)# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

EPOLLET = (1 << 31)# /usr/include/x86_64-linux-gnu/sys/epoll.h: 34

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 81
class union_epoll_data(Union):
    pass

union_epoll_data.__slots__ = [
    'ptr',
    'fd',
    'u32',
    'u64',
]
union_epoll_data._fields_ = [
    ('ptr', POINTER(None)),
    ('fd', c_int),
    ('u32', c_uint32),
    ('u64', c_uint64),
]

epoll_data_t = union_epoll_data# /usr/include/x86_64-linux-gnu/sys/epoll.h: 81

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 83
class struct_epoll_event(Structure):
    pass

struct_epoll_event.__slots__ = [
    'events',
    'data',
]
struct_epoll_event._fields_ = [
    ('events', c_uint32),
    ('data', epoll_data_t),
]

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 96
if _libs["libc.so.6"].has("epoll_create", "cdecl"):
    epoll_create = _libs["libc.so.6"].get("epoll_create", "cdecl")
    epoll_create.argtypes = [c_int]
    epoll_create.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 100
if _libs["libc.so.6"].has("epoll_create1", "cdecl"):
    epoll_create1 = _libs["libc.so.6"].get("epoll_create1", "cdecl")
    epoll_create1.argtypes = [c_int]
    epoll_create1.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 109
if _libs["libc.so.6"].has("epoll_ctl", "cdecl"):
    epoll_ctl = _libs["libc.so.6"].get("epoll_ctl", "cdecl")
    epoll_ctl.argtypes = [c_int, c_int, c_int, POINTER(struct_epoll_event)]
    epoll_ctl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 123
if _libs["libc.so.6"].has("epoll_wait", "cdecl"):
    epoll_wait = _libs["libc.so.6"].get("epoll_wait", "cdecl")
    epoll_wait.argtypes = [c_int, POINTER(struct_epoll_event), c_int, c_int]
    epoll_wait.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 132
if _libs["libc.so.6"].has("epoll_pwait", "cdecl"):
    epoll_pwait = _libs["libc.so.6"].get("epoll_pwait", "cdecl")
    epoll_pwait.argtypes = [c_int, POINTER(struct_epoll_event), c_int, c_int, POINTER(__sigset_t)]
    epoll_pwait.restype = c_int

# /usr/include/errno.h: 37
if _libs["libc.so.6"].has("__errno_location", "cdecl"):
    __errno_location = _libs["libc.so.6"].get("__errno_location", "cdecl")
    __errno_location.argtypes = []
    __errno_location.restype = POINTER(c_int)

enum_anon_79 = c_int# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 23

EFD_SEMAPHORE = 0o0000001# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 23

EFD_CLOEXEC = 0o2000000# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 23

EFD_NONBLOCK = 0o0004000# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 23

eventfd_t = c_uint64# /usr/include/x86_64-linux-gnu/sys/eventfd.h: 27

# /usr/include/x86_64-linux-gnu/sys/eventfd.h: 34
if _libs["libc.so.6"].has("eventfd", "cdecl"):
    eventfd = _libs["libc.so.6"].get("eventfd", "cdecl")
    eventfd.argtypes = [c_uint, c_int]
    eventfd.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/eventfd.h: 37
if _libs["libc.so.6"].has("eventfd_read", "cdecl"):
    eventfd_read = _libs["libc.so.6"].get("eventfd_read", "cdecl")
    eventfd_read.argtypes = [c_int, POINTER(eventfd_t)]
    eventfd_read.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/eventfd.h: 40
if _libs["libc.so.6"].has("eventfd_write", "cdecl"):
    eventfd_write = _libs["libc.so.6"].get("eventfd_write", "cdecl")
    eventfd_write.argtypes = [c_int, eventfd_t]
    eventfd_write.restype = c_int

__u8 = c_ubyte# /usr/include/asm-generic/int-ll64.h: 21

__u16 = c_ushort# /usr/include/asm-generic/int-ll64.h: 24

__u32 = c_uint# /usr/include/asm-generic/int-ll64.h: 27

__u64 = c_ulonglong# /usr/include/asm-generic/int-ll64.h: 34

__kernel_long_t = c_long# /usr/include/asm-generic/posix_types.h: 15

__kernel_ulong_t = c_ulong# /usr/include/asm-generic/posix_types.h: 16

# /usr/include/asm-generic/posix_types.h: 81
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    'val',
]
struct_anon_81._fields_ = [
    ('val', c_int * int(2)),
]

__kernel_fsid_t = struct_anon_81# /usr/include/asm-generic/posix_types.h: 81

__le16 = __u16# /usr/include/linux/types.h: 24

__be16 = __u16# /usr/include/linux/types.h: 25

__le32 = __u32# /usr/include/linux/types.h: 26

__be32 = __u32# /usr/include/linux/types.h: 27

__le64 = __u64# /usr/include/linux/types.h: 28

__be64 = __u64# /usr/include/linux/types.h: 29

__sum16 = __u16# /usr/include/linux/types.h: 31

__wsum = __u32# /usr/include/linux/types.h: 32

__poll_t = c_uint# /usr/include/linux/types.h: 47

# /usr/include/linux/fanotify.h: 121
class struct_fanotify_event_info_header(Structure):
    pass

struct_fanotify_event_info_header.__slots__ = [
    'info_type',
    'pad',
    'len',
]
struct_fanotify_event_info_header._fields_ = [
    ('info_type', __u8),
    ('pad', __u8),
    ('len', __u16),
]

# /usr/include/linux/fanotify.h: 128
class struct_fanotify_event_info_fid(Structure):
    pass

struct_fanotify_event_info_fid.__slots__ = [
    'hdr',
    'fsid',
    'handle',
]
struct_fanotify_event_info_fid._fields_ = [
    ('hdr', struct_fanotify_event_info_header),
    ('fsid', __kernel_fsid_t),
    ('handle', c_ubyte * int(0)),
]

# /usr/include/linux/fanotify.h: 140
for _lib in _libs.values():
    try:
        response = (__u32).in_dll(_lib, "response")
        break
    except:
        pass

# /usr/include/x86_64-linux-gnu/sys/fanotify.h: 28
if _libs["libc.so.6"].has("fanotify_init", "cdecl"):
    fanotify_init = _libs["libc.so.6"].get("fanotify_init", "cdecl")
    fanotify_init.argtypes = [c_uint, c_uint]
    fanotify_init.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/fanotify.h: 32
if _libs["libc.so.6"].has("fanotify_mark", "cdecl"):
    fanotify_mark = _libs["libc.so.6"].get("fanotify_mark", "cdecl")
    fanotify_mark.argtypes = [c_int, c_uint, c_uint64, c_int, String]
    fanotify_mark.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 35
class struct_flock(Structure):
    pass

struct_flock.__slots__ = [
    'l_type',
    'l_whence',
    'l_start',
    'l_len',
    'l_pid',
]
struct_flock._fields_ = [
    ('l_type', c_int),
    ('l_whence', c_int),
    ('l_start', __off_t),
    ('l_len', __off_t),
    ('l_pid', __pid_t),
]

# /usr/include/x86_64-linux-gnu/bits/stat.h: 46
class struct_stat(Structure):
    pass

struct_stat.__slots__ = [
    'st_dev',
    'st_ino',
    'st_nlink',
    'st_mode',
    'st_uid',
    'st_gid',
    '__pad0',
    'st_rdev',
    'st_size',
    'st_blksize',
    'st_blocks',
    'st_atim',
    'st_mtim',
    'st_ctim',
    '__glibc_reserved',
]
struct_stat._fields_ = [
    ('st_dev', __dev_t),
    ('st_ino', __ino_t),
    ('st_nlink', __nlink_t),
    ('st_mode', __mode_t),
    ('st_uid', __uid_t),
    ('st_gid', __gid_t),
    ('__pad0', c_int),
    ('st_rdev', __dev_t),
    ('st_size', __off_t),
    ('st_blksize', __blksize_t),
    ('st_blocks', __blkcnt_t),
    ('st_atim', struct_timespec),
    ('st_mtim', struct_timespec),
    ('st_ctim', struct_timespec),
    ('__glibc_reserved', __syscall_slong_t * int(3)),
]

# /usr/include/fcntl.h: 148
if _libs["libc.so.6"].has("fcntl", "cdecl"):
    _func = _libs["libc.so.6"].get("fcntl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int, c_int]
    fcntl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/fcntl.h: 168
if _libs["libc.so.6"].has("open", "cdecl"):
    _func = _libs["libc.so.6"].get("open", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, c_int]
    open = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/fcntl.h: 192
if _libs["libc.so.6"].has("openat", "cdecl"):
    _func = _libs["libc.so.6"].get("openat", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int, String, c_int]
    openat = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/fcntl.h: 214
if _libs["libc.so.6"].has("creat", "cdecl"):
    creat = _libs["libc.so.6"].get("creat", "cdecl")
    creat.argtypes = [String, mode_t]
    creat.restype = c_int

# /usr/include/fcntl.h: 243
if _libs["libc.so.6"].has("lockf", "cdecl"):
    lockf = _libs["libc.so.6"].get("lockf", "cdecl")
    lockf.argtypes = [c_int, c_int, off_t]
    lockf.restype = c_int

# /usr/include/fcntl.h: 260
if _libs["libc.so.6"].has("posix_fadvise", "cdecl"):
    posix_fadvise = _libs["libc.so.6"].get("posix_fadvise", "cdecl")
    posix_fadvise.argtypes = [c_int, off_t, off_t, c_int]
    posix_fadvise.restype = c_int

# /usr/include/fcntl.h: 282
if _libs["libc.so.6"].has("posix_fallocate", "cdecl"):
    posix_fallocate = _libs["libc.so.6"].get("posix_fallocate", "cdecl")
    posix_fallocate.argtypes = [c_int, off_t, off_t]
    posix_fallocate.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/file.h: 50
if _libs["libc.so.6"].has("flock", "cdecl"):
    flock = _libs["libc.so.6"].get("flock", "cdecl")
    flock.argtypes = [c_int, c_int]
    flock.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/fsuid.h: 28
if _libs["libc.so.6"].has("setfsuid", "cdecl"):
    setfsuid = _libs["libc.so.6"].get("setfsuid", "cdecl")
    setfsuid.argtypes = [__uid_t]
    setfsuid.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/fsuid.h: 31
if _libs["libc.so.6"].has("setfsgid", "cdecl"):
    setfsgid = _libs["libc.so.6"].get("setfsgid", "cdecl")
    setfsgid.argtypes = [__gid_t]
    setfsgid.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 46
class struct___bb(Structure):
    pass

struct___bb.__slots__ = [
    'zero_word',
    'filename',
    'counts',
    'ncounts',
    'next',
    'addresses',
]
struct___bb._fields_ = [
    ('zero_word', c_long),
    ('filename', String),
    ('counts', POINTER(c_long)),
    ('ncounts', c_long),
    ('next', POINTER(struct___bb)),
    ('addresses', POINTER(c_ulong)),
]

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 56
for _lib in _libs.values():
    try:
        __bb_head = (POINTER(struct___bb)).in_dll(_lib, "__bb_head")
        break
    except:
        pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 132
class struct_tostruct(Structure):
    pass

struct_tostruct.__slots__ = [
    'selfpc',
    'count',
    'link',
]
struct_tostruct._fields_ = [
    ('selfpc', c_ulong),
    ('count', c_long),
    ('link', c_ulong),
]

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 142
class struct_rawarc(Structure):
    pass

struct_rawarc.__slots__ = [
    'raw_frompc',
    'raw_selfpc',
    'raw_count',
]
struct_rawarc._fields_ = [
    ('raw_frompc', c_ulong),
    ('raw_selfpc', c_ulong),
    ('raw_count', c_long),
]

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 157
class struct_gmonparam(Structure):
    pass

struct_gmonparam.__slots__ = [
    'state',
    'kcount',
    'kcountsize',
    'froms',
    'fromssize',
    'tos',
    'tossize',
    'tolimit',
    'lowpc',
    'highpc',
    'textsize',
    'hashfraction',
    'log_hashfraction',
]
struct_gmonparam._fields_ = [
    ('state', c_long),
    ('kcount', POINTER(c_ushort)),
    ('kcountsize', c_ulong),
    ('froms', POINTER(c_ulong)),
    ('fromssize', c_ulong),
    ('tos', POINTER(struct_tostruct)),
    ('tossize', c_ulong),
    ('tolimit', c_long),
    ('lowpc', c_ulong),
    ('highpc', c_ulong),
    ('textsize', c_ulong),
    ('hashfraction', c_ulong),
    ('log_hashfraction', c_long),
]

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 193
if _libs["libc.so.6"].has("__monstartup", "cdecl"):
    __monstartup = _libs["libc.so.6"].get("__monstartup", "cdecl")
    __monstartup.argtypes = [c_ulong, c_ulong]
    __monstartup.restype = None

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 194
if _libs["libc.so.6"].has("monstartup", "cdecl"):
    monstartup = _libs["libc.so.6"].get("monstartup", "cdecl")
    monstartup.argtypes = [c_ulong, c_ulong]
    monstartup.restype = None

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 197
if _libs["libc.so.6"].has("_mcleanup", "cdecl"):
    _mcleanup = _libs["libc.so.6"].get("_mcleanup", "cdecl")
    _mcleanup.argtypes = []
    _mcleanup.restype = None

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 45
class struct_gmon_hdr(Structure):
    pass

struct_gmon_hdr.__slots__ = [
    'cookie',
    'version',
    'spare',
]
struct_gmon_hdr._fields_ = [
    ('cookie', c_char * int(4)),
    ('version', c_char * int(4)),
    ('spare', c_char * int((3 * 4))),
]

enum_anon_82 = c_int# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 58

GMON_TAG_TIME_HIST = 0# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 58

GMON_TAG_CG_ARC = 1# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 58

GMON_TAG_BB_COUNT = 2# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 58

GMON_Record_Tag = enum_anon_82# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 58

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 60
class struct_gmon_hist_hdr(Structure):
    pass

struct_gmon_hist_hdr.__slots__ = [
    'low_pc',
    'high_pc',
    'hist_size',
    'prof_rate',
    'dimen',
    'dimen_abbrev',
]
struct_gmon_hist_hdr._fields_ = [
    ('low_pc', c_char * int(sizeof(String))),
    ('high_pc', c_char * int(sizeof(String))),
    ('hist_size', c_char * int(4)),
    ('prof_rate', c_char * int(4)),
    ('dimen', c_char * int(15)),
    ('dimen_abbrev', c_char),
]

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 70
class struct_gmon_cg_arc_record(Structure):
    pass

struct_gmon_cg_arc_record.__slots__ = [
    'from_pc',
    'self_pc',
    'count',
]
struct_gmon_cg_arc_record._fields_ = [
    ('from_pc', c_char * int(sizeof(String))),
    ('self_pc', c_char * int(sizeof(String))),
    ('count', c_char * int(4)),
]

enum_anon_83 = c_int# /usr/include/x86_64-linux-gnu/bits/inotify.h: 23

IN_CLOEXEC = 0o2000000# /usr/include/x86_64-linux-gnu/bits/inotify.h: 23

IN_NONBLOCK = 0o0004000# /usr/include/x86_64-linux-gnu/bits/inotify.h: 23

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 28
class struct_inotify_event(Structure):
    pass

struct_inotify_event.__slots__ = [
    'wd',
    'mask',
    'cookie',
    'len',
    'name',
]
struct_inotify_event._fields_ = [
    ('wd', c_int),
    ('mask', c_uint32),
    ('cookie', c_uint32),
    ('len', c_uint32),
    ('name', POINTER(c_char)),
]

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 85
if _libs["libc.so.6"].has("inotify_init", "cdecl"):
    inotify_init = _libs["libc.so.6"].get("inotify_init", "cdecl")
    inotify_init.argtypes = []
    inotify_init.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 88
if _libs["libc.so.6"].has("inotify_init1", "cdecl"):
    inotify_init1 = _libs["libc.so.6"].get("inotify_init1", "cdecl")
    inotify_init1.argtypes = [c_int]
    inotify_init1.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 92
if _libs["libc.so.6"].has("inotify_add_watch", "cdecl"):
    inotify_add_watch = _libs["libc.so.6"].get("inotify_add_watch", "cdecl")
    inotify_add_watch.argtypes = [c_int, String, c_uint32]
    inotify_add_watch.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 96
if _libs["libc.so.6"].has("inotify_rm_watch", "cdecl"):
    inotify_rm_watch = _libs["libc.so.6"].get("inotify_rm_watch", "cdecl")
    inotify_rm_watch.argtypes = [c_int, c_int]
    inotify_rm_watch.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/io.h: 32
if _libs["libc.so.6"].has("ioperm", "cdecl"):
    ioperm = _libs["libc.so.6"].get("ioperm", "cdecl")
    ioperm.argtypes = [c_ulong, c_ulong, c_int]
    ioperm.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/io.h: 38
if _libs["libc.so.6"].has("iopl", "cdecl"):
    iopl = _libs["libc.so.6"].get("iopl", "cdecl")
    iopl.argtypes = [c_int]
    iopl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/ioctl.h: 41
if _libs["libc.so.6"].has("ioctl", "cdecl"):
    _func = _libs["libc.so.6"].get("ioctl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int, c_ulong]
    ioctl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/x86_64-linux-gnu/bits/ipc-perm.h: 28
class struct_ipc_perm(Structure):
    pass

struct_ipc_perm.__slots__ = [
    '__key',
    'uid',
    'gid',
    'cuid',
    'cgid',
    'mode',
    '__seq',
    '__pad2',
    '__glibc_reserved1',
    '__glibc_reserved2',
]
struct_ipc_perm._fields_ = [
    ('__key', __key_t),
    ('uid', __uid_t),
    ('gid', __gid_t),
    ('cuid', __uid_t),
    ('cgid', __gid_t),
    ('mode', __mode_t),
    ('__seq', c_uint),
    ('__pad2', c_uint),
    ('__glibc_reserved1', __syscall_ulong_t),
    ('__glibc_reserved2', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/sys/ipc.h: 50
if _libs["libc.so.6"].has("ftok", "cdecl"):
    ftok = _libs["libc.so.6"].get("ftok", "cdecl")
    ftok.argtypes = [String, c_int]
    ftok.restype = key_t

# /usr/include/linux/kd.h: 14
class struct_consolefontdesc(Structure):
    pass

struct_consolefontdesc.__slots__ = [
    'charcount',
    'charheight',
    'chardata',
]
struct_consolefontdesc._fields_ = [
    ('charcount', c_ushort),
    ('charheight', c_ushort),
    ('chardata', String),
]

scrnmap_t = c_char# /usr/include/linux/kd.h: 56

# /usr/include/linux/kd.h: 64
class struct_unipair(Structure):
    pass

struct_unipair.__slots__ = [
    'unicode',
    'fontpos',
]
struct_unipair._fields_ = [
    ('unicode', c_ushort),
    ('fontpos', c_ushort),
]

# /usr/include/linux/kd.h: 68
class struct_unimapdesc(Structure):
    pass

struct_unimapdesc.__slots__ = [
    'entry_ct',
    'entries',
]
struct_unimapdesc._fields_ = [
    ('entry_ct', c_ushort),
    ('entries', POINTER(struct_unipair)),
]

# /usr/include/linux/kd.h: 74
class struct_unimapinit(Structure):
    pass

struct_unimapinit.__slots__ = [
    'advised_hashsize',
    'advised_hashstep',
    'advised_hashlevel',
]
struct_unimapinit._fields_ = [
    ('advised_hashsize', c_ushort),
    ('advised_hashstep', c_ushort),
    ('advised_hashlevel', c_ushort),
]

# /usr/include/linux/kd.h: 102
class struct_kbentry(Structure):
    pass

struct_kbentry.__slots__ = [
    'kb_table',
    'kb_index',
    'kb_value',
]
struct_kbentry._fields_ = [
    ('kb_table', c_ubyte),
    ('kb_index', c_ubyte),
    ('kb_value', c_ushort),
]

# /usr/include/linux/kd.h: 115
class struct_kbsentry(Structure):
    pass

struct_kbsentry.__slots__ = [
    'kb_func',
    'kb_string',
]
struct_kbsentry._fields_ = [
    ('kb_func', c_ubyte),
    ('kb_string', c_ubyte * int(512)),
]

# /usr/include/linux/kd.h: 122
class struct_kbdiacr(Structure):
    pass

struct_kbdiacr.__slots__ = [
    'diacr',
    'base',
    'result',
]
struct_kbdiacr._fields_ = [
    ('diacr', c_ubyte),
    ('base', c_ubyte),
    ('result', c_ubyte),
]

# /usr/include/linux/kd.h: 125
class struct_kbdiacrs(Structure):
    pass

struct_kbdiacrs.__slots__ = [
    'kb_cnt',
    'kbdiacr',
]
struct_kbdiacrs._fields_ = [
    ('kb_cnt', c_uint),
    ('kbdiacr', struct_kbdiacr * int(256)),
]

# /usr/include/linux/kd.h: 132
class struct_kbdiacruc(Structure):
    pass

struct_kbdiacruc.__slots__ = [
    'diacr',
    'base',
    'result',
]
struct_kbdiacruc._fields_ = [
    ('diacr', c_uint),
    ('base', c_uint),
    ('result', c_uint),
]

# /usr/include/linux/kd.h: 135
class struct_kbdiacrsuc(Structure):
    pass

struct_kbdiacrsuc.__slots__ = [
    'kb_cnt',
    'kbdiacruc',
]
struct_kbdiacrsuc._fields_ = [
    ('kb_cnt', c_uint),
    ('kbdiacruc', struct_kbdiacruc * int(256)),
]

# /usr/include/linux/kd.h: 142
class struct_kbkeycode(Structure):
    pass

struct_kbkeycode.__slots__ = [
    'scancode',
    'keycode',
]
struct_kbkeycode._fields_ = [
    ('scancode', c_uint),
    ('keycode', c_uint),
]

# /usr/include/linux/kd.h: 150
class struct_kbd_repeat(Structure):
    pass

struct_kbd_repeat.__slots__ = [
    'delay',
    'period',
]
struct_kbd_repeat._fields_ = [
    ('delay', c_int),
    ('period', c_int),
]

# /usr/include/linux/kd.h: 161
class struct_console_font_op(Structure):
    pass

struct_console_font_op.__slots__ = [
    'op',
    'flags',
    'width',
    'height',
    'charcount',
    'data',
]
struct_console_font_op._fields_ = [
    ('op', c_uint),
    ('flags', c_uint),
    ('width', c_uint),
    ('height', c_uint),
    ('charcount', c_uint),
    ('data', POINTER(c_ubyte)),
]

# /usr/include/linux/kd.h: 169
class struct_console_font(Structure):
    pass

struct_console_font.__slots__ = [
    'width',
    'height',
    'charcount',
    'data',
]
struct_console_font._fields_ = [
    ('width', c_uint),
    ('height', c_uint),
    ('charcount', c_uint),
    ('data', POINTER(c_ubyte)),
]

# /usr/include/x86_64-linux-gnu/sys/klog.h: 29
if _libs["libc.so.6"].has("klogctl", "cdecl"):
    klogctl = _libs["libc.so.6"].get("klogctl", "cdecl")
    klogctl.argtypes = [c_int, String, c_int]
    klogctl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 57
if _libs["libc.so.6"].has("mmap", "cdecl"):
    mmap = _libs["libc.so.6"].get("mmap", "cdecl")
    mmap.argtypes = [POINTER(None), c_size_t, c_int, c_int, c_int, __off_t]
    mmap.restype = POINTER(c_ubyte)
    mmap.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/x86_64-linux-gnu/sys/mman.h: 76
if _libs["libc.so.6"].has("munmap", "cdecl"):
    munmap = _libs["libc.so.6"].get("munmap", "cdecl")
    munmap.argtypes = [POINTER(None), c_size_t]
    munmap.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 81
if _libs["libc.so.6"].has("mprotect", "cdecl"):
    mprotect = _libs["libc.so.6"].get("mprotect", "cdecl")
    mprotect.argtypes = [POINTER(None), c_size_t, c_int]
    mprotect.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 89
if _libs["libc.so.6"].has("msync", "cdecl"):
    msync = _libs["libc.so.6"].get("msync", "cdecl")
    msync.argtypes = [POINTER(None), c_size_t, c_int]
    msync.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 94
if _libs["libc.so.6"].has("madvise", "cdecl"):
    madvise = _libs["libc.so.6"].get("madvise", "cdecl")
    madvise.argtypes = [POINTER(None), c_size_t, c_int]
    madvise.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 98
if _libs["libc.so.6"].has("posix_madvise", "cdecl"):
    posix_madvise = _libs["libc.so.6"].get("posix_madvise", "cdecl")
    posix_madvise.argtypes = [POINTER(None), c_size_t, c_int]
    posix_madvise.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 103
if _libs["libc.so.6"].has("mlock", "cdecl"):
    mlock = _libs["libc.so.6"].get("mlock", "cdecl")
    mlock.argtypes = [POINTER(None), c_size_t]
    mlock.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 106
if _libs["libc.so.6"].has("munlock", "cdecl"):
    munlock = _libs["libc.so.6"].get("munlock", "cdecl")
    munlock.argtypes = [POINTER(None), c_size_t]
    munlock.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 111
if _libs["libc.so.6"].has("mlockall", "cdecl"):
    mlockall = _libs["libc.so.6"].get("mlockall", "cdecl")
    mlockall.argtypes = [c_int]
    mlockall.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 115
if _libs["libc.so.6"].has("munlockall", "cdecl"):
    munlockall = _libs["libc.so.6"].get("munlockall", "cdecl")
    munlockall.argtypes = []
    munlockall.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 123
if _libs["libc.so.6"].has("mincore", "cdecl"):
    mincore = _libs["libc.so.6"].get("mincore", "cdecl")
    mincore.argtypes = [POINTER(None), c_size_t, POINTER(c_ubyte)]
    mincore.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mman.h: 144
for _lib in _libs.values():
    if not _lib.has("shm_open", "cdecl"):
        continue
    shm_open = _lib.get("shm_open", "cdecl")
    shm_open.argtypes = [String, c_int, mode_t]
    shm_open.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/mman.h: 147
for _lib in _libs.values():
    if not _lib.has("shm_unlink", "cdecl"):
        continue
    shm_unlink = _lib.get("shm_unlink", "cdecl")
    shm_unlink.argtypes = [String]
    shm_unlink.restype = c_int
    break

enum_anon_84 = c_int# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_RDONLY = 1# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NOSUID = 2# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NODEV = 4# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NOEXEC = 8# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_SYNCHRONOUS = 16# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_REMOUNT = 32# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_MANDLOCK = 64# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_DIRSYNC = 128# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NOATIME = 1024# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NODIRATIME = 2048# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_BIND = 4096# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_MOVE = 8192# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_REC = 16384# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_SILENT = 32768# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_POSIXACL = (1 << 16)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_UNBINDABLE = (1 << 17)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_PRIVATE = (1 << 18)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_SLAVE = (1 << 19)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_SHARED = (1 << 20)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_RELATIME = (1 << 21)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_KERNMOUNT = (1 << 22)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_I_VERSION = (1 << 23)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_STRICTATIME = (1 << 24)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_LAZYTIME = (1 << 25)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_ACTIVE = (1 << 30)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

MS_NOUSER = (1 << 31)# /usr/include/x86_64-linux-gnu/sys/mount.h: 33

enum_anon_85 = c_int# /usr/include/x86_64-linux-gnu/sys/mount.h: 122

MNT_FORCE = 1# /usr/include/x86_64-linux-gnu/sys/mount.h: 122

MNT_DETACH = 2# /usr/include/x86_64-linux-gnu/sys/mount.h: 122

MNT_EXPIRE = 4# /usr/include/x86_64-linux-gnu/sys/mount.h: 122

UMOUNT_NOFOLLOW = 8# /usr/include/x86_64-linux-gnu/sys/mount.h: 122

# /usr/include/x86_64-linux-gnu/sys/mount.h: 138
if _libs["libc.so.6"].has("mount", "cdecl"):
    mount = _libs["libc.so.6"].get("mount", "cdecl")
    mount.argtypes = [String, String, String, c_ulong, POINTER(None)]
    mount.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mount.h: 143
if _libs["libc.so.6"].has("umount", "cdecl"):
    umount = _libs["libc.so.6"].get("umount", "cdecl")
    umount.argtypes = [String]
    umount.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mount.h: 146
if _libs["libc.so.6"].has("umount2", "cdecl"):
    umount2 = _libs["libc.so.6"].get("umount2", "cdecl")
    umount2.argtypes = [String, c_int]
    umount2.restype = c_int

msgqnum_t = __syscall_ulong_t# /usr/include/x86_64-linux-gnu/bits/msq.h: 33

msglen_t = __syscall_ulong_t# /usr/include/x86_64-linux-gnu/bits/msq.h: 34

# /usr/include/x86_64-linux-gnu/bits/msq.h: 49
class struct_msqid_ds(Structure):
    pass

struct_msqid_ds.__slots__ = [
    'msg_perm',
    'msg_stime',
    'msg_rtime',
    'msg_ctime',
    '__msg_cbytes',
    'msg_qnum',
    'msg_qbytes',
    'msg_lspid',
    'msg_lrpid',
    '__glibc_reserved4',
    '__glibc_reserved5',
]
struct_msqid_ds._fields_ = [
    ('msg_perm', struct_ipc_perm),
    ('msg_stime', __time_t),
    ('msg_rtime', __time_t),
    ('msg_ctime', __time_t),
    ('__msg_cbytes', __syscall_ulong_t),
    ('msg_qnum', msgqnum_t),
    ('msg_qbytes', msglen_t),
    ('msg_lspid', __pid_t),
    ('msg_lrpid', __pid_t),
    ('__glibc_reserved4', __syscall_ulong_t),
    ('__glibc_reserved5', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/sys/msg.h: 61
if _libs["libc.so.6"].has("msgctl", "cdecl"):
    msgctl = _libs["libc.so.6"].get("msgctl", "cdecl")
    msgctl.argtypes = [c_int, c_int, POINTER(struct_msqid_ds)]
    msgctl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/msg.h: 64
if _libs["libc.so.6"].has("msgget", "cdecl"):
    msgget = _libs["libc.so.6"].get("msgget", "cdecl")
    msgget.argtypes = [key_t, c_int]
    msgget.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/msg.h: 70
if _libs["libc.so.6"].has("msgrcv", "cdecl"):
    msgrcv = _libs["libc.so.6"].get("msgrcv", "cdecl")
    msgrcv.argtypes = [c_int, POINTER(None), c_size_t, c_long, c_int]
    msgrcv.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/msg.h: 77
if _libs["libc.so.6"].has("msgsnd", "cdecl"):
    msgsnd = _libs["libc.so.6"].get("msgsnd", "cdecl")
    msgsnd.argtypes = [c_int, POINTER(None), c_size_t, c_int]
    msgsnd.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 30
class struct_mtop(Structure):
    pass

struct_mtop.__slots__ = [
    'mt_op',
    'mt_count',
]
struct_mtop._fields_ = [
    ('mt_op', c_int),
    ('mt_count', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 81
class struct_mtget(Structure):
    pass

struct_mtget.__slots__ = [
    'mt_type',
    'mt_resid',
    'mt_dsreg',
    'mt_gstat',
    'mt_erreg',
    'mt_fileno',
    'mt_blkno',
]
struct_mtget._fields_ = [
    ('mt_type', c_long),
    ('mt_resid', c_long),
    ('mt_dsreg', c_long),
    ('mt_gstat', c_long),
    ('mt_erreg', c_long),
    ('mt_fileno', __daddr_t),
    ('mt_blkno', __daddr_t),
]

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 127
class struct_mt_tape_info(Structure):
    pass

struct_mt_tape_info.__slots__ = [
    't_type',
    't_name',
]
struct_mt_tape_info._fields_ = [
    ('t_type', c_long),
    ('t_name', String),
]

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 157
class struct_mtpos(Structure):
    pass

struct_mtpos.__slots__ = [
    'mt_blkno',
]
struct_mtpos._fields_ = [
    ('mt_blkno', c_long),
]

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 167
class struct_mtconfiginfo(Structure):
    pass

struct_mtconfiginfo.__slots__ = [
    'mt_type',
    'ifc_type',
    'irqnr',
    'dmanr',
    'port',
    'debug',
    'have_dens',
    'have_bsf',
    'have_fsr',
    'have_bsr',
    'have_eod',
    'have_seek',
    'have_tell',
    'have_ras1',
    'have_ras2',
    'have_ras3',
    'have_qfa',
    'pad1',
    'reserved',
]
struct_mtconfiginfo._fields_ = [
    ('mt_type', c_long),
    ('ifc_type', c_long),
    ('irqnr', c_uint),
    ('dmanr', c_uint),
    ('port', c_uint),
    ('debug', c_ulong),
    ('have_dens', c_uint, 1),
    ('have_bsf', c_uint, 1),
    ('have_fsr', c_uint, 1),
    ('have_bsr', c_uint, 1),
    ('have_eod', c_uint, 1),
    ('have_seek', c_uint, 1),
    ('have_tell', c_uint, 1),
    ('have_ras1', c_uint, 1),
    ('have_ras2', c_uint, 1),
    ('have_ras3', c_uint, 1),
    ('have_qfa', c_uint, 1),
    ('pad1', c_uint, 5),
    ('reserved', c_char * int(10)),
]

# /usr/include/x86_64-linux-gnu/bits/types/__sigval_t.h: 24
class union_sigval(Union):
    pass

union_sigval.__slots__ = [
    'sival_int',
    'sival_ptr',
]
union_sigval._fields_ = [
    ('sival_int', c_int),
    ('sival_ptr', POINTER(None)),
]

__sigval_t = union_sigval# /usr/include/x86_64-linux-gnu/bits/types/__sigval_t.h: 30

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 56
class struct_anon_86(Structure):
    pass

struct_anon_86.__slots__ = [
    'si_pid',
    'si_uid',
]
struct_anon_86._fields_ = [
    ('si_pid', __pid_t),
    ('si_uid', __uid_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 63
class struct_anon_87(Structure):
    pass

struct_anon_87.__slots__ = [
    'si_tid',
    'si_overrun',
    'si_sigval',
]
struct_anon_87._fields_ = [
    ('si_tid', c_int),
    ('si_overrun', c_int),
    ('si_sigval', __sigval_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 71
class struct_anon_88(Structure):
    pass

struct_anon_88.__slots__ = [
    'si_pid',
    'si_uid',
    'si_sigval',
]
struct_anon_88._fields_ = [
    ('si_pid', __pid_t),
    ('si_uid', __uid_t),
    ('si_sigval', __sigval_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 79
class struct_anon_89(Structure):
    pass

struct_anon_89.__slots__ = [
    'si_pid',
    'si_uid',
    'si_status',
    'si_utime',
    'si_stime',
]
struct_anon_89._fields_ = [
    ('si_pid', __pid_t),
    ('si_uid', __uid_t),
    ('si_status', c_int),
    ('si_utime', __clock_t),
    ('si_stime', __clock_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 97
class struct_anon_90(Structure):
    pass

struct_anon_90.__slots__ = [
    '_lower',
    '_upper',
]
struct_anon_90._fields_ = [
    ('_lower', POINTER(None)),
    ('_upper', POINTER(None)),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 94
class union_anon_91(Union):
    pass

union_anon_91.__slots__ = [
    '_addr_bnd',
    '_pkey',
]
union_anon_91._fields_ = [
    ('_addr_bnd', struct_anon_90),
    ('_pkey', __uint32_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 89
class struct_anon_92(Structure):
    pass

struct_anon_92.__slots__ = [
    'si_addr',
    'si_addr_lsb',
    '_bounds',
]
struct_anon_92._fields_ = [
    ('si_addr', POINTER(None)),
    ('si_addr_lsb', c_int),
    ('_bounds', union_anon_91),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 108
class struct_anon_93(Structure):
    pass

struct_anon_93.__slots__ = [
    'si_band',
    'si_fd',
]
struct_anon_93._fields_ = [
    ('si_band', c_long),
    ('si_fd', c_int),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 116
class struct_anon_94(Structure):
    pass

struct_anon_94.__slots__ = [
    '_call_addr',
    '_syscall',
    '_arch',
]
struct_anon_94._fields_ = [
    ('_call_addr', POINTER(None)),
    ('_syscall', c_int),
    ('_arch', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 51
class union_anon_95(Union):
    pass

union_anon_95.__slots__ = [
    '_pad',
    '_kill',
    '_timer',
    '_rt',
    '_sigchld',
    '_sigfault',
    '_sigpoll',
    '_sigsys',
]
union_anon_95._fields_ = [
    ('_pad', c_int * int(((128 / sizeof(c_int)) - 4))),
    ('_kill', struct_anon_86),
    ('_timer', struct_anon_87),
    ('_rt', struct_anon_88),
    ('_sigchld', struct_anon_89),
    ('_sigfault', struct_anon_92),
    ('_sigpoll', struct_anon_93),
    ('_sigsys', struct_anon_94),
]

# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 124
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'si_signo',
    'si_errno',
    'si_code',
    '__pad0',
    '_sifields',
]
struct_anon_96._fields_ = [
    ('si_signo', c_int),
    ('si_errno', c_int),
    ('si_code', c_int),
    ('__pad0', c_int),
    ('_sifields', union_anon_95),
]

siginfo_t = struct_anon_96# /usr/include/x86_64-linux-gnu/bits/types/siginfo_t.h: 124

# /usr/include/x86_64-linux-gnu/bits/types/sigevent_t.h: 36
class struct_anon_104(Structure):
    pass

struct_anon_104.__slots__ = [
    '_function',
    '_attribute',
]
struct_anon_104._fields_ = [
    ('_function', CFUNCTYPE(UNCHECKED(None), __sigval_t)),
    ('_attribute', POINTER(pthread_attr_t)),
]

# /usr/include/x86_64-linux-gnu/bits/types/sigevent_t.h: 28
class union_anon_105(Union):
    pass

union_anon_105.__slots__ = [
    '_pad',
    '_tid',
    '_sigev_thread',
]
union_anon_105._fields_ = [
    ('_pad', c_int * int(((64 / sizeof(c_int)) - 4))),
    ('_tid', __pid_t),
    ('_sigev_thread', struct_anon_104),
]

# /usr/include/x86_64-linux-gnu/bits/types/sigevent_t.h: 42
class struct_sigevent(Structure):
    pass

struct_sigevent.__slots__ = [
    'sigev_value',
    'sigev_signo',
    'sigev_notify',
    '_sigev_un',
]
struct_sigevent._fields_ = [
    ('sigev_value', __sigval_t),
    ('sigev_signo', c_int),
    ('sigev_notify', c_int),
    ('_sigev_un', union_anon_105),
]

__sighandler_t = CFUNCTYPE(UNCHECKED(None), c_int)# /usr/include/signal.h: 72

# /usr/include/signal.h: 77
if _libs["libc.so.6"].has("__sysv_signal", "cdecl"):
    __sysv_signal = _libs["libc.so.6"].get("__sysv_signal", "cdecl")
    __sysv_signal.argtypes = [c_int, __sighandler_t]
    __sysv_signal.restype = __sighandler_t

# /usr/include/signal.h: 88
if _libs["libc.so.6"].has("signal", "cdecl"):
    signal = _libs["libc.so.6"].get("signal", "cdecl")
    signal.argtypes = [c_int, __sighandler_t]
    signal.restype = __sighandler_t

# /usr/include/signal.h: 112
if _libs["libc.so.6"].has("kill", "cdecl"):
    kill = _libs["libc.so.6"].get("kill", "cdecl")
    kill.argtypes = [__pid_t, c_int]
    kill.restype = c_int

# /usr/include/signal.h: 119
if _libs["libc.so.6"].has("killpg", "cdecl"):
    killpg = _libs["libc.so.6"].get("killpg", "cdecl")
    killpg.argtypes = [__pid_t, c_int]
    killpg.restype = c_int

# /usr/include/signal.h: 123
if _libs["libc.so.6"].has("raise", "cdecl"):
    raise_ = _libs["libc.so.6"].get("raise", "cdecl")
    raise_.argtypes = [c_int]
    raise_.restype = c_int

# /usr/include/signal.h: 127
if _libs["libc.so.6"].has("ssignal", "cdecl"):
    ssignal = _libs["libc.so.6"].get("ssignal", "cdecl")
    ssignal.argtypes = [c_int, __sighandler_t]
    ssignal.restype = __sighandler_t

# /usr/include/signal.h: 129
if _libs["libc.so.6"].has("gsignal", "cdecl"):
    gsignal = _libs["libc.so.6"].get("gsignal", "cdecl")
    gsignal.argtypes = [c_int]
    gsignal.restype = c_int

# /usr/include/signal.h: 134
if _libs["libc.so.6"].has("psignal", "cdecl"):
    psignal = _libs["libc.so.6"].get("psignal", "cdecl")
    psignal.argtypes = [c_int, String]
    psignal.restype = None

# /usr/include/signal.h: 137
if _libs["libc.so.6"].has("psiginfo", "cdecl"):
    psiginfo = _libs["libc.so.6"].get("psiginfo", "cdecl")
    psiginfo.argtypes = [POINTER(siginfo_t), String]
    psiginfo.restype = None

# /usr/include/signal.h: 170
if _libs["libc.so.6"].has("sigblock", "cdecl"):
    sigblock = _libs["libc.so.6"].get("sigblock", "cdecl")
    sigblock.argtypes = [c_int]
    sigblock.restype = c_int

# /usr/include/signal.h: 173
if _libs["libc.so.6"].has("sigsetmask", "cdecl"):
    sigsetmask = _libs["libc.so.6"].get("sigsetmask", "cdecl")
    sigsetmask.argtypes = [c_int]
    sigsetmask.restype = c_int

# /usr/include/signal.h: 176
if _libs["libc.so.6"].has("siggetmask", "cdecl"):
    siggetmask = _libs["libc.so.6"].get("siggetmask", "cdecl")
    siggetmask.argtypes = []
    siggetmask.restype = c_int

sig_t = __sighandler_t# /usr/include/signal.h: 190

# /usr/include/signal.h: 196
if _libs["libc.so.6"].has("sigemptyset", "cdecl"):
    sigemptyset = _libs["libc.so.6"].get("sigemptyset", "cdecl")
    sigemptyset.argtypes = [POINTER(sigset_t)]
    sigemptyset.restype = c_int

# /usr/include/signal.h: 199
if _libs["libc.so.6"].has("sigfillset", "cdecl"):
    sigfillset = _libs["libc.so.6"].get("sigfillset", "cdecl")
    sigfillset.argtypes = [POINTER(sigset_t)]
    sigfillset.restype = c_int

# /usr/include/signal.h: 202
if _libs["libc.so.6"].has("sigaddset", "cdecl"):
    sigaddset = _libs["libc.so.6"].get("sigaddset", "cdecl")
    sigaddset.argtypes = [POINTER(sigset_t), c_int]
    sigaddset.restype = c_int

# /usr/include/signal.h: 205
if _libs["libc.so.6"].has("sigdelset", "cdecl"):
    sigdelset = _libs["libc.so.6"].get("sigdelset", "cdecl")
    sigdelset.argtypes = [POINTER(sigset_t), c_int]
    sigdelset.restype = c_int

# /usr/include/signal.h: 208
if _libs["libc.so.6"].has("sigismember", "cdecl"):
    sigismember = _libs["libc.so.6"].get("sigismember", "cdecl")
    sigismember.argtypes = [POINTER(sigset_t), c_int]
    sigismember.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/sigaction.h: 31
class union_anon_107(Union):
    pass

union_anon_107.__slots__ = [
    'sa_handler',
    'sa_sigaction',
]
union_anon_107._fields_ = [
    ('sa_handler', __sighandler_t),
    ('sa_sigaction', CFUNCTYPE(UNCHECKED(None), c_int, POINTER(siginfo_t), POINTER(None))),
]

# /usr/include/x86_64-linux-gnu/bits/sigaction.h: 27
class struct_sigaction(Structure):
    pass

struct_sigaction.__slots__ = [
    '__sigaction_handler',
    'sa_mask',
    'sa_flags',
    'sa_restorer',
]
struct_sigaction._fields_ = [
    ('__sigaction_handler', union_anon_107),
    ('sa_mask', __sigset_t),
    ('sa_flags', c_int),
    ('sa_restorer', CFUNCTYPE(UNCHECKED(None), )),
]

# /usr/include/signal.h: 229
if _libs["libc.so.6"].has("sigprocmask", "cdecl"):
    sigprocmask = _libs["libc.so.6"].get("sigprocmask", "cdecl")
    sigprocmask.argtypes = [c_int, POINTER(sigset_t), POINTER(sigset_t)]
    sigprocmask.restype = c_int

# /usr/include/signal.h: 237
if _libs["libc.so.6"].has("sigsuspend", "cdecl"):
    sigsuspend = _libs["libc.so.6"].get("sigsuspend", "cdecl")
    sigsuspend.argtypes = [POINTER(sigset_t)]
    sigsuspend.restype = c_int

# /usr/include/signal.h: 240
if _libs["libc.so.6"].has("sigaction", "cdecl"):
    sigaction = _libs["libc.so.6"].get("sigaction", "cdecl")
    sigaction.argtypes = [c_int, POINTER(struct_sigaction), POINTER(struct_sigaction)]
    sigaction.restype = c_int

# /usr/include/signal.h: 244
if _libs["libc.so.6"].has("sigpending", "cdecl"):
    sigpending = _libs["libc.so.6"].get("sigpending", "cdecl")
    sigpending.argtypes = [POINTER(sigset_t)]
    sigpending.restype = c_int

# /usr/include/signal.h: 252
if _libs["libc.so.6"].has("sigwait", "cdecl"):
    sigwait = _libs["libc.so.6"].get("sigwait", "cdecl")
    sigwait.argtypes = [POINTER(sigset_t), POINTER(c_int)]
    sigwait.restype = c_int

# /usr/include/signal.h: 261
if _libs["libc.so.6"].has("sigwaitinfo", "cdecl"):
    sigwaitinfo = _libs["libc.so.6"].get("sigwaitinfo", "cdecl")
    sigwaitinfo.argtypes = [POINTER(sigset_t), POINTER(siginfo_t)]
    sigwaitinfo.restype = c_int

# /usr/include/signal.h: 269
if _libs["libc.so.6"].has("sigtimedwait", "cdecl"):
    sigtimedwait = _libs["libc.so.6"].get("sigtimedwait", "cdecl")
    sigtimedwait.argtypes = [POINTER(sigset_t), POINTER(siginfo_t), POINTER(struct_timespec)]
    sigtimedwait.restype = c_int

# /usr/include/signal.h: 276
if _libs["libc.so.6"].has("sigqueue", "cdecl"):
    sigqueue = _libs["libc.so.6"].get("sigqueue", "cdecl")
    sigqueue.argtypes = [__pid_t, c_int, union_sigval]
    sigqueue.restype = c_int

# /usr/include/signal.h: 286
try:
    _sys_siglist = (POINTER(c_char) * int((64 + 1))).in_dll(_libs["libc.so.6"], "_sys_siglist")
except:
    pass

# /usr/include/signal.h: 287
try:
    sys_siglist = (POINTER(c_char) * int((64 + 1))).in_dll(_libs["libc.so.6"], "sys_siglist")
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sigcontext.h: 46
class struct__fpxreg(Structure):
    pass

struct__fpxreg.__slots__ = [
    'significand',
    'exponent',
    '__glibc_reserved1',
]
struct__fpxreg._fields_ = [
    ('significand', c_ushort * int(4)),
    ('exponent', c_ushort),
    ('__glibc_reserved1', c_ushort * int(3)),
]

# /usr/include/x86_64-linux-gnu/bits/sigcontext.h: 53
class struct__xmmreg(Structure):
    pass

struct__xmmreg.__slots__ = [
    'element',
]
struct__xmmreg._fields_ = [
    ('element', __uint32_t * int(4)),
]

# /usr/include/x86_64-linux-gnu/bits/sigcontext.h: 123
class struct__fpstate(Structure):
    pass

struct__fpstate.__slots__ = [
    'cwd',
    'swd',
    'ftw',
    'fop',
    'rip',
    'rdp',
    'mxcsr',
    'mxcr_mask',
    '_st',
    '_xmm',
    '__glibc_reserved1',
]
struct__fpstate._fields_ = [
    ('cwd', __uint16_t),
    ('swd', __uint16_t),
    ('ftw', __uint16_t),
    ('fop', __uint16_t),
    ('rip', __uint64_t),
    ('rdp', __uint64_t),
    ('mxcsr', __uint32_t),
    ('mxcr_mask', __uint32_t),
    ('_st', struct__fpxreg * int(8)),
    ('_xmm', struct__xmmreg * int(16)),
    ('__glibc_reserved1', __uint32_t * int(24)),
]

# /usr/include/x86_64-linux-gnu/bits/sigcontext.h: 167
class union_anon_108(Union):
    pass

union_anon_108.__slots__ = [
    'fpstate',
    '__fpstate_word',
]
union_anon_108._fields_ = [
    ('fpstate', POINTER(struct__fpstate)),
    ('__fpstate_word', __uint64_t),
]

# /usr/include/x86_64-linux-gnu/bits/sigcontext.h: 139
class struct_sigcontext(Structure):
    pass

struct_sigcontext.__slots__ = [
    'r8',
    'r9',
    'r10',
    'r11',
    'r12',
    'r13',
    'r14',
    'r15',
    'rdi',
    'rsi',
    'rbp',
    'rbx',
    'rdx',
    'rax',
    'rcx',
    'rsp',
    'rip',
    'eflags',
    'cs',
    'gs',
    'fs',
    '__pad0',
    'err',
    'trapno',
    'oldmask',
    'cr2',
    'unnamed_1',
    '__reserved1',
]
struct_sigcontext._anonymous_ = [
    'unnamed_1',
]
struct_sigcontext._fields_ = [
    ('r8', __uint64_t),
    ('r9', __uint64_t),
    ('r10', __uint64_t),
    ('r11', __uint64_t),
    ('r12', __uint64_t),
    ('r13', __uint64_t),
    ('r14', __uint64_t),
    ('r15', __uint64_t),
    ('rdi', __uint64_t),
    ('rsi', __uint64_t),
    ('rbp', __uint64_t),
    ('rbx', __uint64_t),
    ('rdx', __uint64_t),
    ('rax', __uint64_t),
    ('rcx', __uint64_t),
    ('rsp', __uint64_t),
    ('rip', __uint64_t),
    ('eflags', __uint64_t),
    ('cs', c_ushort),
    ('gs', c_ushort),
    ('fs', c_ushort),
    ('__pad0', c_ushort),
    ('err', __uint64_t),
    ('trapno', __uint64_t),
    ('oldmask', __uint64_t),
    ('cr2', __uint64_t),
    ('unnamed_1', union_anon_108),
    ('__reserved1', __uint64_t * int(8)),
]

# /usr/include/signal.h: 294
if _libs["libc.so.6"].has("sigreturn", "cdecl"):
    sigreturn = _libs["libc.so.6"].get("sigreturn", "cdecl")
    sigreturn.argtypes = [POINTER(struct_sigcontext)]
    sigreturn.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/types/stack_t.h: 31
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'ss_sp',
    'ss_flags',
    'ss_size',
]
struct_anon_109._fields_ = [
    ('ss_sp', POINTER(None)),
    ('ss_flags', c_int),
    ('ss_size', c_size_t),
]

stack_t = struct_anon_109# /usr/include/x86_64-linux-gnu/bits/types/stack_t.h: 31

greg_t = c_longlong# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 37

gregset_t = greg_t * int(23)# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 46

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 101
class struct__libc_fpxreg(Structure):
    pass

struct__libc_fpxreg.__slots__ = [
    'significand',
    'exponent',
    '__glibc_reserved1',
]
struct__libc_fpxreg._fields_ = [
    ('significand', c_uint * int(4)),
    ('exponent', c_uint),
    ('__glibc_reserved1', c_uint * int(3)),
]

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 108
class struct__libc_xmmreg(Structure):
    pass

struct__libc_xmmreg.__slots__ = [
    'element',
]
struct__libc_xmmreg._fields_ = [
    ('element', __uint32_t * int(4)),
]

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 113
class struct__libc_fpstate(Structure):
    pass

struct__libc_fpstate.__slots__ = [
    'cwd',
    'swd',
    'ftw',
    'fop',
    'rip',
    'rdp',
    'mxcsr',
    'mxcr_mask',
    '_st',
    '_xmm',
    '__glibc_reserved1',
]
struct__libc_fpstate._fields_ = [
    ('cwd', __uint16_t),
    ('swd', __uint16_t),
    ('ftw', __uint16_t),
    ('fop', __uint16_t),
    ('rip', __uint64_t),
    ('rdp', __uint64_t),
    ('mxcsr', __uint32_t),
    ('mxcr_mask', __uint32_t),
    ('_st', struct__libc_fpxreg * int(8)),
    ('_xmm', struct__libc_xmmreg * int(16)),
    ('__glibc_reserved1', __uint32_t * int(24)),
]

fpregset_t = POINTER(struct__libc_fpstate)# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 130

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 139
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'gregs',
    'fpregs',
    '__reserved1',
]
struct_anon_110._fields_ = [
    ('gregs', gregset_t),
    ('fpregs', fpregset_t),
    ('__reserved1', c_ulonglong * int(8)),
]

mcontext_t = struct_anon_110# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 139

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 142
class struct_ucontext_t(Structure):
    pass

struct_ucontext_t.__slots__ = [
    'uc_flags',
    'uc_link',
    'uc_stack',
    'uc_mcontext',
    'uc_sigmask',
    '__fpregs_mem',
    '__ssp',
]
struct_ucontext_t._fields_ = [
    ('uc_flags', c_ulong),
    ('uc_link', POINTER(struct_ucontext_t)),
    ('uc_stack', stack_t),
    ('uc_mcontext', mcontext_t),
    ('uc_sigmask', sigset_t),
    ('__fpregs_mem', struct__libc_fpstate),
    ('__ssp', c_ulonglong * int(4)),
]

ucontext_t = struct_ucontext_t# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 151

# /usr/include/signal.h: 314
if _libs["libc.so.6"].has("siginterrupt", "cdecl"):
    siginterrupt = _libs["libc.so.6"].get("siginterrupt", "cdecl")
    siginterrupt.argtypes = [c_int, c_int]
    siginterrupt.restype = c_int

# /usr/include/signal.h: 321
if _libs["libc.so.6"].has("sigaltstack", "cdecl"):
    sigaltstack = _libs["libc.so.6"].get("sigaltstack", "cdecl")
    sigaltstack.argtypes = [POINTER(stack_t), POINTER(stack_t)]
    sigaltstack.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/types/struct_sigstack.h: 23
class struct_sigstack(Structure):
    pass

struct_sigstack.__slots__ = [
    'ss_sp',
    'ss_onstack',
]
struct_sigstack._fields_ = [
    ('ss_sp', POINTER(None)),
    ('ss_onstack', c_int),
]

# /usr/include/signal.h: 335
if _libs["libc.so.6"].has("sigstack", "cdecl"):
    sigstack = _libs["libc.so.6"].get("sigstack", "cdecl")
    sigstack.argtypes = [POINTER(struct_sigstack), POINTER(struct_sigstack)]
    sigstack.restype = c_int

# /usr/include/signal.h: 366
if _libs["libc.so.6"].has("__libc_current_sigrtmin", "cdecl"):
    __libc_current_sigrtmin = _libs["libc.so.6"].get("__libc_current_sigrtmin", "cdecl")
    __libc_current_sigrtmin.argtypes = []
    __libc_current_sigrtmin.restype = c_int

# /usr/include/signal.h: 368
if _libs["libc.so.6"].has("__libc_current_sigrtmax", "cdecl"):
    __libc_current_sigrtmax = _libs["libc.so.6"].get("__libc_current_sigrtmax", "cdecl")
    __libc_current_sigrtmax.argtypes = []
    __libc_current_sigrtmax.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/perm.h: 26
if _libs["libc.so.6"].has("ioperm", "cdecl"):
    ioperm = _libs["libc.so.6"].get("ioperm", "cdecl")
    ioperm.argtypes = [c_ulong, c_ulong, c_int]
    ioperm.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/perm.h: 31
if _libs["libc.so.6"].has("iopl", "cdecl"):
    iopl = _libs["libc.so.6"].get("iopl", "cdecl")
    iopl.argtypes = [c_int]
    iopl.restype = c_int

enum_anon_112 = c_int# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

UNAME26 = 0x0020000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

ADDR_NO_RANDOMIZE = 0x0040000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

FDPIC_FUNCPTRS = 0x0080000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

MMAP_PAGE_ZERO = 0x0100000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

ADDR_COMPAT_LAYOUT = 0x0200000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

READ_IMPLIES_EXEC = 0x0400000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

ADDR_LIMIT_32BIT = 0x0800000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

SHORT_INODE = 0x1000000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

WHOLE_SECONDS = 0x2000000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

STICKY_TIMEOUTS = 0x4000000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

ADDR_LIMIT_3GB = 0x8000000# /usr/include/x86_64-linux-gnu/sys/personality.h: 27

enum_anon_113 = c_int# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_LINUX = 0x0000# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_LINUX_32BIT = (0x0000 | ADDR_LIMIT_32BIT)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_LINUX_FDPIC = (0x0000 | FDPIC_FUNCPTRS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_SVR4 = ((0x0001 | STICKY_TIMEOUTS) | MMAP_PAGE_ZERO)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_SVR3 = ((0x0002 | STICKY_TIMEOUTS) | SHORT_INODE)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_SCOSVR3 = (((0x0003 | STICKY_TIMEOUTS) | WHOLE_SECONDS) | SHORT_INODE)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_OSR5 = ((0x0003 | STICKY_TIMEOUTS) | WHOLE_SECONDS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_WYSEV386 = ((0x0004 | STICKY_TIMEOUTS) | SHORT_INODE)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_ISCR4 = (0x0005 | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_BSD = 0x0006# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_SUNOS = (0x0006 | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_XENIX = ((0x0007 | STICKY_TIMEOUTS) | SHORT_INODE)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_LINUX32 = 0x0008# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_LINUX32_3GB = (0x0008 | ADDR_LIMIT_3GB)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_IRIX32 = (0x0009 | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_IRIXN32 = (0x000a | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_IRIX64 = (0x000b | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_RISCOS = 0x000c# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_SOLARIS = (0x000d | STICKY_TIMEOUTS)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_UW7 = ((0x000e | STICKY_TIMEOUTS) | MMAP_PAGE_ZERO)# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_OSF4 = 0x000f# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_HPUX = 0x0010# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

PER_MASK = 0x00ff# /usr/include/x86_64-linux-gnu/sys/personality.h: 46

# /usr/include/x86_64-linux-gnu/sys/personality.h: 76
if _libs["libc.so.6"].has("personality", "cdecl"):
    personality = _libs["libc.so.6"].get("personality", "cdecl")
    personality.argtypes = [c_ulong]
    personality.restype = c_int

nfds_t = c_ulong# /usr/include/x86_64-linux-gnu/sys/poll.h: 33

# /usr/include/x86_64-linux-gnu/sys/poll.h: 36
class struct_pollfd(Structure):
    pass

struct_pollfd.__slots__ = [
    'fd',
    'events',
    'revents',
]
struct_pollfd._fields_ = [
    ('fd', c_int),
    ('events', c_int),
    ('revents', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/poll.h: 54
if _libs["libc.so.6"].has("poll", "cdecl"):
    poll = _libs["libc.so.6"].get("poll", "cdecl")
    poll.argtypes = [POINTER(struct_pollfd), nfds_t, c_int]
    poll.restype = c_int

# /usr/include/linux/prctl.h: 134
class struct_prctl_mm_map(Structure):
    pass

struct_prctl_mm_map.__slots__ = [
    'start_code',
    'end_code',
    'start_data',
    'end_data',
    'start_brk',
    'brk',
    'start_stack',
    'arg_start',
    'arg_end',
    'env_start',
    'env_end',
    'auxv',
    'auxv_size',
    'exe_fd',
]
struct_prctl_mm_map._fields_ = [
    ('start_code', __u64),
    ('end_code', __u64),
    ('start_data', __u64),
    ('end_data', __u64),
    ('start_brk', __u64),
    ('brk', __u64),
    ('start_stack', __u64),
    ('arg_start', __u64),
    ('arg_end', __u64),
    ('env_start', __u64),
    ('env_end', __u64),
    ('auxv', POINTER(__u64)),
    ('auxv_size', __u32),
    ('exe_fd', __u32),
]

# /usr/include/x86_64-linux-gnu/sys/prctl.h: 27
if _libs["libc.so.6"].has("prctl", "cdecl"):
    _func = _libs["libc.so.6"].get("prctl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int]
    prctl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/x86_64-linux-gnu/sys/time.h: 52
class struct_timezone(Structure):
    pass

struct_timezone.__slots__ = [
    'tz_minuteswest',
    'tz_dsttime',
]
struct_timezone._fields_ = [
    ('tz_minuteswest', c_int),
    ('tz_dsttime', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/time.h: 66
if _libs["libc.so.6"].has("gettimeofday", "cdecl"):
    gettimeofday = _libs["libc.so.6"].get("gettimeofday", "cdecl")
    gettimeofday.argtypes = [POINTER(struct_timeval), POINTER(None)]
    gettimeofday.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 75
if _libs["libc.so.6"].has("settimeofday", "cdecl"):
    settimeofday = _libs["libc.so.6"].get("settimeofday", "cdecl")
    settimeofday.argtypes = [POINTER(struct_timeval), POINTER(struct_timezone)]
    settimeofday.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 83
if _libs["libc.so.6"].has("adjtime", "cdecl"):
    adjtime = _libs["libc.so.6"].get("adjtime", "cdecl")
    adjtime.argtypes = [POINTER(struct_timeval), POINTER(struct_timeval)]
    adjtime.restype = c_int

enum___itimer_which = c_int# /usr/include/x86_64-linux-gnu/sys/time.h: 89

ITIMER_REAL = 0# /usr/include/x86_64-linux-gnu/sys/time.h: 89

ITIMER_VIRTUAL = 1# /usr/include/x86_64-linux-gnu/sys/time.h: 89

ITIMER_PROF = 2# /usr/include/x86_64-linux-gnu/sys/time.h: 89

# /usr/include/x86_64-linux-gnu/sys/time.h: 105
class struct_itimerval(Structure):
    pass

struct_itimerval.__slots__ = [
    'it_interval',
    'it_value',
]
struct_itimerval._fields_ = [
    ('it_interval', struct_timeval),
    ('it_value', struct_timeval),
]

__itimer_which_t = c_int# /usr/include/x86_64-linux-gnu/sys/time.h: 118

# /usr/include/x86_64-linux-gnu/sys/time.h: 123
if _libs["libc.so.6"].has("getitimer", "cdecl"):
    getitimer = _libs["libc.so.6"].get("getitimer", "cdecl")
    getitimer.argtypes = [__itimer_which_t, POINTER(struct_itimerval)]
    getitimer.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 129
if _libs["libc.so.6"].has("setitimer", "cdecl"):
    setitimer = _libs["libc.so.6"].get("setitimer", "cdecl")
    setitimer.argtypes = [__itimer_which_t, POINTER(struct_itimerval), POINTER(struct_itimerval)]
    setitimer.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 136
if _libs["libc.so.6"].has("utimes", "cdecl"):
    utimes = _libs["libc.so.6"].get("utimes", "cdecl")
    utimes.argtypes = [String, struct_timeval * int(2)]
    utimes.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 141
if _libs["libc.so.6"].has("lutimes", "cdecl"):
    lutimes = _libs["libc.so.6"].get("lutimes", "cdecl")
    lutimes.argtypes = [String, struct_timeval * int(2)]
    lutimes.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/time.h: 145
if _libs["libc.so.6"].has("futimes", "cdecl"):
    futimes = _libs["libc.so.6"].get("futimes", "cdecl")
    futimes.argtypes = [c_int, struct_timeval * int(2)]
    futimes.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/user.h: 27
class struct_user_fpregs_struct(Structure):
    pass

struct_user_fpregs_struct.__slots__ = [
    'cwd',
    'swd',
    'ftw',
    'fop',
    'rip',
    'rdp',
    'mxcsr',
    'mxcr_mask',
    'st_space',
    'xmm_space',
    'padding',
]
struct_user_fpregs_struct._fields_ = [
    ('cwd', c_uint),
    ('swd', c_uint),
    ('ftw', c_uint),
    ('fop', c_uint),
    ('rip', c_ulonglong),
    ('rdp', c_ulonglong),
    ('mxcsr', c_uint),
    ('mxcr_mask', c_uint),
    ('st_space', c_uint * int(32)),
    ('xmm_space', c_uint * int(64)),
    ('padding', c_uint * int(24)),
]

# /usr/include/x86_64-linux-gnu/sys/user.h: 42
class struct_user_regs_struct(Structure):
    pass

struct_user_regs_struct.__slots__ = [
    'r15',
    'r14',
    'r13',
    'r12',
    'rbp',
    'rbx',
    'r11',
    'r10',
    'r9',
    'r8',
    'rax',
    'rcx',
    'rdx',
    'rsi',
    'rdi',
    'orig_rax',
    'rip',
    'cs',
    'eflags',
    'rsp',
    'ss',
    'fs_base',
    'gs_base',
    'ds',
    'es',
    'fs',
    'gs',
]
struct_user_regs_struct._fields_ = [
    ('r15', c_ulonglong),
    ('r14', c_ulonglong),
    ('r13', c_ulonglong),
    ('r12', c_ulonglong),
    ('rbp', c_ulonglong),
    ('rbx', c_ulonglong),
    ('r11', c_ulonglong),
    ('r10', c_ulonglong),
    ('r9', c_ulonglong),
    ('r8', c_ulonglong),
    ('rax', c_ulonglong),
    ('rcx', c_ulonglong),
    ('rdx', c_ulonglong),
    ('rsi', c_ulonglong),
    ('rdi', c_ulonglong),
    ('orig_rax', c_ulonglong),
    ('rip', c_ulonglong),
    ('cs', c_ulonglong),
    ('eflags', c_ulonglong),
    ('rsp', c_ulonglong),
    ('ss', c_ulonglong),
    ('fs_base', c_ulonglong),
    ('gs_base', c_ulonglong),
    ('ds', c_ulonglong),
    ('es', c_ulonglong),
    ('fs', c_ulonglong),
    ('gs', c_ulonglong),
]

# /usr/include/x86_64-linux-gnu/sys/user.h: 85
class union_anon_114(Union):
    pass

union_anon_114.__slots__ = [
    'u_ar0',
    '__u_ar0_word',
]
union_anon_114._fields_ = [
    ('u_ar0', POINTER(struct_user_regs_struct)),
    ('__u_ar0_word', c_ulonglong),
]

# /usr/include/x86_64-linux-gnu/sys/user.h: 90
class union_anon_115(Union):
    pass

union_anon_115.__slots__ = [
    'u_fpstate',
    '__u_fpstate_word',
]
union_anon_115._fields_ = [
    ('u_fpstate', POINTER(struct_user_fpregs_struct)),
    ('__u_fpstate_word', c_ulonglong),
]

# /usr/include/x86_64-linux-gnu/sys/user.h: 73
class struct_user(Structure):
    pass

struct_user.__slots__ = [
    'regs',
    'u_fpvalid',
    'i387',
    'u_tsize',
    'u_dsize',
    'u_ssize',
    'start_code',
    'start_stack',
    'signal',
    'reserved',
    'unnamed_1',
    'unnamed_2',
    'magic',
    'u_comm',
    'u_debugreg',
]
struct_user._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_user._fields_ = [
    ('regs', struct_user_regs_struct),
    ('u_fpvalid', c_int),
    ('i387', struct_user_fpregs_struct),
    ('u_tsize', c_ulonglong),
    ('u_dsize', c_ulonglong),
    ('u_ssize', c_ulonglong),
    ('start_code', c_ulonglong),
    ('start_stack', c_ulonglong),
    ('signal', c_longlong),
    ('reserved', c_int),
    ('unnamed_1', union_anon_114),
    ('unnamed_2', union_anon_115),
    ('magic', c_ulonglong),
    ('u_comm', c_char * int(32)),
    ('u_debugreg', c_ulonglong * int(8)),
]

elf_greg_t = c_ulonglong# /usr/include/x86_64-linux-gnu/bits/procfs.h: 25

elf_gregset_t = elf_greg_t * int((sizeof(struct_user_regs_struct) / sizeof(elf_greg_t)))# /usr/include/x86_64-linux-gnu/bits/procfs.h: 35

elf_fpregset_t = struct_user_fpregs_struct# /usr/include/x86_64-linux-gnu/bits/procfs.h: 49

__pr_uid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/procfs-id.h: 28

__pr_gid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/procfs-id.h: 29

# /usr/include/x86_64-linux-gnu/sys/procfs.h: 49
class struct_elf_siginfo(Structure):
    pass

struct_elf_siginfo.__slots__ = [
    'si_signo',
    'si_code',
    'si_errno',
]
struct_elf_siginfo._fields_ = [
    ('si_signo', c_int),
    ('si_code', c_int),
    ('si_errno', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/procfs.h: 63
class struct_elf_prstatus(Structure):
    pass

struct_elf_prstatus.__slots__ = [
    'pr_info',
    'pr_cursig',
    'pr_sigpend',
    'pr_sighold',
    'pr_pid',
    'pr_ppid',
    'pr_pgrp',
    'pr_sid',
    'pr_utime',
    'pr_stime',
    'pr_cutime',
    'pr_cstime',
    'pr_reg',
    'pr_fpvalid',
]
struct_elf_prstatus._fields_ = [
    ('pr_info', struct_elf_siginfo),
    ('pr_cursig', c_int),
    ('pr_sigpend', c_ulong),
    ('pr_sighold', c_ulong),
    ('pr_pid', __pid_t),
    ('pr_ppid', __pid_t),
    ('pr_pgrp', __pid_t),
    ('pr_sid', __pid_t),
    ('pr_utime', struct_timeval),
    ('pr_stime', struct_timeval),
    ('pr_cutime', struct_timeval),
    ('pr_cstime', struct_timeval),
    ('pr_reg', elf_gregset_t),
    ('pr_fpvalid', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/procfs.h: 84
class struct_elf_prpsinfo(Structure):
    pass

struct_elf_prpsinfo.__slots__ = [
    'pr_state',
    'pr_sname',
    'pr_zomb',
    'pr_nice',
    'pr_flag',
    'pr_uid',
    'pr_gid',
    'pr_pid',
    'pr_ppid',
    'pr_pgrp',
    'pr_sid',
    'pr_fname',
    'pr_psargs',
]
struct_elf_prpsinfo._fields_ = [
    ('pr_state', c_char),
    ('pr_sname', c_char),
    ('pr_zomb', c_char),
    ('pr_nice', c_char),
    ('pr_flag', c_ulong),
    ('pr_uid', __pr_uid_t),
    ('pr_gid', __pr_gid_t),
    ('pr_pid', c_int),
    ('pr_ppid', c_int),
    ('pr_pgrp', c_int),
    ('pr_sid', c_int),
    ('pr_fname', c_char * int(16)),
    ('pr_psargs', c_char * int(80)),
]

psaddr_t = POINTER(None)# /usr/include/x86_64-linux-gnu/sys/procfs.h: 104

__prgregset_t = elf_gregset_t# /usr/include/x86_64-linux-gnu/bits/procfs-prregset.h: 24

__prfpregset_t = elf_fpregset_t# /usr/include/x86_64-linux-gnu/bits/procfs-prregset.h: 25

prgregset_t = __prgregset_t# /usr/include/x86_64-linux-gnu/sys/procfs.h: 109

prfpregset_t = __prfpregset_t# /usr/include/x86_64-linux-gnu/sys/procfs.h: 110

lwpid_t = __pid_t# /usr/include/x86_64-linux-gnu/sys/procfs.h: 114

prstatus_t = struct_elf_prstatus# /usr/include/x86_64-linux-gnu/sys/procfs.h: 117

prpsinfo_t = struct_elf_prpsinfo# /usr/include/x86_64-linux-gnu/sys/procfs.h: 118

# /usr/include/x86_64-linux-gnu/sys/profil.h: 37
class struct_prof(Structure):
    pass

struct_prof.__slots__ = [
    'pr_base',
    'pr_size',
    'pr_off',
    'pr_scale',
]
struct_prof._fields_ = [
    ('pr_base', POINTER(None)),
    ('pr_size', c_size_t),
    ('pr_off', c_size_t),
    ('pr_scale', c_ulong),
]

enum_anon_116 = c_int# /usr/include/x86_64-linux-gnu/sys/profil.h: 45

PROF_USHORT = 0# /usr/include/x86_64-linux-gnu/sys/profil.h: 45

PROF_UINT = (1 << 0)# /usr/include/x86_64-linux-gnu/sys/profil.h: 45

PROF_FAST = (1 << 1)# /usr/include/x86_64-linux-gnu/sys/profil.h: 45

# /usr/include/x86_64-linux-gnu/sys/profil.h: 55
if _libs["libc.so.6"].has("sprofil", "cdecl"):
    sprofil = _libs["libc.so.6"].get("sprofil", "cdecl")
    sprofil.argtypes = [POINTER(struct_prof), c_int, POINTER(struct_timeval), c_uint]
    sprofil.restype = c_int

enum___ptrace_request = c_int# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_TRACEME = 0# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_PEEKTEXT = 1# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_PEEKDATA = 2# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_PEEKUSER = 3# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_POKETEXT = 4# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_POKEDATA = 5# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_POKEUSER = 6# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_CONT = 7# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_KILL = 8# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SINGLESTEP = 9# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETREGS = 12# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETREGS = 13# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETFPREGS = 14# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETFPREGS = 15# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_ATTACH = 16# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_DETACH = 17# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETFPXREGS = 18# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETFPXREGS = 19# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SYSCALL = 24# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GET_THREAD_AREA = 25# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SET_THREAD_AREA = 26# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_ARCH_PRCTL = 30# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SYSEMU = 31# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SYSEMU_SINGLESTEP = 32# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SINGLEBLOCK = 33# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETOPTIONS = 0x4200# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETEVENTMSG = 0x4201# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETSIGINFO = 0x4202# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETSIGINFO = 0x4203# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETREGSET = 0x4204# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETREGSET = 0x4205# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SEIZE = 0x4206# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_INTERRUPT = 0x4207# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_LISTEN = 0x4208# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_PEEKSIGINFO = 0x4209# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GETSIGMASK = 0x420a# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SETSIGMASK = 0x420b# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SECCOMP_GET_FILTER = 0x420c# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_SECCOMP_GET_METADATA = 0x420d# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

PTRACE_GET_SYSCALL_INFO = 0x420e# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 29

enum_anon_121 = c_int# /usr/include/linux/quota.h: 90

QIF_BLIMITS_B = 0# /usr/include/linux/quota.h: 90

QIF_SPACE_B = (QIF_BLIMITS_B + 1)# /usr/include/linux/quota.h: 90

QIF_ILIMITS_B = (QIF_SPACE_B + 1)# /usr/include/linux/quota.h: 90

QIF_INODES_B = (QIF_ILIMITS_B + 1)# /usr/include/linux/quota.h: 90

QIF_BTIME_B = (QIF_INODES_B + 1)# /usr/include/linux/quota.h: 90

QIF_ITIME_B = (QIF_BTIME_B + 1)# /usr/include/linux/quota.h: 90

# /usr/include/linux/quota.h: 110
class struct_if_dqblk(Structure):
    pass

struct_if_dqblk.__slots__ = [
    'dqb_bhardlimit',
    'dqb_bsoftlimit',
    'dqb_curspace',
    'dqb_ihardlimit',
    'dqb_isoftlimit',
    'dqb_curinodes',
    'dqb_btime',
    'dqb_itime',
    'dqb_valid',
]
struct_if_dqblk._fields_ = [
    ('dqb_bhardlimit', __u64),
    ('dqb_bsoftlimit', __u64),
    ('dqb_curspace', __u64),
    ('dqb_ihardlimit', __u64),
    ('dqb_isoftlimit', __u64),
    ('dqb_curinodes', __u64),
    ('dqb_btime', __u64),
    ('dqb_itime', __u64),
    ('dqb_valid', __u32),
]

# /usr/include/linux/quota.h: 122
class struct_if_nextdqblk(Structure):
    pass

struct_if_nextdqblk.__slots__ = [
    'dqb_bhardlimit',
    'dqb_bsoftlimit',
    'dqb_curspace',
    'dqb_ihardlimit',
    'dqb_isoftlimit',
    'dqb_curinodes',
    'dqb_btime',
    'dqb_itime',
    'dqb_valid',
    'dqb_id',
]
struct_if_nextdqblk._fields_ = [
    ('dqb_bhardlimit', __u64),
    ('dqb_bsoftlimit', __u64),
    ('dqb_curspace', __u64),
    ('dqb_ihardlimit', __u64),
    ('dqb_isoftlimit', __u64),
    ('dqb_curinodes', __u64),
    ('dqb_btime', __u64),
    ('dqb_itime', __u64),
    ('dqb_valid', __u32),
    ('dqb_id', __u32),
]

enum_anon_122 = c_int# /usr/include/linux/quota.h: 144

DQF_ROOT_SQUASH_B = 0# /usr/include/linux/quota.h: 144

DQF_SYS_FILE_B = 16# /usr/include/linux/quota.h: 144

DQF_PRIVATE = (DQF_SYS_FILE_B + 1)# /usr/include/linux/quota.h: 144

# /usr/include/linux/quota.h: 156
class struct_if_dqinfo(Structure):
    pass

struct_if_dqinfo.__slots__ = [
    'dqi_bgrace',
    'dqi_igrace',
    'dqi_flags',
    'dqi_valid',
]
struct_if_dqinfo._fields_ = [
    ('dqi_bgrace', __u64),
    ('dqi_igrace', __u64),
    ('dqi_flags', __u32),
    ('dqi_valid', __u32),
]

enum_anon_123 = c_int# /usr/include/linux/quota.h: 178

QUOTA_NL_C_UNSPEC = 0# /usr/include/linux/quota.h: 178

QUOTA_NL_C_WARNING = (QUOTA_NL_C_UNSPEC + 1)# /usr/include/linux/quota.h: 178

__QUOTA_NL_C_MAX = (QUOTA_NL_C_WARNING + 1)# /usr/include/linux/quota.h: 178

enum_anon_124 = c_int# /usr/include/linux/quota.h: 185

QUOTA_NL_A_UNSPEC = 0# /usr/include/linux/quota.h: 185

QUOTA_NL_A_QTYPE = (QUOTA_NL_A_UNSPEC + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_EXCESS_ID = (QUOTA_NL_A_QTYPE + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_WARNING = (QUOTA_NL_A_EXCESS_ID + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_DEV_MAJOR = (QUOTA_NL_A_WARNING + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_DEV_MINOR = (QUOTA_NL_A_DEV_MAJOR + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_CAUSED_ID = (QUOTA_NL_A_DEV_MINOR + 1)# /usr/include/linux/quota.h: 185

QUOTA_NL_A_PAD = (QUOTA_NL_A_CAUSED_ID + 1)# /usr/include/linux/quota.h: 185

__QUOTA_NL_A_MAX = (QUOTA_NL_A_PAD + 1)# /usr/include/linux/quota.h: 185

# /usr/include/x86_64-linux-gnu/sys/quota.h: 91
class struct_dqblk(Structure):
    pass

struct_dqblk.__slots__ = [
    'dqb_bhardlimit',
    'dqb_bsoftlimit',
    'dqb_curspace',
    'dqb_ihardlimit',
    'dqb_isoftlimit',
    'dqb_curinodes',
    'dqb_btime',
    'dqb_itime',
    'dqb_valid',
]
struct_dqblk._fields_ = [
    ('dqb_bhardlimit', __uint64_t),
    ('dqb_bsoftlimit', __uint64_t),
    ('dqb_curspace', __uint64_t),
    ('dqb_ihardlimit', __uint64_t),
    ('dqb_isoftlimit', __uint64_t),
    ('dqb_curinodes', __uint64_t),
    ('dqb_btime', __uint64_t),
    ('dqb_itime', __uint64_t),
    ('dqb_valid', __uint32_t),
]

# /usr/include/x86_64-linux-gnu/sys/quota.h: 120
class struct_dqinfo(Structure):
    pass

struct_dqinfo.__slots__ = [
    'dqi_bgrace',
    'dqi_igrace',
    'dqi_flags',
    'dqi_valid',
]
struct_dqinfo._fields_ = [
    ('dqi_bgrace', __uint64_t),
    ('dqi_igrace', __uint64_t),
    ('dqi_flags', __uint32_t),
    ('dqi_valid', __uint32_t),
]

# /usr/include/x86_64-linux-gnu/sys/quota.h: 130
if _libs["libc.so.6"].has("quotactl", "cdecl"):
    quotactl = _libs["libc.so.6"].get("quotactl", "cdecl")
    quotactl.argtypes = [c_int, String, c_int, __caddr_t]
    quotactl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/random.h: 33
if _libs["libc.so.6"].has("getrandom", "cdecl"):
    getrandom = _libs["libc.so.6"].get("getrandom", "cdecl")
    getrandom.argtypes = [POINTER(None), c_size_t, c_uint]
    getrandom.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/random.h: 38
if _libs["libc.so.6"].has("getentropy", "cdecl"):
    getentropy = _libs["libc.so.6"].get("getentropy", "cdecl")
    getentropy.argtypes = [POINTER(None), c_size_t]
    getentropy.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/raw.h: 31
class struct_raw_config_request(Structure):
    pass

struct_raw_config_request.__slots__ = [
    'raw_minor',
    'block_major',
    'block_minor',
]
struct_raw_config_request._fields_ = [
    ('raw_minor', c_int),
    ('block_major', c_uint64),
    ('block_minor', c_uint64),
]

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 50
if _libs["libc.so.6"].has("reboot", "cdecl"):
    reboot = _libs["libc.so.6"].get("reboot", "cdecl")
    reboot.argtypes = [c_int]
    reboot.restype = c_int

enum___rlimit_resource = c_int# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_CPU = 0# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_FSIZE = 1# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_DATA = 2# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_STACK = 3# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_CORE = 4# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_RSS = 5# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_NOFILE = 7# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_OFILE = RLIMIT_NOFILE# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

RLIMIT_AS = 9# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_NPROC = 6# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_MEMLOCK = 8# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_LOCKS = 10# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_SIGPENDING = 11# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_MSGQUEUE = 12# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_NICE = 13# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_RTPRIO = 14# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_RTTIME = 15# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIMIT_NLIMITS = 16# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

__RLIM_NLIMITS = __RLIMIT_NLIMITS# /usr/include/x86_64-linux-gnu/bits/resource.h: 31

rlim_t = __rlim_t# /usr/include/x86_64-linux-gnu/bits/resource.h: 131

# /usr/include/x86_64-linux-gnu/bits/resource.h: 139
class struct_rlimit(Structure):
    pass

struct_rlimit.__slots__ = [
    'rlim_cur',
    'rlim_max',
]
struct_rlimit._fields_ = [
    ('rlim_cur', rlim_t),
    ('rlim_max', rlim_t),
]

enum___rusage_who = c_int# /usr/include/x86_64-linux-gnu/bits/resource.h: 158

RUSAGE_SELF = 0# /usr/include/x86_64-linux-gnu/bits/resource.h: 158

RUSAGE_CHILDREN = (-1)# /usr/include/x86_64-linux-gnu/bits/resource.h: 158

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 40
class union_anon_125(Union):
    pass

union_anon_125.__slots__ = [
    'ru_maxrss',
    '__ru_maxrss_word',
]
union_anon_125._fields_ = [
    ('ru_maxrss', c_long),
    ('__ru_maxrss_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 47
class union_anon_126(Union):
    pass

union_anon_126.__slots__ = [
    'ru_ixrss',
    '__ru_ixrss_word',
]
union_anon_126._fields_ = [
    ('ru_ixrss', c_long),
    ('__ru_ixrss_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 53
class union_anon_127(Union):
    pass

union_anon_127.__slots__ = [
    'ru_idrss',
    '__ru_idrss_word',
]
union_anon_127._fields_ = [
    ('ru_idrss', c_long),
    ('__ru_idrss_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 59
class union_anon_128(Union):
    pass

union_anon_128.__slots__ = [
    'ru_isrss',
    '__ru_isrss_word',
]
union_anon_128._fields_ = [
    ('ru_isrss', c_long),
    ('__ru_isrss_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 66
class union_anon_129(Union):
    pass

union_anon_129.__slots__ = [
    'ru_minflt',
    '__ru_minflt_word',
]
union_anon_129._fields_ = [
    ('ru_minflt', c_long),
    ('__ru_minflt_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 72
class union_anon_130(Union):
    pass

union_anon_130.__slots__ = [
    'ru_majflt',
    '__ru_majflt_word',
]
union_anon_130._fields_ = [
    ('ru_majflt', c_long),
    ('__ru_majflt_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 78
class union_anon_131(Union):
    pass

union_anon_131.__slots__ = [
    'ru_nswap',
    '__ru_nswap_word',
]
union_anon_131._fields_ = [
    ('ru_nswap', c_long),
    ('__ru_nswap_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 85
class union_anon_132(Union):
    pass

union_anon_132.__slots__ = [
    'ru_inblock',
    '__ru_inblock_word',
]
union_anon_132._fields_ = [
    ('ru_inblock', c_long),
    ('__ru_inblock_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 91
class union_anon_133(Union):
    pass

union_anon_133.__slots__ = [
    'ru_oublock',
    '__ru_oublock_word',
]
union_anon_133._fields_ = [
    ('ru_oublock', c_long),
    ('__ru_oublock_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 97
class union_anon_134(Union):
    pass

union_anon_134.__slots__ = [
    'ru_msgsnd',
    '__ru_msgsnd_word',
]
union_anon_134._fields_ = [
    ('ru_msgsnd', c_long),
    ('__ru_msgsnd_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 103
class union_anon_135(Union):
    pass

union_anon_135.__slots__ = [
    'ru_msgrcv',
    '__ru_msgrcv_word',
]
union_anon_135._fields_ = [
    ('ru_msgrcv', c_long),
    ('__ru_msgrcv_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 109
class union_anon_136(Union):
    pass

union_anon_136.__slots__ = [
    'ru_nsignals',
    '__ru_nsignals_word',
]
union_anon_136._fields_ = [
    ('ru_nsignals', c_long),
    ('__ru_nsignals_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 117
class union_anon_137(Union):
    pass

union_anon_137.__slots__ = [
    'ru_nvcsw',
    '__ru_nvcsw_word',
]
union_anon_137._fields_ = [
    ('ru_nvcsw', c_long),
    ('__ru_nvcsw_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 124
class union_anon_138(Union):
    pass

union_anon_138.__slots__ = [
    'ru_nivcsw',
    '__ru_nivcsw_word',
]
union_anon_138._fields_ = [
    ('ru_nivcsw', c_long),
    ('__ru_nivcsw_word', __syscall_slong_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_rusage.h: 33
class struct_rusage(Structure):
    pass

struct_rusage.__slots__ = [
    'ru_utime',
    'ru_stime',
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
    'unnamed_7',
    'unnamed_8',
    'unnamed_9',
    'unnamed_10',
    'unnamed_11',
    'unnamed_12',
    'unnamed_13',
    'unnamed_14',
]
struct_rusage._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
    'unnamed_7',
    'unnamed_8',
    'unnamed_9',
    'unnamed_10',
    'unnamed_11',
    'unnamed_12',
    'unnamed_13',
    'unnamed_14',
]
struct_rusage._fields_ = [
    ('ru_utime', struct_timeval),
    ('ru_stime', struct_timeval),
    ('unnamed_1', union_anon_125),
    ('unnamed_2', union_anon_126),
    ('unnamed_3', union_anon_127),
    ('unnamed_4', union_anon_128),
    ('unnamed_5', union_anon_129),
    ('unnamed_6', union_anon_130),
    ('unnamed_7', union_anon_131),
    ('unnamed_8', union_anon_132),
    ('unnamed_9', union_anon_133),
    ('unnamed_10', union_anon_134),
    ('unnamed_11', union_anon_135),
    ('unnamed_12', union_anon_136),
    ('unnamed_13', union_anon_137),
    ('unnamed_14', union_anon_138),
]

enum___priority_which = c_int# /usr/include/x86_64-linux-gnu/bits/resource.h: 187

PRIO_PROCESS = 0# /usr/include/x86_64-linux-gnu/bits/resource.h: 187

PRIO_PGRP = 1# /usr/include/x86_64-linux-gnu/bits/resource.h: 187

PRIO_USER = 2# /usr/include/x86_64-linux-gnu/bits/resource.h: 187

__rlimit_resource_t = c_int# /usr/include/x86_64-linux-gnu/sys/resource.h: 42

__rusage_who_t = c_int# /usr/include/x86_64-linux-gnu/sys/resource.h: 43

__priority_which_t = c_int# /usr/include/x86_64-linux-gnu/sys/resource.h: 44

# /usr/include/x86_64-linux-gnu/sys/resource.h: 50
if _libs["libc.so.6"].has("getrlimit", "cdecl"):
    getrlimit = _libs["libc.so.6"].get("getrlimit", "cdecl")
    getrlimit.argtypes = [__rlimit_resource_t, POINTER(struct_rlimit)]
    getrlimit.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/resource.h: 69
if _libs["libc.so.6"].has("setrlimit", "cdecl"):
    setrlimit = _libs["libc.so.6"].get("setrlimit", "cdecl")
    setrlimit.argtypes = [__rlimit_resource_t, POINTER(struct_rlimit)]
    setrlimit.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/resource.h: 87
if _libs["libc.so.6"].has("getrusage", "cdecl"):
    getrusage = _libs["libc.so.6"].get("getrusage", "cdecl")
    getrusage.argtypes = [__rusage_who_t, POINTER(struct_rusage)]
    getrusage.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/resource.h: 93
if _libs["libc.so.6"].has("getpriority", "cdecl"):
    getpriority = _libs["libc.so.6"].get("getpriority", "cdecl")
    getpriority.argtypes = [__priority_which_t, id_t]
    getpriority.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/resource.h: 97
if _libs["libc.so.6"].has("setpriority", "cdecl"):
    setpriority = _libs["libc.so.6"].get("setpriority", "cdecl")
    setpriority.argtypes = [__priority_which_t, id_t, c_int]
    setpriority.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/sem.h: 50
class struct_semid_ds(Structure):
    pass

struct_semid_ds.__slots__ = [
    'sem_perm',
    'sem_otime',
    '__glibc_reserved1',
    'sem_ctime',
    '__glibc_reserved2',
    'sem_nsems',
    '__glibc_reserved3',
    '__glibc_reserved4',
]
struct_semid_ds._fields_ = [
    ('sem_perm', struct_ipc_perm),
    ('sem_otime', __time_t),
    ('__glibc_reserved1', __syscall_ulong_t),
    ('sem_ctime', __time_t),
    ('__glibc_reserved2', __syscall_ulong_t),
    ('sem_nsems', __syscall_ulong_t),
    ('__glibc_reserved3', __syscall_ulong_t),
    ('__glibc_reserved4', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/bits/sem.h: 83
class struct_seminfo(Structure):
    pass

struct_seminfo.__slots__ = [
    'semmap',
    'semmni',
    'semmns',
    'semmnu',
    'semmsl',
    'semopm',
    'semume',
    'semusz',
    'semvmx',
    'semaem',
]
struct_seminfo._fields_ = [
    ('semmap', c_int),
    ('semmni', c_int),
    ('semmns', c_int),
    ('semmnu', c_int),
    ('semmsl', c_int),
    ('semopm', c_int),
    ('semume', c_int),
    ('semusz', c_int),
    ('semvmx', c_int),
    ('semaem', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/sem.h: 40
class struct_sembuf(Structure):
    pass

struct_sembuf.__slots__ = [
    'sem_num',
    'sem_op',
    'sem_flg',
]
struct_sembuf._fields_ = [
    ('sem_num', c_uint),
    ('sem_op', c_int),
    ('sem_flg', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/sem.h: 51
if _libs["libc.so.6"].has("semctl", "cdecl"):
    _func = _libs["libc.so.6"].get("semctl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [c_int, c_int, c_int]
    semctl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/x86_64-linux-gnu/sys/sem.h: 54
if _libs["libc.so.6"].has("semget", "cdecl"):
    semget = _libs["libc.so.6"].get("semget", "cdecl")
    semget.argtypes = [key_t, c_int, c_int]
    semget.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/sem.h: 57
if _libs["libc.so.6"].has("semop", "cdecl"):
    semop = _libs["libc.so.6"].get("semop", "cdecl")
    semop.argtypes = [c_int, POINTER(struct_sembuf), c_size_t]
    semop.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/sendfile.h: 33
if _libs["libc.so.6"].has("sendfile", "cdecl"):
    sendfile = _libs["libc.so.6"].get("sendfile", "cdecl")
    sendfile.argtypes = [c_int, c_int, POINTER(off_t), c_size_t]
    sendfile.restype = c_ptrdiff_t

shmatt_t = __syscall_ulong_t# /usr/include/x86_64-linux-gnu/bits/shm.h: 44

# /usr/include/x86_64-linux-gnu/bits/shm.h: 58
class struct_shmid_ds(Structure):
    pass

struct_shmid_ds.__slots__ = [
    'shm_perm',
    'shm_segsz',
    'shm_atime',
    'shm_dtime',
    'shm_ctime',
    'shm_cpid',
    'shm_lpid',
    'shm_nattch',
    '__glibc_reserved5',
    '__glibc_reserved6',
]
struct_shmid_ds._fields_ = [
    ('shm_perm', struct_ipc_perm),
    ('shm_segsz', c_size_t),
    ('shm_atime', __time_t),
    ('shm_dtime', __time_t),
    ('shm_ctime', __time_t),
    ('shm_cpid', __pid_t),
    ('shm_lpid', __pid_t),
    ('shm_nattch', shmatt_t),
    ('__glibc_reserved5', __syscall_ulong_t),
    ('__glibc_reserved6', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/bits/shm.h: 93
class struct_shminfo(Structure):
    pass

struct_shminfo.__slots__ = [
    'shmmax',
    'shmmin',
    'shmmni',
    'shmseg',
    'shmall',
    '__glibc_reserved1',
    '__glibc_reserved2',
    '__glibc_reserved3',
    '__glibc_reserved4',
]
struct_shminfo._fields_ = [
    ('shmmax', __syscall_ulong_t),
    ('shmmin', __syscall_ulong_t),
    ('shmmni', __syscall_ulong_t),
    ('shmseg', __syscall_ulong_t),
    ('shmall', __syscall_ulong_t),
    ('__glibc_reserved1', __syscall_ulong_t),
    ('__glibc_reserved2', __syscall_ulong_t),
    ('__glibc_reserved3', __syscall_ulong_t),
    ('__glibc_reserved4', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/bits/shm.h: 106
class struct_shm_info(Structure):
    pass

struct_shm_info.__slots__ = [
    'used_ids',
    'shm_tot',
    'shm_rss',
    'shm_swp',
    'swap_attempts',
    'swap_successes',
]
struct_shm_info._fields_ = [
    ('used_ids', c_int),
    ('shm_tot', __syscall_ulong_t),
    ('shm_rss', __syscall_ulong_t),
    ('shm_swp', __syscall_ulong_t),
    ('swap_attempts', __syscall_ulong_t),
    ('swap_successes', __syscall_ulong_t),
]

# /usr/include/x86_64-linux-gnu/sys/shm.h: 49
if _libs["libc.so.6"].has("shmctl", "cdecl"):
    shmctl = _libs["libc.so.6"].get("shmctl", "cdecl")
    shmctl.argtypes = [c_int, c_int, POINTER(struct_shmid_ds)]
    shmctl.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/shm.h: 52
if _libs["libc.so.6"].has("shmget", "cdecl"):
    shmget = _libs["libc.so.6"].get("shmget", "cdecl")
    shmget.argtypes = [key_t, c_size_t, c_int]
    shmget.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/shm.h: 55
if _libs["libc.so.6"].has("shmat", "cdecl"):
    shmat = _libs["libc.so.6"].get("shmat", "cdecl")
    shmat.argtypes = [c_int, POINTER(None), c_int]
    shmat.restype = POINTER(c_ubyte)
    shmat.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/x86_64-linux-gnu/sys/shm.h: 59
if _libs["libc.so.6"].has("shmdt", "cdecl"):
    shmdt = _libs["libc.so.6"].get("shmdt", "cdecl")
    shmdt.argtypes = [POINTER(None)]
    shmdt.restype = c_int

enum_anon_139 = c_int# /usr/include/x86_64-linux-gnu/bits/signalfd.h: 23

SFD_CLOEXEC = 0o2000000# /usr/include/x86_64-linux-gnu/bits/signalfd.h: 23

SFD_NONBLOCK = 0o0004000# /usr/include/x86_64-linux-gnu/bits/signalfd.h: 23

# /usr/include/x86_64-linux-gnu/sys/signalfd.h: 27
class struct_signalfd_siginfo(Structure):
    pass

struct_signalfd_siginfo.__slots__ = [
    'ssi_signo',
    'ssi_errno',
    'ssi_code',
    'ssi_pid',
    'ssi_uid',
    'ssi_fd',
    'ssi_tid',
    'ssi_band',
    'ssi_overrun',
    'ssi_trapno',
    'ssi_status',
    'ssi_int',
    'ssi_ptr',
    'ssi_utime',
    'ssi_stime',
    'ssi_addr',
    'ssi_addr_lsb',
    '__pad2',
    'ssi_syscall',
    'ssi_call_addr',
    'ssi_arch',
    '__pad',
]
struct_signalfd_siginfo._fields_ = [
    ('ssi_signo', c_uint32),
    ('ssi_errno', c_int32),
    ('ssi_code', c_int32),
    ('ssi_pid', c_uint32),
    ('ssi_uid', c_uint32),
    ('ssi_fd', c_int32),
    ('ssi_tid', c_uint32),
    ('ssi_band', c_uint32),
    ('ssi_overrun', c_uint32),
    ('ssi_trapno', c_uint32),
    ('ssi_status', c_int32),
    ('ssi_int', c_int32),
    ('ssi_ptr', c_uint64),
    ('ssi_utime', c_uint64),
    ('ssi_stime', c_uint64),
    ('ssi_addr', c_uint64),
    ('ssi_addr_lsb', c_uint16),
    ('__pad2', c_uint16),
    ('ssi_syscall', c_int32),
    ('ssi_call_addr', c_uint64),
    ('ssi_arch', c_uint32),
    ('__pad', c_uint8 * int(28)),
]

# /usr/include/x86_64-linux-gnu/sys/signalfd.h: 57
if _libs["libc.so.6"].has("signalfd", "cdecl"):
    signalfd = _libs["libc.so.6"].get("signalfd", "cdecl")
    signalfd.argtypes = [c_int, POINTER(sigset_t), c_int]
    signalfd.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/types/struct_iovec.h: 26
class struct_iovec(Structure):
    pass

struct_iovec.__slots__ = [
    'iov_base',
    'iov_len',
]
struct_iovec._fields_ = [
    ('iov_base', POINTER(None)),
    ('iov_len', c_size_t),
]

socklen_t = __socklen_t# /usr/include/x86_64-linux-gnu/bits/socket.h: 33

sa_family_t = c_uint# /usr/include/x86_64-linux-gnu/bits/sockaddr.h: 28

# /usr/include/x86_64-linux-gnu/bits/socket.h: 178
class struct_sockaddr(Structure):
    pass

struct_sockaddr.__slots__ = [
    'sa_family',
    'sa_data',
]
struct_sockaddr._fields_ = [
    ('sa_family', sa_family_t),
    ('sa_data', c_char * int(14)),
]

# /usr/include/x86_64-linux-gnu/bits/socket.h: 191
class struct_sockaddr_storage(Structure):
    pass

struct_sockaddr_storage.__slots__ = [
    'ss_family',
    '__ss_padding',
    '__ss_align',
]
struct_sockaddr_storage._fields_ = [
    ('ss_family', sa_family_t),
    ('__ss_padding', c_char * int(((128 - sizeof(c_uint)) - sizeof(c_ulong)))),
    ('__ss_align', c_ulong),
]

enum_anon_140 = c_int# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_OOB = 0x01# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_PEEK = 0x02# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_DONTROUTE = 0x04# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_CTRUNC = 0x08# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_PROXY = 0x10# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_TRUNC = 0x20# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_DONTWAIT = 0x40# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_EOR = 0x80# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_WAITALL = 0x100# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_FIN = 0x200# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_SYN = 0x400# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_CONFIRM = 0x800# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_RST = 0x1000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_ERRQUEUE = 0x2000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_NOSIGNAL = 0x4000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_MORE = 0x8000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_WAITFORONE = 0x10000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_BATCH = 0x40000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_ZEROCOPY = 0x4000000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_FASTOPEN = 0x20000000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

MSG_CMSG_CLOEXEC = 0x40000000# /usr/include/x86_64-linux-gnu/bits/socket.h: 200

# /usr/include/x86_64-linux-gnu/bits/socket.h: 257
class struct_msghdr(Structure):
    pass

struct_msghdr.__slots__ = [
    'msg_name',
    'msg_namelen',
    'msg_iov',
    'msg_iovlen',
    'msg_control',
    'msg_controllen',
    'msg_flags',
]
struct_msghdr._fields_ = [
    ('msg_name', POINTER(None)),
    ('msg_namelen', socklen_t),
    ('msg_iov', POINTER(struct_iovec)),
    ('msg_iovlen', c_size_t),
    ('msg_control', POINTER(None)),
    ('msg_controllen', c_size_t),
    ('msg_flags', c_int),
]

# /usr/include/x86_64-linux-gnu/bits/socket.h: 275
class struct_cmsghdr(Structure):
    pass

struct_cmsghdr.__slots__ = [
    'cmsg_len',
    'cmsg_level',
    'cmsg_type',
    '__cmsg_data',
]
struct_cmsghdr._fields_ = [
    ('cmsg_len', c_size_t),
    ('cmsg_level', c_int),
    ('cmsg_type', c_int),
    ('__cmsg_data', POINTER(c_ubyte)),
]

# /usr/include/x86_64-linux-gnu/bits/socket.h: 305
if _libs["libc.so.6"].has("__cmsg_nxthdr", "cdecl"):
    __cmsg_nxthdr = _libs["libc.so.6"].get("__cmsg_nxthdr", "cdecl")
    __cmsg_nxthdr.argtypes = [POINTER(struct_msghdr), POINTER(struct_cmsghdr)]
    __cmsg_nxthdr.restype = POINTER(struct_cmsghdr)

enum_anon_141 = c_int# /usr/include/x86_64-linux-gnu/bits/socket.h: 332

SCM_RIGHTS = 0x01# /usr/include/x86_64-linux-gnu/bits/socket.h: 332

# /usr/include/x86_64-linux-gnu/bits/socket.h: 361
class struct_linger(Structure):
    pass

struct_linger.__slots__ = [
    'l_onoff',
    'l_linger',
]
struct_linger._fields_ = [
    ('l_onoff', c_int),
    ('l_linger', c_int),
]

enum_anon_142 = c_int# /usr/include/x86_64-linux-gnu/sys/socket.h: 41

SHUT_RD = 0# /usr/include/x86_64-linux-gnu/sys/socket.h: 41

SHUT_WR = (SHUT_RD + 1)# /usr/include/x86_64-linux-gnu/sys/socket.h: 41

SHUT_RDWR = (SHUT_WR + 1)# /usr/include/x86_64-linux-gnu/sys/socket.h: 41

# /usr/include/x86_64-linux-gnu/sys/socket.h: 102
if _libs["libc.so.6"].has("socket", "cdecl"):
    socket = _libs["libc.so.6"].get("socket", "cdecl")
    socket.argtypes = [c_int, c_int, c_int]
    socket.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 108
if _libs["libc.so.6"].has("socketpair", "cdecl"):
    socketpair = _libs["libc.so.6"].get("socketpair", "cdecl")
    socketpair.argtypes = [c_int, c_int, c_int, c_int * int(2)]
    socketpair.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 112
if _libs["libc.so.6"].has("bind", "cdecl"):
    bind = _libs["libc.so.6"].get("bind", "cdecl")
    bind.argtypes = [c_int, POINTER(struct_sockaddr), socklen_t]
    bind.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 116
if _libs["libc.so.6"].has("getsockname", "cdecl"):
    getsockname = _libs["libc.so.6"].get("getsockname", "cdecl")
    getsockname.argtypes = [c_int, POINTER(struct_sockaddr), POINTER(socklen_t)]
    getsockname.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 126
if _libs["libc.so.6"].has("connect", "cdecl"):
    connect = _libs["libc.so.6"].get("connect", "cdecl")
    connect.argtypes = [c_int, POINTER(struct_sockaddr), socklen_t]
    connect.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 130
if _libs["libc.so.6"].has("getpeername", "cdecl"):
    getpeername = _libs["libc.so.6"].get("getpeername", "cdecl")
    getpeername.argtypes = [c_int, POINTER(struct_sockaddr), POINTER(socklen_t)]
    getpeername.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 138
if _libs["libc.so.6"].has("send", "cdecl"):
    send = _libs["libc.so.6"].get("send", "cdecl")
    send.argtypes = [c_int, POINTER(None), c_size_t, c_int]
    send.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 145
if _libs["libc.so.6"].has("recv", "cdecl"):
    recv = _libs["libc.so.6"].get("recv", "cdecl")
    recv.argtypes = [c_int, POINTER(None), c_size_t, c_int]
    recv.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 152
if _libs["libc.so.6"].has("sendto", "cdecl"):
    sendto = _libs["libc.so.6"].get("sendto", "cdecl")
    sendto.argtypes = [c_int, POINTER(None), c_size_t, c_int, POINTER(struct_sockaddr), socklen_t]
    sendto.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 163
if _libs["libc.so.6"].has("recvfrom", "cdecl"):
    recvfrom = _libs["libc.so.6"].get("recvfrom", "cdecl")
    recvfrom.argtypes = [c_int, POINTER(None), c_size_t, c_int, POINTER(struct_sockaddr), POINTER(socklen_t)]
    recvfrom.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 173
if _libs["libc.so.6"].has("sendmsg", "cdecl"):
    sendmsg = _libs["libc.so.6"].get("sendmsg", "cdecl")
    sendmsg.argtypes = [c_int, POINTER(struct_msghdr), c_int]
    sendmsg.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 191
if _libs["libc.so.6"].has("recvmsg", "cdecl"):
    recvmsg = _libs["libc.so.6"].get("recvmsg", "cdecl")
    recvmsg.argtypes = [c_int, POINTER(struct_msghdr), c_int]
    recvmsg.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/socket.h: 208
if _libs["libc.so.6"].has("getsockopt", "cdecl"):
    getsockopt = _libs["libc.so.6"].get("getsockopt", "cdecl")
    getsockopt.argtypes = [c_int, c_int, c_int, POINTER(None), POINTER(socklen_t)]
    getsockopt.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 215
if _libs["libc.so.6"].has("setsockopt", "cdecl"):
    setsockopt = _libs["libc.so.6"].get("setsockopt", "cdecl")
    setsockopt.argtypes = [c_int, c_int, c_int, POINTER(None), socklen_t]
    setsockopt.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 222
if _libs["libc.so.6"].has("listen", "cdecl"):
    listen = _libs["libc.so.6"].get("listen", "cdecl")
    listen.argtypes = [c_int, c_int]
    listen.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 232
if _libs["libc.so.6"].has("accept", "cdecl"):
    accept = _libs["libc.so.6"].get("accept", "cdecl")
    accept.argtypes = [c_int, POINTER(struct_sockaddr), POINTER(socklen_t)]
    accept.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 250
if _libs["libc.so.6"].has("shutdown", "cdecl"):
    shutdown = _libs["libc.so.6"].get("shutdown", "cdecl")
    shutdown.argtypes = [c_int, c_int]
    shutdown.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 255
if _libs["libc.so.6"].has("sockatmark", "cdecl"):
    sockatmark = _libs["libc.so.6"].get("sockatmark", "cdecl")
    sockatmark.argtypes = [c_int]
    sockatmark.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/socket.h: 263
if _libs["libc.so.6"].has("isfdtype", "cdecl"):
    isfdtype = _libs["libc.so.6"].get("isfdtype", "cdecl")
    isfdtype.argtypes = [c_int, c_int]
    isfdtype.restype = c_int

# /usr/include/linux/soundcard.h: 153
class struct_synth_control(Structure):
    pass

struct_synth_control.__slots__ = [
    'devno',
    'data',
]
struct_synth_control._fields_ = [
    ('devno', c_int),
    ('data', c_char * int(4000)),
]

synth_control = struct_synth_control# /usr/include/linux/soundcard.h: 153

# /usr/include/linux/soundcard.h: 160
class struct_remove_sample(Structure):
    pass

struct_remove_sample.__slots__ = [
    'devno',
    'bankno',
    'instrno',
]
struct_remove_sample._fields_ = [
    ('devno', c_int),
    ('bankno', c_int),
    ('instrno', c_int),
]

remove_sample = struct_remove_sample# /usr/include/linux/soundcard.h: 160

# /usr/include/linux/soundcard.h: 164
class struct_seq_event_rec(Structure):
    pass

struct_seq_event_rec.__slots__ = [
    'arr',
]
struct_seq_event_rec._fields_ = [
    ('arr', c_ubyte * int(8)),
]

seq_event_rec = struct_seq_event_rec# /usr/include/linux/soundcard.h: 164

# /usr/include/linux/soundcard.h: 209
class struct_patch_info(Structure):
    pass

struct_patch_info.__slots__ = [
    'key',
    'device_no',
    'instr_no',
    'mode',
    'len',
    'loop_start',
    'loop_end',
    'base_freq',
    'base_note',
    'high_note',
    'low_note',
    'panning',
    'detuning',
    'env_rate',
    'env_offset',
    'tremolo_sweep',
    'tremolo_rate',
    'tremolo_depth',
    'vibrato_sweep',
    'vibrato_rate',
    'vibrato_depth',
    'scale_frequency',
    'scale_factor',
    'volume',
    'fractions',
    'reserved1',
    'spare',
    'data',
]
struct_patch_info._fields_ = [
    ('key', c_ushort),
    ('device_no', c_short),
    ('instr_no', c_short),
    ('mode', c_uint),
    ('len', c_int),
    ('loop_start', c_int),
    ('loop_end', c_int),
    ('base_freq', c_uint),
    ('base_note', c_uint),
    ('high_note', c_uint),
    ('low_note', c_uint),
    ('panning', c_int),
    ('detuning', c_int),
    ('env_rate', c_ubyte * int(6)),
    ('env_offset', c_ubyte * int(6)),
    ('tremolo_sweep', c_ubyte),
    ('tremolo_rate', c_ubyte),
    ('tremolo_depth', c_ubyte),
    ('vibrato_sweep', c_ubyte),
    ('vibrato_rate', c_ubyte),
    ('vibrato_depth', c_ubyte),
    ('scale_frequency', c_int),
    ('scale_factor', c_uint),
    ('volume', c_int),
    ('fractions', c_int),
    ('reserved1', c_int),
    ('spare', c_int * int(2)),
    ('data', c_char * int(1)),
]

# /usr/include/linux/soundcard.h: 298
class struct_sysex_info(Structure):
    pass

struct_sysex_info.__slots__ = [
    'key',
    'device_no',
    'len',
    'data',
]
struct_sysex_info._fields_ = [
    ('key', c_short),
    ('device_no', c_short),
    ('len', c_int),
    ('data', c_ubyte * int(1)),
]

sbi_instr_data = c_ubyte * int(32)# /usr/include/linux/soundcard.h: 465

# /usr/include/linux/soundcard.h: 467
class struct_sbi_instrument(Structure):
    pass

struct_sbi_instrument.__slots__ = [
    'key',
    'device',
    'channel',
    'operators',
]
struct_sbi_instrument._fields_ = [
    ('key', c_ushort),
    ('device', c_short),
    ('channel', c_int),
    ('operators', sbi_instr_data),
]

# /usr/include/linux/soundcard.h: 476
class struct_synth_info(Structure):
    pass

struct_synth_info.__slots__ = [
    'name',
    'device',
    'synth_type',
    'synth_subtype',
    'perc_mode',
    'nr_voices',
    'nr_drums',
    'instr_bank_size',
    'capabilities',
    'dummies',
]
struct_synth_info._fields_ = [
    ('name', c_char * int(30)),
    ('device', c_int),
    ('synth_type', c_int),
    ('synth_subtype', c_int),
    ('perc_mode', c_int),
    ('nr_voices', c_int),
    ('nr_drums', c_int),
    ('instr_bank_size', c_int),
    ('capabilities', c_uint),
    ('dummies', c_int * int(19)),
]

# /usr/include/linux/soundcard.h: 504
class struct_sound_timer_info(Structure):
    pass

struct_sound_timer_info.__slots__ = [
    'name',
    'caps',
]
struct_sound_timer_info._fields_ = [
    ('name', c_char * int(32)),
    ('caps', c_int),
]

# /usr/include/linux/soundcard.h: 511
class struct_midi_info(Structure):
    pass

struct_midi_info.__slots__ = [
    'name',
    'device',
    'capabilities',
    'dev_type',
    'dummies',
]
struct_midi_info._fields_ = [
    ('name', c_char * int(30)),
    ('device', c_int),
    ('capabilities', c_uint),
    ('dev_type', c_int),
    ('dummies', c_int * int(18)),
]

# /usr/include/linux/soundcard.h: 526
class struct_anon_143(Structure):
    pass

struct_anon_143.__slots__ = [
    'cmd',
    'nr_args',
    'nr_returns',
    'data',
]
struct_anon_143._fields_ = [
    ('cmd', c_ubyte),
    ('nr_args', c_char),
    ('nr_returns', c_char),
    ('data', c_ubyte * int(30)),
]

mpu_command_rec = struct_anon_143# /usr/include/linux/soundcard.h: 526

# /usr/include/linux/soundcard.h: 575
class struct_audio_buf_info(Structure):
    pass

struct_audio_buf_info.__slots__ = [
    'fragments',
    'fragstotal',
    'fragsize',
    'bytes',
]
struct_audio_buf_info._fields_ = [
    ('fragments', c_int),
    ('fragstotal', c_int),
    ('fragsize', c_int),
    ('bytes', c_int),
]

audio_buf_info = struct_audio_buf_info# /usr/include/linux/soundcard.h: 575

# /usr/include/linux/soundcard.h: 606
class struct_count_info(Structure):
    pass

struct_count_info.__slots__ = [
    'bytes',
    'blocks',
    'ptr',
]
struct_count_info._fields_ = [
    ('bytes', c_int),
    ('blocks', c_int),
    ('ptr', c_int),
]

count_info = struct_count_info# /usr/include/linux/soundcard.h: 606

# /usr/include/linux/soundcard.h: 614
class struct_buffmem_desc(Structure):
    pass

struct_buffmem_desc.__slots__ = [
    'buffer',
    'size',
]
struct_buffmem_desc._fields_ = [
    ('buffer', POINTER(c_uint)),
    ('size', c_int),
]

buffmem_desc = struct_buffmem_desc# /usr/include/linux/soundcard.h: 614

# /usr/include/linux/soundcard.h: 703
class struct_copr_buffer(Structure):
    pass

struct_copr_buffer.__slots__ = [
    'command',
    'flags',
    'len',
    'offs',
    'data',
]
struct_copr_buffer._fields_ = [
    ('command', c_int),
    ('flags', c_int),
    ('len', c_int),
    ('offs', c_int),
    ('data', c_ubyte * int(4000)),
]

copr_buffer = struct_copr_buffer# /usr/include/linux/soundcard.h: 703

# /usr/include/linux/soundcard.h: 711
class struct_copr_debug_buf(Structure):
    pass

struct_copr_debug_buf.__slots__ = [
    'command',
    'parm1',
    'parm2',
    'flags',
    'len',
]
struct_copr_debug_buf._fields_ = [
    ('command', c_int),
    ('parm1', c_int),
    ('parm2', c_int),
    ('flags', c_int),
    ('len', c_int),
]

copr_debug_buf = struct_copr_debug_buf# /usr/include/linux/soundcard.h: 711

# /usr/include/linux/soundcard.h: 716
class struct_copr_msg(Structure):
    pass

struct_copr_msg.__slots__ = [
    'len',
    'data',
]
struct_copr_msg._fields_ = [
    ('len', c_int),
    ('data', c_ubyte * int(4000)),
]

copr_msg = struct_copr_msg# /usr/include/linux/soundcard.h: 716

# /usr/include/linux/soundcard.h: 908
class struct_mixer_info(Structure):
    pass

struct_mixer_info.__slots__ = [
    'id',
    'name',
    'modify_counter',
    'fillers',
]
struct_mixer_info._fields_ = [
    ('id', c_char * int(16)),
    ('name', c_char * int(32)),
    ('modify_counter', c_int),
    ('fillers', c_int * int(10)),
]

mixer_info = struct_mixer_info# /usr/include/linux/soundcard.h: 908

# /usr/include/linux/soundcard.h: 914
class struct__old_mixer_info(Structure):
    pass

struct__old_mixer_info.__slots__ = [
    'id',
    'name',
]
struct__old_mixer_info._fields_ = [
    ('id', c_char * int(16)),
    ('name', c_char * int(32)),
]

_old_mixer_info = struct__old_mixer_info# /usr/include/linux/soundcard.h: 914

mixer_record = c_ubyte * int(128)# /usr/include/linux/soundcard.h: 925

# /usr/include/linux/soundcard.h: 957
class struct_mixer_vol_table(Structure):
    pass

struct_mixer_vol_table.__slots__ = [
    'num',
    'name',
    'levels',
]
struct_mixer_vol_table._fields_ = [
    ('num', c_int),
    ('name', c_char * int(32)),
    ('levels', c_int * int(32)),
]

mixer_vol_table = struct_mixer_vol_table# /usr/include/linux/soundcard.h: 957

# /usr/include/linux/soundcard.h: 1054
for _lib in _libs.values():
    if not _lib.has("seqbuf_dump", "cdecl"):
        continue
    seqbuf_dump = _lib.get("seqbuf_dump", "cdecl")
    seqbuf_dump.argtypes = []
    seqbuf_dump.restype = None
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 205
for _lib in _libs.values():
    if not _lib.has("stat", "cdecl"):
        continue
    stat = _lib.get("stat", "cdecl")
    stat.argtypes = [String, POINTER(struct_stat)]
    stat.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 210
for _lib in _libs.values():
    if not _lib.has("fstat", "cdecl"):
        continue
    fstat = _lib.get("fstat", "cdecl")
    fstat.argtypes = [c_int, POINTER(struct_stat)]
    fstat.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 234
for _lib in _libs.values():
    if not _lib.has("fstatat", "cdecl"):
        continue
    fstatat = _lib.get("fstatat", "cdecl")
    fstatat.argtypes = [c_int, String, POINTER(struct_stat), c_int]
    fstatat.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 259
for _lib in _libs.values():
    if not _lib.has("lstat", "cdecl"):
        continue
    lstat = _lib.get("lstat", "cdecl")
    lstat.argtypes = [String, POINTER(struct_stat)]
    lstat.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 280
if _libs["libc.so.6"].has("chmod", "cdecl"):
    chmod = _libs["libc.so.6"].get("chmod", "cdecl")
    chmod.argtypes = [String, __mode_t]
    chmod.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 287
if _libs["libc.so.6"].has("lchmod", "cdecl"):
    lchmod = _libs["libc.so.6"].get("lchmod", "cdecl")
    lchmod.argtypes = [String, __mode_t]
    lchmod.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 293
if _libs["libc.so.6"].has("fchmod", "cdecl"):
    fchmod = _libs["libc.so.6"].get("fchmod", "cdecl")
    fchmod.argtypes = [c_int, __mode_t]
    fchmod.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 299
if _libs["libc.so.6"].has("fchmodat", "cdecl"):
    fchmodat = _libs["libc.so.6"].get("fchmodat", "cdecl")
    fchmodat.argtypes = [c_int, String, __mode_t, c_int]
    fchmodat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 308
if _libs["libc.so.6"].has("umask", "cdecl"):
    umask = _libs["libc.so.6"].get("umask", "cdecl")
    umask.argtypes = [__mode_t]
    umask.restype = __mode_t

# /usr/include/x86_64-linux-gnu/sys/stat.h: 317
if _libs["libc.so.6"].has("mkdir", "cdecl"):
    mkdir = _libs["libc.so.6"].get("mkdir", "cdecl")
    mkdir.argtypes = [String, __mode_t]
    mkdir.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 324
if _libs["libc.so.6"].has("mkdirat", "cdecl"):
    mkdirat = _libs["libc.so.6"].get("mkdirat", "cdecl")
    mkdirat.argtypes = [c_int, String, __mode_t]
    mkdirat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 332
for _lib in _libs.values():
    if not _lib.has("mknod", "cdecl"):
        continue
    mknod = _lib.get("mknod", "cdecl")
    mknod.argtypes = [String, __mode_t, __dev_t]
    mknod.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 339
for _lib in _libs.values():
    if not _lib.has("mknodat", "cdecl"):
        continue
    mknodat = _lib.get("mknodat", "cdecl")
    mknodat.argtypes = [c_int, String, __mode_t, __dev_t]
    mknodat.restype = c_int
    break

# /usr/include/x86_64-linux-gnu/sys/stat.h: 346
if _libs["libc.so.6"].has("mkfifo", "cdecl"):
    mkfifo = _libs["libc.so.6"].get("mkfifo", "cdecl")
    mkfifo.argtypes = [String, __mode_t]
    mkfifo.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 353
if _libs["libc.so.6"].has("mkfifoat", "cdecl"):
    mkfifoat = _libs["libc.so.6"].get("mkfifoat", "cdecl")
    mkfifoat.argtypes = [c_int, String, __mode_t]
    mkfifoat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 360
if _libs["libc.so.6"].has("utimensat", "cdecl"):
    utimensat = _libs["libc.so.6"].get("utimensat", "cdecl")
    utimensat.argtypes = [c_int, String, struct_timespec * int(2), c_int]
    utimensat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 368
if _libs["libc.so.6"].has("futimens", "cdecl"):
    futimens = _libs["libc.so.6"].get("futimens", "cdecl")
    futimens.argtypes = [c_int, struct_timespec * int(2)]
    futimens.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 395
if _libs["libc.so.6"].has("__fxstat", "cdecl"):
    __fxstat = _libs["libc.so.6"].get("__fxstat", "cdecl")
    __fxstat.argtypes = [c_int, c_int, POINTER(struct_stat)]
    __fxstat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 397
if _libs["libc.so.6"].has("__xstat", "cdecl"):
    __xstat = _libs["libc.so.6"].get("__xstat", "cdecl")
    __xstat.argtypes = [c_int, String, POINTER(struct_stat)]
    __xstat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 399
if _libs["libc.so.6"].has("__lxstat", "cdecl"):
    __lxstat = _libs["libc.so.6"].get("__lxstat", "cdecl")
    __lxstat.argtypes = [c_int, String, POINTER(struct_stat)]
    __lxstat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 401
if _libs["libc.so.6"].has("__fxstatat", "cdecl"):
    __fxstatat = _libs["libc.so.6"].get("__fxstatat", "cdecl")
    __fxstatat.argtypes = [c_int, c_int, String, POINTER(struct_stat), c_int]
    __fxstatat.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 438
if _libs["libc.so.6"].has("__xmknod", "cdecl"):
    __xmknod = _libs["libc.so.6"].get("__xmknod", "cdecl")
    __xmknod.argtypes = [c_int, String, __mode_t, POINTER(__dev_t)]
    __xmknod.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/stat.h: 441
if _libs["libc.so.6"].has("__xmknodat", "cdecl"):
    __xmknodat = _libs["libc.so.6"].get("__xmknodat", "cdecl")
    __xmknodat.argtypes = [c_int, c_int, String, __mode_t, POINTER(__dev_t)]
    __xmknodat.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/statfs.h: 24
class struct_statfs(Structure):
    pass

struct_statfs.__slots__ = [
    'f_type',
    'f_bsize',
    'f_blocks',
    'f_bfree',
    'f_bavail',
    'f_files',
    'f_ffree',
    'f_fsid',
    'f_namelen',
    'f_frsize',
    'f_flags',
    'f_spare',
]
struct_statfs._fields_ = [
    ('f_type', __fsword_t),
    ('f_bsize', __fsword_t),
    ('f_blocks', __fsblkcnt_t),
    ('f_bfree', __fsblkcnt_t),
    ('f_bavail', __fsblkcnt_t),
    ('f_files', __fsfilcnt_t),
    ('f_ffree', __fsfilcnt_t),
    ('f_fsid', __fsid_t),
    ('f_namelen', __fsword_t),
    ('f_frsize', __fsword_t),
    ('f_flags', __fsword_t),
    ('f_spare', __fsword_t * int(4)),
]

# /usr/include/x86_64-linux-gnu/sys/statfs.h: 31
if _libs["libc.so.6"].has("statfs", "cdecl"):
    statfs = _libs["libc.so.6"].get("statfs", "cdecl")
    statfs.argtypes = [String, POINTER(struct_statfs)]
    statfs.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/statfs.h: 50
if _libs["libc.so.6"].has("fstatfs", "cdecl"):
    fstatfs = _libs["libc.so.6"].get("fstatfs", "cdecl")
    fstatfs.argtypes = [c_int, POINTER(struct_statfs)]
    fstatfs.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 29
class struct_statvfs(Structure):
    pass

struct_statvfs.__slots__ = [
    'f_bsize',
    'f_frsize',
    'f_blocks',
    'f_bfree',
    'f_bavail',
    'f_files',
    'f_ffree',
    'f_favail',
    'f_fsid',
    'f_flag',
    'f_namemax',
    '__f_spare',
]
struct_statvfs._fields_ = [
    ('f_bsize', c_ulong),
    ('f_frsize', c_ulong),
    ('f_blocks', __fsblkcnt_t),
    ('f_bfree', __fsblkcnt_t),
    ('f_bavail', __fsblkcnt_t),
    ('f_files', __fsfilcnt_t),
    ('f_ffree', __fsfilcnt_t),
    ('f_favail', __fsfilcnt_t),
    ('f_fsid', c_ulong),
    ('f_flag', c_ulong),
    ('f_namemax', c_ulong),
    ('__f_spare', c_int * int(6)),
]

enum_anon_144 = c_int# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 80

ST_RDONLY = 1# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 80

ST_NOSUID = 2# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 80

# /usr/include/x86_64-linux-gnu/sys/statvfs.h: 51
if _libs["libc.so.6"].has("statvfs", "cdecl"):
    statvfs = _libs["libc.so.6"].get("statvfs", "cdecl")
    statvfs.argtypes = [String, POINTER(struct_statvfs)]
    statvfs.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/statvfs.h: 73
if _libs["libc.so.6"].has("fstatvfs", "cdecl"):
    fstatvfs = _libs["libc.so.6"].get("fstatvfs", "cdecl")
    fstatvfs.argtypes = [c_int, POINTER(struct_statvfs)]
    fstatvfs.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/swap.h: 36
if _libs["libc.so.6"].has("swapon", "cdecl"):
    swapon = _libs["libc.so.6"].get("swapon", "cdecl")
    swapon.argtypes = [String, c_int]
    swapon.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/swap.h: 39
if _libs["libc.so.6"].has("swapoff", "cdecl"):
    swapoff = _libs["libc.so.6"].get("swapoff", "cdecl")
    swapoff.argtypes = [String]
    swapoff.restype = c_int

# /usr/include/linux/sysctl.h: 35
class struct___sysctl_args(Structure):
    pass

struct___sysctl_args.__slots__ = [
    'name',
    'nlen',
    'oldval',
    'oldlenp',
    'newval',
    'newlen',
    '__unused',
]
struct___sysctl_args._fields_ = [
    ('name', POINTER(c_int)),
    ('nlen', c_int),
    ('oldval', POINTER(None)),
    ('oldlenp', POINTER(c_size_t)),
    ('newval', POINTER(None)),
    ('newlen', c_size_t),
    ('__unused', c_ulong * int(4)),
]

enum_anon_145 = c_int# /usr/include/linux/sysctl.h: 49

CTL_KERN = 1# /usr/include/linux/sysctl.h: 49

CTL_VM = 2# /usr/include/linux/sysctl.h: 49

CTL_NET = 3# /usr/include/linux/sysctl.h: 49

CTL_PROC = 4# /usr/include/linux/sysctl.h: 49

CTL_FS = 5# /usr/include/linux/sysctl.h: 49

CTL_DEBUG = 6# /usr/include/linux/sysctl.h: 49

CTL_DEV = 7# /usr/include/linux/sysctl.h: 49

CTL_BUS = 8# /usr/include/linux/sysctl.h: 49

CTL_ABI = 9# /usr/include/linux/sysctl.h: 49

CTL_CPU = 10# /usr/include/linux/sysctl.h: 49

CTL_ARLAN = 254# /usr/include/linux/sysctl.h: 49

CTL_S390DBF = 5677# /usr/include/linux/sysctl.h: 49

CTL_SUNRPC = 7249# /usr/include/linux/sysctl.h: 49

CTL_PM = 9899# /usr/include/linux/sysctl.h: 49

CTL_FRV = 9898# /usr/include/linux/sysctl.h: 49

enum_anon_146 = c_int# /usr/include/linux/sysctl.h: 69

CTL_BUS_ISA = 1# /usr/include/linux/sysctl.h: 69

enum_anon_147 = c_int# /usr/include/linux/sysctl.h: 75

INOTIFY_MAX_USER_INSTANCES = 1# /usr/include/linux/sysctl.h: 75

INOTIFY_MAX_USER_WATCHES = 2# /usr/include/linux/sysctl.h: 75

INOTIFY_MAX_QUEUED_EVENTS = 3# /usr/include/linux/sysctl.h: 75

enum_anon_148 = c_int# /usr/include/linux/sysctl.h: 83

KERN_OSTYPE = 1# /usr/include/linux/sysctl.h: 83

KERN_OSRELEASE = 2# /usr/include/linux/sysctl.h: 83

KERN_OSREV = 3# /usr/include/linux/sysctl.h: 83

KERN_VERSION = 4# /usr/include/linux/sysctl.h: 83

KERN_SECUREMASK = 5# /usr/include/linux/sysctl.h: 83

KERN_PROF = 6# /usr/include/linux/sysctl.h: 83

KERN_NODENAME = 7# /usr/include/linux/sysctl.h: 83

KERN_DOMAINNAME = 8# /usr/include/linux/sysctl.h: 83

KERN_PANIC = 15# /usr/include/linux/sysctl.h: 83

KERN_REALROOTDEV = 16# /usr/include/linux/sysctl.h: 83

KERN_SPARC_REBOOT = 21# /usr/include/linux/sysctl.h: 83

KERN_CTLALTDEL = 22# /usr/include/linux/sysctl.h: 83

KERN_PRINTK = 23# /usr/include/linux/sysctl.h: 83

KERN_NAMETRANS = 24# /usr/include/linux/sysctl.h: 83

KERN_PPC_HTABRECLAIM = 25# /usr/include/linux/sysctl.h: 83

KERN_PPC_ZEROPAGED = 26# /usr/include/linux/sysctl.h: 83

KERN_PPC_POWERSAVE_NAP = 27# /usr/include/linux/sysctl.h: 83

KERN_MODPROBE = 28# /usr/include/linux/sysctl.h: 83

KERN_SG_BIG_BUFF = 29# /usr/include/linux/sysctl.h: 83

KERN_ACCT = 30# /usr/include/linux/sysctl.h: 83

KERN_PPC_L2CR = 31# /usr/include/linux/sysctl.h: 83

KERN_RTSIGNR = 32# /usr/include/linux/sysctl.h: 83

KERN_RTSIGMAX = 33# /usr/include/linux/sysctl.h: 83

KERN_SHMMAX = 34# /usr/include/linux/sysctl.h: 83

KERN_MSGMAX = 35# /usr/include/linux/sysctl.h: 83

KERN_MSGMNB = 36# /usr/include/linux/sysctl.h: 83

KERN_MSGPOOL = 37# /usr/include/linux/sysctl.h: 83

KERN_SYSRQ = 38# /usr/include/linux/sysctl.h: 83

KERN_MAX_THREADS = 39# /usr/include/linux/sysctl.h: 83

KERN_RANDOM = 40# /usr/include/linux/sysctl.h: 83

KERN_SHMALL = 41# /usr/include/linux/sysctl.h: 83

KERN_MSGMNI = 42# /usr/include/linux/sysctl.h: 83

KERN_SEM = 43# /usr/include/linux/sysctl.h: 83

KERN_SPARC_STOP_A = 44# /usr/include/linux/sysctl.h: 83

KERN_SHMMNI = 45# /usr/include/linux/sysctl.h: 83

KERN_OVERFLOWUID = 46# /usr/include/linux/sysctl.h: 83

KERN_OVERFLOWGID = 47# /usr/include/linux/sysctl.h: 83

KERN_SHMPATH = 48# /usr/include/linux/sysctl.h: 83

KERN_HOTPLUG = 49# /usr/include/linux/sysctl.h: 83

KERN_IEEE_EMULATION_WARNINGS = 50# /usr/include/linux/sysctl.h: 83

KERN_S390_USER_DEBUG_LOGGING = 51# /usr/include/linux/sysctl.h: 83

KERN_CORE_USES_PID = 52# /usr/include/linux/sysctl.h: 83

KERN_TAINTED = 53# /usr/include/linux/sysctl.h: 83

KERN_CADPID = 54# /usr/include/linux/sysctl.h: 83

KERN_PIDMAX = 55# /usr/include/linux/sysctl.h: 83

KERN_CORE_PATTERN = 56# /usr/include/linux/sysctl.h: 83

KERN_PANIC_ON_OOPS = 57# /usr/include/linux/sysctl.h: 83

KERN_HPPA_PWRSW = 58# /usr/include/linux/sysctl.h: 83

KERN_HPPA_UNALIGNED = 59# /usr/include/linux/sysctl.h: 83

KERN_PRINTK_RATELIMIT = 60# /usr/include/linux/sysctl.h: 83

KERN_PRINTK_RATELIMIT_BURST = 61# /usr/include/linux/sysctl.h: 83

KERN_PTY = 62# /usr/include/linux/sysctl.h: 83

KERN_NGROUPS_MAX = 63# /usr/include/linux/sysctl.h: 83

KERN_SPARC_SCONS_PWROFF = 64# /usr/include/linux/sysctl.h: 83

KERN_HZ_TIMER = 65# /usr/include/linux/sysctl.h: 83

KERN_UNKNOWN_NMI_PANIC = 66# /usr/include/linux/sysctl.h: 83

KERN_BOOTLOADER_TYPE = 67# /usr/include/linux/sysctl.h: 83

KERN_RANDOMIZE = 68# /usr/include/linux/sysctl.h: 83

KERN_SETUID_DUMPABLE = 69# /usr/include/linux/sysctl.h: 83

KERN_SPIN_RETRY = 70# /usr/include/linux/sysctl.h: 83

KERN_ACPI_VIDEO_FLAGS = 71# /usr/include/linux/sysctl.h: 83

KERN_IA64_UNALIGNED = 72# /usr/include/linux/sysctl.h: 83

KERN_COMPAT_LOG = 73# /usr/include/linux/sysctl.h: 83

KERN_MAX_LOCK_DEPTH = 74# /usr/include/linux/sysctl.h: 83

KERN_NMI_WATCHDOG = 75# /usr/include/linux/sysctl.h: 83

KERN_PANIC_ON_NMI = 76# /usr/include/linux/sysctl.h: 83

KERN_PANIC_ON_WARN = 77# /usr/include/linux/sysctl.h: 83

KERN_PANIC_PRINT = 78# /usr/include/linux/sysctl.h: 83

enum_anon_149 = c_int# /usr/include/linux/sysctl.h: 162

VM_UNUSED1 = 1# /usr/include/linux/sysctl.h: 162

VM_UNUSED2 = 2# /usr/include/linux/sysctl.h: 162

VM_UNUSED3 = 3# /usr/include/linux/sysctl.h: 162

VM_UNUSED4 = 4# /usr/include/linux/sysctl.h: 162

VM_OVERCOMMIT_MEMORY = 5# /usr/include/linux/sysctl.h: 162

VM_UNUSED5 = 6# /usr/include/linux/sysctl.h: 162

VM_UNUSED7 = 7# /usr/include/linux/sysctl.h: 162

VM_UNUSED8 = 8# /usr/include/linux/sysctl.h: 162

VM_UNUSED9 = 9# /usr/include/linux/sysctl.h: 162

VM_PAGE_CLUSTER = 10# /usr/include/linux/sysctl.h: 162

VM_DIRTY_BACKGROUND = 11# /usr/include/linux/sysctl.h: 162

VM_DIRTY_RATIO = 12# /usr/include/linux/sysctl.h: 162

VM_DIRTY_WB_CS = 13# /usr/include/linux/sysctl.h: 162

VM_DIRTY_EXPIRE_CS = 14# /usr/include/linux/sysctl.h: 162

VM_NR_PDFLUSH_THREADS = 15# /usr/include/linux/sysctl.h: 162

VM_OVERCOMMIT_RATIO = 16# /usr/include/linux/sysctl.h: 162

VM_PAGEBUF = 17# /usr/include/linux/sysctl.h: 162

VM_HUGETLB_PAGES = 18# /usr/include/linux/sysctl.h: 162

VM_SWAPPINESS = 19# /usr/include/linux/sysctl.h: 162

VM_LOWMEM_RESERVE_RATIO = 20# /usr/include/linux/sysctl.h: 162

VM_MIN_FREE_KBYTES = 21# /usr/include/linux/sysctl.h: 162

VM_MAX_MAP_COUNT = 22# /usr/include/linux/sysctl.h: 162

VM_LAPTOP_MODE = 23# /usr/include/linux/sysctl.h: 162

VM_BLOCK_DUMP = 24# /usr/include/linux/sysctl.h: 162

VM_HUGETLB_GROUP = 25# /usr/include/linux/sysctl.h: 162

VM_VFS_CACHE_PRESSURE = 26# /usr/include/linux/sysctl.h: 162

VM_LEGACY_VA_LAYOUT = 27# /usr/include/linux/sysctl.h: 162

VM_SWAP_TOKEN_TIMEOUT = 28# /usr/include/linux/sysctl.h: 162

VM_DROP_PAGECACHE = 29# /usr/include/linux/sysctl.h: 162

VM_PERCPU_PAGELIST_FRACTION = 30# /usr/include/linux/sysctl.h: 162

VM_ZONE_RECLAIM_MODE = 31# /usr/include/linux/sysctl.h: 162

VM_MIN_UNMAPPED = 32# /usr/include/linux/sysctl.h: 162

VM_PANIC_ON_OOM = 33# /usr/include/linux/sysctl.h: 162

VM_VDSO_ENABLED = 34# /usr/include/linux/sysctl.h: 162

VM_MIN_SLAB = 35# /usr/include/linux/sysctl.h: 162

enum_anon_150 = c_int# /usr/include/linux/sysctl.h: 203

NET_CORE = 1# /usr/include/linux/sysctl.h: 203

NET_ETHER = 2# /usr/include/linux/sysctl.h: 203

NET_802 = 3# /usr/include/linux/sysctl.h: 203

NET_UNIX = 4# /usr/include/linux/sysctl.h: 203

NET_IPV4 = 5# /usr/include/linux/sysctl.h: 203

NET_IPX = 6# /usr/include/linux/sysctl.h: 203

NET_ATALK = 7# /usr/include/linux/sysctl.h: 203

NET_NETROM = 8# /usr/include/linux/sysctl.h: 203

NET_AX25 = 9# /usr/include/linux/sysctl.h: 203

NET_BRIDGE = 10# /usr/include/linux/sysctl.h: 203

NET_ROSE = 11# /usr/include/linux/sysctl.h: 203

NET_IPV6 = 12# /usr/include/linux/sysctl.h: 203

NET_X25 = 13# /usr/include/linux/sysctl.h: 203

NET_TR = 14# /usr/include/linux/sysctl.h: 203

NET_DECNET = 15# /usr/include/linux/sysctl.h: 203

NET_ECONET = 16# /usr/include/linux/sysctl.h: 203

NET_SCTP = 17# /usr/include/linux/sysctl.h: 203

NET_LLC = 18# /usr/include/linux/sysctl.h: 203

NET_NETFILTER = 19# /usr/include/linux/sysctl.h: 203

NET_DCCP = 20# /usr/include/linux/sysctl.h: 203

NET_IRDA = 412# /usr/include/linux/sysctl.h: 203

enum_anon_151 = c_int# /usr/include/linux/sysctl.h: 229

RANDOM_POOLSIZE = 1# /usr/include/linux/sysctl.h: 229

RANDOM_ENTROPY_COUNT = 2# /usr/include/linux/sysctl.h: 229

RANDOM_READ_THRESH = 3# /usr/include/linux/sysctl.h: 229

RANDOM_WRITE_THRESH = 4# /usr/include/linux/sysctl.h: 229

RANDOM_BOOT_ID = 5# /usr/include/linux/sysctl.h: 229

RANDOM_UUID = 6# /usr/include/linux/sysctl.h: 229

enum_anon_152 = c_int# /usr/include/linux/sysctl.h: 240

PTY_MAX = 1# /usr/include/linux/sysctl.h: 240

PTY_NR = 2# /usr/include/linux/sysctl.h: 240

enum_anon_153 = c_int# /usr/include/linux/sysctl.h: 247

BUS_ISA_MEM_BASE = 1# /usr/include/linux/sysctl.h: 247

BUS_ISA_PORT_BASE = 2# /usr/include/linux/sysctl.h: 247

BUS_ISA_PORT_SHIFT = 3# /usr/include/linux/sysctl.h: 247

enum_anon_154 = c_int# /usr/include/linux/sysctl.h: 255

NET_CORE_WMEM_MAX = 1# /usr/include/linux/sysctl.h: 255

NET_CORE_RMEM_MAX = 2# /usr/include/linux/sysctl.h: 255

NET_CORE_WMEM_DEFAULT = 3# /usr/include/linux/sysctl.h: 255

NET_CORE_RMEM_DEFAULT = 4# /usr/include/linux/sysctl.h: 255

NET_CORE_MAX_BACKLOG = 6# /usr/include/linux/sysctl.h: 255

NET_CORE_FASTROUTE = 7# /usr/include/linux/sysctl.h: 255

NET_CORE_MSG_COST = 8# /usr/include/linux/sysctl.h: 255

NET_CORE_MSG_BURST = 9# /usr/include/linux/sysctl.h: 255

NET_CORE_OPTMEM_MAX = 10# /usr/include/linux/sysctl.h: 255

NET_CORE_HOT_LIST_LENGTH = 11# /usr/include/linux/sysctl.h: 255

NET_CORE_DIVERT_VERSION = 12# /usr/include/linux/sysctl.h: 255

NET_CORE_NO_CONG_THRESH = 13# /usr/include/linux/sysctl.h: 255

NET_CORE_NO_CONG = 14# /usr/include/linux/sysctl.h: 255

NET_CORE_LO_CONG = 15# /usr/include/linux/sysctl.h: 255

NET_CORE_MOD_CONG = 16# /usr/include/linux/sysctl.h: 255

NET_CORE_DEV_WEIGHT = 17# /usr/include/linux/sysctl.h: 255

NET_CORE_SOMAXCONN = 18# /usr/include/linux/sysctl.h: 255

NET_CORE_BUDGET = 19# /usr/include/linux/sysctl.h: 255

NET_CORE_AEVENT_ETIME = 20# /usr/include/linux/sysctl.h: 255

NET_CORE_AEVENT_RSEQTH = 21# /usr/include/linux/sysctl.h: 255

NET_CORE_WARNINGS = 22# /usr/include/linux/sysctl.h: 255

enum_anon_155 = c_int# /usr/include/linux/sysctl.h: 287

NET_UNIX_DESTROY_DELAY = 1# /usr/include/linux/sysctl.h: 287

NET_UNIX_DELETE_DELAY = 2# /usr/include/linux/sysctl.h: 287

NET_UNIX_MAX_DGRAM_QLEN = 3# /usr/include/linux/sysctl.h: 287

enum_anon_156 = c_int# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_MAX = 1# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_SYN_SENT = 2# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_SYN_RECV = 3# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_ESTABLISHED = 4# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_FIN_WAIT = 5# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_CLOSE_WAIT = 6# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_LAST_ACK = 7# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_TIME_WAIT = 8# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_CLOSE = 9# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_UDP_TIMEOUT = 10# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_UDP_TIMEOUT_STREAM = 11# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_ICMP_TIMEOUT = 12# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_GENERIC_TIMEOUT = 13# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_BUCKETS = 14# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_LOG_INVALID = 15# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_TIMEOUT_MAX_RETRANS = 16# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_LOOSE = 17# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_BE_LIBERAL = 18# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_TCP_MAX_RETRANS = 19# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_CLOSED = 20# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_WAIT = 21# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_ECHOED = 22# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_ESTABLISHED = 23# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_SENT = 24# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_RECD = 25# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_ACK_SENT = 26# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_COUNT = 27# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_ICMPV6_TIMEOUT = 28# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_FRAG6_TIMEOUT = 29# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_FRAG6_LOW_THRESH = 30# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_FRAG6_HIGH_THRESH = 31# /usr/include/linux/sysctl.h: 295

NET_NF_CONNTRACK_CHECKSUM = 32# /usr/include/linux/sysctl.h: 295

enum_anon_157 = c_int# /usr/include/linux/sysctl.h: 332

NET_IPV4_FORWARD = 8# /usr/include/linux/sysctl.h: 332

NET_IPV4_DYNADDR = 9# /usr/include/linux/sysctl.h: 332

NET_IPV4_CONF = 16# /usr/include/linux/sysctl.h: 332

NET_IPV4_NEIGH = 17# /usr/include/linux/sysctl.h: 332

NET_IPV4_ROUTE = 18# /usr/include/linux/sysctl.h: 332

NET_IPV4_FIB_HASH = 19# /usr/include/linux/sysctl.h: 332

NET_IPV4_NETFILTER = 20# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_TIMESTAMPS = 33# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_WINDOW_SCALING = 34# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_SACK = 35# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_RETRANS_COLLAPSE = 36# /usr/include/linux/sysctl.h: 332

NET_IPV4_DEFAULT_TTL = 37# /usr/include/linux/sysctl.h: 332

NET_IPV4_AUTOCONFIG = 38# /usr/include/linux/sysctl.h: 332

NET_IPV4_NO_PMTU_DISC = 39# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_SYN_RETRIES = 40# /usr/include/linux/sysctl.h: 332

NET_IPV4_IPFRAG_HIGH_THRESH = 41# /usr/include/linux/sysctl.h: 332

NET_IPV4_IPFRAG_LOW_THRESH = 42# /usr/include/linux/sysctl.h: 332

NET_IPV4_IPFRAG_TIME = 43# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_MAX_KA_PROBES = 44# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_KEEPALIVE_TIME = 45# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_KEEPALIVE_PROBES = 46# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_RETRIES1 = 47# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_RETRIES2 = 48# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_FIN_TIMEOUT = 49# /usr/include/linux/sysctl.h: 332

NET_IPV4_IP_MASQ_DEBUG = 50# /usr/include/linux/sysctl.h: 332

NET_TCP_SYNCOOKIES = 51# /usr/include/linux/sysctl.h: 332

NET_TCP_STDURG = 52# /usr/include/linux/sysctl.h: 332

NET_TCP_RFC1337 = 53# /usr/include/linux/sysctl.h: 332

NET_TCP_SYN_TAILDROP = 54# /usr/include/linux/sysctl.h: 332

NET_TCP_MAX_SYN_BACKLOG = 55# /usr/include/linux/sysctl.h: 332

NET_IPV4_LOCAL_PORT_RANGE = 56# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_ECHO_IGNORE_ALL = 57# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_ECHO_IGNORE_BROADCASTS = 58# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_SOURCEQUENCH_RATE = 59# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_DESTUNREACH_RATE = 60# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_TIMEEXCEED_RATE = 61# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_PARAMPROB_RATE = 62# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_ECHOREPLY_RATE = 63# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_IGNORE_BOGUS_ERROR_RESPONSES = 64# /usr/include/linux/sysctl.h: 332

NET_IPV4_IGMP_MAX_MEMBERSHIPS = 65# /usr/include/linux/sysctl.h: 332

NET_TCP_TW_RECYCLE = 66# /usr/include/linux/sysctl.h: 332

NET_IPV4_ALWAYS_DEFRAG = 67# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_KEEPALIVE_INTVL = 68# /usr/include/linux/sysctl.h: 332

NET_IPV4_INET_PEER_THRESHOLD = 69# /usr/include/linux/sysctl.h: 332

NET_IPV4_INET_PEER_MINTTL = 70# /usr/include/linux/sysctl.h: 332

NET_IPV4_INET_PEER_MAXTTL = 71# /usr/include/linux/sysctl.h: 332

NET_IPV4_INET_PEER_GC_MINTIME = 72# /usr/include/linux/sysctl.h: 332

NET_IPV4_INET_PEER_GC_MAXTIME = 73# /usr/include/linux/sysctl.h: 332

NET_TCP_ORPHAN_RETRIES = 74# /usr/include/linux/sysctl.h: 332

NET_TCP_ABORT_ON_OVERFLOW = 75# /usr/include/linux/sysctl.h: 332

NET_TCP_SYNACK_RETRIES = 76# /usr/include/linux/sysctl.h: 332

NET_TCP_MAX_ORPHANS = 77# /usr/include/linux/sysctl.h: 332

NET_TCP_MAX_TW_BUCKETS = 78# /usr/include/linux/sysctl.h: 332

NET_TCP_FACK = 79# /usr/include/linux/sysctl.h: 332

NET_TCP_REORDERING = 80# /usr/include/linux/sysctl.h: 332

NET_TCP_ECN = 81# /usr/include/linux/sysctl.h: 332

NET_TCP_DSACK = 82# /usr/include/linux/sysctl.h: 332

NET_TCP_MEM = 83# /usr/include/linux/sysctl.h: 332

NET_TCP_WMEM = 84# /usr/include/linux/sysctl.h: 332

NET_TCP_RMEM = 85# /usr/include/linux/sysctl.h: 332

NET_TCP_APP_WIN = 86# /usr/include/linux/sysctl.h: 332

NET_TCP_ADV_WIN_SCALE = 87# /usr/include/linux/sysctl.h: 332

NET_IPV4_NONLOCAL_BIND = 88# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_RATELIMIT = 89# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_RATEMASK = 90# /usr/include/linux/sysctl.h: 332

NET_TCP_TW_REUSE = 91# /usr/include/linux/sysctl.h: 332

NET_TCP_FRTO = 92# /usr/include/linux/sysctl.h: 332

NET_TCP_LOW_LATENCY = 93# /usr/include/linux/sysctl.h: 332

NET_IPV4_IPFRAG_SECRET_INTERVAL = 94# /usr/include/linux/sysctl.h: 332

NET_IPV4_IGMP_MAX_MSF = 96# /usr/include/linux/sysctl.h: 332

NET_TCP_NO_METRICS_SAVE = 97# /usr/include/linux/sysctl.h: 332

NET_TCP_DEFAULT_WIN_SCALE = 105# /usr/include/linux/sysctl.h: 332

NET_TCP_MODERATE_RCVBUF = 106# /usr/include/linux/sysctl.h: 332

NET_TCP_TSO_WIN_DIVISOR = 107# /usr/include/linux/sysctl.h: 332

NET_TCP_BIC_BETA = 108# /usr/include/linux/sysctl.h: 332

NET_IPV4_ICMP_ERRORS_USE_INBOUND_IFADDR = 109# /usr/include/linux/sysctl.h: 332

NET_TCP_CONG_CONTROL = 110# /usr/include/linux/sysctl.h: 332

NET_TCP_ABC = 111# /usr/include/linux/sysctl.h: 332

NET_IPV4_IPFRAG_MAX_DIST = 112# /usr/include/linux/sysctl.h: 332

NET_TCP_MTU_PROBING = 113# /usr/include/linux/sysctl.h: 332

NET_TCP_BASE_MSS = 114# /usr/include/linux/sysctl.h: 332

NET_IPV4_TCP_WORKAROUND_SIGNED_WINDOWS = 115# /usr/include/linux/sysctl.h: 332

NET_TCP_DMA_COPYBREAK = 116# /usr/include/linux/sysctl.h: 332

NET_TCP_SLOW_START_AFTER_IDLE = 117# /usr/include/linux/sysctl.h: 332

NET_CIPSOV4_CACHE_ENABLE = 118# /usr/include/linux/sysctl.h: 332

NET_CIPSOV4_CACHE_BUCKET_SIZE = 119# /usr/include/linux/sysctl.h: 332

NET_CIPSOV4_RBM_OPTFMT = 120# /usr/include/linux/sysctl.h: 332

NET_CIPSOV4_RBM_STRICTVALID = 121# /usr/include/linux/sysctl.h: 332

NET_TCP_AVAIL_CONG_CONTROL = 122# /usr/include/linux/sysctl.h: 332

NET_TCP_ALLOWED_CONG_CONTROL = 123# /usr/include/linux/sysctl.h: 332

NET_TCP_MAX_SSTHRESH = 124# /usr/include/linux/sysctl.h: 332

NET_TCP_FRTO_RESPONSE = 125# /usr/include/linux/sysctl.h: 332

enum_anon_158 = c_int# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_FLUSH = 1# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MIN_DELAY = 2# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MAX_DELAY = 3# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_THRESH = 4# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MAX_SIZE = 5# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_MIN_INTERVAL = 6# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_TIMEOUT = 7# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_INTERVAL = 8# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_REDIRECT_LOAD = 9# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_REDIRECT_NUMBER = 10# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_REDIRECT_SILENCE = 11# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_ERROR_COST = 12# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_ERROR_BURST = 13# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_ELASTICITY = 14# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MTU_EXPIRES = 15# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MIN_PMTU = 16# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_MIN_ADVMSS = 17# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_SECRET_INTERVAL = 18# /usr/include/linux/sysctl.h: 431

NET_IPV4_ROUTE_GC_MIN_INTERVAL_MS = 19# /usr/include/linux/sysctl.h: 431

enum_anon_159 = c_int# /usr/include/linux/sysctl.h: 453

NET_PROTO_CONF_ALL = (-2)# /usr/include/linux/sysctl.h: 453

NET_PROTO_CONF_DEFAULT = (-3)# /usr/include/linux/sysctl.h: 453

enum_anon_160 = c_int# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_FORWARDING = 1# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_MC_FORWARDING = 2# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_PROXY_ARP = 3# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ACCEPT_REDIRECTS = 4# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_SECURE_REDIRECTS = 5# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_SEND_REDIRECTS = 6# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_SHARED_MEDIA = 7# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_RP_FILTER = 8# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ACCEPT_SOURCE_ROUTE = 9# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_BOOTP_RELAY = 10# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_LOG_MARTIANS = 11# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_TAG = 12# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ARPFILTER = 13# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_MEDIUM_ID = 14# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_NOXFRM = 15# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_NOPOLICY = 16# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_FORCE_IGMP_VERSION = 17# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ARP_ANNOUNCE = 18# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ARP_IGNORE = 19# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_PROMOTE_SECONDARIES = 20# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ARP_ACCEPT = 21# /usr/include/linux/sysctl.h: 461

NET_IPV4_CONF_ARP_NOTIFY = 22# /usr/include/linux/sysctl.h: 461

enum_anon_161 = c_int# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_MAX = 1# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_SYN_SENT = 2# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_SYN_RECV = 3# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_ESTABLISHED = 4# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_FIN_WAIT = 5# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_CLOSE_WAIT = 6# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_LAST_ACK = 7# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_TIME_WAIT = 8# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_CLOSE = 9# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_UDP_TIMEOUT = 10# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_UDP_TIMEOUT_STREAM = 11# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_ICMP_TIMEOUT = 12# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_GENERIC_TIMEOUT = 13# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_BUCKETS = 14# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_LOG_INVALID = 15# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_MAX_RETRANS = 16# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_LOOSE = 17# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_BE_LIBERAL = 18# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_TCP_MAX_RETRANS = 19# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_CLOSED = 20# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_WAIT = 21# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_ECHOED = 22# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_ESTABLISHED = 23# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_SENT = 24# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_RECD = 25# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_ACK_SENT = 26# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_COUNT = 27# /usr/include/linux/sysctl.h: 488

NET_IPV4_NF_CONNTRACK_CHECKSUM = 28# /usr/include/linux/sysctl.h: 488

enum_anon_162 = c_int# /usr/include/linux/sysctl.h: 521

NET_IPV6_CONF = 16# /usr/include/linux/sysctl.h: 521

NET_IPV6_NEIGH = 17# /usr/include/linux/sysctl.h: 521

NET_IPV6_ROUTE = 18# /usr/include/linux/sysctl.h: 521

NET_IPV6_ICMP = 19# /usr/include/linux/sysctl.h: 521

NET_IPV6_BINDV6ONLY = 20# /usr/include/linux/sysctl.h: 521

NET_IPV6_IP6FRAG_HIGH_THRESH = 21# /usr/include/linux/sysctl.h: 521

NET_IPV6_IP6FRAG_LOW_THRESH = 22# /usr/include/linux/sysctl.h: 521

NET_IPV6_IP6FRAG_TIME = 23# /usr/include/linux/sysctl.h: 521

NET_IPV6_IP6FRAG_SECRET_INTERVAL = 24# /usr/include/linux/sysctl.h: 521

NET_IPV6_MLD_MAX_MSF = 25# /usr/include/linux/sysctl.h: 521

enum_anon_163 = c_int# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_FLUSH = 1# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_THRESH = 2# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_MAX_SIZE = 3# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_MIN_INTERVAL = 4# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_TIMEOUT = 5# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_INTERVAL = 6# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_ELASTICITY = 7# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_MTU_EXPIRES = 8# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_MIN_ADVMSS = 9# /usr/include/linux/sysctl.h: 534

NET_IPV6_ROUTE_GC_MIN_INTERVAL_MS = 10# /usr/include/linux/sysctl.h: 534

enum_anon_164 = c_int# /usr/include/linux/sysctl.h: 547

NET_IPV6_FORWARDING = 1# /usr/include/linux/sysctl.h: 547

NET_IPV6_HOP_LIMIT = 2# /usr/include/linux/sysctl.h: 547

NET_IPV6_MTU = 3# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA = 4# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_REDIRECTS = 5# /usr/include/linux/sysctl.h: 547

NET_IPV6_AUTOCONF = 6# /usr/include/linux/sysctl.h: 547

NET_IPV6_DAD_TRANSMITS = 7# /usr/include/linux/sysctl.h: 547

NET_IPV6_RTR_SOLICITS = 8# /usr/include/linux/sysctl.h: 547

NET_IPV6_RTR_SOLICIT_INTERVAL = 9# /usr/include/linux/sysctl.h: 547

NET_IPV6_RTR_SOLICIT_DELAY = 10# /usr/include/linux/sysctl.h: 547

NET_IPV6_USE_TEMPADDR = 11# /usr/include/linux/sysctl.h: 547

NET_IPV6_TEMP_VALID_LFT = 12# /usr/include/linux/sysctl.h: 547

NET_IPV6_TEMP_PREFERED_LFT = 13# /usr/include/linux/sysctl.h: 547

NET_IPV6_REGEN_MAX_RETRY = 14# /usr/include/linux/sysctl.h: 547

NET_IPV6_MAX_DESYNC_FACTOR = 15# /usr/include/linux/sysctl.h: 547

NET_IPV6_MAX_ADDRESSES = 16# /usr/include/linux/sysctl.h: 547

NET_IPV6_FORCE_MLD_VERSION = 17# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_DEFRTR = 18# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_PINFO = 19# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_RTR_PREF = 20# /usr/include/linux/sysctl.h: 547

NET_IPV6_RTR_PROBE_INTERVAL = 21# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_RT_INFO_MAX_PLEN = 22# /usr/include/linux/sysctl.h: 547

NET_IPV6_PROXY_NDP = 23# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_SOURCE_ROUTE = 25# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_FROM_LOCAL = 26# /usr/include/linux/sysctl.h: 547

NET_IPV6_ACCEPT_RA_RT_INFO_MIN_PLEN = 27# /usr/include/linux/sysctl.h: 547

__NET_IPV6_MAX = (NET_IPV6_ACCEPT_RA_RT_INFO_MIN_PLEN + 1)# /usr/include/linux/sysctl.h: 547

enum_anon_165 = c_int# /usr/include/linux/sysctl.h: 578

NET_IPV6_ICMP_RATELIMIT = 1# /usr/include/linux/sysctl.h: 578

NET_IPV6_ICMP_ECHO_IGNORE_ALL = 2# /usr/include/linux/sysctl.h: 578

enum_anon_166 = c_int# /usr/include/linux/sysctl.h: 584

NET_NEIGH_MCAST_SOLICIT = 1# /usr/include/linux/sysctl.h: 584

NET_NEIGH_UCAST_SOLICIT = 2# /usr/include/linux/sysctl.h: 584

NET_NEIGH_APP_SOLICIT = 3# /usr/include/linux/sysctl.h: 584

NET_NEIGH_RETRANS_TIME = 4# /usr/include/linux/sysctl.h: 584

NET_NEIGH_REACHABLE_TIME = 5# /usr/include/linux/sysctl.h: 584

NET_NEIGH_DELAY_PROBE_TIME = 6# /usr/include/linux/sysctl.h: 584

NET_NEIGH_GC_STALE_TIME = 7# /usr/include/linux/sysctl.h: 584

NET_NEIGH_UNRES_QLEN = 8# /usr/include/linux/sysctl.h: 584

NET_NEIGH_PROXY_QLEN = 9# /usr/include/linux/sysctl.h: 584

NET_NEIGH_ANYCAST_DELAY = 10# /usr/include/linux/sysctl.h: 584

NET_NEIGH_PROXY_DELAY = 11# /usr/include/linux/sysctl.h: 584

NET_NEIGH_LOCKTIME = 12# /usr/include/linux/sysctl.h: 584

NET_NEIGH_GC_INTERVAL = 13# /usr/include/linux/sysctl.h: 584

NET_NEIGH_GC_THRESH1 = 14# /usr/include/linux/sysctl.h: 584

NET_NEIGH_GC_THRESH2 = 15# /usr/include/linux/sysctl.h: 584

NET_NEIGH_GC_THRESH3 = 16# /usr/include/linux/sysctl.h: 584

NET_NEIGH_RETRANS_TIME_MS = 17# /usr/include/linux/sysctl.h: 584

NET_NEIGH_REACHABLE_TIME_MS = 18# /usr/include/linux/sysctl.h: 584

enum_anon_167 = c_int# /usr/include/linux/sysctl.h: 606

NET_DCCP_DEFAULT = 1# /usr/include/linux/sysctl.h: 606

enum_anon_168 = c_int# /usr/include/linux/sysctl.h: 611

NET_IPX_PPROP_BROADCASTING = 1# /usr/include/linux/sysctl.h: 611

NET_IPX_FORWARDING = 2# /usr/include/linux/sysctl.h: 611

enum_anon_169 = c_int# /usr/include/linux/sysctl.h: 617

NET_LLC2 = 1# /usr/include/linux/sysctl.h: 617

NET_LLC_STATION = 2# /usr/include/linux/sysctl.h: 617

enum_anon_170 = c_int# /usr/include/linux/sysctl.h: 623

NET_LLC2_TIMEOUT = 1# /usr/include/linux/sysctl.h: 623

enum_anon_171 = c_int# /usr/include/linux/sysctl.h: 628

NET_LLC_STATION_ACK_TIMEOUT = 1# /usr/include/linux/sysctl.h: 628

enum_anon_172 = c_int# /usr/include/linux/sysctl.h: 633

NET_LLC2_ACK_TIMEOUT = 1# /usr/include/linux/sysctl.h: 633

NET_LLC2_P_TIMEOUT = 2# /usr/include/linux/sysctl.h: 633

NET_LLC2_REJ_TIMEOUT = 3# /usr/include/linux/sysctl.h: 633

NET_LLC2_BUSY_TIMEOUT = 4# /usr/include/linux/sysctl.h: 633

enum_anon_173 = c_int# /usr/include/linux/sysctl.h: 641

NET_ATALK_AARP_EXPIRY_TIME = 1# /usr/include/linux/sysctl.h: 641

NET_ATALK_AARP_TICK_TIME = 2# /usr/include/linux/sysctl.h: 641

NET_ATALK_AARP_RETRANSMIT_LIMIT = 3# /usr/include/linux/sysctl.h: 641

NET_ATALK_AARP_RESOLVE_TIME = 4# /usr/include/linux/sysctl.h: 641

enum_anon_174 = c_int# /usr/include/linux/sysctl.h: 650

NET_NETROM_DEFAULT_PATH_QUALITY = 1# /usr/include/linux/sysctl.h: 650

NET_NETROM_OBSOLESCENCE_COUNT_INITIALISER = 2# /usr/include/linux/sysctl.h: 650

NET_NETROM_NETWORK_TTL_INITIALISER = 3# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_TIMEOUT = 4# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_MAXIMUM_TRIES = 5# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_ACKNOWLEDGE_DELAY = 6# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_BUSY_DELAY = 7# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_REQUESTED_WINDOW_SIZE = 8# /usr/include/linux/sysctl.h: 650

NET_NETROM_TRANSPORT_NO_ACTIVITY_TIMEOUT = 9# /usr/include/linux/sysctl.h: 650

NET_NETROM_ROUTING_CONTROL = 10# /usr/include/linux/sysctl.h: 650

NET_NETROM_LINK_FAILS_COUNT = 11# /usr/include/linux/sysctl.h: 650

NET_NETROM_RESET = 12# /usr/include/linux/sysctl.h: 650

enum_anon_175 = c_int# /usr/include/linux/sysctl.h: 666

NET_AX25_IP_DEFAULT_MODE = 1# /usr/include/linux/sysctl.h: 666

NET_AX25_DEFAULT_MODE = 2# /usr/include/linux/sysctl.h: 666

NET_AX25_BACKOFF_TYPE = 3# /usr/include/linux/sysctl.h: 666

NET_AX25_CONNECT_MODE = 4# /usr/include/linux/sysctl.h: 666

NET_AX25_STANDARD_WINDOW = 5# /usr/include/linux/sysctl.h: 666

NET_AX25_EXTENDED_WINDOW = 6# /usr/include/linux/sysctl.h: 666

NET_AX25_T1_TIMEOUT = 7# /usr/include/linux/sysctl.h: 666

NET_AX25_T2_TIMEOUT = 8# /usr/include/linux/sysctl.h: 666

NET_AX25_T3_TIMEOUT = 9# /usr/include/linux/sysctl.h: 666

NET_AX25_IDLE_TIMEOUT = 10# /usr/include/linux/sysctl.h: 666

NET_AX25_N2 = 11# /usr/include/linux/sysctl.h: 666

NET_AX25_PACLEN = 12# /usr/include/linux/sysctl.h: 666

NET_AX25_PROTOCOL = 13# /usr/include/linux/sysctl.h: 666

NET_AX25_DAMA_SLAVE_TIMEOUT = 14# /usr/include/linux/sysctl.h: 666

enum_anon_176 = c_int# /usr/include/linux/sysctl.h: 684

NET_ROSE_RESTART_REQUEST_TIMEOUT = 1# /usr/include/linux/sysctl.h: 684

NET_ROSE_CALL_REQUEST_TIMEOUT = 2# /usr/include/linux/sysctl.h: 684

NET_ROSE_RESET_REQUEST_TIMEOUT = 3# /usr/include/linux/sysctl.h: 684

NET_ROSE_CLEAR_REQUEST_TIMEOUT = 4# /usr/include/linux/sysctl.h: 684

NET_ROSE_ACK_HOLD_BACK_TIMEOUT = 5# /usr/include/linux/sysctl.h: 684

NET_ROSE_ROUTING_CONTROL = 6# /usr/include/linux/sysctl.h: 684

NET_ROSE_LINK_FAIL_TIMEOUT = 7# /usr/include/linux/sysctl.h: 684

NET_ROSE_MAX_VCS = 8# /usr/include/linux/sysctl.h: 684

NET_ROSE_WINDOW_SIZE = 9# /usr/include/linux/sysctl.h: 684

NET_ROSE_NO_ACTIVITY_TIMEOUT = 10# /usr/include/linux/sysctl.h: 684

enum_anon_177 = c_int# /usr/include/linux/sysctl.h: 698

NET_X25_RESTART_REQUEST_TIMEOUT = 1# /usr/include/linux/sysctl.h: 698

NET_X25_CALL_REQUEST_TIMEOUT = 2# /usr/include/linux/sysctl.h: 698

NET_X25_RESET_REQUEST_TIMEOUT = 3# /usr/include/linux/sysctl.h: 698

NET_X25_CLEAR_REQUEST_TIMEOUT = 4# /usr/include/linux/sysctl.h: 698

NET_X25_ACK_HOLD_BACK_TIMEOUT = 5# /usr/include/linux/sysctl.h: 698

NET_X25_FORWARD = 6# /usr/include/linux/sysctl.h: 698

enum_anon_178 = c_int# /usr/include/linux/sysctl.h: 708

NET_TR_RIF_TIMEOUT = 1# /usr/include/linux/sysctl.h: 708

enum_anon_179 = c_int# /usr/include/linux/sysctl.h: 714

NET_DECNET_NODE_TYPE = 1# /usr/include/linux/sysctl.h: 714

NET_DECNET_NODE_ADDRESS = 2# /usr/include/linux/sysctl.h: 714

NET_DECNET_NODE_NAME = 3# /usr/include/linux/sysctl.h: 714

NET_DECNET_DEFAULT_DEVICE = 4# /usr/include/linux/sysctl.h: 714

NET_DECNET_TIME_WAIT = 5# /usr/include/linux/sysctl.h: 714

NET_DECNET_DN_COUNT = 6# /usr/include/linux/sysctl.h: 714

NET_DECNET_DI_COUNT = 7# /usr/include/linux/sysctl.h: 714

NET_DECNET_DR_COUNT = 8# /usr/include/linux/sysctl.h: 714

NET_DECNET_DST_GC_INTERVAL = 9# /usr/include/linux/sysctl.h: 714

NET_DECNET_CONF = 10# /usr/include/linux/sysctl.h: 714

NET_DECNET_NO_FC_MAX_CWND = 11# /usr/include/linux/sysctl.h: 714

NET_DECNET_MEM = 12# /usr/include/linux/sysctl.h: 714

NET_DECNET_RMEM = 13# /usr/include/linux/sysctl.h: 714

NET_DECNET_WMEM = 14# /usr/include/linux/sysctl.h: 714

NET_DECNET_DEBUG_LEVEL = 255# /usr/include/linux/sysctl.h: 714

enum_anon_180 = c_int# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_LOOPBACK = (-2)# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_DDCMP = (-3)# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_PPP = (-4)# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_X25 = (-5)# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_GRE = (-6)# /usr/include/linux/sysctl.h: 733

NET_DECNET_CONF_ETHER = (-7)# /usr/include/linux/sysctl.h: 733

enum_anon_181 = c_int# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_PRIORITY = 1# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_T1 = 2# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_T2 = 3# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_T3 = 4# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_FORWARDING = 5# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_BLKSIZE = 6# /usr/include/linux/sysctl.h: 745

NET_DECNET_CONF_DEV_STATE = 7# /usr/include/linux/sysctl.h: 745

enum_anon_182 = c_int# /usr/include/linux/sysctl.h: 756

NET_SCTP_RTO_INITIAL = 1# /usr/include/linux/sysctl.h: 756

NET_SCTP_RTO_MIN = 2# /usr/include/linux/sysctl.h: 756

NET_SCTP_RTO_MAX = 3# /usr/include/linux/sysctl.h: 756

NET_SCTP_RTO_ALPHA = 4# /usr/include/linux/sysctl.h: 756

NET_SCTP_RTO_BETA = 5# /usr/include/linux/sysctl.h: 756

NET_SCTP_VALID_COOKIE_LIFE = 6# /usr/include/linux/sysctl.h: 756

NET_SCTP_ASSOCIATION_MAX_RETRANS = 7# /usr/include/linux/sysctl.h: 756

NET_SCTP_PATH_MAX_RETRANS = 8# /usr/include/linux/sysctl.h: 756

NET_SCTP_MAX_INIT_RETRANSMITS = 9# /usr/include/linux/sysctl.h: 756

NET_SCTP_HB_INTERVAL = 10# /usr/include/linux/sysctl.h: 756

NET_SCTP_PRESERVE_ENABLE = 11# /usr/include/linux/sysctl.h: 756

NET_SCTP_MAX_BURST = 12# /usr/include/linux/sysctl.h: 756

NET_SCTP_ADDIP_ENABLE = 13# /usr/include/linux/sysctl.h: 756

NET_SCTP_PRSCTP_ENABLE = 14# /usr/include/linux/sysctl.h: 756

NET_SCTP_SNDBUF_POLICY = 15# /usr/include/linux/sysctl.h: 756

NET_SCTP_SACK_TIMEOUT = 16# /usr/include/linux/sysctl.h: 756

NET_SCTP_RCVBUF_POLICY = 17# /usr/include/linux/sysctl.h: 756

enum_anon_183 = c_int# /usr/include/linux/sysctl.h: 777

NET_BRIDGE_NF_CALL_ARPTABLES = 1# /usr/include/linux/sysctl.h: 777

NET_BRIDGE_NF_CALL_IPTABLES = 2# /usr/include/linux/sysctl.h: 777

NET_BRIDGE_NF_CALL_IP6TABLES = 3# /usr/include/linux/sysctl.h: 777

NET_BRIDGE_NF_FILTER_VLAN_TAGGED = 4# /usr/include/linux/sysctl.h: 777

NET_BRIDGE_NF_FILTER_PPPOE_TAGGED = 5# /usr/include/linux/sysctl.h: 777

enum_anon_184 = c_int# /usr/include/linux/sysctl.h: 787

FS_NRINODE = 1# /usr/include/linux/sysctl.h: 787

FS_STATINODE = 2# /usr/include/linux/sysctl.h: 787

FS_MAXINODE = 3# /usr/include/linux/sysctl.h: 787

FS_NRDQUOT = 4# /usr/include/linux/sysctl.h: 787

FS_MAXDQUOT = 5# /usr/include/linux/sysctl.h: 787

FS_NRFILE = 6# /usr/include/linux/sysctl.h: 787

FS_MAXFILE = 7# /usr/include/linux/sysctl.h: 787

FS_DENTRY = 8# /usr/include/linux/sysctl.h: 787

FS_NRSUPER = 9# /usr/include/linux/sysctl.h: 787

FS_MAXSUPER = 10# /usr/include/linux/sysctl.h: 787

FS_OVERFLOWUID = 11# /usr/include/linux/sysctl.h: 787

FS_OVERFLOWGID = 12# /usr/include/linux/sysctl.h: 787

FS_LEASES = 13# /usr/include/linux/sysctl.h: 787

FS_DIR_NOTIFY = 14# /usr/include/linux/sysctl.h: 787

FS_LEASE_TIME = 15# /usr/include/linux/sysctl.h: 787

FS_DQSTATS = 16# /usr/include/linux/sysctl.h: 787

FS_XFS = 17# /usr/include/linux/sysctl.h: 787

FS_AIO_NR = 18# /usr/include/linux/sysctl.h: 787

FS_AIO_MAX_NR = 19# /usr/include/linux/sysctl.h: 787

FS_INOTIFY = 20# /usr/include/linux/sysctl.h: 787

FS_OCFS2 = 988# /usr/include/linux/sysctl.h: 787

enum_anon_185 = c_int# /usr/include/linux/sysctl.h: 813

FS_DQ_LOOKUPS = 1# /usr/include/linux/sysctl.h: 813

FS_DQ_DROPS = 2# /usr/include/linux/sysctl.h: 813

FS_DQ_READS = 3# /usr/include/linux/sysctl.h: 813

FS_DQ_WRITES = 4# /usr/include/linux/sysctl.h: 813

FS_DQ_CACHE_HITS = 5# /usr/include/linux/sysctl.h: 813

FS_DQ_ALLOCATED = 6# /usr/include/linux/sysctl.h: 813

FS_DQ_FREE = 7# /usr/include/linux/sysctl.h: 813

FS_DQ_SYNCS = 8# /usr/include/linux/sysctl.h: 813

FS_DQ_WARNINGS = 9# /usr/include/linux/sysctl.h: 813

enum_anon_186 = c_int# /usr/include/linux/sysctl.h: 828

DEV_CDROM = 1# /usr/include/linux/sysctl.h: 828

DEV_HWMON = 2# /usr/include/linux/sysctl.h: 828

DEV_PARPORT = 3# /usr/include/linux/sysctl.h: 828

DEV_RAID = 4# /usr/include/linux/sysctl.h: 828

DEV_MAC_HID = 5# /usr/include/linux/sysctl.h: 828

DEV_SCSI = 6# /usr/include/linux/sysctl.h: 828

DEV_IPMI = 7# /usr/include/linux/sysctl.h: 828

enum_anon_187 = c_int# /usr/include/linux/sysctl.h: 839

DEV_CDROM_INFO = 1# /usr/include/linux/sysctl.h: 839

DEV_CDROM_AUTOCLOSE = 2# /usr/include/linux/sysctl.h: 839

DEV_CDROM_AUTOEJECT = 3# /usr/include/linux/sysctl.h: 839

DEV_CDROM_DEBUG = 4# /usr/include/linux/sysctl.h: 839

DEV_CDROM_LOCK = 5# /usr/include/linux/sysctl.h: 839

DEV_CDROM_CHECK_MEDIA = 6# /usr/include/linux/sysctl.h: 839

enum_anon_188 = c_int# /usr/include/linux/sysctl.h: 849

DEV_PARPORT_DEFAULT = (-3)# /usr/include/linux/sysctl.h: 849

enum_anon_189 = c_int# /usr/include/linux/sysctl.h: 854

DEV_RAID_SPEED_LIMIT_MIN = 1# /usr/include/linux/sysctl.h: 854

DEV_RAID_SPEED_LIMIT_MAX = 2# /usr/include/linux/sysctl.h: 854

enum_anon_190 = c_int# /usr/include/linux/sysctl.h: 860

DEV_PARPORT_DEFAULT_TIMESLICE = 1# /usr/include/linux/sysctl.h: 860

DEV_PARPORT_DEFAULT_SPINTIME = 2# /usr/include/linux/sysctl.h: 860

enum_anon_191 = c_int# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_SPINTIME = 1# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_BASE_ADDR = 2# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_IRQ = 3# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_DMA = 4# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_MODES = 5# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_DEVICES = 6# /usr/include/linux/sysctl.h: 866

DEV_PARPORT_AUTOPROBE = 16# /usr/include/linux/sysctl.h: 866

enum_anon_192 = c_int# /usr/include/linux/sysctl.h: 877

DEV_PARPORT_DEVICES_ACTIVE = (-3)# /usr/include/linux/sysctl.h: 877

enum_anon_193 = c_int# /usr/include/linux/sysctl.h: 882

DEV_PARPORT_DEVICE_TIMESLICE = 1# /usr/include/linux/sysctl.h: 882

enum_anon_194 = c_int# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_KEYBOARD_SENDS_LINUX_KEYCODES = 1# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_KEYBOARD_LOCK_KEYCODES = 2# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_MOUSE_BUTTON_EMULATION = 3# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_MOUSE_BUTTON2_KEYCODE = 4# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_MOUSE_BUTTON3_KEYCODE = 5# /usr/include/linux/sysctl.h: 887

DEV_MAC_HID_ADB_MOUSE_SENDS_KEYCODES = 6# /usr/include/linux/sysctl.h: 887

enum_anon_195 = c_int# /usr/include/linux/sysctl.h: 897

DEV_SCSI_LOGGING_LEVEL = 1# /usr/include/linux/sysctl.h: 897

enum_anon_196 = c_int# /usr/include/linux/sysctl.h: 902

DEV_IPMI_POWEROFF_POWERCYCLE = 1# /usr/include/linux/sysctl.h: 902

enum_anon_197 = c_int# /usr/include/linux/sysctl.h: 907

ABI_DEFHANDLER_COFF = 1# /usr/include/linux/sysctl.h: 907

ABI_DEFHANDLER_ELF = 2# /usr/include/linux/sysctl.h: 907

ABI_DEFHANDLER_LCALL7 = 3# /usr/include/linux/sysctl.h: 907

ABI_DEFHANDLER_LIBCSO = 4# /usr/include/linux/sysctl.h: 907

ABI_TRACE = 5# /usr/include/linux/sysctl.h: 907

ABI_FAKE_UTSNAME = 6# /usr/include/linux/sysctl.h: 907

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 70
if _libs["libc.so.6"].has("sysctl", "cdecl"):
    sysctl = _libs["libc.so.6"].get("sysctl", "cdecl")
    sysctl.argtypes = [POINTER(c_int), c_int, POINTER(None), POINTER(c_size_t), POINTER(None), c_size_t]
    sysctl.restype = c_int

# /usr/include/linux/sysinfo.h: 8
class struct_sysinfo(Structure):
    pass

struct_sysinfo.__slots__ = [
    'uptime',
    'loads',
    'totalram',
    'freeram',
    'sharedram',
    'bufferram',
    'totalswap',
    'freeswap',
    'procs',
    'pad',
    'totalhigh',
    'freehigh',
    'mem_unit',
    '_f',
]
struct_sysinfo._fields_ = [
    ('uptime', __kernel_long_t),
    ('loads', __kernel_ulong_t * int(3)),
    ('totalram', __kernel_ulong_t),
    ('freeram', __kernel_ulong_t),
    ('sharedram', __kernel_ulong_t),
    ('bufferram', __kernel_ulong_t),
    ('totalswap', __kernel_ulong_t),
    ('freeswap', __kernel_ulong_t),
    ('procs', __u16),
    ('pad', __u16),
    ('totalhigh', __kernel_ulong_t),
    ('freehigh', __kernel_ulong_t),
    ('mem_unit', __u32),
    ('_f', c_char * int(((20 - (2 * sizeof(__kernel_ulong_t))) - sizeof(__u32)))),
]

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 29
if _libs["libc.so.6"].has("sysinfo", "cdecl"):
    sysinfo = _libs["libc.so.6"].get("sysinfo", "cdecl")
    sysinfo.argtypes = [POINTER(struct_sysinfo)]
    sysinfo.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 33
if _libs["libc.so.6"].has("get_nprocs_conf", "cdecl"):
    get_nprocs_conf = _libs["libc.so.6"].get("get_nprocs_conf", "cdecl")
    get_nprocs_conf.argtypes = []
    get_nprocs_conf.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 36
if _libs["libc.so.6"].has("get_nprocs", "cdecl"):
    get_nprocs = _libs["libc.so.6"].get("get_nprocs", "cdecl")
    get_nprocs.argtypes = []
    get_nprocs.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 40
if _libs["libc.so.6"].has("get_phys_pages", "cdecl"):
    get_phys_pages = _libs["libc.so.6"].get("get_phys_pages", "cdecl")
    get_phys_pages.argtypes = []
    get_phys_pages.restype = c_long

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 43
if _libs["libc.so.6"].has("get_avphys_pages", "cdecl"):
    get_avphys_pages = _libs["libc.so.6"].get("get_avphys_pages", "cdecl")
    get_avphys_pages.argtypes = []
    get_avphys_pages.restype = c_long

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 175
if _libs["libc.so.6"].has("closelog", "cdecl"):
    closelog = _libs["libc.so.6"].get("closelog", "cdecl")
    closelog.argtypes = []
    closelog.restype = None

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 181
if _libs["libc.so.6"].has("openlog", "cdecl"):
    openlog = _libs["libc.so.6"].get("openlog", "cdecl")
    openlog.argtypes = [String, c_int, c_int]
    openlog.restype = None

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 184
if _libs["libc.so.6"].has("setlogmask", "cdecl"):
    setlogmask = _libs["libc.so.6"].get("setlogmask", "cdecl")
    setlogmask.argtypes = [c_int]
    setlogmask.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 190
if _libs["libc.so.6"].has("syslog", "cdecl"):
    _func = _libs["libc.so.6"].get("syslog", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [c_int, String]
    syslog = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 35
if _libs["libc.so.6"].has("gnu_dev_major", "cdecl"):
    gnu_dev_major = _libs["libc.so.6"].get("gnu_dev_major", "cdecl")
    gnu_dev_major.argtypes = [__dev_t]
    gnu_dev_major.restype = c_uint

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 36
if _libs["libc.so.6"].has("gnu_dev_minor", "cdecl"):
    gnu_dev_minor = _libs["libc.so.6"].get("gnu_dev_minor", "cdecl")
    gnu_dev_minor.argtypes = [__dev_t]
    gnu_dev_minor.restype = c_uint

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 37
if _libs["libc.so.6"].has("gnu_dev_makedev", "cdecl"):
    gnu_dev_makedev = _libs["libc.so.6"].get("gnu_dev_makedev", "cdecl")
    gnu_dev_makedev.argtypes = [c_uint, c_uint]
    gnu_dev_makedev.restype = __dev_t

cc_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/termios.h: 23

speed_t = c_uint# /usr/include/x86_64-linux-gnu/bits/termios.h: 24

tcflag_t = c_uint# /usr/include/x86_64-linux-gnu/bits/termios.h: 25

# /usr/include/x86_64-linux-gnu/bits/termios-struct.h: 24
class struct_termios(Structure):
    pass

struct_termios.__slots__ = [
    'c_iflag',
    'c_oflag',
    'c_cflag',
    'c_lflag',
    'c_line',
    'c_cc',
    'c_ispeed',
    'c_ospeed',
]
struct_termios._fields_ = [
    ('c_iflag', tcflag_t),
    ('c_oflag', tcflag_t),
    ('c_cflag', tcflag_t),
    ('c_lflag', tcflag_t),
    ('c_line', cc_t),
    ('c_cc', cc_t * int(32)),
    ('c_ispeed', speed_t),
    ('c_ospeed', speed_t),
]

# /usr/include/termios.h: 48
if _libs["libc.so.6"].has("cfgetospeed", "cdecl"):
    cfgetospeed = _libs["libc.so.6"].get("cfgetospeed", "cdecl")
    cfgetospeed.argtypes = [POINTER(struct_termios)]
    cfgetospeed.restype = speed_t

# /usr/include/termios.h: 51
if _libs["libc.so.6"].has("cfgetispeed", "cdecl"):
    cfgetispeed = _libs["libc.so.6"].get("cfgetispeed", "cdecl")
    cfgetispeed.argtypes = [POINTER(struct_termios)]
    cfgetispeed.restype = speed_t

# /usr/include/termios.h: 54
if _libs["libc.so.6"].has("cfsetospeed", "cdecl"):
    cfsetospeed = _libs["libc.so.6"].get("cfsetospeed", "cdecl")
    cfsetospeed.argtypes = [POINTER(struct_termios), speed_t]
    cfsetospeed.restype = c_int

# /usr/include/termios.h: 57
if _libs["libc.so.6"].has("cfsetispeed", "cdecl"):
    cfsetispeed = _libs["libc.so.6"].get("cfsetispeed", "cdecl")
    cfsetispeed.argtypes = [POINTER(struct_termios), speed_t]
    cfsetispeed.restype = c_int

# /usr/include/termios.h: 61
if _libs["libc.so.6"].has("cfsetspeed", "cdecl"):
    cfsetspeed = _libs["libc.so.6"].get("cfsetspeed", "cdecl")
    cfsetspeed.argtypes = [POINTER(struct_termios), speed_t]
    cfsetspeed.restype = c_int

# /usr/include/termios.h: 66
if _libs["libc.so.6"].has("tcgetattr", "cdecl"):
    tcgetattr = _libs["libc.so.6"].get("tcgetattr", "cdecl")
    tcgetattr.argtypes = [c_int, POINTER(struct_termios)]
    tcgetattr.restype = c_int

# /usr/include/termios.h: 70
if _libs["libc.so.6"].has("tcsetattr", "cdecl"):
    tcsetattr = _libs["libc.so.6"].get("tcsetattr", "cdecl")
    tcsetattr.argtypes = [c_int, c_int, POINTER(struct_termios)]
    tcsetattr.restype = c_int

# /usr/include/termios.h: 76
if _libs["libc.so.6"].has("cfmakeraw", "cdecl"):
    cfmakeraw = _libs["libc.so.6"].get("cfmakeraw", "cdecl")
    cfmakeraw.argtypes = [POINTER(struct_termios)]
    cfmakeraw.restype = None

# /usr/include/termios.h: 80
if _libs["libc.so.6"].has("tcsendbreak", "cdecl"):
    tcsendbreak = _libs["libc.so.6"].get("tcsendbreak", "cdecl")
    tcsendbreak.argtypes = [c_int, c_int]
    tcsendbreak.restype = c_int

# /usr/include/termios.h: 86
if _libs["libc.so.6"].has("tcdrain", "cdecl"):
    tcdrain = _libs["libc.so.6"].get("tcdrain", "cdecl")
    tcdrain.argtypes = [c_int]
    tcdrain.restype = c_int

# /usr/include/termios.h: 90
if _libs["libc.so.6"].has("tcflush", "cdecl"):
    tcflush = _libs["libc.so.6"].get("tcflush", "cdecl")
    tcflush.argtypes = [c_int, c_int]
    tcflush.restype = c_int

# /usr/include/termios.h: 94
if _libs["libc.so.6"].has("tcflow", "cdecl"):
    tcflow = _libs["libc.so.6"].get("tcflow", "cdecl")
    tcflow.argtypes = [c_int, c_int]
    tcflow.restype = c_int

# /usr/include/termios.h: 99
if _libs["libc.so.6"].has("tcgetsid", "cdecl"):
    tcgetsid = _libs["libc.so.6"].get("tcgetsid", "cdecl")
    tcgetsid.argtypes = [c_int]
    tcgetsid.restype = __pid_t

# /usr/include/x86_64-linux-gnu/sys/timeb.h: 29
class struct_timeb(Structure):
    pass

struct_timeb.__slots__ = [
    'time',
    'millitm',
    'timezone',
    'dstflag',
]
struct_timeb._fields_ = [
    ('time', time_t),
    ('millitm', c_uint),
    ('timezone', c_int),
    ('dstflag', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/timeb.h: 39
if _libs["libc.so.6"].has("ftime", "cdecl"):
    ftime = _libs["libc.so.6"].get("ftime", "cdecl")
    ftime.argtypes = [POINTER(struct_timeb)]
    ftime.restype = c_int

# /usr/include/x86_64-linux-gnu/bits/types/struct_tm.h: 7
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_itimerspec.h: 8
class struct_itimerspec(Structure):
    pass

struct_itimerspec.__slots__ = [
    'it_interval',
    'it_value',
]
struct_itimerspec._fields_ = [
    ('it_interval', struct_timespec),
    ('it_value', struct_timespec),
]

# /usr/include/x86_64-linux-gnu/bits/types/__locale_t.h: 31
class struct___locale_data(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/__locale_t.h: 28
class struct___locale_struct(Structure):
    pass

struct___locale_struct.__slots__ = [
    '__locales',
    '__ctype_b',
    '__ctype_tolower',
    '__ctype_toupper',
    '__names',
]
struct___locale_struct._fields_ = [
    ('__locales', POINTER(struct___locale_data) * int(13)),
    ('__ctype_b', POINTER(c_uint)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', POINTER(c_char) * int(13)),
]

__locale_t = POINTER(struct___locale_struct)# /usr/include/x86_64-linux-gnu/bits/types/__locale_t.h: 42

locale_t = __locale_t# /usr/include/x86_64-linux-gnu/bits/types/locale_t.h: 24

# /usr/include/time.h: 72
if _libs["libc.so.6"].has("clock", "cdecl"):
    clock = _libs["libc.so.6"].get("clock", "cdecl")
    clock.argtypes = []
    clock.restype = clock_t

# /usr/include/time.h: 75
if _libs["libc.so.6"].has("time", "cdecl"):
    time = _libs["libc.so.6"].get("time", "cdecl")
    time.argtypes = [POINTER(time_t)]
    time.restype = time_t

# /usr/include/time.h: 78
if _libs["libc.so.6"].has("difftime", "cdecl"):
    difftime = _libs["libc.so.6"].get("difftime", "cdecl")
    difftime.argtypes = [time_t, time_t]
    difftime.restype = c_double

# /usr/include/time.h: 82
if _libs["libc.so.6"].has("mktime", "cdecl"):
    mktime = _libs["libc.so.6"].get("mktime", "cdecl")
    mktime.argtypes = [POINTER(struct_tm)]
    mktime.restype = time_t

# /usr/include/time.h: 88
if _libs["libc.so.6"].has("strftime", "cdecl"):
    strftime = _libs["libc.so.6"].get("strftime", "cdecl")
    strftime.argtypes = [String, c_size_t, String, POINTER(struct_tm)]
    strftime.restype = c_size_t

# /usr/include/time.h: 104
if _libs["libc.so.6"].has("strftime_l", "cdecl"):
    strftime_l = _libs["libc.so.6"].get("strftime_l", "cdecl")
    strftime_l.argtypes = [String, c_size_t, String, POINTER(struct_tm), locale_t]
    strftime_l.restype = c_size_t

# /usr/include/time.h: 119
if _libs["libc.so.6"].has("gmtime", "cdecl"):
    gmtime = _libs["libc.so.6"].get("gmtime", "cdecl")
    gmtime.argtypes = [POINTER(time_t)]
    gmtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 123
if _libs["libc.so.6"].has("localtime", "cdecl"):
    localtime = _libs["libc.so.6"].get("localtime", "cdecl")
    localtime.argtypes = [POINTER(time_t)]
    localtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 128
if _libs["libc.so.6"].has("gmtime_r", "cdecl"):
    gmtime_r = _libs["libc.so.6"].get("gmtime_r", "cdecl")
    gmtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    gmtime_r.restype = POINTER(struct_tm)

# /usr/include/time.h: 133
if _libs["libc.so.6"].has("localtime_r", "cdecl"):
    localtime_r = _libs["libc.so.6"].get("localtime_r", "cdecl")
    localtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    localtime_r.restype = POINTER(struct_tm)

# /usr/include/time.h: 139
if _libs["libc.so.6"].has("asctime", "cdecl"):
    asctime = _libs["libc.so.6"].get("asctime", "cdecl")
    asctime.argtypes = [POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime.restype = ReturnString
    else:
        asctime.restype = String
        asctime.errcheck = ReturnString

# /usr/include/time.h: 142
if _libs["libc.so.6"].has("ctime", "cdecl"):
    ctime = _libs["libc.so.6"].get("ctime", "cdecl")
    ctime.argtypes = [POINTER(time_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime.restype = ReturnString
    else:
        ctime.restype = String
        ctime.errcheck = ReturnString

# /usr/include/time.h: 149
if _libs["libc.so.6"].has("asctime_r", "cdecl"):
    asctime_r = _libs["libc.so.6"].get("asctime_r", "cdecl")
    asctime_r.argtypes = [POINTER(struct_tm), String]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime_r.restype = ReturnString
    else:
        asctime_r.restype = String
        asctime_r.errcheck = ReturnString

# /usr/include/time.h: 153
if _libs["libc.so.6"].has("ctime_r", "cdecl"):
    ctime_r = _libs["libc.so.6"].get("ctime_r", "cdecl")
    ctime_r.argtypes = [POINTER(time_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime_r.restype = ReturnString
    else:
        ctime_r.restype = String
        ctime_r.errcheck = ReturnString

# /usr/include/time.h: 159
try:
    __tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "__tzname")
except:
    pass

# /usr/include/time.h: 160
try:
    __daylight = (c_int).in_dll(_libs["libc.so.6"], "__daylight")
except:
    pass

# /usr/include/time.h: 161
try:
    __timezone = (c_long).in_dll(_libs["libc.so.6"], "__timezone")
except:
    pass

# /usr/include/time.h: 166
try:
    tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "tzname")
except:
    pass

# /usr/include/time.h: 170
if _libs["libc.so.6"].has("tzset", "cdecl"):
    tzset = _libs["libc.so.6"].get("tzset", "cdecl")
    tzset.argtypes = []
    tzset.restype = None

# /usr/include/time.h: 174
try:
    daylight = (c_int).in_dll(_libs["libc.so.6"], "daylight")
except:
    pass

# /usr/include/time.h: 175
try:
    timezone = (c_long).in_dll(_libs["libc.so.6"], "timezone")
except:
    pass

# /usr/include/time.h: 190
if _libs["libc.so.6"].has("timegm", "cdecl"):
    timegm = _libs["libc.so.6"].get("timegm", "cdecl")
    timegm.argtypes = [POINTER(struct_tm)]
    timegm.restype = time_t

# /usr/include/time.h: 193
if _libs["libc.so.6"].has("timelocal", "cdecl"):
    timelocal = _libs["libc.so.6"].get("timelocal", "cdecl")
    timelocal.argtypes = [POINTER(struct_tm)]
    timelocal.restype = time_t

# /usr/include/time.h: 196
if _libs["libc.so.6"].has("dysize", "cdecl"):
    dysize = _libs["libc.so.6"].get("dysize", "cdecl")
    dysize.argtypes = [c_int]
    dysize.restype = c_int

# /usr/include/time.h: 205
if _libs["libc.so.6"].has("nanosleep", "cdecl"):
    nanosleep = _libs["libc.so.6"].get("nanosleep", "cdecl")
    nanosleep.argtypes = [POINTER(struct_timespec), POINTER(struct_timespec)]
    nanosleep.restype = c_int

# /usr/include/time.h: 210
if _libs["libc.so.6"].has("clock_getres", "cdecl"):
    clock_getres = _libs["libc.so.6"].get("clock_getres", "cdecl")
    clock_getres.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_getres.restype = c_int

# /usr/include/time.h: 213
if _libs["libc.so.6"].has("clock_gettime", "cdecl"):
    clock_gettime = _libs["libc.so.6"].get("clock_gettime", "cdecl")
    clock_gettime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_gettime.restype = c_int

# /usr/include/time.h: 216
if _libs["libc.so.6"].has("clock_settime", "cdecl"):
    clock_settime = _libs["libc.so.6"].get("clock_settime", "cdecl")
    clock_settime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_settime.restype = c_int

# /usr/include/time.h: 224
if _libs["libc.so.6"].has("clock_nanosleep", "cdecl"):
    clock_nanosleep = _libs["libc.so.6"].get("clock_nanosleep", "cdecl")
    clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(struct_timespec), POINTER(struct_timespec)]
    clock_nanosleep.restype = c_int

# /usr/include/time.h: 229
if _libs["libc.so.6"].has("clock_getcpuclockid", "cdecl"):
    clock_getcpuclockid = _libs["libc.so.6"].get("clock_getcpuclockid", "cdecl")
    clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
    clock_getcpuclockid.restype = c_int

# /usr/include/time.h: 234
for _lib in _libs.values():
    if not _lib.has("timer_create", "cdecl"):
        continue
    timer_create = _lib.get("timer_create", "cdecl")
    timer_create.argtypes = [clockid_t, POINTER(struct_sigevent), POINTER(timer_t)]
    timer_create.restype = c_int
    break

# /usr/include/time.h: 239
for _lib in _libs.values():
    if not _lib.has("timer_delete", "cdecl"):
        continue
    timer_delete = _lib.get("timer_delete", "cdecl")
    timer_delete.argtypes = [timer_t]
    timer_delete.restype = c_int
    break

# /usr/include/time.h: 242
for _lib in _libs.values():
    if not _lib.has("timer_settime", "cdecl"):
        continue
    timer_settime = _lib.get("timer_settime", "cdecl")
    timer_settime.argtypes = [timer_t, c_int, POINTER(struct_itimerspec), POINTER(struct_itimerspec)]
    timer_settime.restype = c_int
    break

# /usr/include/time.h: 247
for _lib in _libs.values():
    if not _lib.has("timer_gettime", "cdecl"):
        continue
    timer_gettime = _lib.get("timer_gettime", "cdecl")
    timer_gettime.argtypes = [timer_t, POINTER(struct_itimerspec)]
    timer_gettime.restype = c_int
    break

# /usr/include/time.h: 251
for _lib in _libs.values():
    if not _lib.has("timer_getoverrun", "cdecl"):
        continue
    timer_getoverrun = _lib.get("timer_getoverrun", "cdecl")
    timer_getoverrun.argtypes = [timer_t]
    timer_getoverrun.restype = c_int
    break

# /usr/include/time.h: 257
if _libs["libc.so.6"].has("timespec_get", "cdecl"):
    timespec_get = _libs["libc.so.6"].get("timespec_get", "cdecl")
    timespec_get.argtypes = [POINTER(struct_timespec), c_int]
    timespec_get.restype = c_int

enum_anon_198 = c_int# /usr/include/x86_64-linux-gnu/bits/timerfd.h: 23

TFD_CLOEXEC = 0o2000000# /usr/include/x86_64-linux-gnu/bits/timerfd.h: 23

TFD_NONBLOCK = 0o0004000# /usr/include/x86_64-linux-gnu/bits/timerfd.h: 23

enum_anon_199 = c_int# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 29

TFD_TIMER_ABSTIME = (1 << 0)# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 29

TFD_TIMER_CANCEL_ON_SET = (1 << 1)# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 29

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 41
if _libs["libc.so.6"].has("timerfd_create", "cdecl"):
    timerfd_create = _libs["libc.so.6"].get("timerfd_create", "cdecl")
    timerfd_create.argtypes = [__clockid_t, c_int]
    timerfd_create.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 46
if _libs["libc.so.6"].has("timerfd_settime", "cdecl"):
    timerfd_settime = _libs["libc.so.6"].get("timerfd_settime", "cdecl")
    timerfd_settime.argtypes = [c_int, c_int, POINTER(struct_itimerspec), POINTER(struct_itimerspec)]
    timerfd_settime.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 51
if _libs["libc.so.6"].has("timerfd_gettime", "cdecl"):
    timerfd_gettime = _libs["libc.so.6"].get("timerfd_gettime", "cdecl")
    timerfd_gettime.argtypes = [c_int, POINTER(struct_itimerspec)]
    timerfd_gettime.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/times.h: 32
class struct_tms(Structure):
    pass

struct_tms.__slots__ = [
    'tms_utime',
    'tms_stime',
    'tms_cutime',
    'tms_cstime',
]
struct_tms._fields_ = [
    ('tms_utime', clock_t),
    ('tms_stime', clock_t),
    ('tms_cutime', clock_t),
    ('tms_cstime', clock_t),
]

# /usr/include/x86_64-linux-gnu/sys/times.h: 46
if _libs["libc.so.6"].has("times", "cdecl"):
    times = _libs["libc.so.6"].get("times", "cdecl")
    times.argtypes = [POINTER(struct_tms)]
    times.restype = clock_t

# /usr/include/x86_64-linux-gnu/bits/timex.h: 26
class struct_timex(Structure):
    pass

struct_timex.__slots__ = [
    'modes',
    'offset',
    'freq',
    'maxerror',
    'esterror',
    'status',
    'constant',
    'precision',
    'tolerance',
    'time',
    'tick',
    'ppsfreq',
    'jitter',
    'shift',
    'stabil',
    'jitcnt',
    'calcnt',
    'errcnt',
    'stbcnt',
    'tai',
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
    'unnamed_7',
    'unnamed_8',
    'unnamed_9',
    'unnamed_10',
    'unnamed_11',
]
struct_timex._fields_ = [
    ('modes', c_uint),
    ('offset', __syscall_slong_t),
    ('freq', __syscall_slong_t),
    ('maxerror', __syscall_slong_t),
    ('esterror', __syscall_slong_t),
    ('status', c_int),
    ('constant', __syscall_slong_t),
    ('precision', __syscall_slong_t),
    ('tolerance', __syscall_slong_t),
    ('time', struct_timeval),
    ('tick', __syscall_slong_t),
    ('ppsfreq', __syscall_slong_t),
    ('jitter', __syscall_slong_t),
    ('shift', c_int),
    ('stabil', __syscall_slong_t),
    ('jitcnt', __syscall_slong_t),
    ('calcnt', __syscall_slong_t),
    ('errcnt', __syscall_slong_t),
    ('stbcnt', __syscall_slong_t),
    ('tai', c_int),
    ('unnamed_1', c_int, 32),
    ('unnamed_2', c_int, 32),
    ('unnamed_3', c_int, 32),
    ('unnamed_4', c_int, 32),
    ('unnamed_5', c_int, 32),
    ('unnamed_6', c_int, 32),
    ('unnamed_7', c_int, 32),
    ('unnamed_8', c_int, 32),
    ('unnamed_9', c_int, 32),
    ('unnamed_10', c_int, 32),
    ('unnamed_11', c_int, 32),
]

# /usr/include/x86_64-linux-gnu/sys/timex.h: 30
class struct_ntptimeval(Structure):
    pass

struct_ntptimeval.__slots__ = [
    'time',
    'maxerror',
    'esterror',
    'tai',
    '__glibc_reserved1',
    '__glibc_reserved2',
    '__glibc_reserved3',
    '__glibc_reserved4',
]
struct_ntptimeval._fields_ = [
    ('time', struct_timeval),
    ('maxerror', c_long),
    ('esterror', c_long),
    ('tai', c_long),
    ('__glibc_reserved1', c_long),
    ('__glibc_reserved2', c_long),
    ('__glibc_reserved3', c_long),
    ('__glibc_reserved4', c_long),
]

# /usr/include/x86_64-linux-gnu/sys/timex.h: 57
if _libs["libc.so.6"].has("__adjtimex", "cdecl"):
    __adjtimex = _libs["libc.so.6"].get("__adjtimex", "cdecl")
    __adjtimex.argtypes = [POINTER(struct_timex)]
    __adjtimex.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/timex.h: 58
if _libs["libc.so.6"].has("adjtimex", "cdecl"):
    adjtimex = _libs["libc.so.6"].get("adjtimex", "cdecl")
    adjtimex.argtypes = [POINTER(struct_timex)]
    adjtimex.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/timex.h: 64
if _libs["libc.so.6"].has("ntp_gettimex", "cdecl"):
    ntp_gettimex = _libs["libc.so.6"].get("ntp_gettimex", "cdecl")
    ntp_gettimex.argtypes = [POINTER(struct_ntptimeval)]
    ntp_gettimex.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/timex.h: 67
if _libs["libc.so.6"].has("ntp_adjtime", "cdecl"):
    ntp_adjtime = _libs["libc.so.6"].get("ntp_adjtime", "cdecl")
    ntp_adjtime.argtypes = [POINTER(struct_timex)]
    ntp_adjtime.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/ttychars.h: 40
class struct_ttychars(Structure):
    pass

struct_ttychars.__slots__ = [
    'tc_erase',
    'tc_kill',
    'tc_intrc',
    'tc_quitc',
    'tc_startc',
    'tc_stopc',
    'tc_eofc',
    'tc_brkc',
    'tc_suspc',
    'tc_dsuspc',
    'tc_rprntc',
    'tc_flushc',
    'tc_werasc',
    'tc_lnextc',
]
struct_ttychars._fields_ = [
    ('tc_erase', c_char),
    ('tc_kill', c_char),
    ('tc_intrc', c_char),
    ('tc_quitc', c_char),
    ('tc_startc', c_char),
    ('tc_stopc', c_char),
    ('tc_eofc', c_char),
    ('tc_brkc', c_char),
    ('tc_suspc', c_char),
    ('tc_dsuspc', c_char),
    ('tc_rprntc', c_char),
    ('tc_flushc', c_char),
    ('tc_werasc', c_char),
    ('tc_lnextc', c_char),
]

# /usr/include/x86_64-linux-gnu/sys/uio.h: 41
if _libs["libc.so.6"].has("readv", "cdecl"):
    readv = _libs["libc.so.6"].get("readv", "cdecl")
    readv.argtypes = [c_int, POINTER(struct_iovec), c_int]
    readv.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/uio.h: 52
if _libs["libc.so.6"].has("writev", "cdecl"):
    writev = _libs["libc.so.6"].get("writev", "cdecl")
    writev.argtypes = [c_int, POINTER(struct_iovec), c_int]
    writev.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/uio.h: 67
if _libs["libc.so.6"].has("preadv", "cdecl"):
    preadv = _libs["libc.so.6"].get("preadv", "cdecl")
    preadv.argtypes = [c_int, POINTER(struct_iovec), c_int, __off_t]
    preadv.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/uio.h: 79
if _libs["libc.so.6"].has("pwritev", "cdecl"):
    pwritev = _libs["libc.so.6"].get("pwritev", "cdecl")
    pwritev.argtypes = [c_int, POINTER(struct_iovec), c_int, __off_t]
    pwritev.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/un.h: 29
class struct_sockaddr_un(Structure):
    pass

struct_sockaddr_un.__slots__ = [
    'sun_family',
    'sun_path',
]
struct_sockaddr_un._fields_ = [
    ('sun_family', sa_family_t),
    ('sun_path', c_char * int(108)),
]

# /usr/include/string.h: 385
if _libs["libc.so.6"].has("strlen", "cdecl"):
    strlen = _libs["libc.so.6"].get("strlen", "cdecl")
    strlen.argtypes = [String]
    strlen.restype = c_size_t

useconds_t = __useconds_t# /usr/include/unistd.h: 255

# /usr/include/unistd.h: 287
if _libs["libc.so.6"].has("access", "cdecl"):
    access = _libs["libc.so.6"].get("access", "cdecl")
    access.argtypes = [String, c_int]
    access.restype = c_int

# /usr/include/unistd.h: 304
if _libs["libc.so.6"].has("faccessat", "cdecl"):
    faccessat = _libs["libc.so.6"].get("faccessat", "cdecl")
    faccessat.argtypes = [c_int, String, c_int, c_int]
    faccessat.restype = c_int

# /usr/include/unistd.h: 334
if _libs["libc.so.6"].has("lseek", "cdecl"):
    lseek = _libs["libc.so.6"].get("lseek", "cdecl")
    lseek.argtypes = [c_int, __off_t, c_int]
    lseek.restype = __off_t

# /usr/include/unistd.h: 353
if _libs["libc.so.6"].has("close", "cdecl"):
    close = _libs["libc.so.6"].get("close", "cdecl")
    close.argtypes = [c_int]
    close.restype = c_int

# /usr/include/unistd.h: 360
if _libs["libc.so.6"].has("read", "cdecl"):
    read = _libs["libc.so.6"].get("read", "cdecl")
    read.argtypes = [c_int, POINTER(None), c_size_t]
    read.restype = c_ptrdiff_t

# /usr/include/unistd.h: 366
if _libs["libc.so.6"].has("write", "cdecl"):
    write = _libs["libc.so.6"].get("write", "cdecl")
    write.argtypes = [c_int, POINTER(None), c_size_t]
    write.restype = c_ptrdiff_t

# /usr/include/unistd.h: 376
if _libs["libc.so.6"].has("pread", "cdecl"):
    pread = _libs["libc.so.6"].get("pread", "cdecl")
    pread.argtypes = [c_int, POINTER(None), c_size_t, __off_t]
    pread.restype = c_ptrdiff_t

# /usr/include/unistd.h: 384
if _libs["libc.so.6"].has("pwrite", "cdecl"):
    pwrite = _libs["libc.so.6"].get("pwrite", "cdecl")
    pwrite.argtypes = [c_int, POINTER(None), c_size_t, __off_t]
    pwrite.restype = c_ptrdiff_t

# /usr/include/unistd.h: 417
if _libs["libc.so.6"].has("pipe", "cdecl"):
    pipe = _libs["libc.so.6"].get("pipe", "cdecl")
    pipe.argtypes = [c_int * int(2)]
    pipe.restype = c_int

# /usr/include/unistd.h: 432
if _libs["libc.so.6"].has("alarm", "cdecl"):
    alarm = _libs["libc.so.6"].get("alarm", "cdecl")
    alarm.argtypes = [c_uint]
    alarm.restype = c_uint

# /usr/include/unistd.h: 444
if _libs["libc.so.6"].has("sleep", "cdecl"):
    sleep = _libs["libc.so.6"].get("sleep", "cdecl")
    sleep.argtypes = [c_uint]
    sleep.restype = c_uint

# /usr/include/unistd.h: 452
if _libs["libc.so.6"].has("ualarm", "cdecl"):
    ualarm = _libs["libc.so.6"].get("ualarm", "cdecl")
    ualarm.argtypes = [__useconds_t, __useconds_t]
    ualarm.restype = __useconds_t

# /usr/include/unistd.h: 460
if _libs["libc.so.6"].has("usleep", "cdecl"):
    usleep = _libs["libc.so.6"].get("usleep", "cdecl")
    usleep.argtypes = [__useconds_t]
    usleep.restype = c_int

# /usr/include/unistd.h: 469
if _libs["libc.so.6"].has("pause", "cdecl"):
    pause = _libs["libc.so.6"].get("pause", "cdecl")
    pause.argtypes = []
    pause.restype = c_int

# /usr/include/unistd.h: 473
if _libs["libc.so.6"].has("chown", "cdecl"):
    chown = _libs["libc.so.6"].get("chown", "cdecl")
    chown.argtypes = [String, __uid_t, __gid_t]
    chown.restype = c_int

# /usr/include/unistd.h: 478
if _libs["libc.so.6"].has("fchown", "cdecl"):
    fchown = _libs["libc.so.6"].get("fchown", "cdecl")
    fchown.argtypes = [c_int, __uid_t, __gid_t]
    fchown.restype = c_int

# /usr/include/unistd.h: 483
if _libs["libc.so.6"].has("lchown", "cdecl"):
    lchown = _libs["libc.so.6"].get("lchown", "cdecl")
    lchown.argtypes = [String, __uid_t, __gid_t]
    lchown.restype = c_int

# /usr/include/unistd.h: 491
if _libs["libc.so.6"].has("fchownat", "cdecl"):
    fchownat = _libs["libc.so.6"].get("fchownat", "cdecl")
    fchownat.argtypes = [c_int, String, __uid_t, __gid_t, c_int]
    fchownat.restype = c_int

# /usr/include/unistd.h: 497
if _libs["libc.so.6"].has("chdir", "cdecl"):
    chdir = _libs["libc.so.6"].get("chdir", "cdecl")
    chdir.argtypes = [String]
    chdir.restype = c_int

# /usr/include/unistd.h: 501
if _libs["libc.so.6"].has("fchdir", "cdecl"):
    fchdir = _libs["libc.so.6"].get("fchdir", "cdecl")
    fchdir.argtypes = [c_int]
    fchdir.restype = c_int

# /usr/include/unistd.h: 511
if _libs["libc.so.6"].has("getcwd", "cdecl"):
    getcwd = _libs["libc.so.6"].get("getcwd", "cdecl")
    getcwd.argtypes = [String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        getcwd.restype = ReturnString
    else:
        getcwd.restype = String
        getcwd.errcheck = ReturnString

# /usr/include/unistd.h: 525
if _libs["libc.so.6"].has("getwd", "cdecl"):
    getwd = _libs["libc.so.6"].get("getwd", "cdecl")
    getwd.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getwd.restype = ReturnString
    else:
        getwd.restype = String
        getwd.errcheck = ReturnString

# /usr/include/unistd.h: 531
if _libs["libc.so.6"].has("dup", "cdecl"):
    dup = _libs["libc.so.6"].get("dup", "cdecl")
    dup.argtypes = [c_int]
    dup.restype = c_int

# /usr/include/unistd.h: 534
if _libs["libc.so.6"].has("dup2", "cdecl"):
    dup2 = _libs["libc.so.6"].get("dup2", "cdecl")
    dup2.argtypes = [c_int, c_int]
    dup2.restype = c_int

# /usr/include/unistd.h: 543
try:
    __environ = (POINTER(POINTER(c_char))).in_dll(_libs["libc.so.6"], "__environ")
except:
    pass

# /usr/include/unistd.h: 551
if _libs["libc.so.6"].has("execve", "cdecl"):
    execve = _libs["libc.so.6"].get("execve", "cdecl")
    execve.argtypes = [String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    execve.restype = c_int

# /usr/include/unistd.h: 557
if _libs["libc.so.6"].has("fexecve", "cdecl"):
    fexecve = _libs["libc.so.6"].get("fexecve", "cdecl")
    fexecve.argtypes = [c_int, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    fexecve.restype = c_int

# /usr/include/unistd.h: 563
if _libs["libc.so.6"].has("execv", "cdecl"):
    execv = _libs["libc.so.6"].get("execv", "cdecl")
    execv.argtypes = [String, POINTER(POINTER(c_char))]
    execv.restype = c_int

# /usr/include/unistd.h: 568
if _libs["libc.so.6"].has("execle", "cdecl"):
    _func = _libs["libc.so.6"].get("execle", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    execle = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/unistd.h: 573
if _libs["libc.so.6"].has("execl", "cdecl"):
    _func = _libs["libc.so.6"].get("execl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    execl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/unistd.h: 578
if _libs["libc.so.6"].has("execvp", "cdecl"):
    execvp = _libs["libc.so.6"].get("execvp", "cdecl")
    execvp.argtypes = [String, POINTER(POINTER(c_char))]
    execvp.restype = c_int

# /usr/include/unistd.h: 584
if _libs["libc.so.6"].has("execlp", "cdecl"):
    _func = _libs["libc.so.6"].get("execlp", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    execlp = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/unistd.h: 598
if _libs["libc.so.6"].has("nice", "cdecl"):
    nice = _libs["libc.so.6"].get("nice", "cdecl")
    nice.argtypes = [c_int]
    nice.restype = c_int

# /usr/include/unistd.h: 603
if _libs["libc.so.6"].has("_exit", "cdecl"):
    _exit = _libs["libc.so.6"].get("_exit", "cdecl")
    _exit.argtypes = [c_int]
    _exit.restype = None

# /usr/include/unistd.h: 612
if _libs["libc.so.6"].has("pathconf", "cdecl"):
    pathconf = _libs["libc.so.6"].get("pathconf", "cdecl")
    pathconf.argtypes = [String, c_int]
    pathconf.restype = c_long

# /usr/include/unistd.h: 616
if _libs["libc.so.6"].has("fpathconf", "cdecl"):
    fpathconf = _libs["libc.so.6"].get("fpathconf", "cdecl")
    fpathconf.argtypes = [c_int, c_int]
    fpathconf.restype = c_long

# /usr/include/unistd.h: 619
if _libs["libc.so.6"].has("sysconf", "cdecl"):
    sysconf = _libs["libc.so.6"].get("sysconf", "cdecl")
    sysconf.argtypes = [c_int]
    sysconf.restype = c_long

# /usr/include/unistd.h: 623
if _libs["libc.so.6"].has("confstr", "cdecl"):
    confstr = _libs["libc.so.6"].get("confstr", "cdecl")
    confstr.argtypes = [c_int, String, c_size_t]
    confstr.restype = c_size_t

# /usr/include/unistd.h: 628
if _libs["libc.so.6"].has("getpid", "cdecl"):
    getpid = _libs["libc.so.6"].get("getpid", "cdecl")
    getpid.argtypes = []
    getpid.restype = __pid_t

# /usr/include/unistd.h: 631
if _libs["libc.so.6"].has("getppid", "cdecl"):
    getppid = _libs["libc.so.6"].get("getppid", "cdecl")
    getppid.argtypes = []
    getppid.restype = __pid_t

# /usr/include/unistd.h: 634
if _libs["libc.so.6"].has("getpgrp", "cdecl"):
    getpgrp = _libs["libc.so.6"].get("getpgrp", "cdecl")
    getpgrp.argtypes = []
    getpgrp.restype = __pid_t

# /usr/include/unistd.h: 637
if _libs["libc.so.6"].has("__getpgid", "cdecl"):
    __getpgid = _libs["libc.so.6"].get("__getpgid", "cdecl")
    __getpgid.argtypes = [__pid_t]
    __getpgid.restype = __pid_t

# /usr/include/unistd.h: 639
if _libs["libc.so.6"].has("getpgid", "cdecl"):
    getpgid = _libs["libc.so.6"].get("getpgid", "cdecl")
    getpgid.argtypes = [__pid_t]
    getpgid.restype = __pid_t

# /usr/include/unistd.h: 646
if _libs["libc.so.6"].has("setpgid", "cdecl"):
    setpgid = _libs["libc.so.6"].get("setpgid", "cdecl")
    setpgid.argtypes = [__pid_t, __pid_t]
    setpgid.restype = c_int

# /usr/include/unistd.h: 660
if _libs["libc.so.6"].has("setpgrp", "cdecl"):
    setpgrp = _libs["libc.so.6"].get("setpgrp", "cdecl")
    setpgrp.argtypes = []
    setpgrp.restype = c_int

# /usr/include/unistd.h: 667
if _libs["libc.so.6"].has("setsid", "cdecl"):
    setsid = _libs["libc.so.6"].get("setsid", "cdecl")
    setsid.argtypes = []
    setsid.restype = __pid_t

# /usr/include/unistd.h: 671
if _libs["libc.so.6"].has("getsid", "cdecl"):
    getsid = _libs["libc.so.6"].get("getsid", "cdecl")
    getsid.argtypes = [__pid_t]
    getsid.restype = __pid_t

# /usr/include/unistd.h: 675
if _libs["libc.so.6"].has("getuid", "cdecl"):
    getuid = _libs["libc.so.6"].get("getuid", "cdecl")
    getuid.argtypes = []
    getuid.restype = __uid_t

# /usr/include/unistd.h: 678
if _libs["libc.so.6"].has("geteuid", "cdecl"):
    geteuid = _libs["libc.so.6"].get("geteuid", "cdecl")
    geteuid.argtypes = []
    geteuid.restype = __uid_t

# /usr/include/unistd.h: 681
if _libs["libc.so.6"].has("getgid", "cdecl"):
    getgid = _libs["libc.so.6"].get("getgid", "cdecl")
    getgid.argtypes = []
    getgid.restype = __gid_t

# /usr/include/unistd.h: 684
if _libs["libc.so.6"].has("getegid", "cdecl"):
    getegid = _libs["libc.so.6"].get("getegid", "cdecl")
    getegid.argtypes = []
    getegid.restype = __gid_t

# /usr/include/unistd.h: 689
if _libs["libc.so.6"].has("getgroups", "cdecl"):
    getgroups = _libs["libc.so.6"].get("getgroups", "cdecl")
    getgroups.argtypes = [c_int, POINTER(__gid_t)]
    getgroups.restype = c_int

# /usr/include/unistd.h: 700
if _libs["libc.so.6"].has("setuid", "cdecl"):
    setuid = _libs["libc.so.6"].get("setuid", "cdecl")
    setuid.argtypes = [__uid_t]
    setuid.restype = c_int

# /usr/include/unistd.h: 705
if _libs["libc.so.6"].has("setreuid", "cdecl"):
    setreuid = _libs["libc.so.6"].get("setreuid", "cdecl")
    setreuid.argtypes = [__uid_t, __uid_t]
    setreuid.restype = c_int

# /usr/include/unistd.h: 710
if _libs["libc.so.6"].has("seteuid", "cdecl"):
    seteuid = _libs["libc.so.6"].get("seteuid", "cdecl")
    seteuid.argtypes = [__uid_t]
    seteuid.restype = c_int

# /usr/include/unistd.h: 717
if _libs["libc.so.6"].has("setgid", "cdecl"):
    setgid = _libs["libc.so.6"].get("setgid", "cdecl")
    setgid.argtypes = [__gid_t]
    setgid.restype = c_int

# /usr/include/unistd.h: 722
if _libs["libc.so.6"].has("setregid", "cdecl"):
    setregid = _libs["libc.so.6"].get("setregid", "cdecl")
    setregid.argtypes = [__gid_t, __gid_t]
    setregid.restype = c_int

# /usr/include/unistd.h: 727
if _libs["libc.so.6"].has("setegid", "cdecl"):
    setegid = _libs["libc.so.6"].get("setegid", "cdecl")
    setegid.argtypes = [__gid_t]
    setegid.restype = c_int

# /usr/include/unistd.h: 756
if _libs["libc.so.6"].has("fork", "cdecl"):
    fork = _libs["libc.so.6"].get("fork", "cdecl")
    fork.argtypes = []
    fork.restype = __pid_t

# /usr/include/unistd.h: 764
if _libs["libc.so.6"].has("vfork", "cdecl"):
    vfork = _libs["libc.so.6"].get("vfork", "cdecl")
    vfork.argtypes = []
    vfork.restype = __pid_t

# /usr/include/unistd.h: 770
if _libs["libc.so.6"].has("ttyname", "cdecl"):
    ttyname = _libs["libc.so.6"].get("ttyname", "cdecl")
    ttyname.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ttyname.restype = ReturnString
    else:
        ttyname.restype = String
        ttyname.errcheck = ReturnString

# /usr/include/unistd.h: 774
if _libs["libc.so.6"].has("ttyname_r", "cdecl"):
    ttyname_r = _libs["libc.so.6"].get("ttyname_r", "cdecl")
    ttyname_r.argtypes = [c_int, String, c_size_t]
    ttyname_r.restype = c_int

# /usr/include/unistd.h: 779
if _libs["libc.so.6"].has("isatty", "cdecl"):
    isatty = _libs["libc.so.6"].get("isatty", "cdecl")
    isatty.argtypes = [c_int]
    isatty.restype = c_int

# /usr/include/unistd.h: 784
if _libs["libc.so.6"].has("ttyslot", "cdecl"):
    ttyslot = _libs["libc.so.6"].get("ttyslot", "cdecl")
    ttyslot.argtypes = []
    ttyslot.restype = c_int

# /usr/include/unistd.h: 789
if _libs["libc.so.6"].has("link", "cdecl"):
    link = _libs["libc.so.6"].get("link", "cdecl")
    link.argtypes = [String, String]
    link.restype = c_int

# /usr/include/unistd.h: 795
if _libs["libc.so.6"].has("linkat", "cdecl"):
    linkat = _libs["libc.so.6"].get("linkat", "cdecl")
    linkat.argtypes = [c_int, String, c_int, String, c_int]
    linkat.restype = c_int

# /usr/include/unistd.h: 802
if _libs["libc.so.6"].has("symlink", "cdecl"):
    symlink = _libs["libc.so.6"].get("symlink", "cdecl")
    symlink.argtypes = [String, String]
    symlink.restype = c_int

# /usr/include/unistd.h: 808
if _libs["libc.so.6"].has("readlink", "cdecl"):
    readlink = _libs["libc.so.6"].get("readlink", "cdecl")
    readlink.argtypes = [String, String, c_size_t]
    readlink.restype = c_ptrdiff_t

# /usr/include/unistd.h: 815
if _libs["libc.so.6"].has("symlinkat", "cdecl"):
    symlinkat = _libs["libc.so.6"].get("symlinkat", "cdecl")
    symlinkat.argtypes = [String, c_int, String]
    symlinkat.restype = c_int

# /usr/include/unistd.h: 819
if _libs["libc.so.6"].has("readlinkat", "cdecl"):
    readlinkat = _libs["libc.so.6"].get("readlinkat", "cdecl")
    readlinkat.argtypes = [c_int, String, String, c_size_t]
    readlinkat.restype = c_ptrdiff_t

# /usr/include/unistd.h: 825
if _libs["libc.so.6"].has("unlink", "cdecl"):
    unlink = _libs["libc.so.6"].get("unlink", "cdecl")
    unlink.argtypes = [String]
    unlink.restype = c_int

# /usr/include/unistd.h: 829
if _libs["libc.so.6"].has("unlinkat", "cdecl"):
    unlinkat = _libs["libc.so.6"].get("unlinkat", "cdecl")
    unlinkat.argtypes = [c_int, String, c_int]
    unlinkat.restype = c_int

# /usr/include/unistd.h: 834
if _libs["libc.so.6"].has("rmdir", "cdecl"):
    rmdir = _libs["libc.so.6"].get("rmdir", "cdecl")
    rmdir.argtypes = [String]
    rmdir.restype = c_int

# /usr/include/unistd.h: 838
if _libs["libc.so.6"].has("tcgetpgrp", "cdecl"):
    tcgetpgrp = _libs["libc.so.6"].get("tcgetpgrp", "cdecl")
    tcgetpgrp.argtypes = [c_int]
    tcgetpgrp.restype = __pid_t

# /usr/include/unistd.h: 841
if _libs["libc.so.6"].has("tcsetpgrp", "cdecl"):
    tcsetpgrp = _libs["libc.so.6"].get("tcsetpgrp", "cdecl")
    tcsetpgrp.argtypes = [c_int, __pid_t]
    tcsetpgrp.restype = c_int

# /usr/include/unistd.h: 848
if _libs["libc.so.6"].has("getlogin", "cdecl"):
    getlogin = _libs["libc.so.6"].get("getlogin", "cdecl")
    getlogin.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        getlogin.restype = ReturnString
    else:
        getlogin.restype = String
        getlogin.errcheck = ReturnString

# /usr/include/unistd.h: 856
if _libs["libc.so.6"].has("getlogin_r", "cdecl"):
    getlogin_r = _libs["libc.so.6"].get("getlogin_r", "cdecl")
    getlogin_r.argtypes = [String, c_size_t]
    getlogin_r.restype = c_int

# /usr/include/unistd.h: 861
if _libs["libc.so.6"].has("setlogin", "cdecl"):
    setlogin = _libs["libc.so.6"].get("setlogin", "cdecl")
    setlogin.argtypes = [String]
    setlogin.restype = c_int

# /usr/include/unistd.h: 877
if _libs["libc.so.6"].has("gethostname", "cdecl"):
    gethostname = _libs["libc.so.6"].get("gethostname", "cdecl")
    gethostname.argtypes = [String, c_size_t]
    gethostname.restype = c_int

# /usr/include/unistd.h: 884
if _libs["libc.so.6"].has("sethostname", "cdecl"):
    sethostname = _libs["libc.so.6"].get("sethostname", "cdecl")
    sethostname.argtypes = [String, c_size_t]
    sethostname.restype = c_int

# /usr/include/unistd.h: 889
if _libs["libc.so.6"].has("sethostid", "cdecl"):
    sethostid = _libs["libc.so.6"].get("sethostid", "cdecl")
    sethostid.argtypes = [c_long]
    sethostid.restype = c_int

# /usr/include/unistd.h: 895
if _libs["libc.so.6"].has("getdomainname", "cdecl"):
    getdomainname = _libs["libc.so.6"].get("getdomainname", "cdecl")
    getdomainname.argtypes = [String, c_size_t]
    getdomainname.restype = c_int

# /usr/include/unistd.h: 897
if _libs["libc.so.6"].has("setdomainname", "cdecl"):
    setdomainname = _libs["libc.so.6"].get("setdomainname", "cdecl")
    setdomainname.argtypes = [String, c_size_t]
    setdomainname.restype = c_int

# /usr/include/unistd.h: 904
if _libs["libc.so.6"].has("vhangup", "cdecl"):
    vhangup = _libs["libc.so.6"].get("vhangup", "cdecl")
    vhangup.argtypes = []
    vhangup.restype = c_int

# /usr/include/unistd.h: 907
if _libs["libc.so.6"].has("revoke", "cdecl"):
    revoke = _libs["libc.so.6"].get("revoke", "cdecl")
    revoke.argtypes = [String]
    revoke.restype = c_int

# /usr/include/unistd.h: 915
if _libs["libc.so.6"].has("profil", "cdecl"):
    profil = _libs["libc.so.6"].get("profil", "cdecl")
    profil.argtypes = [POINTER(c_uint), c_size_t, c_size_t, c_uint]
    profil.restype = c_int

# /usr/include/unistd.h: 923
if _libs["libc.so.6"].has("acct", "cdecl"):
    acct = _libs["libc.so.6"].get("acct", "cdecl")
    acct.argtypes = [String]
    acct.restype = c_int

# /usr/include/unistd.h: 927
if _libs["libc.so.6"].has("getusershell", "cdecl"):
    getusershell = _libs["libc.so.6"].get("getusershell", "cdecl")
    getusershell.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        getusershell.restype = ReturnString
    else:
        getusershell.restype = String
        getusershell.errcheck = ReturnString

# /usr/include/unistd.h: 928
if _libs["libc.so.6"].has("endusershell", "cdecl"):
    endusershell = _libs["libc.so.6"].get("endusershell", "cdecl")
    endusershell.argtypes = []
    endusershell.restype = None

# /usr/include/unistd.h: 929
if _libs["libc.so.6"].has("setusershell", "cdecl"):
    setusershell = _libs["libc.so.6"].get("setusershell", "cdecl")
    setusershell.argtypes = []
    setusershell.restype = None

# /usr/include/unistd.h: 935
if _libs["libc.so.6"].has("daemon", "cdecl"):
    daemon = _libs["libc.so.6"].get("daemon", "cdecl")
    daemon.argtypes = [c_int, c_int]
    daemon.restype = c_int

# /usr/include/unistd.h: 942
if _libs["libc.so.6"].has("chroot", "cdecl"):
    chroot = _libs["libc.so.6"].get("chroot", "cdecl")
    chroot.argtypes = [String]
    chroot.restype = c_int

# /usr/include/unistd.h: 946
if _libs["libc.so.6"].has("getpass", "cdecl"):
    getpass = _libs["libc.so.6"].get("getpass", "cdecl")
    getpass.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getpass.restype = ReturnString
    else:
        getpass.restype = String
        getpass.errcheck = ReturnString

# /usr/include/unistd.h: 954
if _libs["libc.so.6"].has("fsync", "cdecl"):
    fsync = _libs["libc.so.6"].get("fsync", "cdecl")
    fsync.argtypes = [c_int]
    fsync.restype = c_int

# /usr/include/unistd.h: 967
if _libs["libc.so.6"].has("gethostid", "cdecl"):
    gethostid = _libs["libc.so.6"].get("gethostid", "cdecl")
    gethostid.argtypes = []
    gethostid.restype = c_long

# /usr/include/unistd.h: 970
if _libs["libc.so.6"].has("sync", "cdecl"):
    sync = _libs["libc.so.6"].get("sync", "cdecl")
    sync.argtypes = []
    sync.restype = None

# /usr/include/unistd.h: 976
if _libs["libc.so.6"].has("getpagesize", "cdecl"):
    getpagesize = _libs["libc.so.6"].get("getpagesize", "cdecl")
    getpagesize.argtypes = []
    getpagesize.restype = c_int

# /usr/include/unistd.h: 981
if _libs["libc.so.6"].has("getdtablesize", "cdecl"):
    getdtablesize = _libs["libc.so.6"].get("getdtablesize", "cdecl")
    getdtablesize.argtypes = []
    getdtablesize.restype = c_int

# /usr/include/unistd.h: 991
if _libs["libc.so.6"].has("truncate", "cdecl"):
    truncate = _libs["libc.so.6"].get("truncate", "cdecl")
    truncate.argtypes = [String, __off_t]
    truncate.restype = c_int

# /usr/include/unistd.h: 1014
if _libs["libc.so.6"].has("ftruncate", "cdecl"):
    ftruncate = _libs["libc.so.6"].get("ftruncate", "cdecl")
    ftruncate.argtypes = [c_int, __off_t]
    ftruncate.restype = c_int

# /usr/include/unistd.h: 1035
if _libs["libc.so.6"].has("brk", "cdecl"):
    brk = _libs["libc.so.6"].get("brk", "cdecl")
    brk.argtypes = [POINTER(None)]
    brk.restype = c_int

# /usr/include/unistd.h: 1041
if _libs["libc.so.6"].has("sbrk", "cdecl"):
    sbrk = _libs["libc.so.6"].get("sbrk", "cdecl")
    sbrk.argtypes = [intptr_t]
    sbrk.restype = POINTER(c_ubyte)
    sbrk.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/unistd.h: 1056
if _libs["libc.so.6"].has("syscall", "cdecl"):
    _func = _libs["libc.so.6"].get("syscall", "cdecl")
    _restype = c_long
    _errcheck = None
    _argtypes = [c_long]
    syscall = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/unistd.h: 1115
if _libs["libc.so.6"].has("fdatasync", "cdecl"):
    fdatasync = _libs["libc.so.6"].get("fdatasync", "cdecl")
    fdatasync.argtypes = [c_int]
    fdatasync.restype = c_int

# /usr/include/unistd.h: 1124
for _lib in _libs.values():
    if not _lib.has("crypt", "cdecl"):
        continue
    crypt = _lib.get("crypt", "cdecl")
    crypt.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        crypt.restype = ReturnString
    else:
        crypt.restype = String
        crypt.errcheck = ReturnString
    break

# /usr/include/unistd.h: 1161
if _libs["libc.so.6"].has("getentropy", "cdecl"):
    getentropy = _libs["libc.so.6"].get("getentropy", "cdecl")
    getentropy.argtypes = [POINTER(None), c_size_t]
    getentropy.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 48
class struct_utsname(Structure):
    pass

struct_utsname.__slots__ = [
    'sysname',
    'nodename',
    'release',
    'version',
    'machine',
    '__domainname',
]
struct_utsname._fields_ = [
    ('sysname', c_char * int(65)),
    ('nodename', c_char * int(65)),
    ('release', c_char * int(65)),
    ('version', c_char * int(65)),
    ('machine', c_char * int(65)),
    ('__domainname', c_char * int(65)),
]

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 81
if _libs["libc.so.6"].has("uname", "cdecl"):
    uname = _libs["libc.so.6"].get("uname", "cdecl")
    uname.argtypes = [POINTER(struct_utsname)]
    uname.restype = c_int

enum___vlimit_resource = c_int# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_NORAISE = 0# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_CPU = (LIM_NORAISE + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_FSIZE = (LIM_CPU + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_DATA = (LIM_FSIZE + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_STACK = (LIM_DATA + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_CORE = (LIM_STACK + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

LIM_MAXRSS = (LIM_CORE + 1)# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 28

# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 62
if _libs["libc.so.6"].has("vlimit", "cdecl"):
    vlimit = _libs["libc.so.6"].get("vlimit", "cdecl")
    vlimit.argtypes = [enum___vlimit_resource, c_int]
    vlimit.restype = c_int

# /usr/include/linux/vt.h: 19
class struct_vt_mode(Structure):
    pass

struct_vt_mode.__slots__ = [
    'mode',
    'waitv',
    'relsig',
    'acqsig',
    'frsig',
]
struct_vt_mode._fields_ = [
    ('mode', c_char),
    ('waitv', c_char),
    ('relsig', c_short),
    ('acqsig', c_short),
    ('frsig', c_short),
]

# /usr/include/linux/vt.h: 32
class struct_vt_stat(Structure):
    pass

struct_vt_stat.__slots__ = [
    'v_active',
    'v_signal',
    'v_state',
]
struct_vt_stat._fields_ = [
    ('v_active', c_ushort),
    ('v_signal', c_ushort),
    ('v_state', c_ushort),
]

# /usr/include/linux/vt.h: 46
class struct_vt_sizes(Structure):
    pass

struct_vt_sizes.__slots__ = [
    'v_rows',
    'v_cols',
    'v_scrollsize',
]
struct_vt_sizes._fields_ = [
    ('v_rows', c_ushort),
    ('v_cols', c_ushort),
    ('v_scrollsize', c_ushort),
]

# /usr/include/linux/vt.h: 53
class struct_vt_consize(Structure):
    pass

struct_vt_consize.__slots__ = [
    'v_rows',
    'v_cols',
    'v_vlin',
    'v_clin',
    'v_vcol',
    'v_ccol',
]
struct_vt_consize._fields_ = [
    ('v_rows', c_ushort),
    ('v_cols', c_ushort),
    ('v_vlin', c_ushort),
    ('v_clin', c_ushort),
    ('v_vcol', c_ushort),
    ('v_ccol', c_ushort),
]

# /usr/include/linux/vt.h: 66
class struct_vt_event(Structure):
    pass

struct_vt_event.__slots__ = [
    'event',
    'oldev',
    'newev',
    'pad',
]
struct_vt_event._fields_ = [
    ('event', c_uint),
    ('oldev', c_uint),
    ('newev', c_uint),
    ('pad', c_uint * int(4)),
]

# /usr/include/linux/vt.h: 80
class struct_vt_setactivate(Structure):
    pass

struct_vt_setactivate.__slots__ = [
    'console',
    'mode',
]
struct_vt_setactivate._fields_ = [
    ('console', c_uint),
    ('mode', struct_vt_mode),
]

# /usr/include/x86_64-linux-gnu/sys/vtimes.h: 31
class struct_vtimes(Structure):
    pass

struct_vtimes.__slots__ = [
    'vm_utime',
    'vm_stime',
    'vm_idsrss',
    'vm_ixrss',
    'vm_maxrss',
    'vm_majflt',
    'vm_minflt',
    'vm_nswap',
    'vm_inblk',
    'vm_oublk',
]
struct_vtimes._fields_ = [
    ('vm_utime', c_int),
    ('vm_stime', c_int),
    ('vm_idsrss', c_uint),
    ('vm_ixrss', c_uint),
    ('vm_maxrss', c_int),
    ('vm_majflt', c_int),
    ('vm_minflt', c_int),
    ('vm_nswap', c_int),
    ('vm_inblk', c_int),
    ('vm_oublk', c_int),
]

# /usr/include/x86_64-linux-gnu/sys/vtimes.h: 64
if _libs["libc.so.6"].has("vtimes", "cdecl"):
    vtimes = _libs["libc.so.6"].get("vtimes", "cdecl")
    vtimes.argtypes = [POINTER(struct_vtimes), POINTER(struct_vtimes)]
    vtimes.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/wait.h: 77
if _libs["libc.so.6"].has("wait", "cdecl"):
    wait = _libs["libc.so.6"].get("wait", "cdecl")
    wait.argtypes = [POINTER(c_int)]
    wait.restype = __pid_t

# /usr/include/x86_64-linux-gnu/sys/wait.h: 100
if _libs["libc.so.6"].has("waitpid", "cdecl"):
    waitpid = _libs["libc.so.6"].get("waitpid", "cdecl")
    waitpid.argtypes = [__pid_t, POINTER(c_int), c_int]
    waitpid.restype = __pid_t

# /usr/include/x86_64-linux-gnu/sys/wait.h: 121
if _libs["libc.so.6"].has("waitid", "cdecl"):
    waitid = _libs["libc.so.6"].get("waitid", "cdecl")
    waitid.argtypes = [idtype_t, __id_t, POINTER(siginfo_t), c_int]
    waitid.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/wait.h: 136
if _libs["libc.so.6"].has("wait3", "cdecl"):
    wait3 = _libs["libc.so.6"].get("wait3", "cdecl")
    wait3.argtypes = [POINTER(c_int), c_int, POINTER(struct_rusage)]
    wait3.restype = __pid_t

# /usr/include/x86_64-linux-gnu/sys/wait.h: 142
if _libs["libc.so.6"].has("wait4", "cdecl"):
    wait4 = _libs["libc.so.6"].get("wait4", "cdecl")
    wait4.argtypes = [__pid_t, POINTER(c_int), c_int, POINTER(struct_rusage)]
    wait4.restype = __pid_t

enum_anon_203 = c_int# /usr/include/x86_64-linux-gnu/sys/xattr.h: 30

XATTR_CREATE = 1# /usr/include/x86_64-linux-gnu/sys/xattr.h: 30

XATTR_REPLACE = 2# /usr/include/x86_64-linux-gnu/sys/xattr.h: 30

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 41
if _libs["libc.so.6"].has("setxattr", "cdecl"):
    setxattr = _libs["libc.so.6"].get("setxattr", "cdecl")
    setxattr.argtypes = [String, String, POINTER(None), c_size_t, c_int]
    setxattr.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 48
if _libs["libc.so.6"].has("lsetxattr", "cdecl"):
    lsetxattr = _libs["libc.so.6"].get("lsetxattr", "cdecl")
    lsetxattr.argtypes = [String, String, POINTER(None), c_size_t, c_int]
    lsetxattr.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 54
if _libs["libc.so.6"].has("fsetxattr", "cdecl"):
    fsetxattr = _libs["libc.so.6"].get("fsetxattr", "cdecl")
    fsetxattr.argtypes = [c_int, String, POINTER(None), c_size_t, c_int]
    fsetxattr.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 59
if _libs["libc.so.6"].has("getxattr", "cdecl"):
    getxattr = _libs["libc.so.6"].get("getxattr", "cdecl")
    getxattr.argtypes = [String, String, POINTER(None), c_size_t]
    getxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 65
if _libs["libc.so.6"].has("lgetxattr", "cdecl"):
    lgetxattr = _libs["libc.so.6"].get("lgetxattr", "cdecl")
    lgetxattr.argtypes = [String, String, POINTER(None), c_size_t]
    lgetxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 70
if _libs["libc.so.6"].has("fgetxattr", "cdecl"):
    fgetxattr = _libs["libc.so.6"].get("fgetxattr", "cdecl")
    fgetxattr.argtypes = [c_int, String, POINTER(None), c_size_t]
    fgetxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 76
if _libs["libc.so.6"].has("listxattr", "cdecl"):
    listxattr = _libs["libc.so.6"].get("listxattr", "cdecl")
    listxattr.argtypes = [String, String, c_size_t]
    listxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 82
if _libs["libc.so.6"].has("llistxattr", "cdecl"):
    llistxattr = _libs["libc.so.6"].get("llistxattr", "cdecl")
    llistxattr.argtypes = [String, String, c_size_t]
    llistxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 87
if _libs["libc.so.6"].has("flistxattr", "cdecl"):
    flistxattr = _libs["libc.so.6"].get("flistxattr", "cdecl")
    flistxattr.argtypes = [c_int, String, c_size_t]
    flistxattr.restype = c_ptrdiff_t

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 92
if _libs["libc.so.6"].has("removexattr", "cdecl"):
    removexattr = _libs["libc.so.6"].get("removexattr", "cdecl")
    removexattr.argtypes = [String, String]
    removexattr.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 97
if _libs["libc.so.6"].has("lremovexattr", "cdecl"):
    lremovexattr = _libs["libc.so.6"].get("lremovexattr", "cdecl")
    lremovexattr.argtypes = [String, String]
    lremovexattr.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 101
if _libs["libc.so.6"].has("fremovexattr", "cdecl"):
    fremovexattr = _libs["libc.so.6"].get("fremovexattr", "cdecl")
    fremovexattr.argtypes = [c_int, String]
    fremovexattr.restype = c_int

# <built-in>
try:
    __WCHAR_MAX__ = 0x7fffffff
except:
    pass

# <built-in>
try:
    __WCHAR_MIN__ = ((-__WCHAR_MAX__) - 1)
except:
    pass

# /usr/include/stdc-predef.h: 19
try:
    _STDC_PREDEF_H = 1
except:
    pass

# /usr/include/stdc-predef.h: 38
try:
    __STDC_IEC_559__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 46
try:
    __STDC_IEC_559_COMPLEX__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 58
try:
    __STDC_ISO_10646__ = 201706
except:
    pass

# /usr/include/stdint.h: 23
try:
    _STDINT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 19
try:
    _SYS_CDEFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 84
def __NTH(fct):
    return fct

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 94
def __glibc_clang_has_extension(ext):
    return 0

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 99
def __P(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 100
def __PMT(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 106
def __STRING(x):
    return x

__ptr_t = POINTER(None)# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 109

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 144
try:
    __glibc_c99_flexarr_available = 1
except:
    pass

__restrict = c_int# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 377

__restrict_arr = c_int# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 393

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 405
def __glibc_unlikely(cond):
    return cond

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 406
def __glibc_likely(cond):
    return cond

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 475
def __LDBL_REDIR1(name, proto, alias):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 476
def __LDBL_REDIR(name, proto):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 512
try:
    __HAVE_GENERIC_SELECTION = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types.h: 24
try:
    _BITS_TYPES_H = 1
except:
    pass

__S16_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 109

__U16_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 110

__S32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 111

__U32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 112

__SLONGWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 113

__ULONGWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 114

__SQUAD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 128

__UQUAD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 129

__SWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 130

__UWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 131

__SLONG32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 132

__ULONG32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 133

__S64_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 134

__U64_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 135

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 97
try:
    __FD_SETSIZE = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wchar.h: 34
try:
    __WCHAR_MAX = __WCHAR_MAX__
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wchar.h: 42
try:
    __WCHAR_MIN = __WCHAR_MIN__
except:
    pass

# /usr/include/stdint.h: 116
try:
    INT8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 117
try:
    INT16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 118
try:
    INT32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 121
try:
    INT8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 122
try:
    INT16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 123
try:
    INT32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 127
try:
    UINT8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 128
try:
    UINT16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 129
try:
    UINT32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 134
try:
    INT_LEAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 135
try:
    INT_LEAST16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 136
try:
    INT_LEAST32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 139
try:
    INT_LEAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 140
try:
    INT_LEAST16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 141
try:
    INT_LEAST32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 145
try:
    UINT_LEAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 146
try:
    UINT_LEAST16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 147
try:
    UINT_LEAST32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 152
try:
    INT_FAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 154
try:
    INT_FAST16_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 155
try:
    INT_FAST32_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 162
try:
    INT_FAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 164
try:
    INT_FAST16_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 165
try:
    INT_FAST32_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 173
try:
    UINT_FAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 175
try:
    UINT_FAST16_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 176
try:
    UINT_FAST32_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 186
try:
    INTPTR_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 187
try:
    INTPTR_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 188
try:
    UINTPTR_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 209
try:
    PTRDIFF_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 210
try:
    PTRDIFF_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 222
try:
    SIG_ATOMIC_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 223
try:
    SIG_ATOMIC_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 227
try:
    SIZE_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 239
try:
    WCHAR_MIN = __WCHAR_MIN
except:
    pass

# /usr/include/stdint.h: 240
try:
    WCHAR_MAX = __WCHAR_MAX
except:
    pass

# /usr/include/stdint.h: 244
try:
    WINT_MIN = 0
except:
    pass

# /usr/include/stdint.h: 245
try:
    WINT_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 248
def INT8_C(c):
    return c

# /usr/include/stdint.h: 249
def INT16_C(c):
    return c

# /usr/include/stdint.h: 250
def INT32_C(c):
    return c

# /usr/include/stdint.h: 258
def UINT8_C(c):
    return c

# /usr/include/stdint.h: 259
def UINT16_C(c):
    return c

# /usr/include/stdio.h: 24
try:
    _STDIO_H = 1
except:
    pass

# /usr/include/stdio.h: 93
try:
    _IOFBF = 0
except:
    pass

# /usr/include/stdio.h: 94
try:
    _IOLBF = 1
except:
    pass

# /usr/include/stdio.h: 95
try:
    _IONBF = 2
except:
    pass

# /usr/include/stdio.h: 99
try:
    BUFSIZ = 8192
except:
    pass

# /usr/include/stdio.h: 104
try:
    EOF = (-1)
except:
    pass

# /usr/include/stdio.h: 109
try:
    SEEK_SET = 0
except:
    pass

# /usr/include/stdio.h: 110
try:
    SEEK_CUR = 1
except:
    pass

# /usr/include/stdio.h: 111
try:
    SEEK_END = 2
except:
    pass

# /usr/include/stdio.h: 120
try:
    P_tmpdir = '/tmp'
except:
    pass

# /usr/include/stdio.h: 141
try:
    stdin = stdin
except:
    pass

# /usr/include/stdio.h: 142
try:
    stdout = stdout
except:
    pass

# /usr/include/stdio.h: 143
try:
    stderr = stderr
except:
    pass

# /usr/include/stdio.h: 421
try:
    fscanf = __isoc99_fscanf
except:
    pass

# /usr/include/stdio.h: 422
try:
    scanf = __isoc99_scanf
except:
    pass

# /usr/include/stdio.h: 423
try:
    sscanf = __isoc99_sscanf
except:
    pass

# /usr/include/stdio_ext.h: 23
try:
    _STDIO_EXT_H = 1
except:
    pass

# /usr/include/stdio_ext.h: 31
try:
    FSETLOCKING_QUERY = FSETLOCKING_QUERY
except:
    pass

# /usr/include/stdio_ext.h: 35
try:
    FSETLOCKING_INTERNAL = FSETLOCKING_INTERNAL
except:
    pass

# /usr/include/stdio_ext.h: 38
try:
    FSETLOCKING_BYCALLER = FSETLOCKING_BYCALLER
except:
    pass

# /usr/include/stdlib.h: 35
try:
    _STDLIB_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 28
def __WEXITSTATUS(status):
    return ((status & 0xff00) >> 8)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 31
def __WTERMSIG(status):
    return (status & 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 34
def __WSTOPSIG(status):
    return (__WEXITSTATUS (status))

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 37
def __WIFEXITED(status):
    return ((__WTERMSIG (status)) == 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 40
def __WIFSIGNALED(status):
    return (((c_char ((((status & 0x7f) + 1)))).value >> 1) > 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 44
def __WIFSTOPPED(status):
    return ((status & 0xff) == 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 49
def __WIFCONTINUED(status):
    return (status == __W_CONTINUED)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 53
def __WCOREDUMP(status):
    return (status & __WCOREFLAG)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 56
def __W_EXITCODE(ret, sig):
    return ((ret << 8) | sig)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 57
def __W_STOPCODE(sig):
    return ((sig << 8) | 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 58
try:
    __W_CONTINUED = 0xffff
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 59
try:
    __WCOREFLAG = 0x80
except:
    pass

# /usr/include/stdlib.h: 43
def WEXITSTATUS(status):
    return (__WEXITSTATUS (status))

# /usr/include/stdlib.h: 44
def WTERMSIG(status):
    return (__WTERMSIG (status))

# /usr/include/stdlib.h: 45
def WSTOPSIG(status):
    return (__WSTOPSIG (status))

# /usr/include/stdlib.h: 46
def WIFEXITED(status):
    return (__WIFEXITED (status))

# /usr/include/stdlib.h: 47
def WIFSIGNALED(status):
    return (__WIFSIGNALED (status))

# /usr/include/stdlib.h: 48
def WIFSTOPPED(status):
    return (__WIFSTOPPED (status))

# /usr/include/stdlib.h: 50
def WIFCONTINUED(status):
    return (__WIFCONTINUED (status))

# /usr/include/stdlib.h: 71
try:
    __ldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 81
try:
    __lldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 86
try:
    RAND_MAX = 2147483647
except:
    pass

# /usr/include/stdlib.h: 91
try:
    EXIT_FAILURE = 1
except:
    pass

# /usr/include/stdlib.h: 92
try:
    EXIT_SUCCESS = 0
except:
    pass

# /usr/include/stdlib.h: 96
try:
    MB_CUR_MAX = (__ctype_get_mb_cur_max ())
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 23
try:
    _SYS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 171
try:
    __BIT_TYPES_DEFINED__ = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 22
try:
    _SYS_SELECT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/select.h: 58
def __FD_SET(d, set):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 60
def __FD_CLR(d, set):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 62
def __FD_ISSET(d, set):
    return ((((__FDS_BITS (set)) [(__FD_ELT (d))]) & (__FD_MASK (d))) != 0)

# /usr/include/x86_64-linux-gnu/sys/select.h: 54
try:
    __NFDBITS = (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 55
def __FD_ELT(d):
    return (d / __NFDBITS)

# /usr/include/x86_64-linux-gnu/sys/select.h: 56
def __FD_MASK(d):
    return (__fd_mask (ord_if_char((1 << (d % __NFDBITS))))).value

# /usr/include/x86_64-linux-gnu/sys/select.h: 68
def __FDS_BITS(set):
    return (set.contents.__fds_bits)

# /usr/include/x86_64-linux-gnu/sys/select.h: 73
try:
    FD_SETSIZE = __FD_SETSIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 80
try:
    NFDBITS = __NFDBITS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 85
def FD_SET(fd, fdsetp):
    return (__FD_SET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 86
def FD_CLR(fd, fdsetp):
    return (__FD_CLR (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 87
def FD_ISSET(fd, fdsetp):
    return (__FD_ISSET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/bits/a.out.h: 9
try:
    __NO_A_OUT_SUPPORT = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 31
def N_MAGIC(exec):
    return (((exec.a_info).value) & 0xffff)

# /usr/include/x86_64-linux-gnu/a.out.h: 32
def N_MACHTYPE(exec):
    return (enum_machine_type (ord_if_char(((((exec.a_info).value) >> 16) & 0xff)))).value

# /usr/include/x86_64-linux-gnu/a.out.h: 33
def N_FLAGS(exec):
    return ((((exec.a_info).value) >> 24) & 0xff)

# /usr/include/x86_64-linux-gnu/a.out.h: 34
def N_SET_INFO(exec, magic, type, flags):
    return (((magic & 0xffff) | (((c_int (ord_if_char(type))).value & 0xff) << 16)) | ((flags & 0xff) << 24))

# /usr/include/x86_64-linux-gnu/a.out.h: 38
def N_SET_MAGIC(exec, magic):
    return ((((exec.a_info).value) & 0xffff0000) | (magic & 0xffff))

# /usr/include/x86_64-linux-gnu/a.out.h: 40
def N_SET_MACHTYPE(exec, machtype):
    return ((((exec.a_info).value) & 0xff00ffff) | (((c_int (ord_if_char(machtype))).value & 0xff) << 16))

# /usr/include/x86_64-linux-gnu/a.out.h: 43
def N_SET_FLAGS(exec, flags):
    return ((((exec.a_info).value) & 0x00ffffff) | ((flags & 0xff) << 24))

# /usr/include/x86_64-linux-gnu/a.out.h: 48
try:
    OMAGIC = 0o407
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 50
try:
    NMAGIC = 0o410
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 52
try:
    ZMAGIC = 0o413
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 55
try:
    QMAGIC = 0o314
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 57
try:
    CMAGIC = 0o421
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 59
def N_TRSIZE(a):
    return (a.a_trsize)

# /usr/include/x86_64-linux-gnu/a.out.h: 60
def N_DRSIZE(a):
    return (a.a_drsize)

# /usr/include/x86_64-linux-gnu/a.out.h: 61
def N_SYMSIZE(a):
    return (a.a_syms)

# /usr/include/x86_64-linux-gnu/a.out.h: 62
def N_BADMAG(x):
    return (((((N_MAGIC (x)) != OMAGIC) and ((N_MAGIC (x)) != NMAGIC)) and ((N_MAGIC (x)) != ZMAGIC)) and ((N_MAGIC (x)) != QMAGIC))

# /usr/include/x86_64-linux-gnu/a.out.h: 65
def _N_HDROFF(x):
    return (1024 - sizeof(struct_exec))

# /usr/include/x86_64-linux-gnu/a.out.h: 66
def N_TXTOFF(x):
    return ((N_MAGIC (x)) == ZMAGIC) and ((_N_HDROFF (x)) + sizeof(struct_exec)) or ((N_MAGIC (x)) == QMAGIC) and 0 or sizeof(struct_exec)

# /usr/include/x86_64-linux-gnu/a.out.h: 69
def N_DATOFF(x):
    return ((N_TXTOFF (x)) + ((x.a_text).value))

# /usr/include/x86_64-linux-gnu/a.out.h: 70
def N_TRELOFF(x):
    return ((N_DATOFF (x)) + ((x.a_data).value))

# /usr/include/x86_64-linux-gnu/a.out.h: 71
def N_DRELOFF(x):
    return ((N_TRELOFF (x)) + (N_TRSIZE (x)))

# /usr/include/x86_64-linux-gnu/a.out.h: 72
def N_SYMOFF(x):
    return ((N_DRELOFF (x)) + (N_DRSIZE (x)))

# /usr/include/x86_64-linux-gnu/a.out.h: 73
def N_STROFF(x):
    return ((N_SYMOFF (x)) + (N_SYMSIZE (x)))

# /usr/include/x86_64-linux-gnu/a.out.h: 76
def N_TXTADDR(x):
    return ((N_MAGIC (x)) == QMAGIC) and 4096 or 0

# /usr/include/x86_64-linux-gnu/a.out.h: 79
try:
    SEGMENT_SIZE = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 81
def _N_SEGMENT_ROUND(x):
    return (((x + SEGMENT_SIZE) - 1) & (~(SEGMENT_SIZE - 1)))

# /usr/include/x86_64-linux-gnu/a.out.h: 82
def _N_TXTENDADDR(x):
    return ((N_TXTADDR (x)) + ((x.a_text).value))

# /usr/include/x86_64-linux-gnu/a.out.h: 84
def N_DATADDR(x):
    return ((N_MAGIC (x)) == OMAGIC) and (_N_TXTENDADDR (x)) or (_N_SEGMENT_ROUND ((_N_TXTENDADDR (x))))

# /usr/include/x86_64-linux-gnu/a.out.h: 87
def N_BSSADDR(x):
    return ((N_DATADDR (x)) + ((x.a_data).value))

# /usr/include/x86_64-linux-gnu/a.out.h: 105
try:
    N_UNDF = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 106
try:
    N_ABS = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 107
try:
    N_TEXT = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 108
try:
    N_DATA = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 109
try:
    N_BSS = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 110
try:
    N_FN = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 111
try:
    N_EXT = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 112
try:
    N_TYPE = 0o36
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 113
try:
    N_STAB = 0o340
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 114
try:
    N_INDR = 0xa
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 115
try:
    N_SETA = 0x14
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 116
try:
    N_SETT = 0x16
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 117
try:
    N_SETD = 0x18
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 118
try:
    N_SETB = 0x1A
except:
    pass

# /usr/include/x86_64-linux-gnu/a.out.h: 119
try:
    N_SETV = 0x1C
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 8
try:
    BYTEORDER = 1234
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 17
try:
    HAVE_DLFCN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 20
try:
    HAVE_FCNTL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 23
try:
    HAVE_GETPAGESIZE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 26
try:
    HAVE_GETRANDOM = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 29
try:
    HAVE_INTTYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 35
try:
    HAVE_MEMORY_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 38
try:
    HAVE_MMAP = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 41
try:
    HAVE_STDINT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 44
try:
    HAVE_STDLIB_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 47
try:
    HAVE_STRINGS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 50
try:
    HAVE_STRING_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 53
try:
    HAVE_SYSCALL_GETRANDOM = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 56
try:
    HAVE_SYS_PARAM_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 59
try:
    HAVE_SYS_STAT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 62
try:
    HAVE_SYS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 65
try:
    HAVE_UNISTD_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 68
try:
    LT_OBJDIR = '.libs/'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 71
try:
    PACKAGE = 'expat'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 74
try:
    PACKAGE_BUGREPORT = 'expat-bugs@libexpat.org'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 77
try:
    PACKAGE_NAME = 'expat'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 80
try:
    PACKAGE_STRING = 'expat 2.2.9'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 83
try:
    PACKAGE_TARNAME = 'expat'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 86
try:
    PACKAGE_URL = ''
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 89
try:
    PACKAGE_VERSION = '2.2.9'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 92
try:
    STDC_HEADERS = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 95
try:
    VERSION = '2.2.9'
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 115
try:
    XML_CONTEXT_BYTES = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 118
try:
    XML_DEV_URANDOM = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 121
try:
    XML_DTD = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/expat_config.h: 124
try:
    XML_NS = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 21
try:
    _FPU_CONTROL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 61
try:
    _FPU_MASK_IM = 0x01
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 62
try:
    _FPU_MASK_DM = 0x02
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 63
try:
    _FPU_MASK_ZM = 0x04
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 64
try:
    _FPU_MASK_OM = 0x08
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 65
try:
    _FPU_MASK_UM = 0x10
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 66
try:
    _FPU_MASK_PM = 0x20
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 69
try:
    _FPU_EXTENDED = 0x300
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 70
try:
    _FPU_DOUBLE = 0x200
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 71
try:
    _FPU_SINGLE = 0x0
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 74
try:
    _FPU_RC_NEAREST = 0x0
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 75
try:
    _FPU_RC_DOWN = 0x400
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 76
try:
    _FPU_RC_UP = 0x800
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 77
try:
    _FPU_RC_ZERO = 0xC00
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 79
try:
    _FPU_RESERVED = 0xF0C0
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 85
try:
    _FPU_DEFAULT = 0x037f
except:
    pass

# /usr/include/x86_64-linux-gnu/fpu_control.h: 88
try:
    _FPU_IEEE = 0x037f
except:
    pass

# /usr/include/x86_64-linux-gnu/ieee754.h: 19
try:
    _IEEE754_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/ieee754.h: 64
try:
    IEEE754_FLOAT_BIAS = 0x7f
except:
    pass

# /usr/include/x86_64-linux-gnu/ieee754.h: 126
try:
    IEEE754_DOUBLE_BIAS = 0x3ff
except:
    pass

# /usr/include/x86_64-linux-gnu/ieee754.h: 194
try:
    IEEE854_LONG_DOUBLE_BIAS = 0x3fff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/acct.h: 19
try:
    _SYS_ACCT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/acct.h: 28
try:
    ACCT_COMM = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/acct.h: 95
try:
    ACCT_BYTEORDER = 0x00
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/acct.h: 98
try:
    AHZ = 100
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/auxv.h: 20
try:
    _SYS_AUXV_H = 1
except:
    pass

# /usr/include/elf.h: 20
try:
    _ELF_H = 1
except:
    pass

# /usr/include/elf.h: 65
try:
    EI_NIDENT = 16
except:
    pass

# /usr/include/elf.h: 107
try:
    EI_MAG0 = 0
except:
    pass

# /usr/include/elf.h: 108
try:
    ELFMAG0 = 0x7f
except:
    pass

# /usr/include/elf.h: 110
try:
    EI_MAG1 = 1
except:
    pass

# /usr/include/elf.h: 111
try:
    ELFMAG1 = 'E'
except:
    pass

# /usr/include/elf.h: 113
try:
    EI_MAG2 = 2
except:
    pass

# /usr/include/elf.h: 114
try:
    ELFMAG2 = 'L'
except:
    pass

# /usr/include/elf.h: 116
try:
    EI_MAG3 = 3
except:
    pass

# /usr/include/elf.h: 117
try:
    ELFMAG3 = 'F'
except:
    pass

# /usr/include/elf.h: 120
try:
    ELFMAG = '\\177ELF'
except:
    pass

# /usr/include/elf.h: 121
try:
    SELFMAG = 4
except:
    pass

# /usr/include/elf.h: 123
try:
    EI_CLASS = 4
except:
    pass

# /usr/include/elf.h: 124
try:
    ELFCLASSNONE = 0
except:
    pass

# /usr/include/elf.h: 125
try:
    ELFCLASS32 = 1
except:
    pass

# /usr/include/elf.h: 126
try:
    ELFCLASS64 = 2
except:
    pass

# /usr/include/elf.h: 127
try:
    ELFCLASSNUM = 3
except:
    pass

# /usr/include/elf.h: 129
try:
    EI_DATA = 5
except:
    pass

# /usr/include/elf.h: 130
try:
    ELFDATANONE = 0
except:
    pass

# /usr/include/elf.h: 131
try:
    ELFDATA2LSB = 1
except:
    pass

# /usr/include/elf.h: 132
try:
    ELFDATA2MSB = 2
except:
    pass

# /usr/include/elf.h: 133
try:
    ELFDATANUM = 3
except:
    pass

# /usr/include/elf.h: 135
try:
    EI_VERSION = 6
except:
    pass

# /usr/include/elf.h: 138
try:
    EI_OSABI = 7
except:
    pass

# /usr/include/elf.h: 139
try:
    ELFOSABI_NONE = 0
except:
    pass

# /usr/include/elf.h: 140
try:
    ELFOSABI_SYSV = 0
except:
    pass

# /usr/include/elf.h: 141
try:
    ELFOSABI_HPUX = 1
except:
    pass

# /usr/include/elf.h: 142
try:
    ELFOSABI_NETBSD = 2
except:
    pass

# /usr/include/elf.h: 143
try:
    ELFOSABI_GNU = 3
except:
    pass

# /usr/include/elf.h: 144
try:
    ELFOSABI_LINUX = ELFOSABI_GNU
except:
    pass

# /usr/include/elf.h: 145
try:
    ELFOSABI_SOLARIS = 6
except:
    pass

# /usr/include/elf.h: 146
try:
    ELFOSABI_AIX = 7
except:
    pass

# /usr/include/elf.h: 147
try:
    ELFOSABI_IRIX = 8
except:
    pass

# /usr/include/elf.h: 148
try:
    ELFOSABI_FREEBSD = 9
except:
    pass

# /usr/include/elf.h: 149
try:
    ELFOSABI_TRU64 = 10
except:
    pass

# /usr/include/elf.h: 150
try:
    ELFOSABI_MODESTO = 11
except:
    pass

# /usr/include/elf.h: 151
try:
    ELFOSABI_OPENBSD = 12
except:
    pass

# /usr/include/elf.h: 152
try:
    ELFOSABI_ARM_AEABI = 64
except:
    pass

# /usr/include/elf.h: 153
try:
    ELFOSABI_ARM = 97
except:
    pass

# /usr/include/elf.h: 154
try:
    ELFOSABI_STANDALONE = 255
except:
    pass

# /usr/include/elf.h: 156
try:
    EI_ABIVERSION = 8
except:
    pass

# /usr/include/elf.h: 158
try:
    EI_PAD = 9
except:
    pass

# /usr/include/elf.h: 162
try:
    ET_NONE = 0
except:
    pass

# /usr/include/elf.h: 163
try:
    ET_REL = 1
except:
    pass

# /usr/include/elf.h: 164
try:
    ET_EXEC = 2
except:
    pass

# /usr/include/elf.h: 165
try:
    ET_DYN = 3
except:
    pass

# /usr/include/elf.h: 166
try:
    ET_CORE = 4
except:
    pass

# /usr/include/elf.h: 167
try:
    ET_NUM = 5
except:
    pass

# /usr/include/elf.h: 168
try:
    ET_LOOS = 0xfe00
except:
    pass

# /usr/include/elf.h: 169
try:
    ET_HIOS = 0xfeff
except:
    pass

# /usr/include/elf.h: 170
try:
    ET_LOPROC = 0xff00
except:
    pass

# /usr/include/elf.h: 171
try:
    ET_HIPROC = 0xffff
except:
    pass

# /usr/include/elf.h: 175
try:
    EM_NONE = 0
except:
    pass

# /usr/include/elf.h: 176
try:
    EM_M32 = 1
except:
    pass

# /usr/include/elf.h: 177
try:
    EM_SPARC = 2
except:
    pass

# /usr/include/elf.h: 178
try:
    EM_386 = 3
except:
    pass

# /usr/include/elf.h: 179
try:
    EM_68K = 4
except:
    pass

# /usr/include/elf.h: 180
try:
    EM_88K = 5
except:
    pass

# /usr/include/elf.h: 181
try:
    EM_IAMCU = 6
except:
    pass

# /usr/include/elf.h: 182
try:
    EM_860 = 7
except:
    pass

# /usr/include/elf.h: 183
try:
    EM_MIPS = 8
except:
    pass

# /usr/include/elf.h: 184
try:
    EM_S370 = 9
except:
    pass

# /usr/include/elf.h: 185
try:
    EM_MIPS_RS3_LE = 10
except:
    pass

# /usr/include/elf.h: 187
try:
    EM_PARISC = 15
except:
    pass

# /usr/include/elf.h: 189
try:
    EM_VPP500 = 17
except:
    pass

# /usr/include/elf.h: 190
try:
    EM_SPARC32PLUS = 18
except:
    pass

# /usr/include/elf.h: 191
try:
    EM_960 = 19
except:
    pass

# /usr/include/elf.h: 192
try:
    EM_PPC = 20
except:
    pass

# /usr/include/elf.h: 193
try:
    EM_PPC64 = 21
except:
    pass

# /usr/include/elf.h: 194
try:
    EM_S390 = 22
except:
    pass

# /usr/include/elf.h: 195
try:
    EM_SPU = 23
except:
    pass

# /usr/include/elf.h: 197
try:
    EM_V800 = 36
except:
    pass

# /usr/include/elf.h: 198
try:
    EM_FR20 = 37
except:
    pass

# /usr/include/elf.h: 199
try:
    EM_RH32 = 38
except:
    pass

# /usr/include/elf.h: 200
try:
    EM_RCE = 39
except:
    pass

# /usr/include/elf.h: 201
try:
    EM_ARM = 40
except:
    pass

# /usr/include/elf.h: 202
try:
    EM_FAKE_ALPHA = 41
except:
    pass

# /usr/include/elf.h: 203
try:
    EM_SH = 42
except:
    pass

# /usr/include/elf.h: 204
try:
    EM_SPARCV9 = 43
except:
    pass

# /usr/include/elf.h: 205
try:
    EM_TRICORE = 44
except:
    pass

# /usr/include/elf.h: 206
try:
    EM_ARC = 45
except:
    pass

# /usr/include/elf.h: 207
try:
    EM_H8_300 = 46
except:
    pass

# /usr/include/elf.h: 208
try:
    EM_H8_300H = 47
except:
    pass

# /usr/include/elf.h: 209
try:
    EM_H8S = 48
except:
    pass

# /usr/include/elf.h: 210
try:
    EM_H8_500 = 49
except:
    pass

# /usr/include/elf.h: 211
try:
    EM_IA_64 = 50
except:
    pass

# /usr/include/elf.h: 212
try:
    EM_MIPS_X = 51
except:
    pass

# /usr/include/elf.h: 213
try:
    EM_COLDFIRE = 52
except:
    pass

# /usr/include/elf.h: 214
try:
    EM_68HC12 = 53
except:
    pass

# /usr/include/elf.h: 215
try:
    EM_MMA = 54
except:
    pass

# /usr/include/elf.h: 216
try:
    EM_PCP = 55
except:
    pass

# /usr/include/elf.h: 217
try:
    EM_NCPU = 56
except:
    pass

# /usr/include/elf.h: 218
try:
    EM_NDR1 = 57
except:
    pass

# /usr/include/elf.h: 219
try:
    EM_STARCORE = 58
except:
    pass

# /usr/include/elf.h: 220
try:
    EM_ME16 = 59
except:
    pass

# /usr/include/elf.h: 221
try:
    EM_ST100 = 60
except:
    pass

# /usr/include/elf.h: 222
try:
    EM_TINYJ = 61
except:
    pass

# /usr/include/elf.h: 223
try:
    EM_X86_64 = 62
except:
    pass

# /usr/include/elf.h: 224
try:
    EM_PDSP = 63
except:
    pass

# /usr/include/elf.h: 225
try:
    EM_PDP10 = 64
except:
    pass

# /usr/include/elf.h: 226
try:
    EM_PDP11 = 65
except:
    pass

# /usr/include/elf.h: 227
try:
    EM_FX66 = 66
except:
    pass

# /usr/include/elf.h: 228
try:
    EM_ST9PLUS = 67
except:
    pass

# /usr/include/elf.h: 229
try:
    EM_ST7 = 68
except:
    pass

# /usr/include/elf.h: 230
try:
    EM_68HC16 = 69
except:
    pass

# /usr/include/elf.h: 231
try:
    EM_68HC11 = 70
except:
    pass

# /usr/include/elf.h: 232
try:
    EM_68HC08 = 71
except:
    pass

# /usr/include/elf.h: 233
try:
    EM_68HC05 = 72
except:
    pass

# /usr/include/elf.h: 234
try:
    EM_SVX = 73
except:
    pass

# /usr/include/elf.h: 235
try:
    EM_ST19 = 74
except:
    pass

# /usr/include/elf.h: 236
try:
    EM_VAX = 75
except:
    pass

# /usr/include/elf.h: 237
try:
    EM_CRIS = 76
except:
    pass

# /usr/include/elf.h: 238
try:
    EM_JAVELIN = 77
except:
    pass

# /usr/include/elf.h: 239
try:
    EM_FIREPATH = 78
except:
    pass

# /usr/include/elf.h: 240
try:
    EM_ZSP = 79
except:
    pass

# /usr/include/elf.h: 241
try:
    EM_MMIX = 80
except:
    pass

# /usr/include/elf.h: 242
try:
    EM_HUANY = 81
except:
    pass

# /usr/include/elf.h: 243
try:
    EM_PRISM = 82
except:
    pass

# /usr/include/elf.h: 244
try:
    EM_AVR = 83
except:
    pass

# /usr/include/elf.h: 245
try:
    EM_FR30 = 84
except:
    pass

# /usr/include/elf.h: 246
try:
    EM_D10V = 85
except:
    pass

# /usr/include/elf.h: 247
try:
    EM_D30V = 86
except:
    pass

# /usr/include/elf.h: 248
try:
    EM_V850 = 87
except:
    pass

# /usr/include/elf.h: 249
try:
    EM_M32R = 88
except:
    pass

# /usr/include/elf.h: 250
try:
    EM_MN10300 = 89
except:
    pass

# /usr/include/elf.h: 251
try:
    EM_MN10200 = 90
except:
    pass

# /usr/include/elf.h: 252
try:
    EM_PJ = 91
except:
    pass

# /usr/include/elf.h: 253
try:
    EM_OPENRISC = 92
except:
    pass

# /usr/include/elf.h: 254
try:
    EM_ARC_COMPACT = 93
except:
    pass

# /usr/include/elf.h: 255
try:
    EM_XTENSA = 94
except:
    pass

# /usr/include/elf.h: 256
try:
    EM_VIDEOCORE = 95
except:
    pass

# /usr/include/elf.h: 257
try:
    EM_TMM_GPP = 96
except:
    pass

# /usr/include/elf.h: 258
try:
    EM_NS32K = 97
except:
    pass

# /usr/include/elf.h: 259
try:
    EM_TPC = 98
except:
    pass

# /usr/include/elf.h: 260
try:
    EM_SNP1K = 99
except:
    pass

# /usr/include/elf.h: 261
try:
    EM_ST200 = 100
except:
    pass

# /usr/include/elf.h: 262
try:
    EM_IP2K = 101
except:
    pass

# /usr/include/elf.h: 263
try:
    EM_MAX = 102
except:
    pass

# /usr/include/elf.h: 264
try:
    EM_CR = 103
except:
    pass

# /usr/include/elf.h: 265
try:
    EM_F2MC16 = 104
except:
    pass

# /usr/include/elf.h: 266
try:
    EM_MSP430 = 105
except:
    pass

# /usr/include/elf.h: 267
try:
    EM_BLACKFIN = 106
except:
    pass

# /usr/include/elf.h: 268
try:
    EM_SE_C33 = 107
except:
    pass

# /usr/include/elf.h: 269
try:
    EM_SEP = 108
except:
    pass

# /usr/include/elf.h: 270
try:
    EM_ARCA = 109
except:
    pass

# /usr/include/elf.h: 271
try:
    EM_UNICORE = 110
except:
    pass

# /usr/include/elf.h: 272
try:
    EM_EXCESS = 111
except:
    pass

# /usr/include/elf.h: 273
try:
    EM_DXP = 112
except:
    pass

# /usr/include/elf.h: 274
try:
    EM_ALTERA_NIOS2 = 113
except:
    pass

# /usr/include/elf.h: 275
try:
    EM_CRX = 114
except:
    pass

# /usr/include/elf.h: 276
try:
    EM_XGATE = 115
except:
    pass

# /usr/include/elf.h: 277
try:
    EM_C166 = 116
except:
    pass

# /usr/include/elf.h: 278
try:
    EM_M16C = 117
except:
    pass

# /usr/include/elf.h: 279
try:
    EM_DSPIC30F = 118
except:
    pass

# /usr/include/elf.h: 280
try:
    EM_CE = 119
except:
    pass

# /usr/include/elf.h: 281
try:
    EM_M32C = 120
except:
    pass

# /usr/include/elf.h: 283
try:
    EM_TSK3000 = 131
except:
    pass

# /usr/include/elf.h: 284
try:
    EM_RS08 = 132
except:
    pass

# /usr/include/elf.h: 285
try:
    EM_SHARC = 133
except:
    pass

# /usr/include/elf.h: 286
try:
    EM_ECOG2 = 134
except:
    pass

# /usr/include/elf.h: 287
try:
    EM_SCORE7 = 135
except:
    pass

# /usr/include/elf.h: 288
try:
    EM_DSP24 = 136
except:
    pass

# /usr/include/elf.h: 289
try:
    EM_VIDEOCORE3 = 137
except:
    pass

# /usr/include/elf.h: 290
try:
    EM_LATTICEMICO32 = 138
except:
    pass

# /usr/include/elf.h: 291
try:
    EM_SE_C17 = 139
except:
    pass

# /usr/include/elf.h: 292
try:
    EM_TI_C6000 = 140
except:
    pass

# /usr/include/elf.h: 293
try:
    EM_TI_C2000 = 141
except:
    pass

# /usr/include/elf.h: 294
try:
    EM_TI_C5500 = 142
except:
    pass

# /usr/include/elf.h: 295
try:
    EM_TI_ARP32 = 143
except:
    pass

# /usr/include/elf.h: 296
try:
    EM_TI_PRU = 144
except:
    pass

# /usr/include/elf.h: 298
try:
    EM_MMDSP_PLUS = 160
except:
    pass

# /usr/include/elf.h: 299
try:
    EM_CYPRESS_M8C = 161
except:
    pass

# /usr/include/elf.h: 300
try:
    EM_R32C = 162
except:
    pass

# /usr/include/elf.h: 301
try:
    EM_TRIMEDIA = 163
except:
    pass

# /usr/include/elf.h: 302
try:
    EM_QDSP6 = 164
except:
    pass

# /usr/include/elf.h: 303
try:
    EM_8051 = 165
except:
    pass

# /usr/include/elf.h: 304
try:
    EM_STXP7X = 166
except:
    pass

# /usr/include/elf.h: 305
try:
    EM_NDS32 = 167
except:
    pass

# /usr/include/elf.h: 306
try:
    EM_ECOG1X = 168
except:
    pass

# /usr/include/elf.h: 307
try:
    EM_MAXQ30 = 169
except:
    pass

# /usr/include/elf.h: 308
try:
    EM_XIMO16 = 170
except:
    pass

# /usr/include/elf.h: 309
try:
    EM_MANIK = 171
except:
    pass

# /usr/include/elf.h: 310
try:
    EM_CRAYNV2 = 172
except:
    pass

# /usr/include/elf.h: 311
try:
    EM_RX = 173
except:
    pass

# /usr/include/elf.h: 312
try:
    EM_METAG = 174
except:
    pass

# /usr/include/elf.h: 313
try:
    EM_MCST_ELBRUS = 175
except:
    pass

# /usr/include/elf.h: 314
try:
    EM_ECOG16 = 176
except:
    pass

# /usr/include/elf.h: 315
try:
    EM_CR16 = 177
except:
    pass

# /usr/include/elf.h: 316
try:
    EM_ETPU = 178
except:
    pass

# /usr/include/elf.h: 317
try:
    EM_SLE9X = 179
except:
    pass

# /usr/include/elf.h: 318
try:
    EM_L10M = 180
except:
    pass

# /usr/include/elf.h: 319
try:
    EM_K10M = 181
except:
    pass

# /usr/include/elf.h: 321
try:
    EM_AARCH64 = 183
except:
    pass

# /usr/include/elf.h: 323
try:
    EM_AVR32 = 185
except:
    pass

# /usr/include/elf.h: 324
try:
    EM_STM8 = 186
except:
    pass

# /usr/include/elf.h: 325
try:
    EM_TILE64 = 187
except:
    pass

# /usr/include/elf.h: 326
try:
    EM_TILEPRO = 188
except:
    pass

# /usr/include/elf.h: 327
try:
    EM_MICROBLAZE = 189
except:
    pass

# /usr/include/elf.h: 328
try:
    EM_CUDA = 190
except:
    pass

# /usr/include/elf.h: 329
try:
    EM_TILEGX = 191
except:
    pass

# /usr/include/elf.h: 330
try:
    EM_CLOUDSHIELD = 192
except:
    pass

# /usr/include/elf.h: 331
try:
    EM_COREA_1ST = 193
except:
    pass

# /usr/include/elf.h: 332
try:
    EM_COREA_2ND = 194
except:
    pass

# /usr/include/elf.h: 333
try:
    EM_ARC_COMPACT2 = 195
except:
    pass

# /usr/include/elf.h: 334
try:
    EM_OPEN8 = 196
except:
    pass

# /usr/include/elf.h: 335
try:
    EM_RL78 = 197
except:
    pass

# /usr/include/elf.h: 336
try:
    EM_VIDEOCORE5 = 198
except:
    pass

# /usr/include/elf.h: 337
try:
    EM_78KOR = 199
except:
    pass

# /usr/include/elf.h: 338
try:
    EM_56800EX = 200
except:
    pass

# /usr/include/elf.h: 339
try:
    EM_BA1 = 201
except:
    pass

# /usr/include/elf.h: 340
try:
    EM_BA2 = 202
except:
    pass

# /usr/include/elf.h: 341
try:
    EM_XCORE = 203
except:
    pass

# /usr/include/elf.h: 342
try:
    EM_MCHP_PIC = 204
except:
    pass

# /usr/include/elf.h: 344
try:
    EM_KM32 = 210
except:
    pass

# /usr/include/elf.h: 345
try:
    EM_KMX32 = 211
except:
    pass

# /usr/include/elf.h: 346
try:
    EM_EMX16 = 212
except:
    pass

# /usr/include/elf.h: 347
try:
    EM_EMX8 = 213
except:
    pass

# /usr/include/elf.h: 348
try:
    EM_KVARC = 214
except:
    pass

# /usr/include/elf.h: 349
try:
    EM_CDP = 215
except:
    pass

# /usr/include/elf.h: 350
try:
    EM_COGE = 216
except:
    pass

# /usr/include/elf.h: 351
try:
    EM_COOL = 217
except:
    pass

# /usr/include/elf.h: 352
try:
    EM_NORC = 218
except:
    pass

# /usr/include/elf.h: 353
try:
    EM_CSR_KALIMBA = 219
except:
    pass

# /usr/include/elf.h: 354
try:
    EM_Z80 = 220
except:
    pass

# /usr/include/elf.h: 355
try:
    EM_VISIUM = 221
except:
    pass

# /usr/include/elf.h: 356
try:
    EM_FT32 = 222
except:
    pass

# /usr/include/elf.h: 357
try:
    EM_MOXIE = 223
except:
    pass

# /usr/include/elf.h: 358
try:
    EM_AMDGPU = 224
except:
    pass

# /usr/include/elf.h: 360
try:
    EM_RISCV = 243
except:
    pass

# /usr/include/elf.h: 362
try:
    EM_BPF = 247
except:
    pass

# /usr/include/elf.h: 363
try:
    EM_CSKY = 252
except:
    pass

# /usr/include/elf.h: 365
try:
    EM_NUM = 253
except:
    pass

# /usr/include/elf.h: 369
try:
    EM_ARC_A5 = EM_ARC_COMPACT
except:
    pass

# /usr/include/elf.h: 375
try:
    EM_ALPHA = 0x9026
except:
    pass

# /usr/include/elf.h: 379
try:
    EV_NONE = 0
except:
    pass

# /usr/include/elf.h: 380
try:
    EV_CURRENT = 1
except:
    pass

# /usr/include/elf.h: 381
try:
    EV_NUM = 2
except:
    pass

# /usr/include/elf.h: 415
try:
    SHN_UNDEF = 0
except:
    pass

# /usr/include/elf.h: 416
try:
    SHN_LORESERVE = 0xff00
except:
    pass

# /usr/include/elf.h: 417
try:
    SHN_LOPROC = 0xff00
except:
    pass

# /usr/include/elf.h: 418
try:
    SHN_BEFORE = 0xff00
except:
    pass

# /usr/include/elf.h: 420
try:
    SHN_AFTER = 0xff01
except:
    pass

# /usr/include/elf.h: 422
try:
    SHN_HIPROC = 0xff1f
except:
    pass

# /usr/include/elf.h: 423
try:
    SHN_LOOS = 0xff20
except:
    pass

# /usr/include/elf.h: 424
try:
    SHN_HIOS = 0xff3f
except:
    pass

# /usr/include/elf.h: 425
try:
    SHN_ABS = 0xfff1
except:
    pass

# /usr/include/elf.h: 426
try:
    SHN_COMMON = 0xfff2
except:
    pass

# /usr/include/elf.h: 427
try:
    SHN_XINDEX = 0xffff
except:
    pass

# /usr/include/elf.h: 428
try:
    SHN_HIRESERVE = 0xffff
except:
    pass

# /usr/include/elf.h: 432
try:
    SHT_NULL = 0
except:
    pass

# /usr/include/elf.h: 433
try:
    SHT_PROGBITS = 1
except:
    pass

# /usr/include/elf.h: 434
try:
    SHT_SYMTAB = 2
except:
    pass

# /usr/include/elf.h: 435
try:
    SHT_STRTAB = 3
except:
    pass

# /usr/include/elf.h: 436
try:
    SHT_RELA = 4
except:
    pass

# /usr/include/elf.h: 437
try:
    SHT_HASH = 5
except:
    pass

# /usr/include/elf.h: 438
try:
    SHT_DYNAMIC = 6
except:
    pass

# /usr/include/elf.h: 439
try:
    SHT_NOTE = 7
except:
    pass

# /usr/include/elf.h: 440
try:
    SHT_NOBITS = 8
except:
    pass

# /usr/include/elf.h: 441
try:
    SHT_REL = 9
except:
    pass

# /usr/include/elf.h: 442
try:
    SHT_SHLIB = 10
except:
    pass

# /usr/include/elf.h: 443
try:
    SHT_DYNSYM = 11
except:
    pass

# /usr/include/elf.h: 444
try:
    SHT_INIT_ARRAY = 14
except:
    pass

# /usr/include/elf.h: 445
try:
    SHT_FINI_ARRAY = 15
except:
    pass

# /usr/include/elf.h: 446
try:
    SHT_PREINIT_ARRAY = 16
except:
    pass

# /usr/include/elf.h: 447
try:
    SHT_GROUP = 17
except:
    pass

# /usr/include/elf.h: 448
try:
    SHT_SYMTAB_SHNDX = 18
except:
    pass

# /usr/include/elf.h: 449
try:
    SHT_NUM = 19
except:
    pass

# /usr/include/elf.h: 450
try:
    SHT_LOOS = 0x60000000
except:
    pass

# /usr/include/elf.h: 451
try:
    SHT_GNU_ATTRIBUTES = 0x6ffffff5
except:
    pass

# /usr/include/elf.h: 452
try:
    SHT_GNU_HASH = 0x6ffffff6
except:
    pass

# /usr/include/elf.h: 453
try:
    SHT_GNU_LIBLIST = 0x6ffffff7
except:
    pass

# /usr/include/elf.h: 454
try:
    SHT_CHECKSUM = 0x6ffffff8
except:
    pass

# /usr/include/elf.h: 455
try:
    SHT_LOSUNW = 0x6ffffffa
except:
    pass

# /usr/include/elf.h: 456
try:
    SHT_SUNW_move = 0x6ffffffa
except:
    pass

# /usr/include/elf.h: 457
try:
    SHT_SUNW_COMDAT = 0x6ffffffb
except:
    pass

# /usr/include/elf.h: 458
try:
    SHT_SUNW_syminfo = 0x6ffffffc
except:
    pass

# /usr/include/elf.h: 459
try:
    SHT_GNU_verdef = 0x6ffffffd
except:
    pass

# /usr/include/elf.h: 460
try:
    SHT_GNU_verneed = 0x6ffffffe
except:
    pass

# /usr/include/elf.h: 461
try:
    SHT_GNU_versym = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 462
try:
    SHT_HISUNW = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 463
try:
    SHT_HIOS = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 464
try:
    SHT_LOPROC = 0x70000000
except:
    pass

# /usr/include/elf.h: 465
try:
    SHT_HIPROC = 0x7fffffff
except:
    pass

# /usr/include/elf.h: 466
try:
    SHT_LOUSER = 0x80000000
except:
    pass

# /usr/include/elf.h: 467
try:
    SHT_HIUSER = 0x8fffffff
except:
    pass

# /usr/include/elf.h: 471
try:
    SHF_WRITE = (1 << 0)
except:
    pass

# /usr/include/elf.h: 472
try:
    SHF_ALLOC = (1 << 1)
except:
    pass

# /usr/include/elf.h: 473
try:
    SHF_EXECINSTR = (1 << 2)
except:
    pass

# /usr/include/elf.h: 474
try:
    SHF_MERGE = (1 << 4)
except:
    pass

# /usr/include/elf.h: 475
try:
    SHF_STRINGS = (1 << 5)
except:
    pass

# /usr/include/elf.h: 476
try:
    SHF_INFO_LINK = (1 << 6)
except:
    pass

# /usr/include/elf.h: 477
try:
    SHF_LINK_ORDER = (1 << 7)
except:
    pass

# /usr/include/elf.h: 478
try:
    SHF_OS_NONCONFORMING = (1 << 8)
except:
    pass

# /usr/include/elf.h: 480
try:
    SHF_GROUP = (1 << 9)
except:
    pass

# /usr/include/elf.h: 481
try:
    SHF_TLS = (1 << 10)
except:
    pass

# /usr/include/elf.h: 482
try:
    SHF_COMPRESSED = (1 << 11)
except:
    pass

# /usr/include/elf.h: 483
try:
    SHF_MASKOS = 0x0ff00000
except:
    pass

# /usr/include/elf.h: 484
try:
    SHF_MASKPROC = 0xf0000000
except:
    pass

# /usr/include/elf.h: 485
try:
    SHF_ORDERED = (1 << 30)
except:
    pass

# /usr/include/elf.h: 487
try:
    SHF_EXCLUDE = (1 << 31)
except:
    pass

# /usr/include/elf.h: 508
try:
    ELFCOMPRESS_ZLIB = 1
except:
    pass

# /usr/include/elf.h: 509
try:
    ELFCOMPRESS_LOOS = 0x60000000
except:
    pass

# /usr/include/elf.h: 510
try:
    ELFCOMPRESS_HIOS = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 511
try:
    ELFCOMPRESS_LOPROC = 0x70000000
except:
    pass

# /usr/include/elf.h: 512
try:
    ELFCOMPRESS_HIPROC = 0x7fffffff
except:
    pass

# /usr/include/elf.h: 515
try:
    GRP_COMDAT = 0x1
except:
    pass

# /usr/include/elf.h: 555
try:
    SYMINFO_BT_SELF = 0xffff
except:
    pass

# /usr/include/elf.h: 556
try:
    SYMINFO_BT_PARENT = 0xfffe
except:
    pass

# /usr/include/elf.h: 557
try:
    SYMINFO_BT_LOWRESERVE = 0xff00
except:
    pass

# /usr/include/elf.h: 560
try:
    SYMINFO_FLG_DIRECT = 0x0001
except:
    pass

# /usr/include/elf.h: 561
try:
    SYMINFO_FLG_PASSTHRU = 0x0002
except:
    pass

# /usr/include/elf.h: 562
try:
    SYMINFO_FLG_COPY = 0x0004
except:
    pass

# /usr/include/elf.h: 563
try:
    SYMINFO_FLG_LAZYLOAD = 0x0008
except:
    pass

# /usr/include/elf.h: 566
try:
    SYMINFO_NONE = 0
except:
    pass

# /usr/include/elf.h: 567
try:
    SYMINFO_CURRENT = 1
except:
    pass

# /usr/include/elf.h: 568
try:
    SYMINFO_NUM = 2
except:
    pass

# /usr/include/elf.h: 573
def ELF32_ST_BIND(val):
    return ((c_ubyte (ord_if_char(val))).value >> 4)

# /usr/include/elf.h: 574
def ELF32_ST_TYPE(val):
    return (val & 0xf)

# /usr/include/elf.h: 575
def ELF32_ST_INFO(bind, type):
    return ((bind << 4) + (type & 0xf))

# /usr/include/elf.h: 578
def ELF64_ST_BIND(val):
    return (ELF32_ST_BIND (val))

# /usr/include/elf.h: 579
def ELF64_ST_TYPE(val):
    return (ELF32_ST_TYPE (val))

# /usr/include/elf.h: 580
def ELF64_ST_INFO(bind, type):
    return (ELF32_ST_INFO (bind, type))

# /usr/include/elf.h: 584
try:
    STB_LOCAL = 0
except:
    pass

# /usr/include/elf.h: 585
try:
    STB_GLOBAL = 1
except:
    pass

# /usr/include/elf.h: 586
try:
    STB_WEAK = 2
except:
    pass

# /usr/include/elf.h: 587
try:
    STB_NUM = 3
except:
    pass

# /usr/include/elf.h: 588
try:
    STB_LOOS = 10
except:
    pass

# /usr/include/elf.h: 589
try:
    STB_GNU_UNIQUE = 10
except:
    pass

# /usr/include/elf.h: 590
try:
    STB_HIOS = 12
except:
    pass

# /usr/include/elf.h: 591
try:
    STB_LOPROC = 13
except:
    pass

# /usr/include/elf.h: 592
try:
    STB_HIPROC = 15
except:
    pass

# /usr/include/elf.h: 596
try:
    STT_NOTYPE = 0
except:
    pass

# /usr/include/elf.h: 597
try:
    STT_OBJECT = 1
except:
    pass

# /usr/include/elf.h: 598
try:
    STT_FUNC = 2
except:
    pass

# /usr/include/elf.h: 599
try:
    STT_SECTION = 3
except:
    pass

# /usr/include/elf.h: 600
try:
    STT_FILE = 4
except:
    pass

# /usr/include/elf.h: 601
try:
    STT_COMMON = 5
except:
    pass

# /usr/include/elf.h: 602
try:
    STT_TLS = 6
except:
    pass

# /usr/include/elf.h: 603
try:
    STT_NUM = 7
except:
    pass

# /usr/include/elf.h: 604
try:
    STT_LOOS = 10
except:
    pass

# /usr/include/elf.h: 605
try:
    STT_GNU_IFUNC = 10
except:
    pass

# /usr/include/elf.h: 606
try:
    STT_HIOS = 12
except:
    pass

# /usr/include/elf.h: 607
try:
    STT_LOPROC = 13
except:
    pass

# /usr/include/elf.h: 608
try:
    STT_HIPROC = 15
except:
    pass

# /usr/include/elf.h: 615
try:
    STN_UNDEF = 0
except:
    pass

# /usr/include/elf.h: 620
def ELF32_ST_VISIBILITY(o):
    return (o & 0x03)

# /usr/include/elf.h: 623
def ELF64_ST_VISIBILITY(o):
    return (ELF32_ST_VISIBILITY (o))

# /usr/include/elf.h: 626
try:
    STV_DEFAULT = 0
except:
    pass

# /usr/include/elf.h: 627
try:
    STV_INTERNAL = 1
except:
    pass

# /usr/include/elf.h: 628
try:
    STV_HIDDEN = 2
except:
    pass

# /usr/include/elf.h: 629
try:
    STV_PROTECTED = 3
except:
    pass

# /usr/include/elf.h: 669
def ELF32_R_SYM(val):
    return (val >> 8)

# /usr/include/elf.h: 670
def ELF32_R_TYPE(val):
    return (val & 0xff)

# /usr/include/elf.h: 671
def ELF32_R_INFO(sym, type):
    return ((sym << 8) + (type & 0xff))

# /usr/include/elf.h: 673
def ELF64_R_SYM(i):
    return (i >> 32)

# /usr/include/elf.h: 674
def ELF64_R_TYPE(i):
    return (i & 0xffffffff)

# /usr/include/elf.h: 675
def ELF64_R_INFO(sym, type):
    return (((Elf64_Xword (ord_if_char(sym))).value << 32) + type)

# /usr/include/elf.h: 707
try:
    PN_XNUM = 0xffff
except:
    pass

# /usr/include/elf.h: 711
try:
    PT_NULL = 0
except:
    pass

# /usr/include/elf.h: 712
try:
    PT_LOAD = 1
except:
    pass

# /usr/include/elf.h: 713
try:
    PT_DYNAMIC = 2
except:
    pass

# /usr/include/elf.h: 714
try:
    PT_INTERP = 3
except:
    pass

# /usr/include/elf.h: 715
try:
    PT_NOTE = 4
except:
    pass

# /usr/include/elf.h: 716
try:
    PT_SHLIB = 5
except:
    pass

# /usr/include/elf.h: 717
try:
    PT_PHDR = 6
except:
    pass

# /usr/include/elf.h: 718
try:
    PT_TLS = 7
except:
    pass

# /usr/include/elf.h: 719
try:
    PT_NUM = 8
except:
    pass

# /usr/include/elf.h: 720
try:
    PT_LOOS = 0x60000000
except:
    pass

# /usr/include/elf.h: 721
try:
    PT_GNU_EH_FRAME = 0x6474e550
except:
    pass

# /usr/include/elf.h: 722
try:
    PT_GNU_STACK = 0x6474e551
except:
    pass

# /usr/include/elf.h: 723
try:
    PT_GNU_RELRO = 0x6474e552
except:
    pass

# /usr/include/elf.h: 724
try:
    PT_LOSUNW = 0x6ffffffa
except:
    pass

# /usr/include/elf.h: 725
try:
    PT_SUNWBSS = 0x6ffffffa
except:
    pass

# /usr/include/elf.h: 726
try:
    PT_SUNWSTACK = 0x6ffffffb
except:
    pass

# /usr/include/elf.h: 727
try:
    PT_HISUNW = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 728
try:
    PT_HIOS = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 729
try:
    PT_LOPROC = 0x70000000
except:
    pass

# /usr/include/elf.h: 730
try:
    PT_HIPROC = 0x7fffffff
except:
    pass

# /usr/include/elf.h: 734
try:
    PF_X = (1 << 0)
except:
    pass

# /usr/include/elf.h: 735
try:
    PF_W = (1 << 1)
except:
    pass

# /usr/include/elf.h: 736
try:
    PF_R = (1 << 2)
except:
    pass

# /usr/include/elf.h: 737
try:
    PF_MASKOS = 0x0ff00000
except:
    pass

# /usr/include/elf.h: 738
try:
    PF_MASKPROC = 0xf0000000
except:
    pass

# /usr/include/elf.h: 742
try:
    NT_PRSTATUS = 1
except:
    pass

# /usr/include/elf.h: 743
try:
    NT_PRFPREG = 2
except:
    pass

# /usr/include/elf.h: 745
try:
    NT_FPREGSET = 2
except:
    pass

# /usr/include/elf.h: 746
try:
    NT_PRPSINFO = 3
except:
    pass

# /usr/include/elf.h: 747
try:
    NT_PRXREG = 4
except:
    pass

# /usr/include/elf.h: 748
try:
    NT_TASKSTRUCT = 4
except:
    pass

# /usr/include/elf.h: 749
try:
    NT_PLATFORM = 5
except:
    pass

# /usr/include/elf.h: 750
try:
    NT_AUXV = 6
except:
    pass

# /usr/include/elf.h: 751
try:
    NT_GWINDOWS = 7
except:
    pass

# /usr/include/elf.h: 752
try:
    NT_ASRS = 8
except:
    pass

# /usr/include/elf.h: 753
try:
    NT_PSTATUS = 10
except:
    pass

# /usr/include/elf.h: 754
try:
    NT_PSINFO = 13
except:
    pass

# /usr/include/elf.h: 755
try:
    NT_PRCRED = 14
except:
    pass

# /usr/include/elf.h: 756
try:
    NT_UTSNAME = 15
except:
    pass

# /usr/include/elf.h: 757
try:
    NT_LWPSTATUS = 16
except:
    pass

# /usr/include/elf.h: 758
try:
    NT_LWPSINFO = 17
except:
    pass

# /usr/include/elf.h: 759
try:
    NT_PRFPXREG = 20
except:
    pass

# /usr/include/elf.h: 760
try:
    NT_SIGINFO = 0x53494749
except:
    pass

# /usr/include/elf.h: 762
try:
    NT_FILE = 0x46494c45
except:
    pass

# /usr/include/elf.h: 764
try:
    NT_PRXFPREG = 0x46e62b7f
except:
    pass

# /usr/include/elf.h: 765
try:
    NT_PPC_VMX = 0x100
except:
    pass

# /usr/include/elf.h: 766
try:
    NT_PPC_SPE = 0x101
except:
    pass

# /usr/include/elf.h: 767
try:
    NT_PPC_VSX = 0x102
except:
    pass

# /usr/include/elf.h: 768
try:
    NT_PPC_TAR = 0x103
except:
    pass

# /usr/include/elf.h: 769
try:
    NT_PPC_PPR = 0x104
except:
    pass

# /usr/include/elf.h: 770
try:
    NT_PPC_DSCR = 0x105
except:
    pass

# /usr/include/elf.h: 771
try:
    NT_PPC_EBB = 0x106
except:
    pass

# /usr/include/elf.h: 772
try:
    NT_PPC_PMU = 0x107
except:
    pass

# /usr/include/elf.h: 773
try:
    NT_PPC_TM_CGPR = 0x108
except:
    pass

# /usr/include/elf.h: 774
try:
    NT_PPC_TM_CFPR = 0x109
except:
    pass

# /usr/include/elf.h: 775
try:
    NT_PPC_TM_CVMX = 0x10a
except:
    pass

# /usr/include/elf.h: 776
try:
    NT_PPC_TM_CVSX = 0x10b
except:
    pass

# /usr/include/elf.h: 777
try:
    NT_PPC_TM_SPR = 0x10c
except:
    pass

# /usr/include/elf.h: 778
try:
    NT_PPC_TM_CTAR = 0x10d
except:
    pass

# /usr/include/elf.h: 780
try:
    NT_PPC_TM_CPPR = 0x10e
except:
    pass

# /usr/include/elf.h: 782
try:
    NT_PPC_TM_CDSCR = 0x10f
except:
    pass

# /usr/include/elf.h: 784
try:
    NT_PPC_PKEY = 0x110
except:
    pass

# /usr/include/elf.h: 786
try:
    NT_386_TLS = 0x200
except:
    pass

# /usr/include/elf.h: 787
try:
    NT_386_IOPERM = 0x201
except:
    pass

# /usr/include/elf.h: 788
try:
    NT_X86_XSTATE = 0x202
except:
    pass

# /usr/include/elf.h: 789
try:
    NT_S390_HIGH_GPRS = 0x300
except:
    pass

# /usr/include/elf.h: 790
try:
    NT_S390_TIMER = 0x301
except:
    pass

# /usr/include/elf.h: 791
try:
    NT_S390_TODCMP = 0x302
except:
    pass

# /usr/include/elf.h: 792
try:
    NT_S390_TODPREG = 0x303
except:
    pass

# /usr/include/elf.h: 793
try:
    NT_S390_CTRS = 0x304
except:
    pass

# /usr/include/elf.h: 794
try:
    NT_S390_PREFIX = 0x305
except:
    pass

# /usr/include/elf.h: 795
try:
    NT_S390_LAST_BREAK = 0x306
except:
    pass

# /usr/include/elf.h: 796
try:
    NT_S390_SYSTEM_CALL = 0x307
except:
    pass

# /usr/include/elf.h: 797
try:
    NT_S390_TDB = 0x308
except:
    pass

# /usr/include/elf.h: 798
try:
    NT_S390_VXRS_LOW = 0x309
except:
    pass

# /usr/include/elf.h: 800
try:
    NT_S390_VXRS_HIGH = 0x30a
except:
    pass

# /usr/include/elf.h: 801
try:
    NT_S390_GS_CB = 0x30b
except:
    pass

# /usr/include/elf.h: 802
try:
    NT_S390_GS_BC = 0x30c
except:
    pass

# /usr/include/elf.h: 804
try:
    NT_S390_RI_CB = 0x30d
except:
    pass

# /usr/include/elf.h: 805
try:
    NT_ARM_VFP = 0x400
except:
    pass

# /usr/include/elf.h: 806
try:
    NT_ARM_TLS = 0x401
except:
    pass

# /usr/include/elf.h: 807
try:
    NT_ARM_HW_BREAK = 0x402
except:
    pass

# /usr/include/elf.h: 808
try:
    NT_ARM_HW_WATCH = 0x403
except:
    pass

# /usr/include/elf.h: 809
try:
    NT_ARM_SYSTEM_CALL = 0x404
except:
    pass

# /usr/include/elf.h: 810
try:
    NT_ARM_SVE = 0x405
except:
    pass

# /usr/include/elf.h: 812
try:
    NT_ARM_PAC_MASK = 0x406
except:
    pass

# /usr/include/elf.h: 814
try:
    NT_ARM_PACA_KEYS = 0x407
except:
    pass

# /usr/include/elf.h: 816
try:
    NT_ARM_PACG_KEYS = 0x408
except:
    pass

# /usr/include/elf.h: 818
try:
    NT_VMCOREDD = 0x700
except:
    pass

# /usr/include/elf.h: 819
try:
    NT_MIPS_DSP = 0x800
except:
    pass

# /usr/include/elf.h: 820
try:
    NT_MIPS_FP_MODE = 0x801
except:
    pass

# /usr/include/elf.h: 821
try:
    NT_MIPS_MSA = 0x802
except:
    pass

# /usr/include/elf.h: 825
try:
    NT_VERSION = 1
except:
    pass

# /usr/include/elf.h: 852
try:
    DT_NULL = 0
except:
    pass

# /usr/include/elf.h: 853
try:
    DT_NEEDED = 1
except:
    pass

# /usr/include/elf.h: 854
try:
    DT_PLTRELSZ = 2
except:
    pass

# /usr/include/elf.h: 855
try:
    DT_PLTGOT = 3
except:
    pass

# /usr/include/elf.h: 856
try:
    DT_HASH = 4
except:
    pass

# /usr/include/elf.h: 857
try:
    DT_STRTAB = 5
except:
    pass

# /usr/include/elf.h: 858
try:
    DT_SYMTAB = 6
except:
    pass

# /usr/include/elf.h: 859
try:
    DT_RELA = 7
except:
    pass

# /usr/include/elf.h: 860
try:
    DT_RELASZ = 8
except:
    pass

# /usr/include/elf.h: 861
try:
    DT_RELAENT = 9
except:
    pass

# /usr/include/elf.h: 862
try:
    DT_STRSZ = 10
except:
    pass

# /usr/include/elf.h: 863
try:
    DT_SYMENT = 11
except:
    pass

# /usr/include/elf.h: 864
try:
    DT_INIT = 12
except:
    pass

# /usr/include/elf.h: 865
try:
    DT_FINI = 13
except:
    pass

# /usr/include/elf.h: 866
try:
    DT_SONAME = 14
except:
    pass

# /usr/include/elf.h: 867
try:
    DT_RPATH = 15
except:
    pass

# /usr/include/elf.h: 868
try:
    DT_SYMBOLIC = 16
except:
    pass

# /usr/include/elf.h: 869
try:
    DT_REL = 17
except:
    pass

# /usr/include/elf.h: 870
try:
    DT_RELSZ = 18
except:
    pass

# /usr/include/elf.h: 871
try:
    DT_RELENT = 19
except:
    pass

# /usr/include/elf.h: 872
try:
    DT_PLTREL = 20
except:
    pass

# /usr/include/elf.h: 873
try:
    DT_DEBUG = 21
except:
    pass

# /usr/include/elf.h: 874
try:
    DT_TEXTREL = 22
except:
    pass

# /usr/include/elf.h: 875
try:
    DT_JMPREL = 23
except:
    pass

# /usr/include/elf.h: 876
try:
    DT_BIND_NOW = 24
except:
    pass

# /usr/include/elf.h: 877
try:
    DT_INIT_ARRAY = 25
except:
    pass

# /usr/include/elf.h: 878
try:
    DT_FINI_ARRAY = 26
except:
    pass

# /usr/include/elf.h: 879
try:
    DT_INIT_ARRAYSZ = 27
except:
    pass

# /usr/include/elf.h: 880
try:
    DT_FINI_ARRAYSZ = 28
except:
    pass

# /usr/include/elf.h: 881
try:
    DT_RUNPATH = 29
except:
    pass

# /usr/include/elf.h: 882
try:
    DT_FLAGS = 30
except:
    pass

# /usr/include/elf.h: 883
try:
    DT_ENCODING = 32
except:
    pass

# /usr/include/elf.h: 884
try:
    DT_PREINIT_ARRAY = 32
except:
    pass

# /usr/include/elf.h: 885
try:
    DT_PREINIT_ARRAYSZ = 33
except:
    pass

# /usr/include/elf.h: 886
try:
    DT_SYMTAB_SHNDX = 34
except:
    pass

# /usr/include/elf.h: 887
try:
    DT_NUM = 35
except:
    pass

# /usr/include/elf.h: 888
try:
    DT_LOOS = 0x6000000d
except:
    pass

# /usr/include/elf.h: 889
try:
    DT_HIOS = 0x6ffff000
except:
    pass

# /usr/include/elf.h: 890
try:
    DT_LOPROC = 0x70000000
except:
    pass

# /usr/include/elf.h: 891
try:
    DT_HIPROC = 0x7fffffff
except:
    pass

# /usr/include/elf.h: 892
try:
    DT_PROCNUM = DT_MIPS_NUM
except:
    pass

# /usr/include/elf.h: 897
try:
    DT_VALRNGLO = 0x6ffffd00
except:
    pass

# /usr/include/elf.h: 898
try:
    DT_GNU_PRELINKED = 0x6ffffdf5
except:
    pass

# /usr/include/elf.h: 899
try:
    DT_GNU_CONFLICTSZ = 0x6ffffdf6
except:
    pass

# /usr/include/elf.h: 900
try:
    DT_GNU_LIBLISTSZ = 0x6ffffdf7
except:
    pass

# /usr/include/elf.h: 901
try:
    DT_CHECKSUM = 0x6ffffdf8
except:
    pass

# /usr/include/elf.h: 902
try:
    DT_PLTPADSZ = 0x6ffffdf9
except:
    pass

# /usr/include/elf.h: 903
try:
    DT_MOVEENT = 0x6ffffdfa
except:
    pass

# /usr/include/elf.h: 904
try:
    DT_MOVESZ = 0x6ffffdfb
except:
    pass

# /usr/include/elf.h: 905
try:
    DT_FEATURE_1 = 0x6ffffdfc
except:
    pass

# /usr/include/elf.h: 906
try:
    DT_POSFLAG_1 = 0x6ffffdfd
except:
    pass

# /usr/include/elf.h: 908
try:
    DT_SYMINSZ = 0x6ffffdfe
except:
    pass

# /usr/include/elf.h: 909
try:
    DT_SYMINENT = 0x6ffffdff
except:
    pass

# /usr/include/elf.h: 910
try:
    DT_VALRNGHI = 0x6ffffdff
except:
    pass

# /usr/include/elf.h: 911
def DT_VALTAGIDX(tag):
    return (DT_VALRNGHI - tag)

# /usr/include/elf.h: 912
try:
    DT_VALNUM = 12
except:
    pass

# /usr/include/elf.h: 919
try:
    DT_ADDRRNGLO = 0x6ffffe00
except:
    pass

# /usr/include/elf.h: 920
try:
    DT_GNU_HASH = 0x6ffffef5
except:
    pass

# /usr/include/elf.h: 921
try:
    DT_TLSDESC_PLT = 0x6ffffef6
except:
    pass

# /usr/include/elf.h: 922
try:
    DT_TLSDESC_GOT = 0x6ffffef7
except:
    pass

# /usr/include/elf.h: 923
try:
    DT_GNU_CONFLICT = 0x6ffffef8
except:
    pass

# /usr/include/elf.h: 924
try:
    DT_GNU_LIBLIST = 0x6ffffef9
except:
    pass

# /usr/include/elf.h: 925
try:
    DT_CONFIG = 0x6ffffefa
except:
    pass

# /usr/include/elf.h: 926
try:
    DT_DEPAUDIT = 0x6ffffefb
except:
    pass

# /usr/include/elf.h: 927
try:
    DT_AUDIT = 0x6ffffefc
except:
    pass

# /usr/include/elf.h: 928
try:
    DT_PLTPAD = 0x6ffffefd
except:
    pass

# /usr/include/elf.h: 929
try:
    DT_MOVETAB = 0x6ffffefe
except:
    pass

# /usr/include/elf.h: 930
try:
    DT_SYMINFO = 0x6ffffeff
except:
    pass

# /usr/include/elf.h: 931
try:
    DT_ADDRRNGHI = 0x6ffffeff
except:
    pass

# /usr/include/elf.h: 932
def DT_ADDRTAGIDX(tag):
    return (DT_ADDRRNGHI - tag)

# /usr/include/elf.h: 933
try:
    DT_ADDRNUM = 11
except:
    pass

# /usr/include/elf.h: 937
try:
    DT_VERSYM = 0x6ffffff0
except:
    pass

# /usr/include/elf.h: 939
try:
    DT_RELACOUNT = 0x6ffffff9
except:
    pass

# /usr/include/elf.h: 940
try:
    DT_RELCOUNT = 0x6ffffffa
except:
    pass

# /usr/include/elf.h: 943
try:
    DT_FLAGS_1 = 0x6ffffffb
except:
    pass

# /usr/include/elf.h: 944
try:
    DT_VERDEF = 0x6ffffffc
except:
    pass

# /usr/include/elf.h: 946
try:
    DT_VERDEFNUM = 0x6ffffffd
except:
    pass

# /usr/include/elf.h: 947
try:
    DT_VERNEED = 0x6ffffffe
except:
    pass

# /usr/include/elf.h: 949
try:
    DT_VERNEEDNUM = 0x6fffffff
except:
    pass

# /usr/include/elf.h: 950
def DT_VERSIONTAGIDX(tag):
    return (DT_VERNEEDNUM - tag)

# /usr/include/elf.h: 951
try:
    DT_VERSIONTAGNUM = 16
except:
    pass

# /usr/include/elf.h: 955
try:
    DT_AUXILIARY = 0x7ffffffd
except:
    pass

# /usr/include/elf.h: 956
try:
    DT_FILTER = 0x7fffffff
except:
    pass

# /usr/include/elf.h: 957
def DT_EXTRATAGIDX(tag):
    return ((Elf32_Word (ord_if_char((-(((Elf32_Sword (ord_if_char(tag))).value << 1) >> 1))))).value - 1)

# /usr/include/elf.h: 958
try:
    DT_EXTRANUM = 3
except:
    pass

# /usr/include/elf.h: 961
try:
    DF_ORIGIN = 0x00000001
except:
    pass

# /usr/include/elf.h: 962
try:
    DF_SYMBOLIC = 0x00000002
except:
    pass

# /usr/include/elf.h: 963
try:
    DF_TEXTREL = 0x00000004
except:
    pass

# /usr/include/elf.h: 964
try:
    DF_BIND_NOW = 0x00000008
except:
    pass

# /usr/include/elf.h: 965
try:
    DF_STATIC_TLS = 0x00000010
except:
    pass

# /usr/include/elf.h: 969
try:
    DF_1_NOW = 0x00000001
except:
    pass

# /usr/include/elf.h: 970
try:
    DF_1_GLOBAL = 0x00000002
except:
    pass

# /usr/include/elf.h: 971
try:
    DF_1_GROUP = 0x00000004
except:
    pass

# /usr/include/elf.h: 972
try:
    DF_1_NODELETE = 0x00000008
except:
    pass

# /usr/include/elf.h: 973
try:
    DF_1_LOADFLTR = 0x00000010
except:
    pass

# /usr/include/elf.h: 974
try:
    DF_1_INITFIRST = 0x00000020
except:
    pass

# /usr/include/elf.h: 975
try:
    DF_1_NOOPEN = 0x00000040
except:
    pass

# /usr/include/elf.h: 976
try:
    DF_1_ORIGIN = 0x00000080
except:
    pass

# /usr/include/elf.h: 977
try:
    DF_1_DIRECT = 0x00000100
except:
    pass

# /usr/include/elf.h: 978
try:
    DF_1_TRANS = 0x00000200
except:
    pass

# /usr/include/elf.h: 979
try:
    DF_1_INTERPOSE = 0x00000400
except:
    pass

# /usr/include/elf.h: 980
try:
    DF_1_NODEFLIB = 0x00000800
except:
    pass

# /usr/include/elf.h: 981
try:
    DF_1_NODUMP = 0x00001000
except:
    pass

# /usr/include/elf.h: 982
try:
    DF_1_CONFALT = 0x00002000
except:
    pass

# /usr/include/elf.h: 983
try:
    DF_1_ENDFILTEE = 0x00004000
except:
    pass

# /usr/include/elf.h: 984
try:
    DF_1_DISPRELDNE = 0x00008000
except:
    pass

# /usr/include/elf.h: 985
try:
    DF_1_DISPRELPND = 0x00010000
except:
    pass

# /usr/include/elf.h: 986
try:
    DF_1_NODIRECT = 0x00020000
except:
    pass

# /usr/include/elf.h: 987
try:
    DF_1_IGNMULDEF = 0x00040000
except:
    pass

# /usr/include/elf.h: 988
try:
    DF_1_NOKSYMS = 0x00080000
except:
    pass

# /usr/include/elf.h: 989
try:
    DF_1_NOHDR = 0x00100000
except:
    pass

# /usr/include/elf.h: 990
try:
    DF_1_EDITED = 0x00200000
except:
    pass

# /usr/include/elf.h: 991
try:
    DF_1_NORELOC = 0x00400000
except:
    pass

# /usr/include/elf.h: 992
try:
    DF_1_SYMINTPOSE = 0x00800000
except:
    pass

# /usr/include/elf.h: 993
try:
    DF_1_GLOBAUDIT = 0x01000000
except:
    pass

# /usr/include/elf.h: 994
try:
    DF_1_SINGLETON = 0x02000000
except:
    pass

# /usr/include/elf.h: 995
try:
    DF_1_STUB = 0x04000000
except:
    pass

# /usr/include/elf.h: 996
try:
    DF_1_PIE = 0x08000000
except:
    pass

# /usr/include/elf.h: 997
try:
    DF_1_KMOD = 0x10000000
except:
    pass

# /usr/include/elf.h: 998
try:
    DF_1_WEAKFILTER = 0x20000000
except:
    pass

# /usr/include/elf.h: 999
try:
    DF_1_NOCOMMON = 0x40000000
except:
    pass

# /usr/include/elf.h: 1002
try:
    DTF_1_PARINIT = 0x00000001
except:
    pass

# /usr/include/elf.h: 1003
try:
    DTF_1_CONFEXP = 0x00000002
except:
    pass

# /usr/include/elf.h: 1006
try:
    DF_P1_LAZYLOAD = 0x00000001
except:
    pass

# /usr/include/elf.h: 1007
try:
    DF_P1_GROUPPERM = 0x00000002
except:
    pass

# /usr/include/elf.h: 1038
try:
    VER_DEF_NONE = 0
except:
    pass

# /usr/include/elf.h: 1039
try:
    VER_DEF_CURRENT = 1
except:
    pass

# /usr/include/elf.h: 1040
try:
    VER_DEF_NUM = 2
except:
    pass

# /usr/include/elf.h: 1043
try:
    VER_FLG_BASE = 0x1
except:
    pass

# /usr/include/elf.h: 1044
try:
    VER_FLG_WEAK = 0x2
except:
    pass

# /usr/include/elf.h: 1047
try:
    VER_NDX_LOCAL = 0
except:
    pass

# /usr/include/elf.h: 1048
try:
    VER_NDX_GLOBAL = 1
except:
    pass

# /usr/include/elf.h: 1049
try:
    VER_NDX_LORESERVE = 0xff00
except:
    pass

# /usr/include/elf.h: 1050
try:
    VER_NDX_ELIMINATE = 0xff01
except:
    pass

# /usr/include/elf.h: 1095
try:
    VER_NEED_NONE = 0
except:
    pass

# /usr/include/elf.h: 1096
try:
    VER_NEED_CURRENT = 1
except:
    pass

# /usr/include/elf.h: 1097
try:
    VER_NEED_NUM = 2
except:
    pass

# /usr/include/elf.h: 1123
try:
    VER_FLG_WEAK = 0x2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 20
try:
    AT_NULL = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 21
try:
    AT_IGNORE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 22
try:
    AT_EXECFD = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 23
try:
    AT_PHDR = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 24
try:
    AT_PHENT = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 25
try:
    AT_PHNUM = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 26
try:
    AT_PAGESZ = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 27
try:
    AT_BASE = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 28
try:
    AT_FLAGS = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 29
try:
    AT_ENTRY = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 30
try:
    AT_NOTELF = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 31
try:
    AT_UID = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 32
try:
    AT_EUID = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 33
try:
    AT_GID = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 34
try:
    AT_EGID = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 35
try:
    AT_CLKTCK = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 38
try:
    AT_PLATFORM = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 39
try:
    AT_HWCAP = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 44
try:
    AT_FPUCW = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 47
try:
    AT_DCACHEBSIZE = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 48
try:
    AT_ICACHEBSIZE = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 49
try:
    AT_UCACHEBSIZE = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 53
try:
    AT_IGNOREPPC = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 55
try:
    AT_SECURE = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 57
try:
    AT_BASE_PLATFORM = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 59
try:
    AT_RANDOM = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 61
try:
    AT_HWCAP2 = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 64
try:
    AT_EXECFN = 31
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 68
try:
    AT_SYSINFO = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 69
try:
    AT_SYSINFO_EHDR = 33
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 73
try:
    AT_L1I_CACHESHAPE = 34
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 74
try:
    AT_L1D_CACHESHAPE = 35
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 75
try:
    AT_L2_CACHESHAPE = 36
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 76
try:
    AT_L3_CACHESHAPE = 37
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 81
try:
    AT_L1I_CACHESIZE = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 82
try:
    AT_L1I_CACHEGEOMETRY = 41
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 83
try:
    AT_L1D_CACHESIZE = 42
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 84
try:
    AT_L1D_CACHEGEOMETRY = 43
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 85
try:
    AT_L2_CACHESIZE = 44
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 86
try:
    AT_L2_CACHEGEOMETRY = 45
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 87
try:
    AT_L3_CACHESIZE = 46
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 88
try:
    AT_L3_CACHEGEOMETRY = 47
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 90
try:
    AT_MINSIGSTKSZ = 51
except:
    pass

# /usr/include/elf.h: 1180
try:
    ELF_NOTE_SOLARIS = 'SUNW Solaris'
except:
    pass

# /usr/include/elf.h: 1183
try:
    ELF_NOTE_GNU = 'GNU'
except:
    pass

# /usr/include/elf.h: 1189
try:
    ELF_NOTE_PAGESIZE_HINT = 1
except:
    pass

# /usr/include/elf.h: 1200
try:
    NT_GNU_ABI_TAG = 1
except:
    pass

# /usr/include/elf.h: 1201
try:
    ELF_NOTE_ABI = NT_GNU_ABI_TAG
except:
    pass

# /usr/include/elf.h: 1205
try:
    ELF_NOTE_OS_LINUX = 0
except:
    pass

# /usr/include/elf.h: 1206
try:
    ELF_NOTE_OS_GNU = 1
except:
    pass

# /usr/include/elf.h: 1207
try:
    ELF_NOTE_OS_SOLARIS2 = 2
except:
    pass

# /usr/include/elf.h: 1208
try:
    ELF_NOTE_OS_FREEBSD = 3
except:
    pass

# /usr/include/elf.h: 1216
try:
    NT_GNU_HWCAP = 2
except:
    pass

# /usr/include/elf.h: 1220
try:
    NT_GNU_BUILD_ID = 3
except:
    pass

# /usr/include/elf.h: 1223
try:
    NT_GNU_GOLD_VERSION = 4
except:
    pass

# /usr/include/elf.h: 1226
try:
    NT_GNU_PROPERTY_TYPE_0 = 5
except:
    pass

# /usr/include/elf.h: 1229
try:
    NOTE_GNU_PROPERTY_SECTION_NAME = '.note.gnu.property'
except:
    pass

# /usr/include/elf.h: 1234
try:
    GNU_PROPERTY_STACK_SIZE = 1
except:
    pass

# /usr/include/elf.h: 1236
try:
    GNU_PROPERTY_NO_COPY_ON_PROTECTED = 2
except:
    pass

# /usr/include/elf.h: 1239
try:
    GNU_PROPERTY_LOPROC = 0xc0000000
except:
    pass

# /usr/include/elf.h: 1241
try:
    GNU_PROPERTY_HIPROC = 0xdfffffff
except:
    pass

# /usr/include/elf.h: 1243
try:
    GNU_PROPERTY_LOUSER = 0xe0000000
except:
    pass

# /usr/include/elf.h: 1245
try:
    GNU_PROPERTY_HIUSER = 0xffffffff
except:
    pass

# /usr/include/elf.h: 1249
try:
    GNU_PROPERTY_X86_ISA_1_USED = 0xc0000000
except:
    pass

# /usr/include/elf.h: 1252
try:
    GNU_PROPERTY_X86_ISA_1_NEEDED = 0xc0000001
except:
    pass

# /usr/include/elf.h: 1254
try:
    GNU_PROPERTY_X86_FEATURE_1_AND = 0xc0000002
except:
    pass

# /usr/include/elf.h: 1256
try:
    GNU_PROPERTY_X86_ISA_1_486 = (1 << 0)
except:
    pass

# /usr/include/elf.h: 1257
try:
    GNU_PROPERTY_X86_ISA_1_586 = (1 << 1)
except:
    pass

# /usr/include/elf.h: 1258
try:
    GNU_PROPERTY_X86_ISA_1_686 = (1 << 2)
except:
    pass

# /usr/include/elf.h: 1259
try:
    GNU_PROPERTY_X86_ISA_1_SSE = (1 << 3)
except:
    pass

# /usr/include/elf.h: 1260
try:
    GNU_PROPERTY_X86_ISA_1_SSE2 = (1 << 4)
except:
    pass

# /usr/include/elf.h: 1261
try:
    GNU_PROPERTY_X86_ISA_1_SSE3 = (1 << 5)
except:
    pass

# /usr/include/elf.h: 1262
try:
    GNU_PROPERTY_X86_ISA_1_SSSE3 = (1 << 6)
except:
    pass

# /usr/include/elf.h: 1263
try:
    GNU_PROPERTY_X86_ISA_1_SSE4_1 = (1 << 7)
except:
    pass

# /usr/include/elf.h: 1264
try:
    GNU_PROPERTY_X86_ISA_1_SSE4_2 = (1 << 8)
except:
    pass

# /usr/include/elf.h: 1265
try:
    GNU_PROPERTY_X86_ISA_1_AVX = (1 << 9)
except:
    pass

# /usr/include/elf.h: 1266
try:
    GNU_PROPERTY_X86_ISA_1_AVX2 = (1 << 10)
except:
    pass

# /usr/include/elf.h: 1267
try:
    GNU_PROPERTY_X86_ISA_1_AVX512F = (1 << 11)
except:
    pass

# /usr/include/elf.h: 1268
try:
    GNU_PROPERTY_X86_ISA_1_AVX512CD = (1 << 12)
except:
    pass

# /usr/include/elf.h: 1269
try:
    GNU_PROPERTY_X86_ISA_1_AVX512ER = (1 << 13)
except:
    pass

# /usr/include/elf.h: 1270
try:
    GNU_PROPERTY_X86_ISA_1_AVX512PF = (1 << 14)
except:
    pass

# /usr/include/elf.h: 1271
try:
    GNU_PROPERTY_X86_ISA_1_AVX512VL = (1 << 15)
except:
    pass

# /usr/include/elf.h: 1272
try:
    GNU_PROPERTY_X86_ISA_1_AVX512DQ = (1 << 16)
except:
    pass

# /usr/include/elf.h: 1273
try:
    GNU_PROPERTY_X86_ISA_1_AVX512BW = (1 << 17)
except:
    pass

# /usr/include/elf.h: 1277
try:
    GNU_PROPERTY_X86_FEATURE_1_IBT = (1 << 0)
except:
    pass

# /usr/include/elf.h: 1280
try:
    GNU_PROPERTY_X86_FEATURE_1_SHSTK = (1 << 1)
except:
    pass

# /usr/include/elf.h: 1302
def ELF32_M_SYM(info):
    return (info >> 8)

# /usr/include/elf.h: 1303
def ELF32_M_SIZE(info):
    return (c_ubyte (ord_if_char(info))).value

# /usr/include/elf.h: 1304
def ELF32_M_INFO(sym, size):
    return ((sym << 8) + (c_ubyte (ord_if_char(size))).value)

# /usr/include/elf.h: 1306
def ELF64_M_SYM(info):
    return (ELF32_M_SYM (info))

# /usr/include/elf.h: 1307
def ELF64_M_SIZE(info):
    return (ELF32_M_SIZE (info))

# /usr/include/elf.h: 1308
def ELF64_M_INFO(sym, size):
    return (ELF32_M_INFO (sym, size))

# /usr/include/elf.h: 1314
try:
    EF_CPU32 = 0x00810000
except:
    pass

# /usr/include/elf.h: 1318
try:
    R_68K_NONE = 0
except:
    pass

# /usr/include/elf.h: 1319
try:
    R_68K_32 = 1
except:
    pass

# /usr/include/elf.h: 1320
try:
    R_68K_16 = 2
except:
    pass

# /usr/include/elf.h: 1321
try:
    R_68K_8 = 3
except:
    pass

# /usr/include/elf.h: 1322
try:
    R_68K_PC32 = 4
except:
    pass

# /usr/include/elf.h: 1323
try:
    R_68K_PC16 = 5
except:
    pass

# /usr/include/elf.h: 1324
try:
    R_68K_PC8 = 6
except:
    pass

# /usr/include/elf.h: 1325
try:
    R_68K_GOT32 = 7
except:
    pass

# /usr/include/elf.h: 1326
try:
    R_68K_GOT16 = 8
except:
    pass

# /usr/include/elf.h: 1327
try:
    R_68K_GOT8 = 9
except:
    pass

# /usr/include/elf.h: 1328
try:
    R_68K_GOT32O = 10
except:
    pass

# /usr/include/elf.h: 1329
try:
    R_68K_GOT16O = 11
except:
    pass

# /usr/include/elf.h: 1330
try:
    R_68K_GOT8O = 12
except:
    pass

# /usr/include/elf.h: 1331
try:
    R_68K_PLT32 = 13
except:
    pass

# /usr/include/elf.h: 1332
try:
    R_68K_PLT16 = 14
except:
    pass

# /usr/include/elf.h: 1333
try:
    R_68K_PLT8 = 15
except:
    pass

# /usr/include/elf.h: 1334
try:
    R_68K_PLT32O = 16
except:
    pass

# /usr/include/elf.h: 1335
try:
    R_68K_PLT16O = 17
except:
    pass

# /usr/include/elf.h: 1336
try:
    R_68K_PLT8O = 18
except:
    pass

# /usr/include/elf.h: 1337
try:
    R_68K_COPY = 19
except:
    pass

# /usr/include/elf.h: 1338
try:
    R_68K_GLOB_DAT = 20
except:
    pass

# /usr/include/elf.h: 1339
try:
    R_68K_JMP_SLOT = 21
except:
    pass

# /usr/include/elf.h: 1340
try:
    R_68K_RELATIVE = 22
except:
    pass

# /usr/include/elf.h: 1341
try:
    R_68K_TLS_GD32 = 25
except:
    pass

# /usr/include/elf.h: 1342
try:
    R_68K_TLS_GD16 = 26
except:
    pass

# /usr/include/elf.h: 1343
try:
    R_68K_TLS_GD8 = 27
except:
    pass

# /usr/include/elf.h: 1344
try:
    R_68K_TLS_LDM32 = 28
except:
    pass

# /usr/include/elf.h: 1345
try:
    R_68K_TLS_LDM16 = 29
except:
    pass

# /usr/include/elf.h: 1346
try:
    R_68K_TLS_LDM8 = 30
except:
    pass

# /usr/include/elf.h: 1347
try:
    R_68K_TLS_LDO32 = 31
except:
    pass

# /usr/include/elf.h: 1348
try:
    R_68K_TLS_LDO16 = 32
except:
    pass

# /usr/include/elf.h: 1349
try:
    R_68K_TLS_LDO8 = 33
except:
    pass

# /usr/include/elf.h: 1350
try:
    R_68K_TLS_IE32 = 34
except:
    pass

# /usr/include/elf.h: 1351
try:
    R_68K_TLS_IE16 = 35
except:
    pass

# /usr/include/elf.h: 1352
try:
    R_68K_TLS_IE8 = 36
except:
    pass

# /usr/include/elf.h: 1353
try:
    R_68K_TLS_LE32 = 37
except:
    pass

# /usr/include/elf.h: 1355
try:
    R_68K_TLS_LE16 = 38
except:
    pass

# /usr/include/elf.h: 1357
try:
    R_68K_TLS_LE8 = 39
except:
    pass

# /usr/include/elf.h: 1359
try:
    R_68K_TLS_DTPMOD32 = 40
except:
    pass

# /usr/include/elf.h: 1360
try:
    R_68K_TLS_DTPREL32 = 41
except:
    pass

# /usr/include/elf.h: 1361
try:
    R_68K_TLS_TPREL32 = 42
except:
    pass

# /usr/include/elf.h: 1363
try:
    R_68K_NUM = 43
except:
    pass

# /usr/include/elf.h: 1369
try:
    R_386_NONE = 0
except:
    pass

# /usr/include/elf.h: 1370
try:
    R_386_32 = 1
except:
    pass

# /usr/include/elf.h: 1371
try:
    R_386_PC32 = 2
except:
    pass

# /usr/include/elf.h: 1372
try:
    R_386_GOT32 = 3
except:
    pass

# /usr/include/elf.h: 1373
try:
    R_386_PLT32 = 4
except:
    pass

# /usr/include/elf.h: 1374
try:
    R_386_COPY = 5
except:
    pass

# /usr/include/elf.h: 1375
try:
    R_386_GLOB_DAT = 6
except:
    pass

# /usr/include/elf.h: 1376
try:
    R_386_JMP_SLOT = 7
except:
    pass

# /usr/include/elf.h: 1377
try:
    R_386_RELATIVE = 8
except:
    pass

# /usr/include/elf.h: 1378
try:
    R_386_GOTOFF = 9
except:
    pass

# /usr/include/elf.h: 1379
try:
    R_386_GOTPC = 10
except:
    pass

# /usr/include/elf.h: 1380
try:
    R_386_32PLT = 11
except:
    pass

# /usr/include/elf.h: 1381
try:
    R_386_TLS_TPOFF = 14
except:
    pass

# /usr/include/elf.h: 1382
try:
    R_386_TLS_IE = 15
except:
    pass

# /usr/include/elf.h: 1384
try:
    R_386_TLS_GOTIE = 16
except:
    pass

# /usr/include/elf.h: 1386
try:
    R_386_TLS_LE = 17
except:
    pass

# /usr/include/elf.h: 1388
try:
    R_386_TLS_GD = 18
except:
    pass

# /usr/include/elf.h: 1390
try:
    R_386_TLS_LDM = 19
except:
    pass

# /usr/include/elf.h: 1393
try:
    R_386_16 = 20
except:
    pass

# /usr/include/elf.h: 1394
try:
    R_386_PC16 = 21
except:
    pass

# /usr/include/elf.h: 1395
try:
    R_386_8 = 22
except:
    pass

# /usr/include/elf.h: 1396
try:
    R_386_PC8 = 23
except:
    pass

# /usr/include/elf.h: 1397
try:
    R_386_TLS_GD_32 = 24
except:
    pass

# /usr/include/elf.h: 1399
try:
    R_386_TLS_GD_PUSH = 25
except:
    pass

# /usr/include/elf.h: 1400
try:
    R_386_TLS_GD_CALL = 26
except:
    pass

# /usr/include/elf.h: 1402
try:
    R_386_TLS_GD_POP = 27
except:
    pass

# /usr/include/elf.h: 1403
try:
    R_386_TLS_LDM_32 = 28
except:
    pass

# /usr/include/elf.h: 1405
try:
    R_386_TLS_LDM_PUSH = 29
except:
    pass

# /usr/include/elf.h: 1406
try:
    R_386_TLS_LDM_CALL = 30
except:
    pass

# /usr/include/elf.h: 1408
try:
    R_386_TLS_LDM_POP = 31
except:
    pass

# /usr/include/elf.h: 1409
try:
    R_386_TLS_LDO_32 = 32
except:
    pass

# /usr/include/elf.h: 1410
try:
    R_386_TLS_IE_32 = 33
except:
    pass

# /usr/include/elf.h: 1412
try:
    R_386_TLS_LE_32 = 34
except:
    pass

# /usr/include/elf.h: 1414
try:
    R_386_TLS_DTPMOD32 = 35
except:
    pass

# /usr/include/elf.h: 1415
try:
    R_386_TLS_DTPOFF32 = 36
except:
    pass

# /usr/include/elf.h: 1416
try:
    R_386_TLS_TPOFF32 = 37
except:
    pass

# /usr/include/elf.h: 1417
try:
    R_386_SIZE32 = 38
except:
    pass

# /usr/include/elf.h: 1418
try:
    R_386_TLS_GOTDESC = 39
except:
    pass

# /usr/include/elf.h: 1419
try:
    R_386_TLS_DESC_CALL = 40
except:
    pass

# /usr/include/elf.h: 1422
try:
    R_386_TLS_DESC = 41
except:
    pass

# /usr/include/elf.h: 1426
try:
    R_386_IRELATIVE = 42
except:
    pass

# /usr/include/elf.h: 1427
try:
    R_386_GOT32X = 43
except:
    pass

# /usr/include/elf.h: 1430
try:
    R_386_NUM = 44
except:
    pass

# /usr/include/elf.h: 1436
try:
    STT_SPARC_REGISTER = 13
except:
    pass

# /usr/include/elf.h: 1440
try:
    EF_SPARCV9_MM = 3
except:
    pass

# /usr/include/elf.h: 1441
try:
    EF_SPARCV9_TSO = 0
except:
    pass

# /usr/include/elf.h: 1442
try:
    EF_SPARCV9_PSO = 1
except:
    pass

# /usr/include/elf.h: 1443
try:
    EF_SPARCV9_RMO = 2
except:
    pass

# /usr/include/elf.h: 1444
try:
    EF_SPARC_LEDATA = 0x800000
except:
    pass

# /usr/include/elf.h: 1445
try:
    EF_SPARC_EXT_MASK = 0xFFFF00
except:
    pass

# /usr/include/elf.h: 1446
try:
    EF_SPARC_32PLUS = 0x000100
except:
    pass

# /usr/include/elf.h: 1447
try:
    EF_SPARC_SUN_US1 = 0x000200
except:
    pass

# /usr/include/elf.h: 1448
try:
    EF_SPARC_HAL_R1 = 0x000400
except:
    pass

# /usr/include/elf.h: 1449
try:
    EF_SPARC_SUN_US3 = 0x000800
except:
    pass

# /usr/include/elf.h: 1453
try:
    R_SPARC_NONE = 0
except:
    pass

# /usr/include/elf.h: 1454
try:
    R_SPARC_8 = 1
except:
    pass

# /usr/include/elf.h: 1455
try:
    R_SPARC_16 = 2
except:
    pass

# /usr/include/elf.h: 1456
try:
    R_SPARC_32 = 3
except:
    pass

# /usr/include/elf.h: 1457
try:
    R_SPARC_DISP8 = 4
except:
    pass

# /usr/include/elf.h: 1458
try:
    R_SPARC_DISP16 = 5
except:
    pass

# /usr/include/elf.h: 1459
try:
    R_SPARC_DISP32 = 6
except:
    pass

# /usr/include/elf.h: 1460
try:
    R_SPARC_WDISP30 = 7
except:
    pass

# /usr/include/elf.h: 1461
try:
    R_SPARC_WDISP22 = 8
except:
    pass

# /usr/include/elf.h: 1462
try:
    R_SPARC_HI22 = 9
except:
    pass

# /usr/include/elf.h: 1463
try:
    R_SPARC_22 = 10
except:
    pass

# /usr/include/elf.h: 1464
try:
    R_SPARC_13 = 11
except:
    pass

# /usr/include/elf.h: 1465
try:
    R_SPARC_LO10 = 12
except:
    pass

# /usr/include/elf.h: 1466
try:
    R_SPARC_GOT10 = 13
except:
    pass

# /usr/include/elf.h: 1467
try:
    R_SPARC_GOT13 = 14
except:
    pass

# /usr/include/elf.h: 1468
try:
    R_SPARC_GOT22 = 15
except:
    pass

# /usr/include/elf.h: 1469
try:
    R_SPARC_PC10 = 16
except:
    pass

# /usr/include/elf.h: 1470
try:
    R_SPARC_PC22 = 17
except:
    pass

# /usr/include/elf.h: 1471
try:
    R_SPARC_WPLT30 = 18
except:
    pass

# /usr/include/elf.h: 1472
try:
    R_SPARC_COPY = 19
except:
    pass

# /usr/include/elf.h: 1473
try:
    R_SPARC_GLOB_DAT = 20
except:
    pass

# /usr/include/elf.h: 1474
try:
    R_SPARC_JMP_SLOT = 21
except:
    pass

# /usr/include/elf.h: 1475
try:
    R_SPARC_RELATIVE = 22
except:
    pass

# /usr/include/elf.h: 1476
try:
    R_SPARC_UA32 = 23
except:
    pass

# /usr/include/elf.h: 1480
try:
    R_SPARC_PLT32 = 24
except:
    pass

# /usr/include/elf.h: 1481
try:
    R_SPARC_HIPLT22 = 25
except:
    pass

# /usr/include/elf.h: 1482
try:
    R_SPARC_LOPLT10 = 26
except:
    pass

# /usr/include/elf.h: 1483
try:
    R_SPARC_PCPLT32 = 27
except:
    pass

# /usr/include/elf.h: 1484
try:
    R_SPARC_PCPLT22 = 28
except:
    pass

# /usr/include/elf.h: 1485
try:
    R_SPARC_PCPLT10 = 29
except:
    pass

# /usr/include/elf.h: 1486
try:
    R_SPARC_10 = 30
except:
    pass

# /usr/include/elf.h: 1487
try:
    R_SPARC_11 = 31
except:
    pass

# /usr/include/elf.h: 1488
try:
    R_SPARC_64 = 32
except:
    pass

# /usr/include/elf.h: 1489
try:
    R_SPARC_OLO10 = 33
except:
    pass

# /usr/include/elf.h: 1490
try:
    R_SPARC_HH22 = 34
except:
    pass

# /usr/include/elf.h: 1491
try:
    R_SPARC_HM10 = 35
except:
    pass

# /usr/include/elf.h: 1492
try:
    R_SPARC_LM22 = 36
except:
    pass

# /usr/include/elf.h: 1493
try:
    R_SPARC_PC_HH22 = 37
except:
    pass

# /usr/include/elf.h: 1494
try:
    R_SPARC_PC_HM10 = 38
except:
    pass

# /usr/include/elf.h: 1495
try:
    R_SPARC_PC_LM22 = 39
except:
    pass

# /usr/include/elf.h: 1496
try:
    R_SPARC_WDISP16 = 40
except:
    pass

# /usr/include/elf.h: 1497
try:
    R_SPARC_WDISP19 = 41
except:
    pass

# /usr/include/elf.h: 1498
try:
    R_SPARC_GLOB_JMP = 42
except:
    pass

# /usr/include/elf.h: 1499
try:
    R_SPARC_7 = 43
except:
    pass

# /usr/include/elf.h: 1500
try:
    R_SPARC_5 = 44
except:
    pass

# /usr/include/elf.h: 1501
try:
    R_SPARC_6 = 45
except:
    pass

# /usr/include/elf.h: 1502
try:
    R_SPARC_DISP64 = 46
except:
    pass

# /usr/include/elf.h: 1503
try:
    R_SPARC_PLT64 = 47
except:
    pass

# /usr/include/elf.h: 1504
try:
    R_SPARC_HIX22 = 48
except:
    pass

# /usr/include/elf.h: 1505
try:
    R_SPARC_LOX10 = 49
except:
    pass

# /usr/include/elf.h: 1506
try:
    R_SPARC_H44 = 50
except:
    pass

# /usr/include/elf.h: 1507
try:
    R_SPARC_M44 = 51
except:
    pass

# /usr/include/elf.h: 1508
try:
    R_SPARC_L44 = 52
except:
    pass

# /usr/include/elf.h: 1509
try:
    R_SPARC_REGISTER = 53
except:
    pass

# /usr/include/elf.h: 1510
try:
    R_SPARC_UA64 = 54
except:
    pass

# /usr/include/elf.h: 1511
try:
    R_SPARC_UA16 = 55
except:
    pass

# /usr/include/elf.h: 1512
try:
    R_SPARC_TLS_GD_HI22 = 56
except:
    pass

# /usr/include/elf.h: 1513
try:
    R_SPARC_TLS_GD_LO10 = 57
except:
    pass

# /usr/include/elf.h: 1514
try:
    R_SPARC_TLS_GD_ADD = 58
except:
    pass

# /usr/include/elf.h: 1515
try:
    R_SPARC_TLS_GD_CALL = 59
except:
    pass

# /usr/include/elf.h: 1516
try:
    R_SPARC_TLS_LDM_HI22 = 60
except:
    pass

# /usr/include/elf.h: 1517
try:
    R_SPARC_TLS_LDM_LO10 = 61
except:
    pass

# /usr/include/elf.h: 1518
try:
    R_SPARC_TLS_LDM_ADD = 62
except:
    pass

# /usr/include/elf.h: 1519
try:
    R_SPARC_TLS_LDM_CALL = 63
except:
    pass

# /usr/include/elf.h: 1520
try:
    R_SPARC_TLS_LDO_HIX22 = 64
except:
    pass

# /usr/include/elf.h: 1521
try:
    R_SPARC_TLS_LDO_LOX10 = 65
except:
    pass

# /usr/include/elf.h: 1522
try:
    R_SPARC_TLS_LDO_ADD = 66
except:
    pass

# /usr/include/elf.h: 1523
try:
    R_SPARC_TLS_IE_HI22 = 67
except:
    pass

# /usr/include/elf.h: 1524
try:
    R_SPARC_TLS_IE_LO10 = 68
except:
    pass

# /usr/include/elf.h: 1525
try:
    R_SPARC_TLS_IE_LD = 69
except:
    pass

# /usr/include/elf.h: 1526
try:
    R_SPARC_TLS_IE_LDX = 70
except:
    pass

# /usr/include/elf.h: 1527
try:
    R_SPARC_TLS_IE_ADD = 71
except:
    pass

# /usr/include/elf.h: 1528
try:
    R_SPARC_TLS_LE_HIX22 = 72
except:
    pass

# /usr/include/elf.h: 1529
try:
    R_SPARC_TLS_LE_LOX10 = 73
except:
    pass

# /usr/include/elf.h: 1530
try:
    R_SPARC_TLS_DTPMOD32 = 74
except:
    pass

# /usr/include/elf.h: 1531
try:
    R_SPARC_TLS_DTPMOD64 = 75
except:
    pass

# /usr/include/elf.h: 1532
try:
    R_SPARC_TLS_DTPOFF32 = 76
except:
    pass

# /usr/include/elf.h: 1533
try:
    R_SPARC_TLS_DTPOFF64 = 77
except:
    pass

# /usr/include/elf.h: 1534
try:
    R_SPARC_TLS_TPOFF32 = 78
except:
    pass

# /usr/include/elf.h: 1535
try:
    R_SPARC_TLS_TPOFF64 = 79
except:
    pass

# /usr/include/elf.h: 1536
try:
    R_SPARC_GOTDATA_HIX22 = 80
except:
    pass

# /usr/include/elf.h: 1537
try:
    R_SPARC_GOTDATA_LOX10 = 81
except:
    pass

# /usr/include/elf.h: 1538
try:
    R_SPARC_GOTDATA_OP_HIX22 = 82
except:
    pass

# /usr/include/elf.h: 1539
try:
    R_SPARC_GOTDATA_OP_LOX10 = 83
except:
    pass

# /usr/include/elf.h: 1540
try:
    R_SPARC_GOTDATA_OP = 84
except:
    pass

# /usr/include/elf.h: 1541
try:
    R_SPARC_H34 = 85
except:
    pass

# /usr/include/elf.h: 1542
try:
    R_SPARC_SIZE32 = 86
except:
    pass

# /usr/include/elf.h: 1543
try:
    R_SPARC_SIZE64 = 87
except:
    pass

# /usr/include/elf.h: 1544
try:
    R_SPARC_WDISP10 = 88
except:
    pass

# /usr/include/elf.h: 1545
try:
    R_SPARC_JMP_IREL = 248
except:
    pass

# /usr/include/elf.h: 1546
try:
    R_SPARC_IRELATIVE = 249
except:
    pass

# /usr/include/elf.h: 1547
try:
    R_SPARC_GNU_VTINHERIT = 250
except:
    pass

# /usr/include/elf.h: 1548
try:
    R_SPARC_GNU_VTENTRY = 251
except:
    pass

# /usr/include/elf.h: 1549
try:
    R_SPARC_REV32 = 252
except:
    pass

# /usr/include/elf.h: 1551
try:
    R_SPARC_NUM = 253
except:
    pass

# /usr/include/elf.h: 1555
try:
    DT_SPARC_REGISTER = 0x70000001
except:
    pass

# /usr/include/elf.h: 1556
try:
    DT_SPARC_NUM = 2
except:
    pass

# /usr/include/elf.h: 1562
try:
    EF_MIPS_NOREORDER = 1
except:
    pass

# /usr/include/elf.h: 1563
try:
    EF_MIPS_PIC = 2
except:
    pass

# /usr/include/elf.h: 1564
try:
    EF_MIPS_CPIC = 4
except:
    pass

# /usr/include/elf.h: 1565
try:
    EF_MIPS_XGOT = 8
except:
    pass

# /usr/include/elf.h: 1566
try:
    EF_MIPS_64BIT_WHIRL = 16
except:
    pass

# /usr/include/elf.h: 1567
try:
    EF_MIPS_ABI2 = 32
except:
    pass

# /usr/include/elf.h: 1568
try:
    EF_MIPS_ABI_ON32 = 64
except:
    pass

# /usr/include/elf.h: 1569
try:
    EF_MIPS_FP64 = 512
except:
    pass

# /usr/include/elf.h: 1570
try:
    EF_MIPS_NAN2008 = 1024
except:
    pass

# /usr/include/elf.h: 1571
try:
    EF_MIPS_ARCH = 0xf0000000
except:
    pass

# /usr/include/elf.h: 1575
try:
    EF_MIPS_ARCH_1 = 0x00000000
except:
    pass

# /usr/include/elf.h: 1576
try:
    EF_MIPS_ARCH_2 = 0x10000000
except:
    pass

# /usr/include/elf.h: 1577
try:
    EF_MIPS_ARCH_3 = 0x20000000
except:
    pass

# /usr/include/elf.h: 1578
try:
    EF_MIPS_ARCH_4 = 0x30000000
except:
    pass

# /usr/include/elf.h: 1579
try:
    EF_MIPS_ARCH_5 = 0x40000000
except:
    pass

# /usr/include/elf.h: 1580
try:
    EF_MIPS_ARCH_32 = 0x50000000
except:
    pass

# /usr/include/elf.h: 1581
try:
    EF_MIPS_ARCH_64 = 0x60000000
except:
    pass

# /usr/include/elf.h: 1582
try:
    EF_MIPS_ARCH_32R2 = 0x70000000
except:
    pass

# /usr/include/elf.h: 1583
try:
    EF_MIPS_ARCH_64R2 = 0x80000000
except:
    pass

# /usr/include/elf.h: 1587
try:
    E_MIPS_ARCH_1 = EF_MIPS_ARCH_1
except:
    pass

# /usr/include/elf.h: 1588
try:
    E_MIPS_ARCH_2 = EF_MIPS_ARCH_2
except:
    pass

# /usr/include/elf.h: 1589
try:
    E_MIPS_ARCH_3 = EF_MIPS_ARCH_3
except:
    pass

# /usr/include/elf.h: 1590
try:
    E_MIPS_ARCH_4 = EF_MIPS_ARCH_4
except:
    pass

# /usr/include/elf.h: 1591
try:
    E_MIPS_ARCH_5 = EF_MIPS_ARCH_5
except:
    pass

# /usr/include/elf.h: 1592
try:
    E_MIPS_ARCH_32 = EF_MIPS_ARCH_32
except:
    pass

# /usr/include/elf.h: 1593
try:
    E_MIPS_ARCH_64 = EF_MIPS_ARCH_64
except:
    pass

# /usr/include/elf.h: 1597
try:
    SHN_MIPS_ACOMMON = 0xff00
except:
    pass

# /usr/include/elf.h: 1598
try:
    SHN_MIPS_TEXT = 0xff01
except:
    pass

# /usr/include/elf.h: 1599
try:
    SHN_MIPS_DATA = 0xff02
except:
    pass

# /usr/include/elf.h: 1600
try:
    SHN_MIPS_SCOMMON = 0xff03
except:
    pass

# /usr/include/elf.h: 1601
try:
    SHN_MIPS_SUNDEFINED = 0xff04
except:
    pass

# /usr/include/elf.h: 1605
try:
    SHT_MIPS_LIBLIST = 0x70000000
except:
    pass

# /usr/include/elf.h: 1606
try:
    SHT_MIPS_MSYM = 0x70000001
except:
    pass

# /usr/include/elf.h: 1607
try:
    SHT_MIPS_CONFLICT = 0x70000002
except:
    pass

# /usr/include/elf.h: 1608
try:
    SHT_MIPS_GPTAB = 0x70000003
except:
    pass

# /usr/include/elf.h: 1609
try:
    SHT_MIPS_UCODE = 0x70000004
except:
    pass

# /usr/include/elf.h: 1610
try:
    SHT_MIPS_DEBUG = 0x70000005
except:
    pass

# /usr/include/elf.h: 1611
try:
    SHT_MIPS_REGINFO = 0x70000006
except:
    pass

# /usr/include/elf.h: 1612
try:
    SHT_MIPS_PACKAGE = 0x70000007
except:
    pass

# /usr/include/elf.h: 1613
try:
    SHT_MIPS_PACKSYM = 0x70000008
except:
    pass

# /usr/include/elf.h: 1614
try:
    SHT_MIPS_RELD = 0x70000009
except:
    pass

# /usr/include/elf.h: 1615
try:
    SHT_MIPS_IFACE = 0x7000000b
except:
    pass

# /usr/include/elf.h: 1616
try:
    SHT_MIPS_CONTENT = 0x7000000c
except:
    pass

# /usr/include/elf.h: 1617
try:
    SHT_MIPS_OPTIONS = 0x7000000d
except:
    pass

# /usr/include/elf.h: 1618
try:
    SHT_MIPS_SHDR = 0x70000010
except:
    pass

# /usr/include/elf.h: 1619
try:
    SHT_MIPS_FDESC = 0x70000011
except:
    pass

# /usr/include/elf.h: 1620
try:
    SHT_MIPS_EXTSYM = 0x70000012
except:
    pass

# /usr/include/elf.h: 1621
try:
    SHT_MIPS_DENSE = 0x70000013
except:
    pass

# /usr/include/elf.h: 1622
try:
    SHT_MIPS_PDESC = 0x70000014
except:
    pass

# /usr/include/elf.h: 1623
try:
    SHT_MIPS_LOCSYM = 0x70000015
except:
    pass

# /usr/include/elf.h: 1624
try:
    SHT_MIPS_AUXSYM = 0x70000016
except:
    pass

# /usr/include/elf.h: 1625
try:
    SHT_MIPS_OPTSYM = 0x70000017
except:
    pass

# /usr/include/elf.h: 1626
try:
    SHT_MIPS_LOCSTR = 0x70000018
except:
    pass

# /usr/include/elf.h: 1627
try:
    SHT_MIPS_LINE = 0x70000019
except:
    pass

# /usr/include/elf.h: 1628
try:
    SHT_MIPS_RFDESC = 0x7000001a
except:
    pass

# /usr/include/elf.h: 1629
try:
    SHT_MIPS_DELTASYM = 0x7000001b
except:
    pass

# /usr/include/elf.h: 1630
try:
    SHT_MIPS_DELTAINST = 0x7000001c
except:
    pass

# /usr/include/elf.h: 1631
try:
    SHT_MIPS_DELTACLASS = 0x7000001d
except:
    pass

# /usr/include/elf.h: 1632
try:
    SHT_MIPS_DWARF = 0x7000001e
except:
    pass

# /usr/include/elf.h: 1633
try:
    SHT_MIPS_DELTADECL = 0x7000001f
except:
    pass

# /usr/include/elf.h: 1634
try:
    SHT_MIPS_SYMBOL_LIB = 0x70000020
except:
    pass

# /usr/include/elf.h: 1635
try:
    SHT_MIPS_EVENTS = 0x70000021
except:
    pass

# /usr/include/elf.h: 1636
try:
    SHT_MIPS_TRANSLATE = 0x70000022
except:
    pass

# /usr/include/elf.h: 1637
try:
    SHT_MIPS_PIXIE = 0x70000023
except:
    pass

# /usr/include/elf.h: 1638
try:
    SHT_MIPS_XLATE = 0x70000024
except:
    pass

# /usr/include/elf.h: 1639
try:
    SHT_MIPS_XLATE_DEBUG = 0x70000025
except:
    pass

# /usr/include/elf.h: 1640
try:
    SHT_MIPS_WHIRL = 0x70000026
except:
    pass

# /usr/include/elf.h: 1641
try:
    SHT_MIPS_EH_REGION = 0x70000027
except:
    pass

# /usr/include/elf.h: 1642
try:
    SHT_MIPS_XLATE_OLD = 0x70000028
except:
    pass

# /usr/include/elf.h: 1643
try:
    SHT_MIPS_PDR_EXCEPTION = 0x70000029
except:
    pass

# /usr/include/elf.h: 1644
try:
    SHT_MIPS_XHASH = 0x7000002b
except:
    pass

# /usr/include/elf.h: 1648
try:
    SHF_MIPS_GPREL = 0x10000000
except:
    pass

# /usr/include/elf.h: 1649
try:
    SHF_MIPS_MERGE = 0x20000000
except:
    pass

# /usr/include/elf.h: 1650
try:
    SHF_MIPS_ADDR = 0x40000000
except:
    pass

# /usr/include/elf.h: 1651
try:
    SHF_MIPS_STRINGS = 0x80000000
except:
    pass

# /usr/include/elf.h: 1652
try:
    SHF_MIPS_NOSTRIP = 0x08000000
except:
    pass

# /usr/include/elf.h: 1653
try:
    SHF_MIPS_LOCAL = 0x04000000
except:
    pass

# /usr/include/elf.h: 1654
try:
    SHF_MIPS_NAMES = 0x02000000
except:
    pass

# /usr/include/elf.h: 1655
try:
    SHF_MIPS_NODUPE = 0x01000000
except:
    pass

# /usr/include/elf.h: 1661
try:
    STO_MIPS_DEFAULT = 0x0
except:
    pass

# /usr/include/elf.h: 1662
try:
    STO_MIPS_INTERNAL = 0x1
except:
    pass

# /usr/include/elf.h: 1663
try:
    STO_MIPS_HIDDEN = 0x2
except:
    pass

# /usr/include/elf.h: 1664
try:
    STO_MIPS_PROTECTED = 0x3
except:
    pass

# /usr/include/elf.h: 1665
try:
    STO_MIPS_PLT = 0x8
except:
    pass

# /usr/include/elf.h: 1666
try:
    STO_MIPS_SC_ALIGN_UNUSED = 0xff
except:
    pass

# /usr/include/elf.h: 1669
try:
    STB_MIPS_SPLIT_COMMON = 13
except:
    pass

# /usr/include/elf.h: 1710
try:
    ODK_NULL = 0
except:
    pass

# /usr/include/elf.h: 1711
try:
    ODK_REGINFO = 1
except:
    pass

# /usr/include/elf.h: 1712
try:
    ODK_EXCEPTIONS = 2
except:
    pass

# /usr/include/elf.h: 1713
try:
    ODK_PAD = 3
except:
    pass

# /usr/include/elf.h: 1714
try:
    ODK_HWPATCH = 4
except:
    pass

# /usr/include/elf.h: 1715
try:
    ODK_FILL = 5
except:
    pass

# /usr/include/elf.h: 1716
try:
    ODK_TAGS = 6
except:
    pass

# /usr/include/elf.h: 1717
try:
    ODK_HWAND = 7
except:
    pass

# /usr/include/elf.h: 1718
try:
    ODK_HWOR = 8
except:
    pass

# /usr/include/elf.h: 1722
try:
    OEX_FPU_MIN = 0x1f
except:
    pass

# /usr/include/elf.h: 1723
try:
    OEX_FPU_MAX = 0x1f00
except:
    pass

# /usr/include/elf.h: 1724
try:
    OEX_PAGE0 = 0x10000
except:
    pass

# /usr/include/elf.h: 1725
try:
    OEX_SMM = 0x20000
except:
    pass

# /usr/include/elf.h: 1726
try:
    OEX_FPDBUG = 0x40000
except:
    pass

# /usr/include/elf.h: 1727
try:
    OEX_PRECISEFP = OEX_FPDBUG
except:
    pass

# /usr/include/elf.h: 1728
try:
    OEX_DISMISS = 0x80000
except:
    pass

# /usr/include/elf.h: 1730
try:
    OEX_FPU_INVAL = 0x10
except:
    pass

# /usr/include/elf.h: 1731
try:
    OEX_FPU_DIV0 = 0x08
except:
    pass

# /usr/include/elf.h: 1732
try:
    OEX_FPU_OFLO = 0x04
except:
    pass

# /usr/include/elf.h: 1733
try:
    OEX_FPU_UFLO = 0x02
except:
    pass

# /usr/include/elf.h: 1734
try:
    OEX_FPU_INEX = 0x01
except:
    pass

# /usr/include/elf.h: 1738
try:
    OHW_R4KEOP = 0x1
except:
    pass

# /usr/include/elf.h: 1739
try:
    OHW_R8KPFETCH = 0x2
except:
    pass

# /usr/include/elf.h: 1740
try:
    OHW_R5KEOP = 0x4
except:
    pass

# /usr/include/elf.h: 1741
try:
    OHW_R5KCVTL = 0x8
except:
    pass

# /usr/include/elf.h: 1743
try:
    OPAD_PREFIX = 0x1
except:
    pass

# /usr/include/elf.h: 1744
try:
    OPAD_POSTFIX = 0x2
except:
    pass

# /usr/include/elf.h: 1745
try:
    OPAD_SYMBOL = 0x4
except:
    pass

# /usr/include/elf.h: 1757
try:
    OHWA0_R4KEOP_CHECKED = 0x00000001
except:
    pass

# /usr/include/elf.h: 1758
try:
    OHWA1_R4KEOP_CLEAN = 0x00000002
except:
    pass

# /usr/include/elf.h: 1762
try:
    R_MIPS_NONE = 0
except:
    pass

# /usr/include/elf.h: 1763
try:
    R_MIPS_16 = 1
except:
    pass

# /usr/include/elf.h: 1764
try:
    R_MIPS_32 = 2
except:
    pass

# /usr/include/elf.h: 1765
try:
    R_MIPS_REL32 = 3
except:
    pass

# /usr/include/elf.h: 1766
try:
    R_MIPS_26 = 4
except:
    pass

# /usr/include/elf.h: 1767
try:
    R_MIPS_HI16 = 5
except:
    pass

# /usr/include/elf.h: 1768
try:
    R_MIPS_LO16 = 6
except:
    pass

# /usr/include/elf.h: 1769
try:
    R_MIPS_GPREL16 = 7
except:
    pass

# /usr/include/elf.h: 1770
try:
    R_MIPS_LITERAL = 8
except:
    pass

# /usr/include/elf.h: 1771
try:
    R_MIPS_GOT16 = 9
except:
    pass

# /usr/include/elf.h: 1772
try:
    R_MIPS_PC16 = 10
except:
    pass

# /usr/include/elf.h: 1773
try:
    R_MIPS_CALL16 = 11
except:
    pass

# /usr/include/elf.h: 1774
try:
    R_MIPS_GPREL32 = 12
except:
    pass

# /usr/include/elf.h: 1776
try:
    R_MIPS_SHIFT5 = 16
except:
    pass

# /usr/include/elf.h: 1777
try:
    R_MIPS_SHIFT6 = 17
except:
    pass

# /usr/include/elf.h: 1778
try:
    R_MIPS_64 = 18
except:
    pass

# /usr/include/elf.h: 1779
try:
    R_MIPS_GOT_DISP = 19
except:
    pass

# /usr/include/elf.h: 1780
try:
    R_MIPS_GOT_PAGE = 20
except:
    pass

# /usr/include/elf.h: 1781
try:
    R_MIPS_GOT_OFST = 21
except:
    pass

# /usr/include/elf.h: 1782
try:
    R_MIPS_GOT_HI16 = 22
except:
    pass

# /usr/include/elf.h: 1783
try:
    R_MIPS_GOT_LO16 = 23
except:
    pass

# /usr/include/elf.h: 1784
try:
    R_MIPS_SUB = 24
except:
    pass

# /usr/include/elf.h: 1785
try:
    R_MIPS_INSERT_A = 25
except:
    pass

# /usr/include/elf.h: 1786
try:
    R_MIPS_INSERT_B = 26
except:
    pass

# /usr/include/elf.h: 1787
try:
    R_MIPS_DELETE = 27
except:
    pass

# /usr/include/elf.h: 1788
try:
    R_MIPS_HIGHER = 28
except:
    pass

# /usr/include/elf.h: 1789
try:
    R_MIPS_HIGHEST = 29
except:
    pass

# /usr/include/elf.h: 1790
try:
    R_MIPS_CALL_HI16 = 30
except:
    pass

# /usr/include/elf.h: 1791
try:
    R_MIPS_CALL_LO16 = 31
except:
    pass

# /usr/include/elf.h: 1792
try:
    R_MIPS_SCN_DISP = 32
except:
    pass

# /usr/include/elf.h: 1793
try:
    R_MIPS_REL16 = 33
except:
    pass

# /usr/include/elf.h: 1794
try:
    R_MIPS_ADD_IMMEDIATE = 34
except:
    pass

# /usr/include/elf.h: 1795
try:
    R_MIPS_PJUMP = 35
except:
    pass

# /usr/include/elf.h: 1796
try:
    R_MIPS_RELGOT = 36
except:
    pass

# /usr/include/elf.h: 1797
try:
    R_MIPS_JALR = 37
except:
    pass

# /usr/include/elf.h: 1798
try:
    R_MIPS_TLS_DTPMOD32 = 38
except:
    pass

# /usr/include/elf.h: 1799
try:
    R_MIPS_TLS_DTPREL32 = 39
except:
    pass

# /usr/include/elf.h: 1800
try:
    R_MIPS_TLS_DTPMOD64 = 40
except:
    pass

# /usr/include/elf.h: 1801
try:
    R_MIPS_TLS_DTPREL64 = 41
except:
    pass

# /usr/include/elf.h: 1802
try:
    R_MIPS_TLS_GD = 42
except:
    pass

# /usr/include/elf.h: 1803
try:
    R_MIPS_TLS_LDM = 43
except:
    pass

# /usr/include/elf.h: 1804
try:
    R_MIPS_TLS_DTPREL_HI16 = 44
except:
    pass

# /usr/include/elf.h: 1805
try:
    R_MIPS_TLS_DTPREL_LO16 = 45
except:
    pass

# /usr/include/elf.h: 1806
try:
    R_MIPS_TLS_GOTTPREL = 46
except:
    pass

# /usr/include/elf.h: 1807
try:
    R_MIPS_TLS_TPREL32 = 47
except:
    pass

# /usr/include/elf.h: 1808
try:
    R_MIPS_TLS_TPREL64 = 48
except:
    pass

# /usr/include/elf.h: 1809
try:
    R_MIPS_TLS_TPREL_HI16 = 49
except:
    pass

# /usr/include/elf.h: 1810
try:
    R_MIPS_TLS_TPREL_LO16 = 50
except:
    pass

# /usr/include/elf.h: 1811
try:
    R_MIPS_GLOB_DAT = 51
except:
    pass

# /usr/include/elf.h: 1812
try:
    R_MIPS_COPY = 126
except:
    pass

# /usr/include/elf.h: 1813
try:
    R_MIPS_JUMP_SLOT = 127
except:
    pass

# /usr/include/elf.h: 1815
try:
    R_MIPS_NUM = 128
except:
    pass

# /usr/include/elf.h: 1819
try:
    PT_MIPS_REGINFO = 0x70000000
except:
    pass

# /usr/include/elf.h: 1820
try:
    PT_MIPS_RTPROC = 0x70000001
except:
    pass

# /usr/include/elf.h: 1821
try:
    PT_MIPS_OPTIONS = 0x70000002
except:
    pass

# /usr/include/elf.h: 1822
try:
    PT_MIPS_ABIFLAGS = 0x70000003
except:
    pass

# /usr/include/elf.h: 1826
try:
    PF_MIPS_LOCAL = 0x10000000
except:
    pass

# /usr/include/elf.h: 1830
try:
    DT_MIPS_RLD_VERSION = 0x70000001
except:
    pass

# /usr/include/elf.h: 1831
try:
    DT_MIPS_TIME_STAMP = 0x70000002
except:
    pass

# /usr/include/elf.h: 1832
try:
    DT_MIPS_ICHECKSUM = 0x70000003
except:
    pass

# /usr/include/elf.h: 1833
try:
    DT_MIPS_IVERSION = 0x70000004
except:
    pass

# /usr/include/elf.h: 1834
try:
    DT_MIPS_FLAGS = 0x70000005
except:
    pass

# /usr/include/elf.h: 1835
try:
    DT_MIPS_BASE_ADDRESS = 0x70000006
except:
    pass

# /usr/include/elf.h: 1836
try:
    DT_MIPS_MSYM = 0x70000007
except:
    pass

# /usr/include/elf.h: 1837
try:
    DT_MIPS_CONFLICT = 0x70000008
except:
    pass

# /usr/include/elf.h: 1838
try:
    DT_MIPS_LIBLIST = 0x70000009
except:
    pass

# /usr/include/elf.h: 1839
try:
    DT_MIPS_LOCAL_GOTNO = 0x7000000a
except:
    pass

# /usr/include/elf.h: 1840
try:
    DT_MIPS_CONFLICTNO = 0x7000000b
except:
    pass

# /usr/include/elf.h: 1841
try:
    DT_MIPS_LIBLISTNO = 0x70000010
except:
    pass

# /usr/include/elf.h: 1842
try:
    DT_MIPS_SYMTABNO = 0x70000011
except:
    pass

# /usr/include/elf.h: 1843
try:
    DT_MIPS_UNREFEXTNO = 0x70000012
except:
    pass

# /usr/include/elf.h: 1844
try:
    DT_MIPS_GOTSYM = 0x70000013
except:
    pass

# /usr/include/elf.h: 1845
try:
    DT_MIPS_HIPAGENO = 0x70000014
except:
    pass

# /usr/include/elf.h: 1846
try:
    DT_MIPS_RLD_MAP = 0x70000016
except:
    pass

# /usr/include/elf.h: 1847
try:
    DT_MIPS_DELTA_CLASS = 0x70000017
except:
    pass

# /usr/include/elf.h: 1848
try:
    DT_MIPS_DELTA_CLASS_NO = 0x70000018
except:
    pass

# /usr/include/elf.h: 1850
try:
    DT_MIPS_DELTA_INSTANCE = 0x70000019
except:
    pass

# /usr/include/elf.h: 1851
try:
    DT_MIPS_DELTA_INSTANCE_NO = 0x7000001a
except:
    pass

# /usr/include/elf.h: 1853
try:
    DT_MIPS_DELTA_RELOC = 0x7000001b
except:
    pass

# /usr/include/elf.h: 1854
try:
    DT_MIPS_DELTA_RELOC_NO = 0x7000001c
except:
    pass

# /usr/include/elf.h: 1856
try:
    DT_MIPS_DELTA_SYM = 0x7000001d
except:
    pass

# /usr/include/elf.h: 1858
try:
    DT_MIPS_DELTA_SYM_NO = 0x7000001e
except:
    pass

# /usr/include/elf.h: 1860
try:
    DT_MIPS_DELTA_CLASSSYM = 0x70000020
except:
    pass

# /usr/include/elf.h: 1862
try:
    DT_MIPS_DELTA_CLASSSYM_NO = 0x70000021
except:
    pass

# /usr/include/elf.h: 1864
try:
    DT_MIPS_CXX_FLAGS = 0x70000022
except:
    pass

# /usr/include/elf.h: 1865
try:
    DT_MIPS_PIXIE_INIT = 0x70000023
except:
    pass

# /usr/include/elf.h: 1866
try:
    DT_MIPS_SYMBOL_LIB = 0x70000024
except:
    pass

# /usr/include/elf.h: 1867
try:
    DT_MIPS_LOCALPAGE_GOTIDX = 0x70000025
except:
    pass

# /usr/include/elf.h: 1868
try:
    DT_MIPS_LOCAL_GOTIDX = 0x70000026
except:
    pass

# /usr/include/elf.h: 1869
try:
    DT_MIPS_HIDDEN_GOTIDX = 0x70000027
except:
    pass

# /usr/include/elf.h: 1870
try:
    DT_MIPS_PROTECTED_GOTIDX = 0x70000028
except:
    pass

# /usr/include/elf.h: 1871
try:
    DT_MIPS_OPTIONS = 0x70000029
except:
    pass

# /usr/include/elf.h: 1872
try:
    DT_MIPS_INTERFACE = 0x7000002a
except:
    pass

# /usr/include/elf.h: 1873
try:
    DT_MIPS_DYNSTR_ALIGN = 0x7000002b
except:
    pass

# /usr/include/elf.h: 1874
try:
    DT_MIPS_INTERFACE_SIZE = 0x7000002c
except:
    pass

# /usr/include/elf.h: 1875
try:
    DT_MIPS_RLD_TEXT_RESOLVE_ADDR = 0x7000002d
except:
    pass

# /usr/include/elf.h: 1877
try:
    DT_MIPS_PERF_SUFFIX = 0x7000002e
except:
    pass

# /usr/include/elf.h: 1879
try:
    DT_MIPS_COMPACT_SIZE = 0x7000002f
except:
    pass

# /usr/include/elf.h: 1880
try:
    DT_MIPS_GP_VALUE = 0x70000030
except:
    pass

# /usr/include/elf.h: 1881
try:
    DT_MIPS_AUX_DYNAMIC = 0x70000031
except:
    pass

# /usr/include/elf.h: 1883
try:
    DT_MIPS_PLTGOT = 0x70000032
except:
    pass

# /usr/include/elf.h: 1887
try:
    DT_MIPS_RWPLT = 0x70000034
except:
    pass

# /usr/include/elf.h: 1891
try:
    DT_MIPS_RLD_MAP_REL = 0x70000035
except:
    pass

# /usr/include/elf.h: 1893
try:
    DT_MIPS_XHASH = 0x70000036
except:
    pass

# /usr/include/elf.h: 1894
try:
    DT_MIPS_NUM = 0x37
except:
    pass

# /usr/include/elf.h: 1898
try:
    RHF_NONE = 0
except:
    pass

# /usr/include/elf.h: 1899
try:
    RHF_QUICKSTART = (1 << 0)
except:
    pass

# /usr/include/elf.h: 1900
try:
    RHF_NOTPOT = (1 << 1)
except:
    pass

# /usr/include/elf.h: 1901
try:
    RHF_NO_LIBRARY_REPLACEMENT = (1 << 2)
except:
    pass

# /usr/include/elf.h: 1902
try:
    RHF_NO_MOVE = (1 << 3)
except:
    pass

# /usr/include/elf.h: 1903
try:
    RHF_SGI_ONLY = (1 << 4)
except:
    pass

# /usr/include/elf.h: 1904
try:
    RHF_GUARANTEE_INIT = (1 << 5)
except:
    pass

# /usr/include/elf.h: 1905
try:
    RHF_DELTA_C_PLUS_PLUS = (1 << 6)
except:
    pass

# /usr/include/elf.h: 1906
try:
    RHF_GUARANTEE_START_INIT = (1 << 7)
except:
    pass

# /usr/include/elf.h: 1907
try:
    RHF_PIXIE = (1 << 8)
except:
    pass

# /usr/include/elf.h: 1908
try:
    RHF_DEFAULT_DELAY_LOAD = (1 << 9)
except:
    pass

# /usr/include/elf.h: 1909
try:
    RHF_REQUICKSTART = (1 << 10)
except:
    pass

# /usr/include/elf.h: 1910
try:
    RHF_REQUICKSTARTED = (1 << 11)
except:
    pass

# /usr/include/elf.h: 1911
try:
    RHF_CORD = (1 << 12)
except:
    pass

# /usr/include/elf.h: 1912
try:
    RHF_NO_UNRES_UNDEF = (1 << 13)
except:
    pass

# /usr/include/elf.h: 1913
try:
    RHF_RLD_ORDER_SAFE = (1 << 14)
except:
    pass

# /usr/include/elf.h: 1938
try:
    LL_NONE = 0
except:
    pass

# /usr/include/elf.h: 1939
try:
    LL_EXACT_MATCH = (1 << 0)
except:
    pass

# /usr/include/elf.h: 1940
try:
    LL_IGNORE_INT_VER = (1 << 1)
except:
    pass

# /usr/include/elf.h: 1941
try:
    LL_REQUIRE_MINOR = (1 << 2)
except:
    pass

# /usr/include/elf.h: 1942
try:
    LL_EXPORTS = (1 << 3)
except:
    pass

# /usr/include/elf.h: 1943
try:
    LL_DELAY_LOAD = (1 << 4)
except:
    pass

# /usr/include/elf.h: 1944
try:
    LL_DELTA = (1 << 5)
except:
    pass

# /usr/include/elf.h: 1977
try:
    MIPS_AFL_REG_NONE = 0x00
except:
    pass

# /usr/include/elf.h: 1978
try:
    MIPS_AFL_REG_32 = 0x01
except:
    pass

# /usr/include/elf.h: 1979
try:
    MIPS_AFL_REG_64 = 0x02
except:
    pass

# /usr/include/elf.h: 1980
try:
    MIPS_AFL_REG_128 = 0x03
except:
    pass

# /usr/include/elf.h: 1984
try:
    MIPS_AFL_ASE_DSP = 0x00000001
except:
    pass

# /usr/include/elf.h: 1985
try:
    MIPS_AFL_ASE_DSPR2 = 0x00000002
except:
    pass

# /usr/include/elf.h: 1986
try:
    MIPS_AFL_ASE_EVA = 0x00000004
except:
    pass

# /usr/include/elf.h: 1987
try:
    MIPS_AFL_ASE_MCU = 0x00000008
except:
    pass

# /usr/include/elf.h: 1988
try:
    MIPS_AFL_ASE_MDMX = 0x00000010
except:
    pass

# /usr/include/elf.h: 1989
try:
    MIPS_AFL_ASE_MIPS3D = 0x00000020
except:
    pass

# /usr/include/elf.h: 1990
try:
    MIPS_AFL_ASE_MT = 0x00000040
except:
    pass

# /usr/include/elf.h: 1991
try:
    MIPS_AFL_ASE_SMARTMIPS = 0x00000080
except:
    pass

# /usr/include/elf.h: 1992
try:
    MIPS_AFL_ASE_VIRT = 0x00000100
except:
    pass

# /usr/include/elf.h: 1993
try:
    MIPS_AFL_ASE_MSA = 0x00000200
except:
    pass

# /usr/include/elf.h: 1994
try:
    MIPS_AFL_ASE_MIPS16 = 0x00000400
except:
    pass

# /usr/include/elf.h: 1995
try:
    MIPS_AFL_ASE_MICROMIPS = 0x00000800
except:
    pass

# /usr/include/elf.h: 1996
try:
    MIPS_AFL_ASE_XPA = 0x00001000
except:
    pass

# /usr/include/elf.h: 1997
try:
    MIPS_AFL_ASE_MASK = 0x00001fff
except:
    pass

# /usr/include/elf.h: 2001
try:
    MIPS_AFL_EXT_XLR = 1
except:
    pass

# /usr/include/elf.h: 2002
try:
    MIPS_AFL_EXT_OCTEON2 = 2
except:
    pass

# /usr/include/elf.h: 2003
try:
    MIPS_AFL_EXT_OCTEONP = 3
except:
    pass

# /usr/include/elf.h: 2004
try:
    MIPS_AFL_EXT_LOONGSON_3A = 4
except:
    pass

# /usr/include/elf.h: 2005
try:
    MIPS_AFL_EXT_OCTEON = 5
except:
    pass

# /usr/include/elf.h: 2006
try:
    MIPS_AFL_EXT_5900 = 6
except:
    pass

# /usr/include/elf.h: 2007
try:
    MIPS_AFL_EXT_4650 = 7
except:
    pass

# /usr/include/elf.h: 2008
try:
    MIPS_AFL_EXT_4010 = 8
except:
    pass

# /usr/include/elf.h: 2009
try:
    MIPS_AFL_EXT_4100 = 9
except:
    pass

# /usr/include/elf.h: 2010
try:
    MIPS_AFL_EXT_3900 = 10
except:
    pass

# /usr/include/elf.h: 2011
try:
    MIPS_AFL_EXT_10000 = 11
except:
    pass

# /usr/include/elf.h: 2012
try:
    MIPS_AFL_EXT_SB1 = 12
except:
    pass

# /usr/include/elf.h: 2013
try:
    MIPS_AFL_EXT_4111 = 13
except:
    pass

# /usr/include/elf.h: 2014
try:
    MIPS_AFL_EXT_4120 = 14
except:
    pass

# /usr/include/elf.h: 2015
try:
    MIPS_AFL_EXT_5400 = 15
except:
    pass

# /usr/include/elf.h: 2016
try:
    MIPS_AFL_EXT_5500 = 16
except:
    pass

# /usr/include/elf.h: 2017
try:
    MIPS_AFL_EXT_LOONGSON_2E = 17
except:
    pass

# /usr/include/elf.h: 2018
try:
    MIPS_AFL_EXT_LOONGSON_2F = 18
except:
    pass

# /usr/include/elf.h: 2021
try:
    MIPS_AFL_FLAGS1_ODDSPREG = 1
except:
    pass

# /usr/include/elf.h: 2050
try:
    EF_PARISC_TRAPNIL = 0x00010000
except:
    pass

# /usr/include/elf.h: 2051
try:
    EF_PARISC_EXT = 0x00020000
except:
    pass

# /usr/include/elf.h: 2052
try:
    EF_PARISC_LSB = 0x00040000
except:
    pass

# /usr/include/elf.h: 2053
try:
    EF_PARISC_WIDE = 0x00080000
except:
    pass

# /usr/include/elf.h: 2054
try:
    EF_PARISC_NO_KABP = 0x00100000
except:
    pass

# /usr/include/elf.h: 2056
try:
    EF_PARISC_LAZYSWAP = 0x00400000
except:
    pass

# /usr/include/elf.h: 2057
try:
    EF_PARISC_ARCH = 0x0000ffff
except:
    pass

# /usr/include/elf.h: 2061
try:
    EFA_PARISC_1_0 = 0x020b
except:
    pass

# /usr/include/elf.h: 2062
try:
    EFA_PARISC_1_1 = 0x0210
except:
    pass

# /usr/include/elf.h: 2063
try:
    EFA_PARISC_2_0 = 0x0214
except:
    pass

# /usr/include/elf.h: 2067
try:
    SHN_PARISC_ANSI_COMMON = 0xff00
except:
    pass

# /usr/include/elf.h: 2069
try:
    SHN_PARISC_HUGE_COMMON = 0xff01
except:
    pass

# /usr/include/elf.h: 2073
try:
    SHT_PARISC_EXT = 0x70000000
except:
    pass

# /usr/include/elf.h: 2074
try:
    SHT_PARISC_UNWIND = 0x70000001
except:
    pass

# /usr/include/elf.h: 2075
try:
    SHT_PARISC_DOC = 0x70000002
except:
    pass

# /usr/include/elf.h: 2079
try:
    SHF_PARISC_SHORT = 0x20000000
except:
    pass

# /usr/include/elf.h: 2080
try:
    SHF_PARISC_HUGE = 0x40000000
except:
    pass

# /usr/include/elf.h: 2081
try:
    SHF_PARISC_SBP = 0x80000000
except:
    pass

# /usr/include/elf.h: 2085
try:
    STT_PARISC_MILLICODE = 13
except:
    pass

# /usr/include/elf.h: 2087
try:
    STT_HP_OPAQUE = (STT_LOOS + 0x1)
except:
    pass

# /usr/include/elf.h: 2088
try:
    STT_HP_STUB = (STT_LOOS + 0x2)
except:
    pass

# /usr/include/elf.h: 2092
try:
    R_PARISC_NONE = 0
except:
    pass

# /usr/include/elf.h: 2093
try:
    R_PARISC_DIR32 = 1
except:
    pass

# /usr/include/elf.h: 2094
try:
    R_PARISC_DIR21L = 2
except:
    pass

# /usr/include/elf.h: 2095
try:
    R_PARISC_DIR17R = 3
except:
    pass

# /usr/include/elf.h: 2096
try:
    R_PARISC_DIR17F = 4
except:
    pass

# /usr/include/elf.h: 2097
try:
    R_PARISC_DIR14R = 6
except:
    pass

# /usr/include/elf.h: 2098
try:
    R_PARISC_PCREL32 = 9
except:
    pass

# /usr/include/elf.h: 2099
try:
    R_PARISC_PCREL21L = 10
except:
    pass

# /usr/include/elf.h: 2100
try:
    R_PARISC_PCREL17R = 11
except:
    pass

# /usr/include/elf.h: 2101
try:
    R_PARISC_PCREL17F = 12
except:
    pass

# /usr/include/elf.h: 2102
try:
    R_PARISC_PCREL14R = 14
except:
    pass

# /usr/include/elf.h: 2103
try:
    R_PARISC_DPREL21L = 18
except:
    pass

# /usr/include/elf.h: 2104
try:
    R_PARISC_DPREL14R = 22
except:
    pass

# /usr/include/elf.h: 2105
try:
    R_PARISC_GPREL21L = 26
except:
    pass

# /usr/include/elf.h: 2106
try:
    R_PARISC_GPREL14R = 30
except:
    pass

# /usr/include/elf.h: 2107
try:
    R_PARISC_LTOFF21L = 34
except:
    pass

# /usr/include/elf.h: 2108
try:
    R_PARISC_LTOFF14R = 38
except:
    pass

# /usr/include/elf.h: 2109
try:
    R_PARISC_SECREL32 = 41
except:
    pass

# /usr/include/elf.h: 2110
try:
    R_PARISC_SEGBASE = 48
except:
    pass

# /usr/include/elf.h: 2111
try:
    R_PARISC_SEGREL32 = 49
except:
    pass

# /usr/include/elf.h: 2112
try:
    R_PARISC_PLTOFF21L = 50
except:
    pass

# /usr/include/elf.h: 2113
try:
    R_PARISC_PLTOFF14R = 54
except:
    pass

# /usr/include/elf.h: 2114
try:
    R_PARISC_LTOFF_FPTR32 = 57
except:
    pass

# /usr/include/elf.h: 2115
try:
    R_PARISC_LTOFF_FPTR21L = 58
except:
    pass

# /usr/include/elf.h: 2116
try:
    R_PARISC_LTOFF_FPTR14R = 62
except:
    pass

# /usr/include/elf.h: 2117
try:
    R_PARISC_FPTR64 = 64
except:
    pass

# /usr/include/elf.h: 2118
try:
    R_PARISC_PLABEL32 = 65
except:
    pass

# /usr/include/elf.h: 2119
try:
    R_PARISC_PLABEL21L = 66
except:
    pass

# /usr/include/elf.h: 2120
try:
    R_PARISC_PLABEL14R = 70
except:
    pass

# /usr/include/elf.h: 2121
try:
    R_PARISC_PCREL64 = 72
except:
    pass

# /usr/include/elf.h: 2122
try:
    R_PARISC_PCREL22F = 74
except:
    pass

# /usr/include/elf.h: 2123
try:
    R_PARISC_PCREL14WR = 75
except:
    pass

# /usr/include/elf.h: 2124
try:
    R_PARISC_PCREL14DR = 76
except:
    pass

# /usr/include/elf.h: 2125
try:
    R_PARISC_PCREL16F = 77
except:
    pass

# /usr/include/elf.h: 2126
try:
    R_PARISC_PCREL16WF = 78
except:
    pass

# /usr/include/elf.h: 2127
try:
    R_PARISC_PCREL16DF = 79
except:
    pass

# /usr/include/elf.h: 2128
try:
    R_PARISC_DIR64 = 80
except:
    pass

# /usr/include/elf.h: 2129
try:
    R_PARISC_DIR14WR = 83
except:
    pass

# /usr/include/elf.h: 2130
try:
    R_PARISC_DIR14DR = 84
except:
    pass

# /usr/include/elf.h: 2131
try:
    R_PARISC_DIR16F = 85
except:
    pass

# /usr/include/elf.h: 2132
try:
    R_PARISC_DIR16WF = 86
except:
    pass

# /usr/include/elf.h: 2133
try:
    R_PARISC_DIR16DF = 87
except:
    pass

# /usr/include/elf.h: 2134
try:
    R_PARISC_GPREL64 = 88
except:
    pass

# /usr/include/elf.h: 2135
try:
    R_PARISC_GPREL14WR = 91
except:
    pass

# /usr/include/elf.h: 2136
try:
    R_PARISC_GPREL14DR = 92
except:
    pass

# /usr/include/elf.h: 2137
try:
    R_PARISC_GPREL16F = 93
except:
    pass

# /usr/include/elf.h: 2138
try:
    R_PARISC_GPREL16WF = 94
except:
    pass

# /usr/include/elf.h: 2139
try:
    R_PARISC_GPREL16DF = 95
except:
    pass

# /usr/include/elf.h: 2140
try:
    R_PARISC_LTOFF64 = 96
except:
    pass

# /usr/include/elf.h: 2141
try:
    R_PARISC_LTOFF14WR = 99
except:
    pass

# /usr/include/elf.h: 2142
try:
    R_PARISC_LTOFF14DR = 100
except:
    pass

# /usr/include/elf.h: 2143
try:
    R_PARISC_LTOFF16F = 101
except:
    pass

# /usr/include/elf.h: 2144
try:
    R_PARISC_LTOFF16WF = 102
except:
    pass

# /usr/include/elf.h: 2145
try:
    R_PARISC_LTOFF16DF = 103
except:
    pass

# /usr/include/elf.h: 2146
try:
    R_PARISC_SECREL64 = 104
except:
    pass

# /usr/include/elf.h: 2147
try:
    R_PARISC_SEGREL64 = 112
except:
    pass

# /usr/include/elf.h: 2148
try:
    R_PARISC_PLTOFF14WR = 115
except:
    pass

# /usr/include/elf.h: 2149
try:
    R_PARISC_PLTOFF14DR = 116
except:
    pass

# /usr/include/elf.h: 2150
try:
    R_PARISC_PLTOFF16F = 117
except:
    pass

# /usr/include/elf.h: 2151
try:
    R_PARISC_PLTOFF16WF = 118
except:
    pass

# /usr/include/elf.h: 2152
try:
    R_PARISC_PLTOFF16DF = 119
except:
    pass

# /usr/include/elf.h: 2153
try:
    R_PARISC_LTOFF_FPTR64 = 120
except:
    pass

# /usr/include/elf.h: 2154
try:
    R_PARISC_LTOFF_FPTR14WR = 123
except:
    pass

# /usr/include/elf.h: 2155
try:
    R_PARISC_LTOFF_FPTR14DR = 124
except:
    pass

# /usr/include/elf.h: 2156
try:
    R_PARISC_LTOFF_FPTR16F = 125
except:
    pass

# /usr/include/elf.h: 2157
try:
    R_PARISC_LTOFF_FPTR16WF = 126
except:
    pass

# /usr/include/elf.h: 2158
try:
    R_PARISC_LTOFF_FPTR16DF = 127
except:
    pass

# /usr/include/elf.h: 2159
try:
    R_PARISC_LORESERVE = 128
except:
    pass

# /usr/include/elf.h: 2160
try:
    R_PARISC_COPY = 128
except:
    pass

# /usr/include/elf.h: 2161
try:
    R_PARISC_IPLT = 129
except:
    pass

# /usr/include/elf.h: 2162
try:
    R_PARISC_EPLT = 130
except:
    pass

# /usr/include/elf.h: 2163
try:
    R_PARISC_TPREL32 = 153
except:
    pass

# /usr/include/elf.h: 2164
try:
    R_PARISC_TPREL21L = 154
except:
    pass

# /usr/include/elf.h: 2165
try:
    R_PARISC_TPREL14R = 158
except:
    pass

# /usr/include/elf.h: 2166
try:
    R_PARISC_LTOFF_TP21L = 162
except:
    pass

# /usr/include/elf.h: 2167
try:
    R_PARISC_LTOFF_TP14R = 166
except:
    pass

# /usr/include/elf.h: 2168
try:
    R_PARISC_LTOFF_TP14F = 167
except:
    pass

# /usr/include/elf.h: 2169
try:
    R_PARISC_TPREL64 = 216
except:
    pass

# /usr/include/elf.h: 2170
try:
    R_PARISC_TPREL14WR = 219
except:
    pass

# /usr/include/elf.h: 2171
try:
    R_PARISC_TPREL14DR = 220
except:
    pass

# /usr/include/elf.h: 2172
try:
    R_PARISC_TPREL16F = 221
except:
    pass

# /usr/include/elf.h: 2173
try:
    R_PARISC_TPREL16WF = 222
except:
    pass

# /usr/include/elf.h: 2174
try:
    R_PARISC_TPREL16DF = 223
except:
    pass

# /usr/include/elf.h: 2175
try:
    R_PARISC_LTOFF_TP64 = 224
except:
    pass

# /usr/include/elf.h: 2176
try:
    R_PARISC_LTOFF_TP14WR = 227
except:
    pass

# /usr/include/elf.h: 2177
try:
    R_PARISC_LTOFF_TP14DR = 228
except:
    pass

# /usr/include/elf.h: 2178
try:
    R_PARISC_LTOFF_TP16F = 229
except:
    pass

# /usr/include/elf.h: 2179
try:
    R_PARISC_LTOFF_TP16WF = 230
except:
    pass

# /usr/include/elf.h: 2180
try:
    R_PARISC_LTOFF_TP16DF = 231
except:
    pass

# /usr/include/elf.h: 2181
try:
    R_PARISC_GNU_VTENTRY = 232
except:
    pass

# /usr/include/elf.h: 2182
try:
    R_PARISC_GNU_VTINHERIT = 233
except:
    pass

# /usr/include/elf.h: 2183
try:
    R_PARISC_TLS_GD21L = 234
except:
    pass

# /usr/include/elf.h: 2184
try:
    R_PARISC_TLS_GD14R = 235
except:
    pass

# /usr/include/elf.h: 2185
try:
    R_PARISC_TLS_GDCALL = 236
except:
    pass

# /usr/include/elf.h: 2186
try:
    R_PARISC_TLS_LDM21L = 237
except:
    pass

# /usr/include/elf.h: 2187
try:
    R_PARISC_TLS_LDM14R = 238
except:
    pass

# /usr/include/elf.h: 2188
try:
    R_PARISC_TLS_LDMCALL = 239
except:
    pass

# /usr/include/elf.h: 2189
try:
    R_PARISC_TLS_LDO21L = 240
except:
    pass

# /usr/include/elf.h: 2190
try:
    R_PARISC_TLS_LDO14R = 241
except:
    pass

# /usr/include/elf.h: 2191
try:
    R_PARISC_TLS_DTPMOD32 = 242
except:
    pass

# /usr/include/elf.h: 2192
try:
    R_PARISC_TLS_DTPMOD64 = 243
except:
    pass

# /usr/include/elf.h: 2193
try:
    R_PARISC_TLS_DTPOFF32 = 244
except:
    pass

# /usr/include/elf.h: 2194
try:
    R_PARISC_TLS_DTPOFF64 = 245
except:
    pass

# /usr/include/elf.h: 2195
try:
    R_PARISC_TLS_LE21L = R_PARISC_TPREL21L
except:
    pass

# /usr/include/elf.h: 2196
try:
    R_PARISC_TLS_LE14R = R_PARISC_TPREL14R
except:
    pass

# /usr/include/elf.h: 2197
try:
    R_PARISC_TLS_IE21L = R_PARISC_LTOFF_TP21L
except:
    pass

# /usr/include/elf.h: 2198
try:
    R_PARISC_TLS_IE14R = R_PARISC_LTOFF_TP14R
except:
    pass

# /usr/include/elf.h: 2199
try:
    R_PARISC_TLS_TPREL32 = R_PARISC_TPREL32
except:
    pass

# /usr/include/elf.h: 2200
try:
    R_PARISC_TLS_TPREL64 = R_PARISC_TPREL64
except:
    pass

# /usr/include/elf.h: 2201
try:
    R_PARISC_HIRESERVE = 255
except:
    pass

# /usr/include/elf.h: 2205
try:
    PT_HP_TLS = (PT_LOOS + 0x0)
except:
    pass

# /usr/include/elf.h: 2206
try:
    PT_HP_CORE_NONE = (PT_LOOS + 0x1)
except:
    pass

# /usr/include/elf.h: 2207
try:
    PT_HP_CORE_VERSION = (PT_LOOS + 0x2)
except:
    pass

# /usr/include/elf.h: 2208
try:
    PT_HP_CORE_KERNEL = (PT_LOOS + 0x3)
except:
    pass

# /usr/include/elf.h: 2209
try:
    PT_HP_CORE_COMM = (PT_LOOS + 0x4)
except:
    pass

# /usr/include/elf.h: 2210
try:
    PT_HP_CORE_PROC = (PT_LOOS + 0x5)
except:
    pass

# /usr/include/elf.h: 2211
try:
    PT_HP_CORE_LOADABLE = (PT_LOOS + 0x6)
except:
    pass

# /usr/include/elf.h: 2212
try:
    PT_HP_CORE_STACK = (PT_LOOS + 0x7)
except:
    pass

# /usr/include/elf.h: 2213
try:
    PT_HP_CORE_SHM = (PT_LOOS + 0x8)
except:
    pass

# /usr/include/elf.h: 2214
try:
    PT_HP_CORE_MMF = (PT_LOOS + 0x9)
except:
    pass

# /usr/include/elf.h: 2215
try:
    PT_HP_PARALLEL = (PT_LOOS + 0x10)
except:
    pass

# /usr/include/elf.h: 2216
try:
    PT_HP_FASTBIND = (PT_LOOS + 0x11)
except:
    pass

# /usr/include/elf.h: 2217
try:
    PT_HP_OPT_ANNOT = (PT_LOOS + 0x12)
except:
    pass

# /usr/include/elf.h: 2218
try:
    PT_HP_HSL_ANNOT = (PT_LOOS + 0x13)
except:
    pass

# /usr/include/elf.h: 2219
try:
    PT_HP_STACK = (PT_LOOS + 0x14)
except:
    pass

# /usr/include/elf.h: 2221
try:
    PT_PARISC_ARCHEXT = 0x70000000
except:
    pass

# /usr/include/elf.h: 2222
try:
    PT_PARISC_UNWIND = 0x70000001
except:
    pass

# /usr/include/elf.h: 2226
try:
    PF_PARISC_SBP = 0x08000000
except:
    pass

# /usr/include/elf.h: 2228
try:
    PF_HP_PAGE_SIZE = 0x00100000
except:
    pass

# /usr/include/elf.h: 2229
try:
    PF_HP_FAR_SHARED = 0x00200000
except:
    pass

# /usr/include/elf.h: 2230
try:
    PF_HP_NEAR_SHARED = 0x00400000
except:
    pass

# /usr/include/elf.h: 2231
try:
    PF_HP_CODE = 0x01000000
except:
    pass

# /usr/include/elf.h: 2232
try:
    PF_HP_MODIFY = 0x02000000
except:
    pass

# /usr/include/elf.h: 2233
try:
    PF_HP_LAZYSWAP = 0x04000000
except:
    pass

# /usr/include/elf.h: 2234
try:
    PF_HP_SBP = 0x08000000
except:
    pass

# /usr/include/elf.h: 2241
try:
    EF_ALPHA_32BIT = 1
except:
    pass

# /usr/include/elf.h: 2242
try:
    EF_ALPHA_CANRELAX = 2
except:
    pass

# /usr/include/elf.h: 2247
try:
    SHT_ALPHA_DEBUG = 0x70000001
except:
    pass

# /usr/include/elf.h: 2248
try:
    SHT_ALPHA_REGINFO = 0x70000002
except:
    pass

# /usr/include/elf.h: 2252
try:
    SHF_ALPHA_GPREL = 0x10000000
except:
    pass

# /usr/include/elf.h: 2255
try:
    STO_ALPHA_NOPV = 0x80
except:
    pass

# /usr/include/elf.h: 2256
try:
    STO_ALPHA_STD_GPLOAD = 0x88
except:
    pass

# /usr/include/elf.h: 2260
try:
    R_ALPHA_NONE = 0
except:
    pass

# /usr/include/elf.h: 2261
try:
    R_ALPHA_REFLONG = 1
except:
    pass

# /usr/include/elf.h: 2262
try:
    R_ALPHA_REFQUAD = 2
except:
    pass

# /usr/include/elf.h: 2263
try:
    R_ALPHA_GPREL32 = 3
except:
    pass

# /usr/include/elf.h: 2264
try:
    R_ALPHA_LITERAL = 4
except:
    pass

# /usr/include/elf.h: 2265
try:
    R_ALPHA_LITUSE = 5
except:
    pass

# /usr/include/elf.h: 2266
try:
    R_ALPHA_GPDISP = 6
except:
    pass

# /usr/include/elf.h: 2267
try:
    R_ALPHA_BRADDR = 7
except:
    pass

# /usr/include/elf.h: 2268
try:
    R_ALPHA_HINT = 8
except:
    pass

# /usr/include/elf.h: 2269
try:
    R_ALPHA_SREL16 = 9
except:
    pass

# /usr/include/elf.h: 2270
try:
    R_ALPHA_SREL32 = 10
except:
    pass

# /usr/include/elf.h: 2271
try:
    R_ALPHA_SREL64 = 11
except:
    pass

# /usr/include/elf.h: 2272
try:
    R_ALPHA_GPRELHIGH = 17
except:
    pass

# /usr/include/elf.h: 2273
try:
    R_ALPHA_GPRELLOW = 18
except:
    pass

# /usr/include/elf.h: 2274
try:
    R_ALPHA_GPREL16 = 19
except:
    pass

# /usr/include/elf.h: 2275
try:
    R_ALPHA_COPY = 24
except:
    pass

# /usr/include/elf.h: 2276
try:
    R_ALPHA_GLOB_DAT = 25
except:
    pass

# /usr/include/elf.h: 2277
try:
    R_ALPHA_JMP_SLOT = 26
except:
    pass

# /usr/include/elf.h: 2278
try:
    R_ALPHA_RELATIVE = 27
except:
    pass

# /usr/include/elf.h: 2279
try:
    R_ALPHA_TLS_GD_HI = 28
except:
    pass

# /usr/include/elf.h: 2280
try:
    R_ALPHA_TLSGD = 29
except:
    pass

# /usr/include/elf.h: 2281
try:
    R_ALPHA_TLS_LDM = 30
except:
    pass

# /usr/include/elf.h: 2282
try:
    R_ALPHA_DTPMOD64 = 31
except:
    pass

# /usr/include/elf.h: 2283
try:
    R_ALPHA_GOTDTPREL = 32
except:
    pass

# /usr/include/elf.h: 2284
try:
    R_ALPHA_DTPREL64 = 33
except:
    pass

# /usr/include/elf.h: 2285
try:
    R_ALPHA_DTPRELHI = 34
except:
    pass

# /usr/include/elf.h: 2286
try:
    R_ALPHA_DTPRELLO = 35
except:
    pass

# /usr/include/elf.h: 2287
try:
    R_ALPHA_DTPREL16 = 36
except:
    pass

# /usr/include/elf.h: 2288
try:
    R_ALPHA_GOTTPREL = 37
except:
    pass

# /usr/include/elf.h: 2289
try:
    R_ALPHA_TPREL64 = 38
except:
    pass

# /usr/include/elf.h: 2290
try:
    R_ALPHA_TPRELHI = 39
except:
    pass

# /usr/include/elf.h: 2291
try:
    R_ALPHA_TPRELLO = 40
except:
    pass

# /usr/include/elf.h: 2292
try:
    R_ALPHA_TPREL16 = 41
except:
    pass

# /usr/include/elf.h: 2294
try:
    R_ALPHA_NUM = 46
except:
    pass

# /usr/include/elf.h: 2297
try:
    LITUSE_ALPHA_ADDR = 0
except:
    pass

# /usr/include/elf.h: 2298
try:
    LITUSE_ALPHA_BASE = 1
except:
    pass

# /usr/include/elf.h: 2299
try:
    LITUSE_ALPHA_BYTOFF = 2
except:
    pass

# /usr/include/elf.h: 2300
try:
    LITUSE_ALPHA_JSR = 3
except:
    pass

# /usr/include/elf.h: 2301
try:
    LITUSE_ALPHA_TLS_GD = 4
except:
    pass

# /usr/include/elf.h: 2302
try:
    LITUSE_ALPHA_TLS_LDM = 5
except:
    pass

# /usr/include/elf.h: 2305
try:
    DT_ALPHA_PLTRO = (DT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 2306
try:
    DT_ALPHA_NUM = 1
except:
    pass

# /usr/include/elf.h: 2311
try:
    EF_PPC_EMB = 0x80000000
except:
    pass

# /usr/include/elf.h: 2314
try:
    EF_PPC_RELOCATABLE = 0x00010000
except:
    pass

# /usr/include/elf.h: 2315
try:
    EF_PPC_RELOCATABLE_LIB = 0x00008000
except:
    pass

# /usr/include/elf.h: 2319
try:
    R_PPC_NONE = 0
except:
    pass

# /usr/include/elf.h: 2320
try:
    R_PPC_ADDR32 = 1
except:
    pass

# /usr/include/elf.h: 2321
try:
    R_PPC_ADDR24 = 2
except:
    pass

# /usr/include/elf.h: 2322
try:
    R_PPC_ADDR16 = 3
except:
    pass

# /usr/include/elf.h: 2323
try:
    R_PPC_ADDR16_LO = 4
except:
    pass

# /usr/include/elf.h: 2324
try:
    R_PPC_ADDR16_HI = 5
except:
    pass

# /usr/include/elf.h: 2325
try:
    R_PPC_ADDR16_HA = 6
except:
    pass

# /usr/include/elf.h: 2326
try:
    R_PPC_ADDR14 = 7
except:
    pass

# /usr/include/elf.h: 2327
try:
    R_PPC_ADDR14_BRTAKEN = 8
except:
    pass

# /usr/include/elf.h: 2328
try:
    R_PPC_ADDR14_BRNTAKEN = 9
except:
    pass

# /usr/include/elf.h: 2329
try:
    R_PPC_REL24 = 10
except:
    pass

# /usr/include/elf.h: 2330
try:
    R_PPC_REL14 = 11
except:
    pass

# /usr/include/elf.h: 2331
try:
    R_PPC_REL14_BRTAKEN = 12
except:
    pass

# /usr/include/elf.h: 2332
try:
    R_PPC_REL14_BRNTAKEN = 13
except:
    pass

# /usr/include/elf.h: 2333
try:
    R_PPC_GOT16 = 14
except:
    pass

# /usr/include/elf.h: 2334
try:
    R_PPC_GOT16_LO = 15
except:
    pass

# /usr/include/elf.h: 2335
try:
    R_PPC_GOT16_HI = 16
except:
    pass

# /usr/include/elf.h: 2336
try:
    R_PPC_GOT16_HA = 17
except:
    pass

# /usr/include/elf.h: 2337
try:
    R_PPC_PLTREL24 = 18
except:
    pass

# /usr/include/elf.h: 2338
try:
    R_PPC_COPY = 19
except:
    pass

# /usr/include/elf.h: 2339
try:
    R_PPC_GLOB_DAT = 20
except:
    pass

# /usr/include/elf.h: 2340
try:
    R_PPC_JMP_SLOT = 21
except:
    pass

# /usr/include/elf.h: 2341
try:
    R_PPC_RELATIVE = 22
except:
    pass

# /usr/include/elf.h: 2342
try:
    R_PPC_LOCAL24PC = 23
except:
    pass

# /usr/include/elf.h: 2343
try:
    R_PPC_UADDR32 = 24
except:
    pass

# /usr/include/elf.h: 2344
try:
    R_PPC_UADDR16 = 25
except:
    pass

# /usr/include/elf.h: 2345
try:
    R_PPC_REL32 = 26
except:
    pass

# /usr/include/elf.h: 2346
try:
    R_PPC_PLT32 = 27
except:
    pass

# /usr/include/elf.h: 2347
try:
    R_PPC_PLTREL32 = 28
except:
    pass

# /usr/include/elf.h: 2348
try:
    R_PPC_PLT16_LO = 29
except:
    pass

# /usr/include/elf.h: 2349
try:
    R_PPC_PLT16_HI = 30
except:
    pass

# /usr/include/elf.h: 2350
try:
    R_PPC_PLT16_HA = 31
except:
    pass

# /usr/include/elf.h: 2351
try:
    R_PPC_SDAREL16 = 32
except:
    pass

# /usr/include/elf.h: 2352
try:
    R_PPC_SECTOFF = 33
except:
    pass

# /usr/include/elf.h: 2353
try:
    R_PPC_SECTOFF_LO = 34
except:
    pass

# /usr/include/elf.h: 2354
try:
    R_PPC_SECTOFF_HI = 35
except:
    pass

# /usr/include/elf.h: 2355
try:
    R_PPC_SECTOFF_HA = 36
except:
    pass

# /usr/include/elf.h: 2358
try:
    R_PPC_TLS = 67
except:
    pass

# /usr/include/elf.h: 2359
try:
    R_PPC_DTPMOD32 = 68
except:
    pass

# /usr/include/elf.h: 2360
try:
    R_PPC_TPREL16 = 69
except:
    pass

# /usr/include/elf.h: 2361
try:
    R_PPC_TPREL16_LO = 70
except:
    pass

# /usr/include/elf.h: 2362
try:
    R_PPC_TPREL16_HI = 71
except:
    pass

# /usr/include/elf.h: 2363
try:
    R_PPC_TPREL16_HA = 72
except:
    pass

# /usr/include/elf.h: 2364
try:
    R_PPC_TPREL32 = 73
except:
    pass

# /usr/include/elf.h: 2365
try:
    R_PPC_DTPREL16 = 74
except:
    pass

# /usr/include/elf.h: 2366
try:
    R_PPC_DTPREL16_LO = 75
except:
    pass

# /usr/include/elf.h: 2367
try:
    R_PPC_DTPREL16_HI = 76
except:
    pass

# /usr/include/elf.h: 2368
try:
    R_PPC_DTPREL16_HA = 77
except:
    pass

# /usr/include/elf.h: 2369
try:
    R_PPC_DTPREL32 = 78
except:
    pass

# /usr/include/elf.h: 2370
try:
    R_PPC_GOT_TLSGD16 = 79
except:
    pass

# /usr/include/elf.h: 2371
try:
    R_PPC_GOT_TLSGD16_LO = 80
except:
    pass

# /usr/include/elf.h: 2372
try:
    R_PPC_GOT_TLSGD16_HI = 81
except:
    pass

# /usr/include/elf.h: 2373
try:
    R_PPC_GOT_TLSGD16_HA = 82
except:
    pass

# /usr/include/elf.h: 2374
try:
    R_PPC_GOT_TLSLD16 = 83
except:
    pass

# /usr/include/elf.h: 2375
try:
    R_PPC_GOT_TLSLD16_LO = 84
except:
    pass

# /usr/include/elf.h: 2376
try:
    R_PPC_GOT_TLSLD16_HI = 85
except:
    pass

# /usr/include/elf.h: 2377
try:
    R_PPC_GOT_TLSLD16_HA = 86
except:
    pass

# /usr/include/elf.h: 2378
try:
    R_PPC_GOT_TPREL16 = 87
except:
    pass

# /usr/include/elf.h: 2379
try:
    R_PPC_GOT_TPREL16_LO = 88
except:
    pass

# /usr/include/elf.h: 2380
try:
    R_PPC_GOT_TPREL16_HI = 89
except:
    pass

# /usr/include/elf.h: 2381
try:
    R_PPC_GOT_TPREL16_HA = 90
except:
    pass

# /usr/include/elf.h: 2382
try:
    R_PPC_GOT_DTPREL16 = 91
except:
    pass

# /usr/include/elf.h: 2383
try:
    R_PPC_GOT_DTPREL16_LO = 92
except:
    pass

# /usr/include/elf.h: 2384
try:
    R_PPC_GOT_DTPREL16_HI = 93
except:
    pass

# /usr/include/elf.h: 2385
try:
    R_PPC_GOT_DTPREL16_HA = 94
except:
    pass

# /usr/include/elf.h: 2386
try:
    R_PPC_TLSGD = 95
except:
    pass

# /usr/include/elf.h: 2387
try:
    R_PPC_TLSLD = 96
except:
    pass

# /usr/include/elf.h: 2391
try:
    R_PPC_EMB_NADDR32 = 101
except:
    pass

# /usr/include/elf.h: 2392
try:
    R_PPC_EMB_NADDR16 = 102
except:
    pass

# /usr/include/elf.h: 2393
try:
    R_PPC_EMB_NADDR16_LO = 103
except:
    pass

# /usr/include/elf.h: 2394
try:
    R_PPC_EMB_NADDR16_HI = 104
except:
    pass

# /usr/include/elf.h: 2395
try:
    R_PPC_EMB_NADDR16_HA = 105
except:
    pass

# /usr/include/elf.h: 2396
try:
    R_PPC_EMB_SDAI16 = 106
except:
    pass

# /usr/include/elf.h: 2397
try:
    R_PPC_EMB_SDA2I16 = 107
except:
    pass

# /usr/include/elf.h: 2398
try:
    R_PPC_EMB_SDA2REL = 108
except:
    pass

# /usr/include/elf.h: 2399
try:
    R_PPC_EMB_SDA21 = 109
except:
    pass

# /usr/include/elf.h: 2400
try:
    R_PPC_EMB_MRKREF = 110
except:
    pass

# /usr/include/elf.h: 2401
try:
    R_PPC_EMB_RELSEC16 = 111
except:
    pass

# /usr/include/elf.h: 2402
try:
    R_PPC_EMB_RELST_LO = 112
except:
    pass

# /usr/include/elf.h: 2403
try:
    R_PPC_EMB_RELST_HI = 113
except:
    pass

# /usr/include/elf.h: 2404
try:
    R_PPC_EMB_RELST_HA = 114
except:
    pass

# /usr/include/elf.h: 2405
try:
    R_PPC_EMB_BIT_FLD = 115
except:
    pass

# /usr/include/elf.h: 2406
try:
    R_PPC_EMB_RELSDA = 116
except:
    pass

# /usr/include/elf.h: 2409
try:
    R_PPC_DIAB_SDA21_LO = 180
except:
    pass

# /usr/include/elf.h: 2410
try:
    R_PPC_DIAB_SDA21_HI = 181
except:
    pass

# /usr/include/elf.h: 2411
try:
    R_PPC_DIAB_SDA21_HA = 182
except:
    pass

# /usr/include/elf.h: 2412
try:
    R_PPC_DIAB_RELSDA_LO = 183
except:
    pass

# /usr/include/elf.h: 2413
try:
    R_PPC_DIAB_RELSDA_HI = 184
except:
    pass

# /usr/include/elf.h: 2414
try:
    R_PPC_DIAB_RELSDA_HA = 185
except:
    pass

# /usr/include/elf.h: 2417
try:
    R_PPC_IRELATIVE = 248
except:
    pass

# /usr/include/elf.h: 2420
try:
    R_PPC_REL16 = 249
except:
    pass

# /usr/include/elf.h: 2421
try:
    R_PPC_REL16_LO = 250
except:
    pass

# /usr/include/elf.h: 2422
try:
    R_PPC_REL16_HI = 251
except:
    pass

# /usr/include/elf.h: 2423
try:
    R_PPC_REL16_HA = 252
except:
    pass

# /usr/include/elf.h: 2427
try:
    R_PPC_TOC16 = 255
except:
    pass

# /usr/include/elf.h: 2430
try:
    DT_PPC_GOT = (DT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 2431
try:
    DT_PPC_OPT = (DT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 2432
try:
    DT_PPC_NUM = 2
except:
    pass

# /usr/include/elf.h: 2435
try:
    PPC_OPT_TLS = 1
except:
    pass

# /usr/include/elf.h: 2438
try:
    R_PPC64_NONE = R_PPC_NONE
except:
    pass

# /usr/include/elf.h: 2439
try:
    R_PPC64_ADDR32 = R_PPC_ADDR32
except:
    pass

# /usr/include/elf.h: 2440
try:
    R_PPC64_ADDR24 = R_PPC_ADDR24
except:
    pass

# /usr/include/elf.h: 2441
try:
    R_PPC64_ADDR16 = R_PPC_ADDR16
except:
    pass

# /usr/include/elf.h: 2442
try:
    R_PPC64_ADDR16_LO = R_PPC_ADDR16_LO
except:
    pass

# /usr/include/elf.h: 2443
try:
    R_PPC64_ADDR16_HI = R_PPC_ADDR16_HI
except:
    pass

# /usr/include/elf.h: 2444
try:
    R_PPC64_ADDR16_HA = R_PPC_ADDR16_HA
except:
    pass

# /usr/include/elf.h: 2445
try:
    R_PPC64_ADDR14 = R_PPC_ADDR14
except:
    pass

# /usr/include/elf.h: 2446
try:
    R_PPC64_ADDR14_BRTAKEN = R_PPC_ADDR14_BRTAKEN
except:
    pass

# /usr/include/elf.h: 2447
try:
    R_PPC64_ADDR14_BRNTAKEN = R_PPC_ADDR14_BRNTAKEN
except:
    pass

# /usr/include/elf.h: 2448
try:
    R_PPC64_REL24 = R_PPC_REL24
except:
    pass

# /usr/include/elf.h: 2449
try:
    R_PPC64_REL14 = R_PPC_REL14
except:
    pass

# /usr/include/elf.h: 2450
try:
    R_PPC64_REL14_BRTAKEN = R_PPC_REL14_BRTAKEN
except:
    pass

# /usr/include/elf.h: 2451
try:
    R_PPC64_REL14_BRNTAKEN = R_PPC_REL14_BRNTAKEN
except:
    pass

# /usr/include/elf.h: 2452
try:
    R_PPC64_GOT16 = R_PPC_GOT16
except:
    pass

# /usr/include/elf.h: 2453
try:
    R_PPC64_GOT16_LO = R_PPC_GOT16_LO
except:
    pass

# /usr/include/elf.h: 2454
try:
    R_PPC64_GOT16_HI = R_PPC_GOT16_HI
except:
    pass

# /usr/include/elf.h: 2455
try:
    R_PPC64_GOT16_HA = R_PPC_GOT16_HA
except:
    pass

# /usr/include/elf.h: 2457
try:
    R_PPC64_COPY = R_PPC_COPY
except:
    pass

# /usr/include/elf.h: 2458
try:
    R_PPC64_GLOB_DAT = R_PPC_GLOB_DAT
except:
    pass

# /usr/include/elf.h: 2459
try:
    R_PPC64_JMP_SLOT = R_PPC_JMP_SLOT
except:
    pass

# /usr/include/elf.h: 2460
try:
    R_PPC64_RELATIVE = R_PPC_RELATIVE
except:
    pass

# /usr/include/elf.h: 2462
try:
    R_PPC64_UADDR32 = R_PPC_UADDR32
except:
    pass

# /usr/include/elf.h: 2463
try:
    R_PPC64_UADDR16 = R_PPC_UADDR16
except:
    pass

# /usr/include/elf.h: 2464
try:
    R_PPC64_REL32 = R_PPC_REL32
except:
    pass

# /usr/include/elf.h: 2465
try:
    R_PPC64_PLT32 = R_PPC_PLT32
except:
    pass

# /usr/include/elf.h: 2466
try:
    R_PPC64_PLTREL32 = R_PPC_PLTREL32
except:
    pass

# /usr/include/elf.h: 2467
try:
    R_PPC64_PLT16_LO = R_PPC_PLT16_LO
except:
    pass

# /usr/include/elf.h: 2468
try:
    R_PPC64_PLT16_HI = R_PPC_PLT16_HI
except:
    pass

# /usr/include/elf.h: 2469
try:
    R_PPC64_PLT16_HA = R_PPC_PLT16_HA
except:
    pass

# /usr/include/elf.h: 2471
try:
    R_PPC64_SECTOFF = R_PPC_SECTOFF
except:
    pass

# /usr/include/elf.h: 2472
try:
    R_PPC64_SECTOFF_LO = R_PPC_SECTOFF_LO
except:
    pass

# /usr/include/elf.h: 2473
try:
    R_PPC64_SECTOFF_HI = R_PPC_SECTOFF_HI
except:
    pass

# /usr/include/elf.h: 2474
try:
    R_PPC64_SECTOFF_HA = R_PPC_SECTOFF_HA
except:
    pass

# /usr/include/elf.h: 2475
try:
    R_PPC64_ADDR30 = 37
except:
    pass

# /usr/include/elf.h: 2476
try:
    R_PPC64_ADDR64 = 38
except:
    pass

# /usr/include/elf.h: 2477
try:
    R_PPC64_ADDR16_HIGHER = 39
except:
    pass

# /usr/include/elf.h: 2478
try:
    R_PPC64_ADDR16_HIGHERA = 40
except:
    pass

# /usr/include/elf.h: 2479
try:
    R_PPC64_ADDR16_HIGHEST = 41
except:
    pass

# /usr/include/elf.h: 2480
try:
    R_PPC64_ADDR16_HIGHESTA = 42
except:
    pass

# /usr/include/elf.h: 2481
try:
    R_PPC64_UADDR64 = 43
except:
    pass

# /usr/include/elf.h: 2482
try:
    R_PPC64_REL64 = 44
except:
    pass

# /usr/include/elf.h: 2483
try:
    R_PPC64_PLT64 = 45
except:
    pass

# /usr/include/elf.h: 2484
try:
    R_PPC64_PLTREL64 = 46
except:
    pass

# /usr/include/elf.h: 2485
try:
    R_PPC64_TOC16 = 47
except:
    pass

# /usr/include/elf.h: 2486
try:
    R_PPC64_TOC16_LO = 48
except:
    pass

# /usr/include/elf.h: 2487
try:
    R_PPC64_TOC16_HI = 49
except:
    pass

# /usr/include/elf.h: 2488
try:
    R_PPC64_TOC16_HA = 50
except:
    pass

# /usr/include/elf.h: 2489
try:
    R_PPC64_TOC = 51
except:
    pass

# /usr/include/elf.h: 2490
try:
    R_PPC64_PLTGOT16 = 52
except:
    pass

# /usr/include/elf.h: 2491
try:
    R_PPC64_PLTGOT16_LO = 53
except:
    pass

# /usr/include/elf.h: 2492
try:
    R_PPC64_PLTGOT16_HI = 54
except:
    pass

# /usr/include/elf.h: 2493
try:
    R_PPC64_PLTGOT16_HA = 55
except:
    pass

# /usr/include/elf.h: 2495
try:
    R_PPC64_ADDR16_DS = 56
except:
    pass

# /usr/include/elf.h: 2496
try:
    R_PPC64_ADDR16_LO_DS = 57
except:
    pass

# /usr/include/elf.h: 2497
try:
    R_PPC64_GOT16_DS = 58
except:
    pass

# /usr/include/elf.h: 2498
try:
    R_PPC64_GOT16_LO_DS = 59
except:
    pass

# /usr/include/elf.h: 2499
try:
    R_PPC64_PLT16_LO_DS = 60
except:
    pass

# /usr/include/elf.h: 2500
try:
    R_PPC64_SECTOFF_DS = 61
except:
    pass

# /usr/include/elf.h: 2501
try:
    R_PPC64_SECTOFF_LO_DS = 62
except:
    pass

# /usr/include/elf.h: 2502
try:
    R_PPC64_TOC16_DS = 63
except:
    pass

# /usr/include/elf.h: 2503
try:
    R_PPC64_TOC16_LO_DS = 64
except:
    pass

# /usr/include/elf.h: 2504
try:
    R_PPC64_PLTGOT16_DS = 65
except:
    pass

# /usr/include/elf.h: 2505
try:
    R_PPC64_PLTGOT16_LO_DS = 66
except:
    pass

# /usr/include/elf.h: 2508
try:
    R_PPC64_TLS = 67
except:
    pass

# /usr/include/elf.h: 2509
try:
    R_PPC64_DTPMOD64 = 68
except:
    pass

# /usr/include/elf.h: 2510
try:
    R_PPC64_TPREL16 = 69
except:
    pass

# /usr/include/elf.h: 2511
try:
    R_PPC64_TPREL16_LO = 70
except:
    pass

# /usr/include/elf.h: 2512
try:
    R_PPC64_TPREL16_HI = 71
except:
    pass

# /usr/include/elf.h: 2513
try:
    R_PPC64_TPREL16_HA = 72
except:
    pass

# /usr/include/elf.h: 2514
try:
    R_PPC64_TPREL64 = 73
except:
    pass

# /usr/include/elf.h: 2515
try:
    R_PPC64_DTPREL16 = 74
except:
    pass

# /usr/include/elf.h: 2516
try:
    R_PPC64_DTPREL16_LO = 75
except:
    pass

# /usr/include/elf.h: 2517
try:
    R_PPC64_DTPREL16_HI = 76
except:
    pass

# /usr/include/elf.h: 2518
try:
    R_PPC64_DTPREL16_HA = 77
except:
    pass

# /usr/include/elf.h: 2519
try:
    R_PPC64_DTPREL64 = 78
except:
    pass

# /usr/include/elf.h: 2520
try:
    R_PPC64_GOT_TLSGD16 = 79
except:
    pass

# /usr/include/elf.h: 2521
try:
    R_PPC64_GOT_TLSGD16_LO = 80
except:
    pass

# /usr/include/elf.h: 2522
try:
    R_PPC64_GOT_TLSGD16_HI = 81
except:
    pass

# /usr/include/elf.h: 2523
try:
    R_PPC64_GOT_TLSGD16_HA = 82
except:
    pass

# /usr/include/elf.h: 2524
try:
    R_PPC64_GOT_TLSLD16 = 83
except:
    pass

# /usr/include/elf.h: 2525
try:
    R_PPC64_GOT_TLSLD16_LO = 84
except:
    pass

# /usr/include/elf.h: 2526
try:
    R_PPC64_GOT_TLSLD16_HI = 85
except:
    pass

# /usr/include/elf.h: 2527
try:
    R_PPC64_GOT_TLSLD16_HA = 86
except:
    pass

# /usr/include/elf.h: 2528
try:
    R_PPC64_GOT_TPREL16_DS = 87
except:
    pass

# /usr/include/elf.h: 2529
try:
    R_PPC64_GOT_TPREL16_LO_DS = 88
except:
    pass

# /usr/include/elf.h: 2530
try:
    R_PPC64_GOT_TPREL16_HI = 89
except:
    pass

# /usr/include/elf.h: 2531
try:
    R_PPC64_GOT_TPREL16_HA = 90
except:
    pass

# /usr/include/elf.h: 2532
try:
    R_PPC64_GOT_DTPREL16_DS = 91
except:
    pass

# /usr/include/elf.h: 2533
try:
    R_PPC64_GOT_DTPREL16_LO_DS = 92
except:
    pass

# /usr/include/elf.h: 2534
try:
    R_PPC64_GOT_DTPREL16_HI = 93
except:
    pass

# /usr/include/elf.h: 2535
try:
    R_PPC64_GOT_DTPREL16_HA = 94
except:
    pass

# /usr/include/elf.h: 2536
try:
    R_PPC64_TPREL16_DS = 95
except:
    pass

# /usr/include/elf.h: 2537
try:
    R_PPC64_TPREL16_LO_DS = 96
except:
    pass

# /usr/include/elf.h: 2538
try:
    R_PPC64_TPREL16_HIGHER = 97
except:
    pass

# /usr/include/elf.h: 2539
try:
    R_PPC64_TPREL16_HIGHERA = 98
except:
    pass

# /usr/include/elf.h: 2540
try:
    R_PPC64_TPREL16_HIGHEST = 99
except:
    pass

# /usr/include/elf.h: 2541
try:
    R_PPC64_TPREL16_HIGHESTA = 100
except:
    pass

# /usr/include/elf.h: 2542
try:
    R_PPC64_DTPREL16_DS = 101
except:
    pass

# /usr/include/elf.h: 2543
try:
    R_PPC64_DTPREL16_LO_DS = 102
except:
    pass

# /usr/include/elf.h: 2544
try:
    R_PPC64_DTPREL16_HIGHER = 103
except:
    pass

# /usr/include/elf.h: 2545
try:
    R_PPC64_DTPREL16_HIGHERA = 104
except:
    pass

# /usr/include/elf.h: 2546
try:
    R_PPC64_DTPREL16_HIGHEST = 105
except:
    pass

# /usr/include/elf.h: 2547
try:
    R_PPC64_DTPREL16_HIGHESTA = 106
except:
    pass

# /usr/include/elf.h: 2548
try:
    R_PPC64_TLSGD = 107
except:
    pass

# /usr/include/elf.h: 2549
try:
    R_PPC64_TLSLD = 108
except:
    pass

# /usr/include/elf.h: 2550
try:
    R_PPC64_TOCSAVE = 109
except:
    pass

# /usr/include/elf.h: 2553
try:
    R_PPC64_ADDR16_HIGH = 110
except:
    pass

# /usr/include/elf.h: 2554
try:
    R_PPC64_ADDR16_HIGHA = 111
except:
    pass

# /usr/include/elf.h: 2555
try:
    R_PPC64_TPREL16_HIGH = 112
except:
    pass

# /usr/include/elf.h: 2556
try:
    R_PPC64_TPREL16_HIGHA = 113
except:
    pass

# /usr/include/elf.h: 2557
try:
    R_PPC64_DTPREL16_HIGH = 114
except:
    pass

# /usr/include/elf.h: 2558
try:
    R_PPC64_DTPREL16_HIGHA = 115
except:
    pass

# /usr/include/elf.h: 2561
try:
    R_PPC64_JMP_IREL = 247
except:
    pass

# /usr/include/elf.h: 2562
try:
    R_PPC64_IRELATIVE = 248
except:
    pass

# /usr/include/elf.h: 2563
try:
    R_PPC64_REL16 = 249
except:
    pass

# /usr/include/elf.h: 2564
try:
    R_PPC64_REL16_LO = 250
except:
    pass

# /usr/include/elf.h: 2565
try:
    R_PPC64_REL16_HI = 251
except:
    pass

# /usr/include/elf.h: 2566
try:
    R_PPC64_REL16_HA = 252
except:
    pass

# /usr/include/elf.h: 2572
try:
    EF_PPC64_ABI = 3
except:
    pass

# /usr/include/elf.h: 2575
try:
    DT_PPC64_GLINK = (DT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 2576
try:
    DT_PPC64_OPD = (DT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 2577
try:
    DT_PPC64_OPDSZ = (DT_LOPROC + 2)
except:
    pass

# /usr/include/elf.h: 2578
try:
    DT_PPC64_OPT = (DT_LOPROC + 3)
except:
    pass

# /usr/include/elf.h: 2579
try:
    DT_PPC64_NUM = 4
except:
    pass

# /usr/include/elf.h: 2582
try:
    PPC64_OPT_TLS = 1
except:
    pass

# /usr/include/elf.h: 2583
try:
    PPC64_OPT_MULTI_TOC = 2
except:
    pass

# /usr/include/elf.h: 2584
try:
    PPC64_OPT_LOCALENTRY = 4
except:
    pass

# /usr/include/elf.h: 2587
try:
    STO_PPC64_LOCAL_BIT = 5
except:
    pass

# /usr/include/elf.h: 2588
try:
    STO_PPC64_LOCAL_MASK = (7 << STO_PPC64_LOCAL_BIT)
except:
    pass

# /usr/include/elf.h: 2589
def PPC64_LOCAL_ENTRY_OFFSET(other):
    return (((1 << ((other & STO_PPC64_LOCAL_MASK) >> STO_PPC64_LOCAL_BIT)) >> 2) << 2)

# /usr/include/elf.h: 2596
try:
    EF_ARM_RELEXEC = 0x01
except:
    pass

# /usr/include/elf.h: 2597
try:
    EF_ARM_HASENTRY = 0x02
except:
    pass

# /usr/include/elf.h: 2598
try:
    EF_ARM_INTERWORK = 0x04
except:
    pass

# /usr/include/elf.h: 2599
try:
    EF_ARM_APCS_26 = 0x08
except:
    pass

# /usr/include/elf.h: 2600
try:
    EF_ARM_APCS_FLOAT = 0x10
except:
    pass

# /usr/include/elf.h: 2601
try:
    EF_ARM_PIC = 0x20
except:
    pass

# /usr/include/elf.h: 2602
try:
    EF_ARM_ALIGN8 = 0x40
except:
    pass

# /usr/include/elf.h: 2603
try:
    EF_ARM_NEW_ABI = 0x80
except:
    pass

# /usr/include/elf.h: 2604
try:
    EF_ARM_OLD_ABI = 0x100
except:
    pass

# /usr/include/elf.h: 2605
try:
    EF_ARM_SOFT_FLOAT = 0x200
except:
    pass

# /usr/include/elf.h: 2606
try:
    EF_ARM_VFP_FLOAT = 0x400
except:
    pass

# /usr/include/elf.h: 2607
try:
    EF_ARM_MAVERICK_FLOAT = 0x800
except:
    pass

# /usr/include/elf.h: 2609
try:
    EF_ARM_ABI_FLOAT_SOFT = 0x200
except:
    pass

# /usr/include/elf.h: 2610
try:
    EF_ARM_ABI_FLOAT_HARD = 0x400
except:
    pass

# /usr/include/elf.h: 2615
try:
    EF_ARM_SYMSARESORTED = 0x04
except:
    pass

# /usr/include/elf.h: 2616
try:
    EF_ARM_DYNSYMSUSESEGIDX = 0x08
except:
    pass

# /usr/include/elf.h: 2617
try:
    EF_ARM_MAPSYMSFIRST = 0x10
except:
    pass

# /usr/include/elf.h: 2618
try:
    EF_ARM_EABIMASK = 0XFF000000
except:
    pass

# /usr/include/elf.h: 2621
try:
    EF_ARM_BE8 = 0x00800000
except:
    pass

# /usr/include/elf.h: 2622
try:
    EF_ARM_LE8 = 0x00400000
except:
    pass

# /usr/include/elf.h: 2624
def EF_ARM_EABI_VERSION(flags):
    return (flags & EF_ARM_EABIMASK)

# /usr/include/elf.h: 2625
try:
    EF_ARM_EABI_UNKNOWN = 0x00000000
except:
    pass

# /usr/include/elf.h: 2626
try:
    EF_ARM_EABI_VER1 = 0x01000000
except:
    pass

# /usr/include/elf.h: 2627
try:
    EF_ARM_EABI_VER2 = 0x02000000
except:
    pass

# /usr/include/elf.h: 2628
try:
    EF_ARM_EABI_VER3 = 0x03000000
except:
    pass

# /usr/include/elf.h: 2629
try:
    EF_ARM_EABI_VER4 = 0x04000000
except:
    pass

# /usr/include/elf.h: 2630
try:
    EF_ARM_EABI_VER5 = 0x05000000
except:
    pass

# /usr/include/elf.h: 2633
try:
    STT_ARM_TFUNC = STT_LOPROC
except:
    pass

# /usr/include/elf.h: 2634
try:
    STT_ARM_16BIT = STT_HIPROC
except:
    pass

# /usr/include/elf.h: 2637
try:
    SHF_ARM_ENTRYSECT = 0x10000000
except:
    pass

# /usr/include/elf.h: 2638
try:
    SHF_ARM_COMDEF = 0x80000000
except:
    pass

# /usr/include/elf.h: 2642
try:
    PF_ARM_SB = 0x10000000
except:
    pass

# /usr/include/elf.h: 2644
try:
    PF_ARM_PI = 0x20000000
except:
    pass

# /usr/include/elf.h: 2645
try:
    PF_ARM_ABS = 0x40000000
except:
    pass

# /usr/include/elf.h: 2648
try:
    PT_ARM_EXIDX = (PT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 2651
try:
    SHT_ARM_EXIDX = (SHT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 2652
try:
    SHT_ARM_PREEMPTMAP = (SHT_LOPROC + 2)
except:
    pass

# /usr/include/elf.h: 2653
try:
    SHT_ARM_ATTRIBUTES = (SHT_LOPROC + 3)
except:
    pass

# /usr/include/elf.h: 2658
try:
    R_AARCH64_NONE = 0
except:
    pass

# /usr/include/elf.h: 2661
try:
    R_AARCH64_P32_ABS32 = 1
except:
    pass

# /usr/include/elf.h: 2662
try:
    R_AARCH64_P32_COPY = 180
except:
    pass

# /usr/include/elf.h: 2663
try:
    R_AARCH64_P32_GLOB_DAT = 181
except:
    pass

# /usr/include/elf.h: 2664
try:
    R_AARCH64_P32_JUMP_SLOT = 182
except:
    pass

# /usr/include/elf.h: 2665
try:
    R_AARCH64_P32_RELATIVE = 183
except:
    pass

# /usr/include/elf.h: 2666
try:
    R_AARCH64_P32_TLS_DTPMOD = 184
except:
    pass

# /usr/include/elf.h: 2667
try:
    R_AARCH64_P32_TLS_DTPREL = 185
except:
    pass

# /usr/include/elf.h: 2668
try:
    R_AARCH64_P32_TLS_TPREL = 186
except:
    pass

# /usr/include/elf.h: 2669
try:
    R_AARCH64_P32_TLSDESC = 187
except:
    pass

# /usr/include/elf.h: 2670
try:
    R_AARCH64_P32_IRELATIVE = 188
except:
    pass

# /usr/include/elf.h: 2673
try:
    R_AARCH64_ABS64 = 257
except:
    pass

# /usr/include/elf.h: 2674
try:
    R_AARCH64_ABS32 = 258
except:
    pass

# /usr/include/elf.h: 2675
try:
    R_AARCH64_ABS16 = 259
except:
    pass

# /usr/include/elf.h: 2676
try:
    R_AARCH64_PREL64 = 260
except:
    pass

# /usr/include/elf.h: 2677
try:
    R_AARCH64_PREL32 = 261
except:
    pass

# /usr/include/elf.h: 2678
try:
    R_AARCH64_PREL16 = 262
except:
    pass

# /usr/include/elf.h: 2679
try:
    R_AARCH64_MOVW_UABS_G0 = 263
except:
    pass

# /usr/include/elf.h: 2680
try:
    R_AARCH64_MOVW_UABS_G0_NC = 264
except:
    pass

# /usr/include/elf.h: 2681
try:
    R_AARCH64_MOVW_UABS_G1 = 265
except:
    pass

# /usr/include/elf.h: 2682
try:
    R_AARCH64_MOVW_UABS_G1_NC = 266
except:
    pass

# /usr/include/elf.h: 2683
try:
    R_AARCH64_MOVW_UABS_G2 = 267
except:
    pass

# /usr/include/elf.h: 2684
try:
    R_AARCH64_MOVW_UABS_G2_NC = 268
except:
    pass

# /usr/include/elf.h: 2685
try:
    R_AARCH64_MOVW_UABS_G3 = 269
except:
    pass

# /usr/include/elf.h: 2686
try:
    R_AARCH64_MOVW_SABS_G0 = 270
except:
    pass

# /usr/include/elf.h: 2687
try:
    R_AARCH64_MOVW_SABS_G1 = 271
except:
    pass

# /usr/include/elf.h: 2688
try:
    R_AARCH64_MOVW_SABS_G2 = 272
except:
    pass

# /usr/include/elf.h: 2689
try:
    R_AARCH64_LD_PREL_LO19 = 273
except:
    pass

# /usr/include/elf.h: 2690
try:
    R_AARCH64_ADR_PREL_LO21 = 274
except:
    pass

# /usr/include/elf.h: 2691
try:
    R_AARCH64_ADR_PREL_PG_HI21 = 275
except:
    pass

# /usr/include/elf.h: 2692
try:
    R_AARCH64_ADR_PREL_PG_HI21_NC = 276
except:
    pass

# /usr/include/elf.h: 2693
try:
    R_AARCH64_ADD_ABS_LO12_NC = 277
except:
    pass

# /usr/include/elf.h: 2694
try:
    R_AARCH64_LDST8_ABS_LO12_NC = 278
except:
    pass

# /usr/include/elf.h: 2695
try:
    R_AARCH64_TSTBR14 = 279
except:
    pass

# /usr/include/elf.h: 2696
try:
    R_AARCH64_CONDBR19 = 280
except:
    pass

# /usr/include/elf.h: 2697
try:
    R_AARCH64_JUMP26 = 282
except:
    pass

# /usr/include/elf.h: 2698
try:
    R_AARCH64_CALL26 = 283
except:
    pass

# /usr/include/elf.h: 2699
try:
    R_AARCH64_LDST16_ABS_LO12_NC = 284
except:
    pass

# /usr/include/elf.h: 2700
try:
    R_AARCH64_LDST32_ABS_LO12_NC = 285
except:
    pass

# /usr/include/elf.h: 2701
try:
    R_AARCH64_LDST64_ABS_LO12_NC = 286
except:
    pass

# /usr/include/elf.h: 2702
try:
    R_AARCH64_MOVW_PREL_G0 = 287
except:
    pass

# /usr/include/elf.h: 2703
try:
    R_AARCH64_MOVW_PREL_G0_NC = 288
except:
    pass

# /usr/include/elf.h: 2704
try:
    R_AARCH64_MOVW_PREL_G1 = 289
except:
    pass

# /usr/include/elf.h: 2705
try:
    R_AARCH64_MOVW_PREL_G1_NC = 290
except:
    pass

# /usr/include/elf.h: 2706
try:
    R_AARCH64_MOVW_PREL_G2 = 291
except:
    pass

# /usr/include/elf.h: 2707
try:
    R_AARCH64_MOVW_PREL_G2_NC = 292
except:
    pass

# /usr/include/elf.h: 2708
try:
    R_AARCH64_MOVW_PREL_G3 = 293
except:
    pass

# /usr/include/elf.h: 2709
try:
    R_AARCH64_LDST128_ABS_LO12_NC = 299
except:
    pass

# /usr/include/elf.h: 2710
try:
    R_AARCH64_MOVW_GOTOFF_G0 = 300
except:
    pass

# /usr/include/elf.h: 2711
try:
    R_AARCH64_MOVW_GOTOFF_G0_NC = 301
except:
    pass

# /usr/include/elf.h: 2712
try:
    R_AARCH64_MOVW_GOTOFF_G1 = 302
except:
    pass

# /usr/include/elf.h: 2713
try:
    R_AARCH64_MOVW_GOTOFF_G1_NC = 303
except:
    pass

# /usr/include/elf.h: 2714
try:
    R_AARCH64_MOVW_GOTOFF_G2 = 304
except:
    pass

# /usr/include/elf.h: 2715
try:
    R_AARCH64_MOVW_GOTOFF_G2_NC = 305
except:
    pass

# /usr/include/elf.h: 2716
try:
    R_AARCH64_MOVW_GOTOFF_G3 = 306
except:
    pass

# /usr/include/elf.h: 2717
try:
    R_AARCH64_GOTREL64 = 307
except:
    pass

# /usr/include/elf.h: 2718
try:
    R_AARCH64_GOTREL32 = 308
except:
    pass

# /usr/include/elf.h: 2719
try:
    R_AARCH64_GOT_LD_PREL19 = 309
except:
    pass

# /usr/include/elf.h: 2720
try:
    R_AARCH64_LD64_GOTOFF_LO15 = 310
except:
    pass

# /usr/include/elf.h: 2721
try:
    R_AARCH64_ADR_GOT_PAGE = 311
except:
    pass

# /usr/include/elf.h: 2722
try:
    R_AARCH64_LD64_GOT_LO12_NC = 312
except:
    pass

# /usr/include/elf.h: 2723
try:
    R_AARCH64_LD64_GOTPAGE_LO15 = 313
except:
    pass

# /usr/include/elf.h: 2724
try:
    R_AARCH64_TLSGD_ADR_PREL21 = 512
except:
    pass

# /usr/include/elf.h: 2725
try:
    R_AARCH64_TLSGD_ADR_PAGE21 = 513
except:
    pass

# /usr/include/elf.h: 2726
try:
    R_AARCH64_TLSGD_ADD_LO12_NC = 514
except:
    pass

# /usr/include/elf.h: 2727
try:
    R_AARCH64_TLSGD_MOVW_G1 = 515
except:
    pass

# /usr/include/elf.h: 2728
try:
    R_AARCH64_TLSGD_MOVW_G0_NC = 516
except:
    pass

# /usr/include/elf.h: 2729
try:
    R_AARCH64_TLSLD_ADR_PREL21 = 517
except:
    pass

# /usr/include/elf.h: 2730
try:
    R_AARCH64_TLSLD_ADR_PAGE21 = 518
except:
    pass

# /usr/include/elf.h: 2731
try:
    R_AARCH64_TLSLD_ADD_LO12_NC = 519
except:
    pass

# /usr/include/elf.h: 2732
try:
    R_AARCH64_TLSLD_MOVW_G1 = 520
except:
    pass

# /usr/include/elf.h: 2733
try:
    R_AARCH64_TLSLD_MOVW_G0_NC = 521
except:
    pass

# /usr/include/elf.h: 2734
try:
    R_AARCH64_TLSLD_LD_PREL19 = 522
except:
    pass

# /usr/include/elf.h: 2735
try:
    R_AARCH64_TLSLD_MOVW_DTPREL_G2 = 523
except:
    pass

# /usr/include/elf.h: 2736
try:
    R_AARCH64_TLSLD_MOVW_DTPREL_G1 = 524
except:
    pass

# /usr/include/elf.h: 2737
try:
    R_AARCH64_TLSLD_MOVW_DTPREL_G1_NC = 525
except:
    pass

# /usr/include/elf.h: 2738
try:
    R_AARCH64_TLSLD_MOVW_DTPREL_G0 = 526
except:
    pass

# /usr/include/elf.h: 2739
try:
    R_AARCH64_TLSLD_MOVW_DTPREL_G0_NC = 527
except:
    pass

# /usr/include/elf.h: 2740
try:
    R_AARCH64_TLSLD_ADD_DTPREL_HI12 = 528
except:
    pass

# /usr/include/elf.h: 2741
try:
    R_AARCH64_TLSLD_ADD_DTPREL_LO12 = 529
except:
    pass

# /usr/include/elf.h: 2742
try:
    R_AARCH64_TLSLD_ADD_DTPREL_LO12_NC = 530
except:
    pass

# /usr/include/elf.h: 2743
try:
    R_AARCH64_TLSLD_LDST8_DTPREL_LO12 = 531
except:
    pass

# /usr/include/elf.h: 2744
try:
    R_AARCH64_TLSLD_LDST8_DTPREL_LO12_NC = 532
except:
    pass

# /usr/include/elf.h: 2745
try:
    R_AARCH64_TLSLD_LDST16_DTPREL_LO12 = 533
except:
    pass

# /usr/include/elf.h: 2746
try:
    R_AARCH64_TLSLD_LDST16_DTPREL_LO12_NC = 534
except:
    pass

# /usr/include/elf.h: 2747
try:
    R_AARCH64_TLSLD_LDST32_DTPREL_LO12 = 535
except:
    pass

# /usr/include/elf.h: 2748
try:
    R_AARCH64_TLSLD_LDST32_DTPREL_LO12_NC = 536
except:
    pass

# /usr/include/elf.h: 2749
try:
    R_AARCH64_TLSLD_LDST64_DTPREL_LO12 = 537
except:
    pass

# /usr/include/elf.h: 2750
try:
    R_AARCH64_TLSLD_LDST64_DTPREL_LO12_NC = 538
except:
    pass

# /usr/include/elf.h: 2751
try:
    R_AARCH64_TLSIE_MOVW_GOTTPREL_G1 = 539
except:
    pass

# /usr/include/elf.h: 2752
try:
    R_AARCH64_TLSIE_MOVW_GOTTPREL_G0_NC = 540
except:
    pass

# /usr/include/elf.h: 2753
try:
    R_AARCH64_TLSIE_ADR_GOTTPREL_PAGE21 = 541
except:
    pass

# /usr/include/elf.h: 2754
try:
    R_AARCH64_TLSIE_LD64_GOTTPREL_LO12_NC = 542
except:
    pass

# /usr/include/elf.h: 2755
try:
    R_AARCH64_TLSIE_LD_GOTTPREL_PREL19 = 543
except:
    pass

# /usr/include/elf.h: 2756
try:
    R_AARCH64_TLSLE_MOVW_TPREL_G2 = 544
except:
    pass

# /usr/include/elf.h: 2757
try:
    R_AARCH64_TLSLE_MOVW_TPREL_G1 = 545
except:
    pass

# /usr/include/elf.h: 2758
try:
    R_AARCH64_TLSLE_MOVW_TPREL_G1_NC = 546
except:
    pass

# /usr/include/elf.h: 2759
try:
    R_AARCH64_TLSLE_MOVW_TPREL_G0 = 547
except:
    pass

# /usr/include/elf.h: 2760
try:
    R_AARCH64_TLSLE_MOVW_TPREL_G0_NC = 548
except:
    pass

# /usr/include/elf.h: 2761
try:
    R_AARCH64_TLSLE_ADD_TPREL_HI12 = 549
except:
    pass

# /usr/include/elf.h: 2762
try:
    R_AARCH64_TLSLE_ADD_TPREL_LO12 = 550
except:
    pass

# /usr/include/elf.h: 2763
try:
    R_AARCH64_TLSLE_ADD_TPREL_LO12_NC = 551
except:
    pass

# /usr/include/elf.h: 2764
try:
    R_AARCH64_TLSLE_LDST8_TPREL_LO12 = 552
except:
    pass

# /usr/include/elf.h: 2765
try:
    R_AARCH64_TLSLE_LDST8_TPREL_LO12_NC = 553
except:
    pass

# /usr/include/elf.h: 2766
try:
    R_AARCH64_TLSLE_LDST16_TPREL_LO12 = 554
except:
    pass

# /usr/include/elf.h: 2767
try:
    R_AARCH64_TLSLE_LDST16_TPREL_LO12_NC = 555
except:
    pass

# /usr/include/elf.h: 2768
try:
    R_AARCH64_TLSLE_LDST32_TPREL_LO12 = 556
except:
    pass

# /usr/include/elf.h: 2769
try:
    R_AARCH64_TLSLE_LDST32_TPREL_LO12_NC = 557
except:
    pass

# /usr/include/elf.h: 2770
try:
    R_AARCH64_TLSLE_LDST64_TPREL_LO12 = 558
except:
    pass

# /usr/include/elf.h: 2771
try:
    R_AARCH64_TLSLE_LDST64_TPREL_LO12_NC = 559
except:
    pass

# /usr/include/elf.h: 2772
try:
    R_AARCH64_TLSDESC_LD_PREL19 = 560
except:
    pass

# /usr/include/elf.h: 2773
try:
    R_AARCH64_TLSDESC_ADR_PREL21 = 561
except:
    pass

# /usr/include/elf.h: 2774
try:
    R_AARCH64_TLSDESC_ADR_PAGE21 = 562
except:
    pass

# /usr/include/elf.h: 2775
try:
    R_AARCH64_TLSDESC_LD64_LO12 = 563
except:
    pass

# /usr/include/elf.h: 2776
try:
    R_AARCH64_TLSDESC_ADD_LO12 = 564
except:
    pass

# /usr/include/elf.h: 2777
try:
    R_AARCH64_TLSDESC_OFF_G1 = 565
except:
    pass

# /usr/include/elf.h: 2778
try:
    R_AARCH64_TLSDESC_OFF_G0_NC = 566
except:
    pass

# /usr/include/elf.h: 2779
try:
    R_AARCH64_TLSDESC_LDR = 567
except:
    pass

# /usr/include/elf.h: 2780
try:
    R_AARCH64_TLSDESC_ADD = 568
except:
    pass

# /usr/include/elf.h: 2781
try:
    R_AARCH64_TLSDESC_CALL = 569
except:
    pass

# /usr/include/elf.h: 2782
try:
    R_AARCH64_TLSLE_LDST128_TPREL_LO12 = 570
except:
    pass

# /usr/include/elf.h: 2783
try:
    R_AARCH64_TLSLE_LDST128_TPREL_LO12_NC = 571
except:
    pass

# /usr/include/elf.h: 2784
try:
    R_AARCH64_TLSLD_LDST128_DTPREL_LO12 = 572
except:
    pass

# /usr/include/elf.h: 2785
try:
    R_AARCH64_TLSLD_LDST128_DTPREL_LO12_NC = 573
except:
    pass

# /usr/include/elf.h: 2786
try:
    R_AARCH64_COPY = 1024
except:
    pass

# /usr/include/elf.h: 2787
try:
    R_AARCH64_GLOB_DAT = 1025
except:
    pass

# /usr/include/elf.h: 2788
try:
    R_AARCH64_JUMP_SLOT = 1026
except:
    pass

# /usr/include/elf.h: 2789
try:
    R_AARCH64_RELATIVE = 1027
except:
    pass

# /usr/include/elf.h: 2790
try:
    R_AARCH64_TLS_DTPMOD = 1028
except:
    pass

# /usr/include/elf.h: 2791
try:
    R_AARCH64_TLS_DTPREL = 1029
except:
    pass

# /usr/include/elf.h: 2792
try:
    R_AARCH64_TLS_TPREL = 1030
except:
    pass

# /usr/include/elf.h: 2793
try:
    R_AARCH64_TLSDESC = 1031
except:
    pass

# /usr/include/elf.h: 2794
try:
    R_AARCH64_IRELATIVE = 1032
except:
    pass

# /usr/include/elf.h: 2797
try:
    DT_AARCH64_VARIANT_PCS = (DT_LOPROC + 5)
except:
    pass

# /usr/include/elf.h: 2798
try:
    DT_AARCH64_NUM = 6
except:
    pass

# /usr/include/elf.h: 2801
try:
    STO_AARCH64_VARIANT_PCS = 0x80
except:
    pass

# /usr/include/elf.h: 2805
try:
    R_ARM_NONE = 0
except:
    pass

# /usr/include/elf.h: 2806
try:
    R_ARM_PC24 = 1
except:
    pass

# /usr/include/elf.h: 2808
try:
    R_ARM_ABS32 = 2
except:
    pass

# /usr/include/elf.h: 2809
try:
    R_ARM_REL32 = 3
except:
    pass

# /usr/include/elf.h: 2810
try:
    R_ARM_PC13 = 4
except:
    pass

# /usr/include/elf.h: 2811
try:
    R_ARM_ABS16 = 5
except:
    pass

# /usr/include/elf.h: 2812
try:
    R_ARM_ABS12 = 6
except:
    pass

# /usr/include/elf.h: 2813
try:
    R_ARM_THM_ABS5 = 7
except:
    pass

# /usr/include/elf.h: 2814
try:
    R_ARM_ABS8 = 8
except:
    pass

# /usr/include/elf.h: 2815
try:
    R_ARM_SBREL32 = 9
except:
    pass

# /usr/include/elf.h: 2816
try:
    R_ARM_THM_PC22 = 10
except:
    pass

# /usr/include/elf.h: 2817
try:
    R_ARM_THM_PC8 = 11
except:
    pass

# /usr/include/elf.h: 2819
try:
    R_ARM_AMP_VCALL9 = 12
except:
    pass

# /usr/include/elf.h: 2820
try:
    R_ARM_SWI24 = 13
except:
    pass

# /usr/include/elf.h: 2821
try:
    R_ARM_TLS_DESC = 13
except:
    pass

# /usr/include/elf.h: 2822
try:
    R_ARM_THM_SWI8 = 14
except:
    pass

# /usr/include/elf.h: 2823
try:
    R_ARM_XPC25 = 15
except:
    pass

# /usr/include/elf.h: 2824
try:
    R_ARM_THM_XPC22 = 16
except:
    pass

# /usr/include/elf.h: 2825
try:
    R_ARM_TLS_DTPMOD32 = 17
except:
    pass

# /usr/include/elf.h: 2826
try:
    R_ARM_TLS_DTPOFF32 = 18
except:
    pass

# /usr/include/elf.h: 2827
try:
    R_ARM_TLS_TPOFF32 = 19
except:
    pass

# /usr/include/elf.h: 2828
try:
    R_ARM_COPY = 20
except:
    pass

# /usr/include/elf.h: 2829
try:
    R_ARM_GLOB_DAT = 21
except:
    pass

# /usr/include/elf.h: 2830
try:
    R_ARM_JUMP_SLOT = 22
except:
    pass

# /usr/include/elf.h: 2831
try:
    R_ARM_RELATIVE = 23
except:
    pass

# /usr/include/elf.h: 2832
try:
    R_ARM_GOTOFF = 24
except:
    pass

# /usr/include/elf.h: 2833
try:
    R_ARM_GOTPC = 25
except:
    pass

# /usr/include/elf.h: 2834
try:
    R_ARM_GOT32 = 26
except:
    pass

# /usr/include/elf.h: 2835
try:
    R_ARM_PLT32 = 27
except:
    pass

# /usr/include/elf.h: 2836
try:
    R_ARM_CALL = 28
except:
    pass

# /usr/include/elf.h: 2837
try:
    R_ARM_JUMP24 = 29
except:
    pass

# /usr/include/elf.h: 2839
try:
    R_ARM_THM_JUMP24 = 30
except:
    pass

# /usr/include/elf.h: 2840
try:
    R_ARM_BASE_ABS = 31
except:
    pass

# /usr/include/elf.h: 2841
try:
    R_ARM_ALU_PCREL_7_0 = 32
except:
    pass

# /usr/include/elf.h: 2842
try:
    R_ARM_ALU_PCREL_15_8 = 33
except:
    pass

# /usr/include/elf.h: 2843
try:
    R_ARM_ALU_PCREL_23_15 = 34
except:
    pass

# /usr/include/elf.h: 2844
try:
    R_ARM_LDR_SBREL_11_0 = 35
except:
    pass

# /usr/include/elf.h: 2845
try:
    R_ARM_ALU_SBREL_19_12 = 36
except:
    pass

# /usr/include/elf.h: 2846
try:
    R_ARM_ALU_SBREL_27_20 = 37
except:
    pass

# /usr/include/elf.h: 2847
try:
    R_ARM_TARGET1 = 38
except:
    pass

# /usr/include/elf.h: 2848
try:
    R_ARM_SBREL31 = 39
except:
    pass

# /usr/include/elf.h: 2849
try:
    R_ARM_V4BX = 40
except:
    pass

# /usr/include/elf.h: 2850
try:
    R_ARM_TARGET2 = 41
except:
    pass

# /usr/include/elf.h: 2851
try:
    R_ARM_PREL31 = 42
except:
    pass

# /usr/include/elf.h: 2852
try:
    R_ARM_MOVW_ABS_NC = 43
except:
    pass

# /usr/include/elf.h: 2853
try:
    R_ARM_MOVT_ABS = 44
except:
    pass

# /usr/include/elf.h: 2854
try:
    R_ARM_MOVW_PREL_NC = 45
except:
    pass

# /usr/include/elf.h: 2855
try:
    R_ARM_MOVT_PREL = 46
except:
    pass

# /usr/include/elf.h: 2856
try:
    R_ARM_THM_MOVW_ABS_NC = 47
except:
    pass

# /usr/include/elf.h: 2857
try:
    R_ARM_THM_MOVT_ABS = 48
except:
    pass

# /usr/include/elf.h: 2859
try:
    R_ARM_THM_MOVW_PREL_NC = 49
except:
    pass

# /usr/include/elf.h: 2861
try:
    R_ARM_THM_MOVT_PREL = 50
except:
    pass

# /usr/include/elf.h: 2863
try:
    R_ARM_THM_JUMP19 = 51
except:
    pass

# /usr/include/elf.h: 2865
try:
    R_ARM_THM_JUMP6 = 52
except:
    pass

# /usr/include/elf.h: 2867
try:
    R_ARM_THM_ALU_PREL_11_0 = 53
except:
    pass

# /usr/include/elf.h: 2869
try:
    R_ARM_THM_PC12 = 54
except:
    pass

# /usr/include/elf.h: 2871
try:
    R_ARM_ABS32_NOI = 55
except:
    pass

# /usr/include/elf.h: 2872
try:
    R_ARM_REL32_NOI = 56
except:
    pass

# /usr/include/elf.h: 2873
try:
    R_ARM_ALU_PC_G0_NC = 57
except:
    pass

# /usr/include/elf.h: 2874
try:
    R_ARM_ALU_PC_G0 = 58
except:
    pass

# /usr/include/elf.h: 2875
try:
    R_ARM_ALU_PC_G1_NC = 59
except:
    pass

# /usr/include/elf.h: 2876
try:
    R_ARM_ALU_PC_G1 = 60
except:
    pass

# /usr/include/elf.h: 2877
try:
    R_ARM_ALU_PC_G2 = 61
except:
    pass

# /usr/include/elf.h: 2878
try:
    R_ARM_LDR_PC_G1 = 62
except:
    pass

# /usr/include/elf.h: 2879
try:
    R_ARM_LDR_PC_G2 = 63
except:
    pass

# /usr/include/elf.h: 2880
try:
    R_ARM_LDRS_PC_G0 = 64
except:
    pass

# /usr/include/elf.h: 2882
try:
    R_ARM_LDRS_PC_G1 = 65
except:
    pass

# /usr/include/elf.h: 2884
try:
    R_ARM_LDRS_PC_G2 = 66
except:
    pass

# /usr/include/elf.h: 2886
try:
    R_ARM_LDC_PC_G0 = 67
except:
    pass

# /usr/include/elf.h: 2887
try:
    R_ARM_LDC_PC_G1 = 68
except:
    pass

# /usr/include/elf.h: 2888
try:
    R_ARM_LDC_PC_G2 = 69
except:
    pass

# /usr/include/elf.h: 2889
try:
    R_ARM_ALU_SB_G0_NC = 70
except:
    pass

# /usr/include/elf.h: 2890
try:
    R_ARM_ALU_SB_G0 = 71
except:
    pass

# /usr/include/elf.h: 2891
try:
    R_ARM_ALU_SB_G1_NC = 72
except:
    pass

# /usr/include/elf.h: 2892
try:
    R_ARM_ALU_SB_G1 = 73
except:
    pass

# /usr/include/elf.h: 2893
try:
    R_ARM_ALU_SB_G2 = 74
except:
    pass

# /usr/include/elf.h: 2894
try:
    R_ARM_LDR_SB_G0 = 75
except:
    pass

# /usr/include/elf.h: 2896
try:
    R_ARM_LDR_SB_G1 = 76
except:
    pass

# /usr/include/elf.h: 2898
try:
    R_ARM_LDR_SB_G2 = 77
except:
    pass

# /usr/include/elf.h: 2900
try:
    R_ARM_LDRS_SB_G0 = 78
except:
    pass

# /usr/include/elf.h: 2902
try:
    R_ARM_LDRS_SB_G1 = 79
except:
    pass

# /usr/include/elf.h: 2904
try:
    R_ARM_LDRS_SB_G2 = 80
except:
    pass

# /usr/include/elf.h: 2906
try:
    R_ARM_LDC_SB_G0 = 81
except:
    pass

# /usr/include/elf.h: 2907
try:
    R_ARM_LDC_SB_G1 = 82
except:
    pass

# /usr/include/elf.h: 2908
try:
    R_ARM_LDC_SB_G2 = 83
except:
    pass

# /usr/include/elf.h: 2909
try:
    R_ARM_MOVW_BREL_NC = 84
except:
    pass

# /usr/include/elf.h: 2911
try:
    R_ARM_MOVT_BREL = 85
except:
    pass

# /usr/include/elf.h: 2913
try:
    R_ARM_MOVW_BREL = 86
except:
    pass

# /usr/include/elf.h: 2915
try:
    R_ARM_THM_MOVW_BREL_NC = 87
except:
    pass

# /usr/include/elf.h: 2917
try:
    R_ARM_THM_MOVT_BREL = 88
except:
    pass

# /usr/include/elf.h: 2919
try:
    R_ARM_THM_MOVW_BREL = 89
except:
    pass

# /usr/include/elf.h: 2921
try:
    R_ARM_TLS_GOTDESC = 90
except:
    pass

# /usr/include/elf.h: 2922
try:
    R_ARM_TLS_CALL = 91
except:
    pass

# /usr/include/elf.h: 2923
try:
    R_ARM_TLS_DESCSEQ = 92
except:
    pass

# /usr/include/elf.h: 2924
try:
    R_ARM_THM_TLS_CALL = 93
except:
    pass

# /usr/include/elf.h: 2925
try:
    R_ARM_PLT32_ABS = 94
except:
    pass

# /usr/include/elf.h: 2926
try:
    R_ARM_GOT_ABS = 95
except:
    pass

# /usr/include/elf.h: 2927
try:
    R_ARM_GOT_PREL = 96
except:
    pass

# /usr/include/elf.h: 2928
try:
    R_ARM_GOT_BREL12 = 97
except:
    pass

# /usr/include/elf.h: 2930
try:
    R_ARM_GOTOFF12 = 98
except:
    pass

# /usr/include/elf.h: 2932
try:
    R_ARM_GOTRELAX = 99
except:
    pass

# /usr/include/elf.h: 2933
try:
    R_ARM_GNU_VTENTRY = 100
except:
    pass

# /usr/include/elf.h: 2934
try:
    R_ARM_GNU_VTINHERIT = 101
except:
    pass

# /usr/include/elf.h: 2935
try:
    R_ARM_THM_PC11 = 102
except:
    pass

# /usr/include/elf.h: 2936
try:
    R_ARM_THM_PC9 = 103
except:
    pass

# /usr/include/elf.h: 2938
try:
    R_ARM_TLS_GD32 = 104
except:
    pass

# /usr/include/elf.h: 2940
try:
    R_ARM_TLS_LDM32 = 105
except:
    pass

# /usr/include/elf.h: 2942
try:
    R_ARM_TLS_LDO32 = 106
except:
    pass

# /usr/include/elf.h: 2944
try:
    R_ARM_TLS_IE32 = 107
except:
    pass

# /usr/include/elf.h: 2946
try:
    R_ARM_TLS_LE32 = 108
except:
    pass

# /usr/include/elf.h: 2948
try:
    R_ARM_TLS_LDO12 = 109
except:
    pass

# /usr/include/elf.h: 2950
try:
    R_ARM_TLS_LE12 = 110
except:
    pass

# /usr/include/elf.h: 2952
try:
    R_ARM_TLS_IE12GP = 111
except:
    pass

# /usr/include/elf.h: 2954
try:
    R_ARM_ME_TOO = 128
except:
    pass

# /usr/include/elf.h: 2955
try:
    R_ARM_THM_TLS_DESCSEQ = 129
except:
    pass

# /usr/include/elf.h: 2956
try:
    R_ARM_THM_TLS_DESCSEQ16 = 129
except:
    pass

# /usr/include/elf.h: 2957
try:
    R_ARM_THM_TLS_DESCSEQ32 = 130
except:
    pass

# /usr/include/elf.h: 2958
try:
    R_ARM_THM_GOT_BREL12 = 131
except:
    pass

# /usr/include/elf.h: 2960
try:
    R_ARM_IRELATIVE = 160
except:
    pass

# /usr/include/elf.h: 2961
try:
    R_ARM_RXPC25 = 249
except:
    pass

# /usr/include/elf.h: 2962
try:
    R_ARM_RSBREL32 = 250
except:
    pass

# /usr/include/elf.h: 2963
try:
    R_ARM_THM_RPC22 = 251
except:
    pass

# /usr/include/elf.h: 2964
try:
    R_ARM_RREL32 = 252
except:
    pass

# /usr/include/elf.h: 2965
try:
    R_ARM_RABS22 = 253
except:
    pass

# /usr/include/elf.h: 2966
try:
    R_ARM_RPC24 = 254
except:
    pass

# /usr/include/elf.h: 2967
try:
    R_ARM_RBASE = 255
except:
    pass

# /usr/include/elf.h: 2969
try:
    R_ARM_NUM = 256
except:
    pass

# /usr/include/elf.h: 2972
try:
    R_CKCORE_NONE = 0
except:
    pass

# /usr/include/elf.h: 2973
try:
    R_CKCORE_ADDR32 = 1
except:
    pass

# /usr/include/elf.h: 2974
try:
    R_CKCORE_PCRELIMM8BY4 = 2
except:
    pass

# /usr/include/elf.h: 2975
try:
    R_CKCORE_PCRELIMM11BY2 = 3
except:
    pass

# /usr/include/elf.h: 2976
try:
    R_CKCORE_PCREL32 = 5
except:
    pass

# /usr/include/elf.h: 2977
try:
    R_CKCORE_PCRELJSR_IMM11BY2 = 6
except:
    pass

# /usr/include/elf.h: 2978
try:
    R_CKCORE_RELATIVE = 9
except:
    pass

# /usr/include/elf.h: 2979
try:
    R_CKCORE_COPY = 10
except:
    pass

# /usr/include/elf.h: 2980
try:
    R_CKCORE_GLOB_DAT = 11
except:
    pass

# /usr/include/elf.h: 2981
try:
    R_CKCORE_JUMP_SLOT = 12
except:
    pass

# /usr/include/elf.h: 2982
try:
    R_CKCORE_GOTOFF = 13
except:
    pass

# /usr/include/elf.h: 2983
try:
    R_CKCORE_GOTPC = 14
except:
    pass

# /usr/include/elf.h: 2984
try:
    R_CKCORE_GOT32 = 15
except:
    pass

# /usr/include/elf.h: 2985
try:
    R_CKCORE_PLT32 = 16
except:
    pass

# /usr/include/elf.h: 2986
try:
    R_CKCORE_ADDRGOT = 17
except:
    pass

# /usr/include/elf.h: 2987
try:
    R_CKCORE_ADDRPLT = 18
except:
    pass

# /usr/include/elf.h: 2988
try:
    R_CKCORE_PCREL_IMM26BY2 = 19
except:
    pass

# /usr/include/elf.h: 2989
try:
    R_CKCORE_PCREL_IMM16BY2 = 20
except:
    pass

# /usr/include/elf.h: 2990
try:
    R_CKCORE_PCREL_IMM16BY4 = 21
except:
    pass

# /usr/include/elf.h: 2991
try:
    R_CKCORE_PCREL_IMM10BY2 = 22
except:
    pass

# /usr/include/elf.h: 2992
try:
    R_CKCORE_PCREL_IMM10BY4 = 23
except:
    pass

# /usr/include/elf.h: 2993
try:
    R_CKCORE_ADDR_HI16 = 24
except:
    pass

# /usr/include/elf.h: 2995
try:
    R_CKCORE_ADDR_LO16 = 25
except:
    pass

# /usr/include/elf.h: 2996
try:
    R_CKCORE_GOTPC_HI16 = 26
except:
    pass

# /usr/include/elf.h: 2998
try:
    R_CKCORE_GOTPC_LO16 = 27
except:
    pass

# /usr/include/elf.h: 2999
try:
    R_CKCORE_GOTOFF_HI16 = 28
except:
    pass

# /usr/include/elf.h: 3001
try:
    R_CKCORE_GOTOFF_LO16 = 29
except:
    pass

# /usr/include/elf.h: 3002
try:
    R_CKCORE_GOT12 = 30
except:
    pass

# /usr/include/elf.h: 3003
try:
    R_CKCORE_GOT_HI16 = 31
except:
    pass

# /usr/include/elf.h: 3005
try:
    R_CKCORE_GOT_LO16 = 32
except:
    pass

# /usr/include/elf.h: 3006
try:
    R_CKCORE_PLT12 = 33
except:
    pass

# /usr/include/elf.h: 3007
try:
    R_CKCORE_PLT_HI16 = 34
except:
    pass

# /usr/include/elf.h: 3009
try:
    R_CKCORE_PLT_LO16 = 35
except:
    pass

# /usr/include/elf.h: 3010
try:
    R_CKCORE_ADDRGOT_HI16 = 36
except:
    pass

# /usr/include/elf.h: 3012
try:
    R_CKCORE_ADDRGOT_LO16 = 37
except:
    pass

# /usr/include/elf.h: 3013
try:
    R_CKCORE_ADDRPLT_HI16 = 38
except:
    pass

# /usr/include/elf.h: 3015
try:
    R_CKCORE_ADDRPLT_LO16 = 39
except:
    pass

# /usr/include/elf.h: 3016
try:
    R_CKCORE_PCREL_JSR_IMM26BY2 = 40
except:
    pass

# /usr/include/elf.h: 3017
try:
    R_CKCORE_TOFFSET_LO16 = 41
except:
    pass

# /usr/include/elf.h: 3018
try:
    R_CKCORE_DOFFSET_LO16 = 42
except:
    pass

# /usr/include/elf.h: 3019
try:
    R_CKCORE_PCREL_IMM18BY2 = 43
except:
    pass

# /usr/include/elf.h: 3020
try:
    R_CKCORE_DOFFSET_IMM18 = 44
except:
    pass

# /usr/include/elf.h: 3021
try:
    R_CKCORE_DOFFSET_IMM18BY2 = 45
except:
    pass

# /usr/include/elf.h: 3022
try:
    R_CKCORE_DOFFSET_IMM18BY4 = 46
except:
    pass

# /usr/include/elf.h: 3023
try:
    R_CKCORE_GOT_IMM18BY4 = 48
except:
    pass

# /usr/include/elf.h: 3024
try:
    R_CKCORE_PLT_IMM18BY4 = 49
except:
    pass

# /usr/include/elf.h: 3025
try:
    R_CKCORE_PCREL_IMM7BY4 = 50
except:
    pass

# /usr/include/elf.h: 3026
try:
    R_CKCORE_TLS_LE32 = 51
except:
    pass

# /usr/include/elf.h: 3027
try:
    R_CKCORE_TLS_IE32 = 52
except:
    pass

# /usr/include/elf.h: 3028
try:
    R_CKCORE_TLS_GD32 = 53
except:
    pass

# /usr/include/elf.h: 3029
try:
    R_CKCORE_TLS_LDM32 = 54
except:
    pass

# /usr/include/elf.h: 3030
try:
    R_CKCORE_TLS_LDO32 = 55
except:
    pass

# /usr/include/elf.h: 3031
try:
    R_CKCORE_TLS_DTPMOD32 = 56
except:
    pass

# /usr/include/elf.h: 3032
try:
    R_CKCORE_TLS_DTPOFF32 = 57
except:
    pass

# /usr/include/elf.h: 3033
try:
    R_CKCORE_TLS_TPOFF32 = 58
except:
    pass

# /usr/include/elf.h: 3036
try:
    EF_CSKY_ABIMASK = 0XF0000000
except:
    pass

# /usr/include/elf.h: 3037
try:
    EF_CSKY_OTHER = 0X0FFF0000
except:
    pass

# /usr/include/elf.h: 3038
try:
    EF_CSKY_PROCESSOR = 0X0000FFFF
except:
    pass

# /usr/include/elf.h: 3040
try:
    EF_CSKY_ABIV1 = 0X10000000
except:
    pass

# /usr/include/elf.h: 3041
try:
    EF_CSKY_ABIV2 = 0X20000000
except:
    pass

# /usr/include/elf.h: 3044
try:
    SHT_CSKY_ATTRIBUTES = (SHT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 3049
try:
    EF_IA_64_MASKOS = 0x0000000f
except:
    pass

# /usr/include/elf.h: 3050
try:
    EF_IA_64_ABI64 = 0x00000010
except:
    pass

# /usr/include/elf.h: 3051
try:
    EF_IA_64_ARCH = 0xff000000
except:
    pass

# /usr/include/elf.h: 3054
try:
    PT_IA_64_ARCHEXT = (PT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 3055
try:
    PT_IA_64_UNWIND = (PT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 3056
try:
    PT_IA_64_HP_OPT_ANOT = (PT_LOOS + 0x12)
except:
    pass

# /usr/include/elf.h: 3057
try:
    PT_IA_64_HP_HSL_ANOT = (PT_LOOS + 0x13)
except:
    pass

# /usr/include/elf.h: 3058
try:
    PT_IA_64_HP_STACK = (PT_LOOS + 0x14)
except:
    pass

# /usr/include/elf.h: 3061
try:
    PF_IA_64_NORECOV = 0x80000000
except:
    pass

# /usr/include/elf.h: 3064
try:
    SHT_IA_64_EXT = (SHT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 3065
try:
    SHT_IA_64_UNWIND = (SHT_LOPROC + 1)
except:
    pass

# /usr/include/elf.h: 3068
try:
    SHF_IA_64_SHORT = 0x10000000
except:
    pass

# /usr/include/elf.h: 3069
try:
    SHF_IA_64_NORECOV = 0x20000000
except:
    pass

# /usr/include/elf.h: 3072
try:
    DT_IA_64_PLT_RESERVE = (DT_LOPROC + 0)
except:
    pass

# /usr/include/elf.h: 3073
try:
    DT_IA_64_NUM = 1
except:
    pass

# /usr/include/elf.h: 3076
try:
    R_IA64_NONE = 0x00
except:
    pass

# /usr/include/elf.h: 3077
try:
    R_IA64_IMM14 = 0x21
except:
    pass

# /usr/include/elf.h: 3078
try:
    R_IA64_IMM22 = 0x22
except:
    pass

# /usr/include/elf.h: 3079
try:
    R_IA64_IMM64 = 0x23
except:
    pass

# /usr/include/elf.h: 3080
try:
    R_IA64_DIR32MSB = 0x24
except:
    pass

# /usr/include/elf.h: 3081
try:
    R_IA64_DIR32LSB = 0x25
except:
    pass

# /usr/include/elf.h: 3082
try:
    R_IA64_DIR64MSB = 0x26
except:
    pass

# /usr/include/elf.h: 3083
try:
    R_IA64_DIR64LSB = 0x27
except:
    pass

# /usr/include/elf.h: 3084
try:
    R_IA64_GPREL22 = 0x2a
except:
    pass

# /usr/include/elf.h: 3085
try:
    R_IA64_GPREL64I = 0x2b
except:
    pass

# /usr/include/elf.h: 3086
try:
    R_IA64_GPREL32MSB = 0x2c
except:
    pass

# /usr/include/elf.h: 3087
try:
    R_IA64_GPREL32LSB = 0x2d
except:
    pass

# /usr/include/elf.h: 3088
try:
    R_IA64_GPREL64MSB = 0x2e
except:
    pass

# /usr/include/elf.h: 3089
try:
    R_IA64_GPREL64LSB = 0x2f
except:
    pass

# /usr/include/elf.h: 3090
try:
    R_IA64_LTOFF22 = 0x32
except:
    pass

# /usr/include/elf.h: 3091
try:
    R_IA64_LTOFF64I = 0x33
except:
    pass

# /usr/include/elf.h: 3092
try:
    R_IA64_PLTOFF22 = 0x3a
except:
    pass

# /usr/include/elf.h: 3093
try:
    R_IA64_PLTOFF64I = 0x3b
except:
    pass

# /usr/include/elf.h: 3094
try:
    R_IA64_PLTOFF64MSB = 0x3e
except:
    pass

# /usr/include/elf.h: 3095
try:
    R_IA64_PLTOFF64LSB = 0x3f
except:
    pass

# /usr/include/elf.h: 3096
try:
    R_IA64_FPTR64I = 0x43
except:
    pass

# /usr/include/elf.h: 3097
try:
    R_IA64_FPTR32MSB = 0x44
except:
    pass

# /usr/include/elf.h: 3098
try:
    R_IA64_FPTR32LSB = 0x45
except:
    pass

# /usr/include/elf.h: 3099
try:
    R_IA64_FPTR64MSB = 0x46
except:
    pass

# /usr/include/elf.h: 3100
try:
    R_IA64_FPTR64LSB = 0x47
except:
    pass

# /usr/include/elf.h: 3101
try:
    R_IA64_PCREL60B = 0x48
except:
    pass

# /usr/include/elf.h: 3102
try:
    R_IA64_PCREL21B = 0x49
except:
    pass

# /usr/include/elf.h: 3103
try:
    R_IA64_PCREL21M = 0x4a
except:
    pass

# /usr/include/elf.h: 3104
try:
    R_IA64_PCREL21F = 0x4b
except:
    pass

# /usr/include/elf.h: 3105
try:
    R_IA64_PCREL32MSB = 0x4c
except:
    pass

# /usr/include/elf.h: 3106
try:
    R_IA64_PCREL32LSB = 0x4d
except:
    pass

# /usr/include/elf.h: 3107
try:
    R_IA64_PCREL64MSB = 0x4e
except:
    pass

# /usr/include/elf.h: 3108
try:
    R_IA64_PCREL64LSB = 0x4f
except:
    pass

# /usr/include/elf.h: 3109
try:
    R_IA64_LTOFF_FPTR22 = 0x52
except:
    pass

# /usr/include/elf.h: 3110
try:
    R_IA64_LTOFF_FPTR64I = 0x53
except:
    pass

# /usr/include/elf.h: 3111
try:
    R_IA64_LTOFF_FPTR32MSB = 0x54
except:
    pass

# /usr/include/elf.h: 3112
try:
    R_IA64_LTOFF_FPTR32LSB = 0x55
except:
    pass

# /usr/include/elf.h: 3113
try:
    R_IA64_LTOFF_FPTR64MSB = 0x56
except:
    pass

# /usr/include/elf.h: 3114
try:
    R_IA64_LTOFF_FPTR64LSB = 0x57
except:
    pass

# /usr/include/elf.h: 3115
try:
    R_IA64_SEGREL32MSB = 0x5c
except:
    pass

# /usr/include/elf.h: 3116
try:
    R_IA64_SEGREL32LSB = 0x5d
except:
    pass

# /usr/include/elf.h: 3117
try:
    R_IA64_SEGREL64MSB = 0x5e
except:
    pass

# /usr/include/elf.h: 3118
try:
    R_IA64_SEGREL64LSB = 0x5f
except:
    pass

# /usr/include/elf.h: 3119
try:
    R_IA64_SECREL32MSB = 0x64
except:
    pass

# /usr/include/elf.h: 3120
try:
    R_IA64_SECREL32LSB = 0x65
except:
    pass

# /usr/include/elf.h: 3121
try:
    R_IA64_SECREL64MSB = 0x66
except:
    pass

# /usr/include/elf.h: 3122
try:
    R_IA64_SECREL64LSB = 0x67
except:
    pass

# /usr/include/elf.h: 3123
try:
    R_IA64_REL32MSB = 0x6c
except:
    pass

# /usr/include/elf.h: 3124
try:
    R_IA64_REL32LSB = 0x6d
except:
    pass

# /usr/include/elf.h: 3125
try:
    R_IA64_REL64MSB = 0x6e
except:
    pass

# /usr/include/elf.h: 3126
try:
    R_IA64_REL64LSB = 0x6f
except:
    pass

# /usr/include/elf.h: 3127
try:
    R_IA64_LTV32MSB = 0x74
except:
    pass

# /usr/include/elf.h: 3128
try:
    R_IA64_LTV32LSB = 0x75
except:
    pass

# /usr/include/elf.h: 3129
try:
    R_IA64_LTV64MSB = 0x76
except:
    pass

# /usr/include/elf.h: 3130
try:
    R_IA64_LTV64LSB = 0x77
except:
    pass

# /usr/include/elf.h: 3131
try:
    R_IA64_PCREL21BI = 0x79
except:
    pass

# /usr/include/elf.h: 3132
try:
    R_IA64_PCREL22 = 0x7a
except:
    pass

# /usr/include/elf.h: 3133
try:
    R_IA64_PCREL64I = 0x7b
except:
    pass

# /usr/include/elf.h: 3134
try:
    R_IA64_IPLTMSB = 0x80
except:
    pass

# /usr/include/elf.h: 3135
try:
    R_IA64_IPLTLSB = 0x81
except:
    pass

# /usr/include/elf.h: 3136
try:
    R_IA64_COPY = 0x84
except:
    pass

# /usr/include/elf.h: 3137
try:
    R_IA64_SUB = 0x85
except:
    pass

# /usr/include/elf.h: 3138
try:
    R_IA64_LTOFF22X = 0x86
except:
    pass

# /usr/include/elf.h: 3139
try:
    R_IA64_LDXMOV = 0x87
except:
    pass

# /usr/include/elf.h: 3140
try:
    R_IA64_TPREL14 = 0x91
except:
    pass

# /usr/include/elf.h: 3141
try:
    R_IA64_TPREL22 = 0x92
except:
    pass

# /usr/include/elf.h: 3142
try:
    R_IA64_TPREL64I = 0x93
except:
    pass

# /usr/include/elf.h: 3143
try:
    R_IA64_TPREL64MSB = 0x96
except:
    pass

# /usr/include/elf.h: 3144
try:
    R_IA64_TPREL64LSB = 0x97
except:
    pass

# /usr/include/elf.h: 3145
try:
    R_IA64_LTOFF_TPREL22 = 0x9a
except:
    pass

# /usr/include/elf.h: 3146
try:
    R_IA64_DTPMOD64MSB = 0xa6
except:
    pass

# /usr/include/elf.h: 3147
try:
    R_IA64_DTPMOD64LSB = 0xa7
except:
    pass

# /usr/include/elf.h: 3148
try:
    R_IA64_LTOFF_DTPMOD22 = 0xaa
except:
    pass

# /usr/include/elf.h: 3149
try:
    R_IA64_DTPREL14 = 0xb1
except:
    pass

# /usr/include/elf.h: 3150
try:
    R_IA64_DTPREL22 = 0xb2
except:
    pass

# /usr/include/elf.h: 3151
try:
    R_IA64_DTPREL64I = 0xb3
except:
    pass

# /usr/include/elf.h: 3152
try:
    R_IA64_DTPREL32MSB = 0xb4
except:
    pass

# /usr/include/elf.h: 3153
try:
    R_IA64_DTPREL32LSB = 0xb5
except:
    pass

# /usr/include/elf.h: 3154
try:
    R_IA64_DTPREL64MSB = 0xb6
except:
    pass

# /usr/include/elf.h: 3155
try:
    R_IA64_DTPREL64LSB = 0xb7
except:
    pass

# /usr/include/elf.h: 3156
try:
    R_IA64_LTOFF_DTPREL22 = 0xba
except:
    pass

# /usr/include/elf.h: 3161
try:
    EF_SH_MACH_MASK = 0x1f
except:
    pass

# /usr/include/elf.h: 3162
try:
    EF_SH_UNKNOWN = 0x0
except:
    pass

# /usr/include/elf.h: 3163
try:
    EF_SH1 = 0x1
except:
    pass

# /usr/include/elf.h: 3164
try:
    EF_SH2 = 0x2
except:
    pass

# /usr/include/elf.h: 3165
try:
    EF_SH3 = 0x3
except:
    pass

# /usr/include/elf.h: 3166
try:
    EF_SH_DSP = 0x4
except:
    pass

# /usr/include/elf.h: 3167
try:
    EF_SH3_DSP = 0x5
except:
    pass

# /usr/include/elf.h: 3168
try:
    EF_SH4AL_DSP = 0x6
except:
    pass

# /usr/include/elf.h: 3169
try:
    EF_SH3E = 0x8
except:
    pass

# /usr/include/elf.h: 3170
try:
    EF_SH4 = 0x9
except:
    pass

# /usr/include/elf.h: 3171
try:
    EF_SH2E = 0xb
except:
    pass

# /usr/include/elf.h: 3172
try:
    EF_SH4A = 0xc
except:
    pass

# /usr/include/elf.h: 3173
try:
    EF_SH2A = 0xd
except:
    pass

# /usr/include/elf.h: 3174
try:
    EF_SH4_NOFPU = 0x10
except:
    pass

# /usr/include/elf.h: 3175
try:
    EF_SH4A_NOFPU = 0x11
except:
    pass

# /usr/include/elf.h: 3176
try:
    EF_SH4_NOMMU_NOFPU = 0x12
except:
    pass

# /usr/include/elf.h: 3177
try:
    EF_SH2A_NOFPU = 0x13
except:
    pass

# /usr/include/elf.h: 3178
try:
    EF_SH3_NOMMU = 0x14
except:
    pass

# /usr/include/elf.h: 3179
try:
    EF_SH2A_SH4_NOFPU = 0x15
except:
    pass

# /usr/include/elf.h: 3180
try:
    EF_SH2A_SH3_NOFPU = 0x16
except:
    pass

# /usr/include/elf.h: 3181
try:
    EF_SH2A_SH4 = 0x17
except:
    pass

# /usr/include/elf.h: 3182
try:
    EF_SH2A_SH3E = 0x18
except:
    pass

# /usr/include/elf.h: 3185
try:
    R_SH_NONE = 0
except:
    pass

# /usr/include/elf.h: 3186
try:
    R_SH_DIR32 = 1
except:
    pass

# /usr/include/elf.h: 3187
try:
    R_SH_REL32 = 2
except:
    pass

# /usr/include/elf.h: 3188
try:
    R_SH_DIR8WPN = 3
except:
    pass

# /usr/include/elf.h: 3189
try:
    R_SH_IND12W = 4
except:
    pass

# /usr/include/elf.h: 3190
try:
    R_SH_DIR8WPL = 5
except:
    pass

# /usr/include/elf.h: 3191
try:
    R_SH_DIR8WPZ = 6
except:
    pass

# /usr/include/elf.h: 3192
try:
    R_SH_DIR8BP = 7
except:
    pass

# /usr/include/elf.h: 3193
try:
    R_SH_DIR8W = 8
except:
    pass

# /usr/include/elf.h: 3194
try:
    R_SH_DIR8L = 9
except:
    pass

# /usr/include/elf.h: 3195
try:
    R_SH_SWITCH16 = 25
except:
    pass

# /usr/include/elf.h: 3196
try:
    R_SH_SWITCH32 = 26
except:
    pass

# /usr/include/elf.h: 3197
try:
    R_SH_USES = 27
except:
    pass

# /usr/include/elf.h: 3198
try:
    R_SH_COUNT = 28
except:
    pass

# /usr/include/elf.h: 3199
try:
    R_SH_ALIGN = 29
except:
    pass

# /usr/include/elf.h: 3200
try:
    R_SH_CODE = 30
except:
    pass

# /usr/include/elf.h: 3201
try:
    R_SH_DATA = 31
except:
    pass

# /usr/include/elf.h: 3202
try:
    R_SH_LABEL = 32
except:
    pass

# /usr/include/elf.h: 3203
try:
    R_SH_SWITCH8 = 33
except:
    pass

# /usr/include/elf.h: 3204
try:
    R_SH_GNU_VTINHERIT = 34
except:
    pass

# /usr/include/elf.h: 3205
try:
    R_SH_GNU_VTENTRY = 35
except:
    pass

# /usr/include/elf.h: 3206
try:
    R_SH_TLS_GD_32 = 144
except:
    pass

# /usr/include/elf.h: 3207
try:
    R_SH_TLS_LD_32 = 145
except:
    pass

# /usr/include/elf.h: 3208
try:
    R_SH_TLS_LDO_32 = 146
except:
    pass

# /usr/include/elf.h: 3209
try:
    R_SH_TLS_IE_32 = 147
except:
    pass

# /usr/include/elf.h: 3210
try:
    R_SH_TLS_LE_32 = 148
except:
    pass

# /usr/include/elf.h: 3211
try:
    R_SH_TLS_DTPMOD32 = 149
except:
    pass

# /usr/include/elf.h: 3212
try:
    R_SH_TLS_DTPOFF32 = 150
except:
    pass

# /usr/include/elf.h: 3213
try:
    R_SH_TLS_TPOFF32 = 151
except:
    pass

# /usr/include/elf.h: 3214
try:
    R_SH_GOT32 = 160
except:
    pass

# /usr/include/elf.h: 3215
try:
    R_SH_PLT32 = 161
except:
    pass

# /usr/include/elf.h: 3216
try:
    R_SH_COPY = 162
except:
    pass

# /usr/include/elf.h: 3217
try:
    R_SH_GLOB_DAT = 163
except:
    pass

# /usr/include/elf.h: 3218
try:
    R_SH_JMP_SLOT = 164
except:
    pass

# /usr/include/elf.h: 3219
try:
    R_SH_RELATIVE = 165
except:
    pass

# /usr/include/elf.h: 3220
try:
    R_SH_GOTOFF = 166
except:
    pass

# /usr/include/elf.h: 3221
try:
    R_SH_GOTPC = 167
except:
    pass

# /usr/include/elf.h: 3223
try:
    R_SH_NUM = 256
except:
    pass

# /usr/include/elf.h: 3229
try:
    EF_S390_HIGH_GPRS = 0x00000001
except:
    pass

# /usr/include/elf.h: 3233
try:
    R_390_NONE = 0
except:
    pass

# /usr/include/elf.h: 3234
try:
    R_390_8 = 1
except:
    pass

# /usr/include/elf.h: 3235
try:
    R_390_12 = 2
except:
    pass

# /usr/include/elf.h: 3236
try:
    R_390_16 = 3
except:
    pass

# /usr/include/elf.h: 3237
try:
    R_390_32 = 4
except:
    pass

# /usr/include/elf.h: 3238
try:
    R_390_PC32 = 5
except:
    pass

# /usr/include/elf.h: 3239
try:
    R_390_GOT12 = 6
except:
    pass

# /usr/include/elf.h: 3240
try:
    R_390_GOT32 = 7
except:
    pass

# /usr/include/elf.h: 3241
try:
    R_390_PLT32 = 8
except:
    pass

# /usr/include/elf.h: 3242
try:
    R_390_COPY = 9
except:
    pass

# /usr/include/elf.h: 3243
try:
    R_390_GLOB_DAT = 10
except:
    pass

# /usr/include/elf.h: 3244
try:
    R_390_JMP_SLOT = 11
except:
    pass

# /usr/include/elf.h: 3245
try:
    R_390_RELATIVE = 12
except:
    pass

# /usr/include/elf.h: 3246
try:
    R_390_GOTOFF32 = 13
except:
    pass

# /usr/include/elf.h: 3247
try:
    R_390_GOTPC = 14
except:
    pass

# /usr/include/elf.h: 3248
try:
    R_390_GOT16 = 15
except:
    pass

# /usr/include/elf.h: 3249
try:
    R_390_PC16 = 16
except:
    pass

# /usr/include/elf.h: 3250
try:
    R_390_PC16DBL = 17
except:
    pass

# /usr/include/elf.h: 3251
try:
    R_390_PLT16DBL = 18
except:
    pass

# /usr/include/elf.h: 3252
try:
    R_390_PC32DBL = 19
except:
    pass

# /usr/include/elf.h: 3253
try:
    R_390_PLT32DBL = 20
except:
    pass

# /usr/include/elf.h: 3254
try:
    R_390_GOTPCDBL = 21
except:
    pass

# /usr/include/elf.h: 3255
try:
    R_390_64 = 22
except:
    pass

# /usr/include/elf.h: 3256
try:
    R_390_PC64 = 23
except:
    pass

# /usr/include/elf.h: 3257
try:
    R_390_GOT64 = 24
except:
    pass

# /usr/include/elf.h: 3258
try:
    R_390_PLT64 = 25
except:
    pass

# /usr/include/elf.h: 3259
try:
    R_390_GOTENT = 26
except:
    pass

# /usr/include/elf.h: 3260
try:
    R_390_GOTOFF16 = 27
except:
    pass

# /usr/include/elf.h: 3261
try:
    R_390_GOTOFF64 = 28
except:
    pass

# /usr/include/elf.h: 3262
try:
    R_390_GOTPLT12 = 29
except:
    pass

# /usr/include/elf.h: 3263
try:
    R_390_GOTPLT16 = 30
except:
    pass

# /usr/include/elf.h: 3264
try:
    R_390_GOTPLT32 = 31
except:
    pass

# /usr/include/elf.h: 3265
try:
    R_390_GOTPLT64 = 32
except:
    pass

# /usr/include/elf.h: 3266
try:
    R_390_GOTPLTENT = 33
except:
    pass

# /usr/include/elf.h: 3267
try:
    R_390_PLTOFF16 = 34
except:
    pass

# /usr/include/elf.h: 3268
try:
    R_390_PLTOFF32 = 35
except:
    pass

# /usr/include/elf.h: 3269
try:
    R_390_PLTOFF64 = 36
except:
    pass

# /usr/include/elf.h: 3270
try:
    R_390_TLS_LOAD = 37
except:
    pass

# /usr/include/elf.h: 3271
try:
    R_390_TLS_GDCALL = 38
except:
    pass

# /usr/include/elf.h: 3273
try:
    R_390_TLS_LDCALL = 39
except:
    pass

# /usr/include/elf.h: 3275
try:
    R_390_TLS_GD32 = 40
except:
    pass

# /usr/include/elf.h: 3277
try:
    R_390_TLS_GD64 = 41
except:
    pass

# /usr/include/elf.h: 3279
try:
    R_390_TLS_GOTIE12 = 42
except:
    pass

# /usr/include/elf.h: 3281
try:
    R_390_TLS_GOTIE32 = 43
except:
    pass

# /usr/include/elf.h: 3283
try:
    R_390_TLS_GOTIE64 = 44
except:
    pass

# /usr/include/elf.h: 3285
try:
    R_390_TLS_LDM32 = 45
except:
    pass

# /usr/include/elf.h: 3287
try:
    R_390_TLS_LDM64 = 46
except:
    pass

# /usr/include/elf.h: 3289
try:
    R_390_TLS_IE32 = 47
except:
    pass

# /usr/include/elf.h: 3291
try:
    R_390_TLS_IE64 = 48
except:
    pass

# /usr/include/elf.h: 3293
try:
    R_390_TLS_IEENT = 49
except:
    pass

# /usr/include/elf.h: 3295
try:
    R_390_TLS_LE32 = 50
except:
    pass

# /usr/include/elf.h: 3297
try:
    R_390_TLS_LE64 = 51
except:
    pass

# /usr/include/elf.h: 3299
try:
    R_390_TLS_LDO32 = 52
except:
    pass

# /usr/include/elf.h: 3301
try:
    R_390_TLS_LDO64 = 53
except:
    pass

# /usr/include/elf.h: 3303
try:
    R_390_TLS_DTPMOD = 54
except:
    pass

# /usr/include/elf.h: 3304
try:
    R_390_TLS_DTPOFF = 55
except:
    pass

# /usr/include/elf.h: 3305
try:
    R_390_TLS_TPOFF = 56
except:
    pass

# /usr/include/elf.h: 3307
try:
    R_390_20 = 57
except:
    pass

# /usr/include/elf.h: 3308
try:
    R_390_GOT20 = 58
except:
    pass

# /usr/include/elf.h: 3309
try:
    R_390_GOTPLT20 = 59
except:
    pass

# /usr/include/elf.h: 3310
try:
    R_390_TLS_GOTIE20 = 60
except:
    pass

# /usr/include/elf.h: 3312
try:
    R_390_IRELATIVE = 61
except:
    pass

# /usr/include/elf.h: 3314
try:
    R_390_NUM = 62
except:
    pass

# /usr/include/elf.h: 3318
try:
    R_CRIS_NONE = 0
except:
    pass

# /usr/include/elf.h: 3319
try:
    R_CRIS_8 = 1
except:
    pass

# /usr/include/elf.h: 3320
try:
    R_CRIS_16 = 2
except:
    pass

# /usr/include/elf.h: 3321
try:
    R_CRIS_32 = 3
except:
    pass

# /usr/include/elf.h: 3322
try:
    R_CRIS_8_PCREL = 4
except:
    pass

# /usr/include/elf.h: 3323
try:
    R_CRIS_16_PCREL = 5
except:
    pass

# /usr/include/elf.h: 3324
try:
    R_CRIS_32_PCREL = 6
except:
    pass

# /usr/include/elf.h: 3325
try:
    R_CRIS_GNU_VTINHERIT = 7
except:
    pass

# /usr/include/elf.h: 3326
try:
    R_CRIS_GNU_VTENTRY = 8
except:
    pass

# /usr/include/elf.h: 3327
try:
    R_CRIS_COPY = 9
except:
    pass

# /usr/include/elf.h: 3328
try:
    R_CRIS_GLOB_DAT = 10
except:
    pass

# /usr/include/elf.h: 3329
try:
    R_CRIS_JUMP_SLOT = 11
except:
    pass

# /usr/include/elf.h: 3330
try:
    R_CRIS_RELATIVE = 12
except:
    pass

# /usr/include/elf.h: 3331
try:
    R_CRIS_16_GOT = 13
except:
    pass

# /usr/include/elf.h: 3332
try:
    R_CRIS_32_GOT = 14
except:
    pass

# /usr/include/elf.h: 3333
try:
    R_CRIS_16_GOTPLT = 15
except:
    pass

# /usr/include/elf.h: 3334
try:
    R_CRIS_32_GOTPLT = 16
except:
    pass

# /usr/include/elf.h: 3335
try:
    R_CRIS_32_GOTREL = 17
except:
    pass

# /usr/include/elf.h: 3336
try:
    R_CRIS_32_PLT_GOTREL = 18
except:
    pass

# /usr/include/elf.h: 3337
try:
    R_CRIS_32_PLT_PCREL = 19
except:
    pass

# /usr/include/elf.h: 3339
try:
    R_CRIS_NUM = 20
except:
    pass

# /usr/include/elf.h: 3343
try:
    R_X86_64_NONE = 0
except:
    pass

# /usr/include/elf.h: 3344
try:
    R_X86_64_64 = 1
except:
    pass

# /usr/include/elf.h: 3345
try:
    R_X86_64_PC32 = 2
except:
    pass

# /usr/include/elf.h: 3346
try:
    R_X86_64_GOT32 = 3
except:
    pass

# /usr/include/elf.h: 3347
try:
    R_X86_64_PLT32 = 4
except:
    pass

# /usr/include/elf.h: 3348
try:
    R_X86_64_COPY = 5
except:
    pass

# /usr/include/elf.h: 3349
try:
    R_X86_64_GLOB_DAT = 6
except:
    pass

# /usr/include/elf.h: 3350
try:
    R_X86_64_JUMP_SLOT = 7
except:
    pass

# /usr/include/elf.h: 3351
try:
    R_X86_64_RELATIVE = 8
except:
    pass

# /usr/include/elf.h: 3352
try:
    R_X86_64_GOTPCREL = 9
except:
    pass

# /usr/include/elf.h: 3354
try:
    R_X86_64_32 = 10
except:
    pass

# /usr/include/elf.h: 3355
try:
    R_X86_64_32S = 11
except:
    pass

# /usr/include/elf.h: 3356
try:
    R_X86_64_16 = 12
except:
    pass

# /usr/include/elf.h: 3357
try:
    R_X86_64_PC16 = 13
except:
    pass

# /usr/include/elf.h: 3358
try:
    R_X86_64_8 = 14
except:
    pass

# /usr/include/elf.h: 3359
try:
    R_X86_64_PC8 = 15
except:
    pass

# /usr/include/elf.h: 3360
try:
    R_X86_64_DTPMOD64 = 16
except:
    pass

# /usr/include/elf.h: 3361
try:
    R_X86_64_DTPOFF64 = 17
except:
    pass

# /usr/include/elf.h: 3362
try:
    R_X86_64_TPOFF64 = 18
except:
    pass

# /usr/include/elf.h: 3363
try:
    R_X86_64_TLSGD = 19
except:
    pass

# /usr/include/elf.h: 3365
try:
    R_X86_64_TLSLD = 20
except:
    pass

# /usr/include/elf.h: 3367
try:
    R_X86_64_DTPOFF32 = 21
except:
    pass

# /usr/include/elf.h: 3368
try:
    R_X86_64_GOTTPOFF = 22
except:
    pass

# /usr/include/elf.h: 3370
try:
    R_X86_64_TPOFF32 = 23
except:
    pass

# /usr/include/elf.h: 3371
try:
    R_X86_64_PC64 = 24
except:
    pass

# /usr/include/elf.h: 3372
try:
    R_X86_64_GOTOFF64 = 25
except:
    pass

# /usr/include/elf.h: 3373
try:
    R_X86_64_GOTPC32 = 26
except:
    pass

# /usr/include/elf.h: 3375
try:
    R_X86_64_GOT64 = 27
except:
    pass

# /usr/include/elf.h: 3376
try:
    R_X86_64_GOTPCREL64 = 28
except:
    pass

# /usr/include/elf.h: 3378
try:
    R_X86_64_GOTPC64 = 29
except:
    pass

# /usr/include/elf.h: 3379
try:
    R_X86_64_GOTPLT64 = 30
except:
    pass

# /usr/include/elf.h: 3380
try:
    R_X86_64_PLTOFF64 = 31
except:
    pass

# /usr/include/elf.h: 3382
try:
    R_X86_64_SIZE32 = 32
except:
    pass

# /usr/include/elf.h: 3383
try:
    R_X86_64_SIZE64 = 33
except:
    pass

# /usr/include/elf.h: 3384
try:
    R_X86_64_GOTPC32_TLSDESC = 34
except:
    pass

# /usr/include/elf.h: 3385
try:
    R_X86_64_TLSDESC_CALL = 35
except:
    pass

# /usr/include/elf.h: 3387
try:
    R_X86_64_TLSDESC = 36
except:
    pass

# /usr/include/elf.h: 3388
try:
    R_X86_64_IRELATIVE = 37
except:
    pass

# /usr/include/elf.h: 3389
try:
    R_X86_64_RELATIVE64 = 38
except:
    pass

# /usr/include/elf.h: 3392
try:
    R_X86_64_GOTPCRELX = 41
except:
    pass

# /usr/include/elf.h: 3395
try:
    R_X86_64_REX_GOTPCRELX = 42
except:
    pass

# /usr/include/elf.h: 3398
try:
    R_X86_64_NUM = 43
except:
    pass

# /usr/include/elf.h: 3401
try:
    SHT_X86_64_UNWIND = 0x70000001
except:
    pass

# /usr/include/elf.h: 3405
try:
    R_MN10300_NONE = 0
except:
    pass

# /usr/include/elf.h: 3406
try:
    R_MN10300_32 = 1
except:
    pass

# /usr/include/elf.h: 3407
try:
    R_MN10300_16 = 2
except:
    pass

# /usr/include/elf.h: 3408
try:
    R_MN10300_8 = 3
except:
    pass

# /usr/include/elf.h: 3409
try:
    R_MN10300_PCREL32 = 4
except:
    pass

# /usr/include/elf.h: 3410
try:
    R_MN10300_PCREL16 = 5
except:
    pass

# /usr/include/elf.h: 3411
try:
    R_MN10300_PCREL8 = 6
except:
    pass

# /usr/include/elf.h: 3412
try:
    R_MN10300_GNU_VTINHERIT = 7
except:
    pass

# /usr/include/elf.h: 3413
try:
    R_MN10300_GNU_VTENTRY = 8
except:
    pass

# /usr/include/elf.h: 3414
try:
    R_MN10300_24 = 9
except:
    pass

# /usr/include/elf.h: 3415
try:
    R_MN10300_GOTPC32 = 10
except:
    pass

# /usr/include/elf.h: 3416
try:
    R_MN10300_GOTPC16 = 11
except:
    pass

# /usr/include/elf.h: 3417
try:
    R_MN10300_GOTOFF32 = 12
except:
    pass

# /usr/include/elf.h: 3418
try:
    R_MN10300_GOTOFF24 = 13
except:
    pass

# /usr/include/elf.h: 3419
try:
    R_MN10300_GOTOFF16 = 14
except:
    pass

# /usr/include/elf.h: 3420
try:
    R_MN10300_PLT32 = 15
except:
    pass

# /usr/include/elf.h: 3421
try:
    R_MN10300_PLT16 = 16
except:
    pass

# /usr/include/elf.h: 3422
try:
    R_MN10300_GOT32 = 17
except:
    pass

# /usr/include/elf.h: 3423
try:
    R_MN10300_GOT24 = 18
except:
    pass

# /usr/include/elf.h: 3424
try:
    R_MN10300_GOT16 = 19
except:
    pass

# /usr/include/elf.h: 3425
try:
    R_MN10300_COPY = 20
except:
    pass

# /usr/include/elf.h: 3426
try:
    R_MN10300_GLOB_DAT = 21
except:
    pass

# /usr/include/elf.h: 3427
try:
    R_MN10300_JMP_SLOT = 22
except:
    pass

# /usr/include/elf.h: 3428
try:
    R_MN10300_RELATIVE = 23
except:
    pass

# /usr/include/elf.h: 3429
try:
    R_MN10300_TLS_GD = 24
except:
    pass

# /usr/include/elf.h: 3430
try:
    R_MN10300_TLS_LD = 25
except:
    pass

# /usr/include/elf.h: 3431
try:
    R_MN10300_TLS_LDO = 26
except:
    pass

# /usr/include/elf.h: 3432
try:
    R_MN10300_TLS_GOTIE = 27
except:
    pass

# /usr/include/elf.h: 3434
try:
    R_MN10300_TLS_IE = 28
except:
    pass

# /usr/include/elf.h: 3436
try:
    R_MN10300_TLS_LE = 29
except:
    pass

# /usr/include/elf.h: 3438
try:
    R_MN10300_TLS_DTPMOD = 30
except:
    pass

# /usr/include/elf.h: 3439
try:
    R_MN10300_TLS_DTPOFF = 31
except:
    pass

# /usr/include/elf.h: 3440
try:
    R_MN10300_TLS_TPOFF = 32
except:
    pass

# /usr/include/elf.h: 3441
try:
    R_MN10300_SYM_DIFF = 33
except:
    pass

# /usr/include/elf.h: 3443
try:
    R_MN10300_ALIGN = 34
except:
    pass

# /usr/include/elf.h: 3445
try:
    R_MN10300_NUM = 35
except:
    pass

# /usr/include/elf.h: 3449
try:
    R_M32R_NONE = 0
except:
    pass

# /usr/include/elf.h: 3450
try:
    R_M32R_16 = 1
except:
    pass

# /usr/include/elf.h: 3451
try:
    R_M32R_32 = 2
except:
    pass

# /usr/include/elf.h: 3452
try:
    R_M32R_24 = 3
except:
    pass

# /usr/include/elf.h: 3453
try:
    R_M32R_10_PCREL = 4
except:
    pass

# /usr/include/elf.h: 3454
try:
    R_M32R_18_PCREL = 5
except:
    pass

# /usr/include/elf.h: 3455
try:
    R_M32R_26_PCREL = 6
except:
    pass

# /usr/include/elf.h: 3456
try:
    R_M32R_HI16_ULO = 7
except:
    pass

# /usr/include/elf.h: 3457
try:
    R_M32R_HI16_SLO = 8
except:
    pass

# /usr/include/elf.h: 3458
try:
    R_M32R_LO16 = 9
except:
    pass

# /usr/include/elf.h: 3459
try:
    R_M32R_SDA16 = 10
except:
    pass

# /usr/include/elf.h: 3460
try:
    R_M32R_GNU_VTINHERIT = 11
except:
    pass

# /usr/include/elf.h: 3461
try:
    R_M32R_GNU_VTENTRY = 12
except:
    pass

# /usr/include/elf.h: 3463
try:
    R_M32R_16_RELA = 33
except:
    pass

# /usr/include/elf.h: 3464
try:
    R_M32R_32_RELA = 34
except:
    pass

# /usr/include/elf.h: 3465
try:
    R_M32R_24_RELA = 35
except:
    pass

# /usr/include/elf.h: 3466
try:
    R_M32R_10_PCREL_RELA = 36
except:
    pass

# /usr/include/elf.h: 3467
try:
    R_M32R_18_PCREL_RELA = 37
except:
    pass

# /usr/include/elf.h: 3468
try:
    R_M32R_26_PCREL_RELA = 38
except:
    pass

# /usr/include/elf.h: 3469
try:
    R_M32R_HI16_ULO_RELA = 39
except:
    pass

# /usr/include/elf.h: 3470
try:
    R_M32R_HI16_SLO_RELA = 40
except:
    pass

# /usr/include/elf.h: 3471
try:
    R_M32R_LO16_RELA = 41
except:
    pass

# /usr/include/elf.h: 3472
try:
    R_M32R_SDA16_RELA = 42
except:
    pass

# /usr/include/elf.h: 3473
try:
    R_M32R_RELA_GNU_VTINHERIT = 43
except:
    pass

# /usr/include/elf.h: 3474
try:
    R_M32R_RELA_GNU_VTENTRY = 44
except:
    pass

# /usr/include/elf.h: 3475
try:
    R_M32R_REL32 = 45
except:
    pass

# /usr/include/elf.h: 3477
try:
    R_M32R_GOT24 = 48
except:
    pass

# /usr/include/elf.h: 3478
try:
    R_M32R_26_PLTREL = 49
except:
    pass

# /usr/include/elf.h: 3479
try:
    R_M32R_COPY = 50
except:
    pass

# /usr/include/elf.h: 3480
try:
    R_M32R_GLOB_DAT = 51
except:
    pass

# /usr/include/elf.h: 3481
try:
    R_M32R_JMP_SLOT = 52
except:
    pass

# /usr/include/elf.h: 3482
try:
    R_M32R_RELATIVE = 53
except:
    pass

# /usr/include/elf.h: 3483
try:
    R_M32R_GOTOFF = 54
except:
    pass

# /usr/include/elf.h: 3484
try:
    R_M32R_GOTPC24 = 55
except:
    pass

# /usr/include/elf.h: 3485
try:
    R_M32R_GOT16_HI_ULO = 56
except:
    pass

# /usr/include/elf.h: 3487
try:
    R_M32R_GOT16_HI_SLO = 57
except:
    pass

# /usr/include/elf.h: 3489
try:
    R_M32R_GOT16_LO = 58
except:
    pass

# /usr/include/elf.h: 3490
try:
    R_M32R_GOTPC_HI_ULO = 59
except:
    pass

# /usr/include/elf.h: 3492
try:
    R_M32R_GOTPC_HI_SLO = 60
except:
    pass

# /usr/include/elf.h: 3494
try:
    R_M32R_GOTPC_LO = 61
except:
    pass

# /usr/include/elf.h: 3496
try:
    R_M32R_GOTOFF_HI_ULO = 62
except:
    pass

# /usr/include/elf.h: 3498
try:
    R_M32R_GOTOFF_HI_SLO = 63
except:
    pass

# /usr/include/elf.h: 3500
try:
    R_M32R_GOTOFF_LO = 64
except:
    pass

# /usr/include/elf.h: 3501
try:
    R_M32R_NUM = 256
except:
    pass

# /usr/include/elf.h: 3504
try:
    R_MICROBLAZE_NONE = 0
except:
    pass

# /usr/include/elf.h: 3505
try:
    R_MICROBLAZE_32 = 1
except:
    pass

# /usr/include/elf.h: 3506
try:
    R_MICROBLAZE_32_PCREL = 2
except:
    pass

# /usr/include/elf.h: 3507
try:
    R_MICROBLAZE_64_PCREL = 3
except:
    pass

# /usr/include/elf.h: 3508
try:
    R_MICROBLAZE_32_PCREL_LO = 4
except:
    pass

# /usr/include/elf.h: 3509
try:
    R_MICROBLAZE_64 = 5
except:
    pass

# /usr/include/elf.h: 3510
try:
    R_MICROBLAZE_32_LO = 6
except:
    pass

# /usr/include/elf.h: 3511
try:
    R_MICROBLAZE_SRO32 = 7
except:
    pass

# /usr/include/elf.h: 3512
try:
    R_MICROBLAZE_SRW32 = 8
except:
    pass

# /usr/include/elf.h: 3513
try:
    R_MICROBLAZE_64_NONE = 9
except:
    pass

# /usr/include/elf.h: 3514
try:
    R_MICROBLAZE_32_SYM_OP_SYM = 10
except:
    pass

# /usr/include/elf.h: 3515
try:
    R_MICROBLAZE_GNU_VTINHERIT = 11
except:
    pass

# /usr/include/elf.h: 3516
try:
    R_MICROBLAZE_GNU_VTENTRY = 12
except:
    pass

# /usr/include/elf.h: 3517
try:
    R_MICROBLAZE_GOTPC_64 = 13
except:
    pass

# /usr/include/elf.h: 3518
try:
    R_MICROBLAZE_GOT_64 = 14
except:
    pass

# /usr/include/elf.h: 3519
try:
    R_MICROBLAZE_PLT_64 = 15
except:
    pass

# /usr/include/elf.h: 3520
try:
    R_MICROBLAZE_REL = 16
except:
    pass

# /usr/include/elf.h: 3521
try:
    R_MICROBLAZE_JUMP_SLOT = 17
except:
    pass

# /usr/include/elf.h: 3522
try:
    R_MICROBLAZE_GLOB_DAT = 18
except:
    pass

# /usr/include/elf.h: 3523
try:
    R_MICROBLAZE_GOTOFF_64 = 19
except:
    pass

# /usr/include/elf.h: 3524
try:
    R_MICROBLAZE_GOTOFF_32 = 20
except:
    pass

# /usr/include/elf.h: 3525
try:
    R_MICROBLAZE_COPY = 21
except:
    pass

# /usr/include/elf.h: 3526
try:
    R_MICROBLAZE_TLS = 22
except:
    pass

# /usr/include/elf.h: 3527
try:
    R_MICROBLAZE_TLSGD = 23
except:
    pass

# /usr/include/elf.h: 3528
try:
    R_MICROBLAZE_TLSLD = 24
except:
    pass

# /usr/include/elf.h: 3529
try:
    R_MICROBLAZE_TLSDTPMOD32 = 25
except:
    pass

# /usr/include/elf.h: 3530
try:
    R_MICROBLAZE_TLSDTPREL32 = 26
except:
    pass

# /usr/include/elf.h: 3531
try:
    R_MICROBLAZE_TLSDTPREL64 = 27
except:
    pass

# /usr/include/elf.h: 3532
try:
    R_MICROBLAZE_TLSGOTTPREL32 = 28
except:
    pass

# /usr/include/elf.h: 3533
try:
    R_MICROBLAZE_TLSTPREL32 = 29
except:
    pass

# /usr/include/elf.h: 3536
try:
    DT_NIOS2_GP = 0x70000002
except:
    pass

# /usr/include/elf.h: 3539
try:
    R_NIOS2_NONE = 0
except:
    pass

# /usr/include/elf.h: 3540
try:
    R_NIOS2_S16 = 1
except:
    pass

# /usr/include/elf.h: 3541
try:
    R_NIOS2_U16 = 2
except:
    pass

# /usr/include/elf.h: 3542
try:
    R_NIOS2_PCREL16 = 3
except:
    pass

# /usr/include/elf.h: 3543
try:
    R_NIOS2_CALL26 = 4
except:
    pass

# /usr/include/elf.h: 3544
try:
    R_NIOS2_IMM5 = 5
except:
    pass

# /usr/include/elf.h: 3545
try:
    R_NIOS2_CACHE_OPX = 6
except:
    pass

# /usr/include/elf.h: 3546
try:
    R_NIOS2_IMM6 = 7
except:
    pass

# /usr/include/elf.h: 3547
try:
    R_NIOS2_IMM8 = 8
except:
    pass

# /usr/include/elf.h: 3548
try:
    R_NIOS2_HI16 = 9
except:
    pass

# /usr/include/elf.h: 3549
try:
    R_NIOS2_LO16 = 10
except:
    pass

# /usr/include/elf.h: 3550
try:
    R_NIOS2_HIADJ16 = 11
except:
    pass

# /usr/include/elf.h: 3551
try:
    R_NIOS2_BFD_RELOC_32 = 12
except:
    pass

# /usr/include/elf.h: 3552
try:
    R_NIOS2_BFD_RELOC_16 = 13
except:
    pass

# /usr/include/elf.h: 3553
try:
    R_NIOS2_BFD_RELOC_8 = 14
except:
    pass

# /usr/include/elf.h: 3554
try:
    R_NIOS2_GPREL = 15
except:
    pass

# /usr/include/elf.h: 3555
try:
    R_NIOS2_GNU_VTINHERIT = 16
except:
    pass

# /usr/include/elf.h: 3556
try:
    R_NIOS2_GNU_VTENTRY = 17
except:
    pass

# /usr/include/elf.h: 3557
try:
    R_NIOS2_UJMP = 18
except:
    pass

# /usr/include/elf.h: 3558
try:
    R_NIOS2_CJMP = 19
except:
    pass

# /usr/include/elf.h: 3559
try:
    R_NIOS2_CALLR = 20
except:
    pass

# /usr/include/elf.h: 3560
try:
    R_NIOS2_ALIGN = 21
except:
    pass

# /usr/include/elf.h: 3562
try:
    R_NIOS2_GOT16 = 22
except:
    pass

# /usr/include/elf.h: 3563
try:
    R_NIOS2_CALL16 = 23
except:
    pass

# /usr/include/elf.h: 3564
try:
    R_NIOS2_GOTOFF_LO = 24
except:
    pass

# /usr/include/elf.h: 3565
try:
    R_NIOS2_GOTOFF_HA = 25
except:
    pass

# /usr/include/elf.h: 3566
try:
    R_NIOS2_PCREL_LO = 26
except:
    pass

# /usr/include/elf.h: 3567
try:
    R_NIOS2_PCREL_HA = 27
except:
    pass

# /usr/include/elf.h: 3568
try:
    R_NIOS2_TLS_GD16 = 28
except:
    pass

# /usr/include/elf.h: 3569
try:
    R_NIOS2_TLS_LDM16 = 29
except:
    pass

# /usr/include/elf.h: 3570
try:
    R_NIOS2_TLS_LDO16 = 30
except:
    pass

# /usr/include/elf.h: 3571
try:
    R_NIOS2_TLS_IE16 = 31
except:
    pass

# /usr/include/elf.h: 3572
try:
    R_NIOS2_TLS_LE16 = 32
except:
    pass

# /usr/include/elf.h: 3573
try:
    R_NIOS2_TLS_DTPMOD = 33
except:
    pass

# /usr/include/elf.h: 3574
try:
    R_NIOS2_TLS_DTPREL = 34
except:
    pass

# /usr/include/elf.h: 3575
try:
    R_NIOS2_TLS_TPREL = 35
except:
    pass

# /usr/include/elf.h: 3576
try:
    R_NIOS2_COPY = 36
except:
    pass

# /usr/include/elf.h: 3577
try:
    R_NIOS2_GLOB_DAT = 37
except:
    pass

# /usr/include/elf.h: 3578
try:
    R_NIOS2_JUMP_SLOT = 38
except:
    pass

# /usr/include/elf.h: 3579
try:
    R_NIOS2_RELATIVE = 39
except:
    pass

# /usr/include/elf.h: 3580
try:
    R_NIOS2_GOTOFF = 40
except:
    pass

# /usr/include/elf.h: 3581
try:
    R_NIOS2_CALL26_NOAT = 41
except:
    pass

# /usr/include/elf.h: 3582
try:
    R_NIOS2_GOT_LO = 42
except:
    pass

# /usr/include/elf.h: 3583
try:
    R_NIOS2_GOT_HA = 43
except:
    pass

# /usr/include/elf.h: 3584
try:
    R_NIOS2_CALL_LO = 44
except:
    pass

# /usr/include/elf.h: 3585
try:
    R_NIOS2_CALL_HA = 45
except:
    pass

# /usr/include/elf.h: 3588
try:
    R_TILEPRO_NONE = 0
except:
    pass

# /usr/include/elf.h: 3589
try:
    R_TILEPRO_32 = 1
except:
    pass

# /usr/include/elf.h: 3590
try:
    R_TILEPRO_16 = 2
except:
    pass

# /usr/include/elf.h: 3591
try:
    R_TILEPRO_8 = 3
except:
    pass

# /usr/include/elf.h: 3592
try:
    R_TILEPRO_32_PCREL = 4
except:
    pass

# /usr/include/elf.h: 3593
try:
    R_TILEPRO_16_PCREL = 5
except:
    pass

# /usr/include/elf.h: 3594
try:
    R_TILEPRO_8_PCREL = 6
except:
    pass

# /usr/include/elf.h: 3595
try:
    R_TILEPRO_LO16 = 7
except:
    pass

# /usr/include/elf.h: 3596
try:
    R_TILEPRO_HI16 = 8
except:
    pass

# /usr/include/elf.h: 3597
try:
    R_TILEPRO_HA16 = 9
except:
    pass

# /usr/include/elf.h: 3598
try:
    R_TILEPRO_COPY = 10
except:
    pass

# /usr/include/elf.h: 3599
try:
    R_TILEPRO_GLOB_DAT = 11
except:
    pass

# /usr/include/elf.h: 3600
try:
    R_TILEPRO_JMP_SLOT = 12
except:
    pass

# /usr/include/elf.h: 3601
try:
    R_TILEPRO_RELATIVE = 13
except:
    pass

# /usr/include/elf.h: 3602
try:
    R_TILEPRO_BROFF_X1 = 14
except:
    pass

# /usr/include/elf.h: 3603
try:
    R_TILEPRO_JOFFLONG_X1 = 15
except:
    pass

# /usr/include/elf.h: 3604
try:
    R_TILEPRO_JOFFLONG_X1_PLT = 16
except:
    pass

# /usr/include/elf.h: 3605
try:
    R_TILEPRO_IMM8_X0 = 17
except:
    pass

# /usr/include/elf.h: 3606
try:
    R_TILEPRO_IMM8_Y0 = 18
except:
    pass

# /usr/include/elf.h: 3607
try:
    R_TILEPRO_IMM8_X1 = 19
except:
    pass

# /usr/include/elf.h: 3608
try:
    R_TILEPRO_IMM8_Y1 = 20
except:
    pass

# /usr/include/elf.h: 3609
try:
    R_TILEPRO_MT_IMM15_X1 = 21
except:
    pass

# /usr/include/elf.h: 3610
try:
    R_TILEPRO_MF_IMM15_X1 = 22
except:
    pass

# /usr/include/elf.h: 3611
try:
    R_TILEPRO_IMM16_X0 = 23
except:
    pass

# /usr/include/elf.h: 3612
try:
    R_TILEPRO_IMM16_X1 = 24
except:
    pass

# /usr/include/elf.h: 3613
try:
    R_TILEPRO_IMM16_X0_LO = 25
except:
    pass

# /usr/include/elf.h: 3614
try:
    R_TILEPRO_IMM16_X1_LO = 26
except:
    pass

# /usr/include/elf.h: 3615
try:
    R_TILEPRO_IMM16_X0_HI = 27
except:
    pass

# /usr/include/elf.h: 3616
try:
    R_TILEPRO_IMM16_X1_HI = 28
except:
    pass

# /usr/include/elf.h: 3617
try:
    R_TILEPRO_IMM16_X0_HA = 29
except:
    pass

# /usr/include/elf.h: 3618
try:
    R_TILEPRO_IMM16_X1_HA = 30
except:
    pass

# /usr/include/elf.h: 3619
try:
    R_TILEPRO_IMM16_X0_PCREL = 31
except:
    pass

# /usr/include/elf.h: 3620
try:
    R_TILEPRO_IMM16_X1_PCREL = 32
except:
    pass

# /usr/include/elf.h: 3621
try:
    R_TILEPRO_IMM16_X0_LO_PCREL = 33
except:
    pass

# /usr/include/elf.h: 3622
try:
    R_TILEPRO_IMM16_X1_LO_PCREL = 34
except:
    pass

# /usr/include/elf.h: 3623
try:
    R_TILEPRO_IMM16_X0_HI_PCREL = 35
except:
    pass

# /usr/include/elf.h: 3624
try:
    R_TILEPRO_IMM16_X1_HI_PCREL = 36
except:
    pass

# /usr/include/elf.h: 3625
try:
    R_TILEPRO_IMM16_X0_HA_PCREL = 37
except:
    pass

# /usr/include/elf.h: 3626
try:
    R_TILEPRO_IMM16_X1_HA_PCREL = 38
except:
    pass

# /usr/include/elf.h: 3627
try:
    R_TILEPRO_IMM16_X0_GOT = 39
except:
    pass

# /usr/include/elf.h: 3628
try:
    R_TILEPRO_IMM16_X1_GOT = 40
except:
    pass

# /usr/include/elf.h: 3629
try:
    R_TILEPRO_IMM16_X0_GOT_LO = 41
except:
    pass

# /usr/include/elf.h: 3630
try:
    R_TILEPRO_IMM16_X1_GOT_LO = 42
except:
    pass

# /usr/include/elf.h: 3631
try:
    R_TILEPRO_IMM16_X0_GOT_HI = 43
except:
    pass

# /usr/include/elf.h: 3632
try:
    R_TILEPRO_IMM16_X1_GOT_HI = 44
except:
    pass

# /usr/include/elf.h: 3633
try:
    R_TILEPRO_IMM16_X0_GOT_HA = 45
except:
    pass

# /usr/include/elf.h: 3634
try:
    R_TILEPRO_IMM16_X1_GOT_HA = 46
except:
    pass

# /usr/include/elf.h: 3635
try:
    R_TILEPRO_MMSTART_X0 = 47
except:
    pass

# /usr/include/elf.h: 3636
try:
    R_TILEPRO_MMEND_X0 = 48
except:
    pass

# /usr/include/elf.h: 3637
try:
    R_TILEPRO_MMSTART_X1 = 49
except:
    pass

# /usr/include/elf.h: 3638
try:
    R_TILEPRO_MMEND_X1 = 50
except:
    pass

# /usr/include/elf.h: 3639
try:
    R_TILEPRO_SHAMT_X0 = 51
except:
    pass

# /usr/include/elf.h: 3640
try:
    R_TILEPRO_SHAMT_X1 = 52
except:
    pass

# /usr/include/elf.h: 3641
try:
    R_TILEPRO_SHAMT_Y0 = 53
except:
    pass

# /usr/include/elf.h: 3642
try:
    R_TILEPRO_SHAMT_Y1 = 54
except:
    pass

# /usr/include/elf.h: 3643
try:
    R_TILEPRO_DEST_IMM8_X1 = 55
except:
    pass

# /usr/include/elf.h: 3645
try:
    R_TILEPRO_TLS_GD_CALL = 60
except:
    pass

# /usr/include/elf.h: 3646
try:
    R_TILEPRO_IMM8_X0_TLS_GD_ADD = 61
except:
    pass

# /usr/include/elf.h: 3647
try:
    R_TILEPRO_IMM8_X1_TLS_GD_ADD = 62
except:
    pass

# /usr/include/elf.h: 3648
try:
    R_TILEPRO_IMM8_Y0_TLS_GD_ADD = 63
except:
    pass

# /usr/include/elf.h: 3649
try:
    R_TILEPRO_IMM8_Y1_TLS_GD_ADD = 64
except:
    pass

# /usr/include/elf.h: 3650
try:
    R_TILEPRO_TLS_IE_LOAD = 65
except:
    pass

# /usr/include/elf.h: 3651
try:
    R_TILEPRO_IMM16_X0_TLS_GD = 66
except:
    pass

# /usr/include/elf.h: 3652
try:
    R_TILEPRO_IMM16_X1_TLS_GD = 67
except:
    pass

# /usr/include/elf.h: 3653
try:
    R_TILEPRO_IMM16_X0_TLS_GD_LO = 68
except:
    pass

# /usr/include/elf.h: 3654
try:
    R_TILEPRO_IMM16_X1_TLS_GD_LO = 69
except:
    pass

# /usr/include/elf.h: 3655
try:
    R_TILEPRO_IMM16_X0_TLS_GD_HI = 70
except:
    pass

# /usr/include/elf.h: 3656
try:
    R_TILEPRO_IMM16_X1_TLS_GD_HI = 71
except:
    pass

# /usr/include/elf.h: 3657
try:
    R_TILEPRO_IMM16_X0_TLS_GD_HA = 72
except:
    pass

# /usr/include/elf.h: 3658
try:
    R_TILEPRO_IMM16_X1_TLS_GD_HA = 73
except:
    pass

# /usr/include/elf.h: 3659
try:
    R_TILEPRO_IMM16_X0_TLS_IE = 74
except:
    pass

# /usr/include/elf.h: 3660
try:
    R_TILEPRO_IMM16_X1_TLS_IE = 75
except:
    pass

# /usr/include/elf.h: 3661
try:
    R_TILEPRO_IMM16_X0_TLS_IE_LO = 76
except:
    pass

# /usr/include/elf.h: 3662
try:
    R_TILEPRO_IMM16_X1_TLS_IE_LO = 77
except:
    pass

# /usr/include/elf.h: 3663
try:
    R_TILEPRO_IMM16_X0_TLS_IE_HI = 78
except:
    pass

# /usr/include/elf.h: 3664
try:
    R_TILEPRO_IMM16_X1_TLS_IE_HI = 79
except:
    pass

# /usr/include/elf.h: 3665
try:
    R_TILEPRO_IMM16_X0_TLS_IE_HA = 80
except:
    pass

# /usr/include/elf.h: 3666
try:
    R_TILEPRO_IMM16_X1_TLS_IE_HA = 81
except:
    pass

# /usr/include/elf.h: 3667
try:
    R_TILEPRO_TLS_DTPMOD32 = 82
except:
    pass

# /usr/include/elf.h: 3668
try:
    R_TILEPRO_TLS_DTPOFF32 = 83
except:
    pass

# /usr/include/elf.h: 3669
try:
    R_TILEPRO_TLS_TPOFF32 = 84
except:
    pass

# /usr/include/elf.h: 3670
try:
    R_TILEPRO_IMM16_X0_TLS_LE = 85
except:
    pass

# /usr/include/elf.h: 3671
try:
    R_TILEPRO_IMM16_X1_TLS_LE = 86
except:
    pass

# /usr/include/elf.h: 3672
try:
    R_TILEPRO_IMM16_X0_TLS_LE_LO = 87
except:
    pass

# /usr/include/elf.h: 3673
try:
    R_TILEPRO_IMM16_X1_TLS_LE_LO = 88
except:
    pass

# /usr/include/elf.h: 3674
try:
    R_TILEPRO_IMM16_X0_TLS_LE_HI = 89
except:
    pass

# /usr/include/elf.h: 3675
try:
    R_TILEPRO_IMM16_X1_TLS_LE_HI = 90
except:
    pass

# /usr/include/elf.h: 3676
try:
    R_TILEPRO_IMM16_X0_TLS_LE_HA = 91
except:
    pass

# /usr/include/elf.h: 3677
try:
    R_TILEPRO_IMM16_X1_TLS_LE_HA = 92
except:
    pass

# /usr/include/elf.h: 3679
try:
    R_TILEPRO_GNU_VTINHERIT = 128
except:
    pass

# /usr/include/elf.h: 3680
try:
    R_TILEPRO_GNU_VTENTRY = 129
except:
    pass

# /usr/include/elf.h: 3682
try:
    R_TILEPRO_NUM = 130
except:
    pass

# /usr/include/elf.h: 3686
try:
    R_TILEGX_NONE = 0
except:
    pass

# /usr/include/elf.h: 3687
try:
    R_TILEGX_64 = 1
except:
    pass

# /usr/include/elf.h: 3688
try:
    R_TILEGX_32 = 2
except:
    pass

# /usr/include/elf.h: 3689
try:
    R_TILEGX_16 = 3
except:
    pass

# /usr/include/elf.h: 3690
try:
    R_TILEGX_8 = 4
except:
    pass

# /usr/include/elf.h: 3691
try:
    R_TILEGX_64_PCREL = 5
except:
    pass

# /usr/include/elf.h: 3692
try:
    R_TILEGX_32_PCREL = 6
except:
    pass

# /usr/include/elf.h: 3693
try:
    R_TILEGX_16_PCREL = 7
except:
    pass

# /usr/include/elf.h: 3694
try:
    R_TILEGX_8_PCREL = 8
except:
    pass

# /usr/include/elf.h: 3695
try:
    R_TILEGX_HW0 = 9
except:
    pass

# /usr/include/elf.h: 3696
try:
    R_TILEGX_HW1 = 10
except:
    pass

# /usr/include/elf.h: 3697
try:
    R_TILEGX_HW2 = 11
except:
    pass

# /usr/include/elf.h: 3698
try:
    R_TILEGX_HW3 = 12
except:
    pass

# /usr/include/elf.h: 3699
try:
    R_TILEGX_HW0_LAST = 13
except:
    pass

# /usr/include/elf.h: 3700
try:
    R_TILEGX_HW1_LAST = 14
except:
    pass

# /usr/include/elf.h: 3701
try:
    R_TILEGX_HW2_LAST = 15
except:
    pass

# /usr/include/elf.h: 3702
try:
    R_TILEGX_COPY = 16
except:
    pass

# /usr/include/elf.h: 3703
try:
    R_TILEGX_GLOB_DAT = 17
except:
    pass

# /usr/include/elf.h: 3704
try:
    R_TILEGX_JMP_SLOT = 18
except:
    pass

# /usr/include/elf.h: 3705
try:
    R_TILEGX_RELATIVE = 19
except:
    pass

# /usr/include/elf.h: 3706
try:
    R_TILEGX_BROFF_X1 = 20
except:
    pass

# /usr/include/elf.h: 3707
try:
    R_TILEGX_JUMPOFF_X1 = 21
except:
    pass

# /usr/include/elf.h: 3708
try:
    R_TILEGX_JUMPOFF_X1_PLT = 22
except:
    pass

# /usr/include/elf.h: 3709
try:
    R_TILEGX_IMM8_X0 = 23
except:
    pass

# /usr/include/elf.h: 3710
try:
    R_TILEGX_IMM8_Y0 = 24
except:
    pass

# /usr/include/elf.h: 3711
try:
    R_TILEGX_IMM8_X1 = 25
except:
    pass

# /usr/include/elf.h: 3712
try:
    R_TILEGX_IMM8_Y1 = 26
except:
    pass

# /usr/include/elf.h: 3713
try:
    R_TILEGX_DEST_IMM8_X1 = 27
except:
    pass

# /usr/include/elf.h: 3714
try:
    R_TILEGX_MT_IMM14_X1 = 28
except:
    pass

# /usr/include/elf.h: 3715
try:
    R_TILEGX_MF_IMM14_X1 = 29
except:
    pass

# /usr/include/elf.h: 3716
try:
    R_TILEGX_MMSTART_X0 = 30
except:
    pass

# /usr/include/elf.h: 3717
try:
    R_TILEGX_MMEND_X0 = 31
except:
    pass

# /usr/include/elf.h: 3718
try:
    R_TILEGX_SHAMT_X0 = 32
except:
    pass

# /usr/include/elf.h: 3719
try:
    R_TILEGX_SHAMT_X1 = 33
except:
    pass

# /usr/include/elf.h: 3720
try:
    R_TILEGX_SHAMT_Y0 = 34
except:
    pass

# /usr/include/elf.h: 3721
try:
    R_TILEGX_SHAMT_Y1 = 35
except:
    pass

# /usr/include/elf.h: 3722
try:
    R_TILEGX_IMM16_X0_HW0 = 36
except:
    pass

# /usr/include/elf.h: 3723
try:
    R_TILEGX_IMM16_X1_HW0 = 37
except:
    pass

# /usr/include/elf.h: 3724
try:
    R_TILEGX_IMM16_X0_HW1 = 38
except:
    pass

# /usr/include/elf.h: 3725
try:
    R_TILEGX_IMM16_X1_HW1 = 39
except:
    pass

# /usr/include/elf.h: 3726
try:
    R_TILEGX_IMM16_X0_HW2 = 40
except:
    pass

# /usr/include/elf.h: 3727
try:
    R_TILEGX_IMM16_X1_HW2 = 41
except:
    pass

# /usr/include/elf.h: 3728
try:
    R_TILEGX_IMM16_X0_HW3 = 42
except:
    pass

# /usr/include/elf.h: 3729
try:
    R_TILEGX_IMM16_X1_HW3 = 43
except:
    pass

# /usr/include/elf.h: 3730
try:
    R_TILEGX_IMM16_X0_HW0_LAST = 44
except:
    pass

# /usr/include/elf.h: 3731
try:
    R_TILEGX_IMM16_X1_HW0_LAST = 45
except:
    pass

# /usr/include/elf.h: 3732
try:
    R_TILEGX_IMM16_X0_HW1_LAST = 46
except:
    pass

# /usr/include/elf.h: 3733
try:
    R_TILEGX_IMM16_X1_HW1_LAST = 47
except:
    pass

# /usr/include/elf.h: 3734
try:
    R_TILEGX_IMM16_X0_HW2_LAST = 48
except:
    pass

# /usr/include/elf.h: 3735
try:
    R_TILEGX_IMM16_X1_HW2_LAST = 49
except:
    pass

# /usr/include/elf.h: 3736
try:
    R_TILEGX_IMM16_X0_HW0_PCREL = 50
except:
    pass

# /usr/include/elf.h: 3737
try:
    R_TILEGX_IMM16_X1_HW0_PCREL = 51
except:
    pass

# /usr/include/elf.h: 3738
try:
    R_TILEGX_IMM16_X0_HW1_PCREL = 52
except:
    pass

# /usr/include/elf.h: 3739
try:
    R_TILEGX_IMM16_X1_HW1_PCREL = 53
except:
    pass

# /usr/include/elf.h: 3740
try:
    R_TILEGX_IMM16_X0_HW2_PCREL = 54
except:
    pass

# /usr/include/elf.h: 3741
try:
    R_TILEGX_IMM16_X1_HW2_PCREL = 55
except:
    pass

# /usr/include/elf.h: 3742
try:
    R_TILEGX_IMM16_X0_HW3_PCREL = 56
except:
    pass

# /usr/include/elf.h: 3743
try:
    R_TILEGX_IMM16_X1_HW3_PCREL = 57
except:
    pass

# /usr/include/elf.h: 3744
try:
    R_TILEGX_IMM16_X0_HW0_LAST_PCREL = 58
except:
    pass

# /usr/include/elf.h: 3745
try:
    R_TILEGX_IMM16_X1_HW0_LAST_PCREL = 59
except:
    pass

# /usr/include/elf.h: 3746
try:
    R_TILEGX_IMM16_X0_HW1_LAST_PCREL = 60
except:
    pass

# /usr/include/elf.h: 3747
try:
    R_TILEGX_IMM16_X1_HW1_LAST_PCREL = 61
except:
    pass

# /usr/include/elf.h: 3748
try:
    R_TILEGX_IMM16_X0_HW2_LAST_PCREL = 62
except:
    pass

# /usr/include/elf.h: 3749
try:
    R_TILEGX_IMM16_X1_HW2_LAST_PCREL = 63
except:
    pass

# /usr/include/elf.h: 3750
try:
    R_TILEGX_IMM16_X0_HW0_GOT = 64
except:
    pass

# /usr/include/elf.h: 3751
try:
    R_TILEGX_IMM16_X1_HW0_GOT = 65
except:
    pass

# /usr/include/elf.h: 3752
try:
    R_TILEGX_IMM16_X0_HW0_PLT_PCREL = 66
except:
    pass

# /usr/include/elf.h: 3753
try:
    R_TILEGX_IMM16_X1_HW0_PLT_PCREL = 67
except:
    pass

# /usr/include/elf.h: 3754
try:
    R_TILEGX_IMM16_X0_HW1_PLT_PCREL = 68
except:
    pass

# /usr/include/elf.h: 3755
try:
    R_TILEGX_IMM16_X1_HW1_PLT_PCREL = 69
except:
    pass

# /usr/include/elf.h: 3756
try:
    R_TILEGX_IMM16_X0_HW2_PLT_PCREL = 70
except:
    pass

# /usr/include/elf.h: 3757
try:
    R_TILEGX_IMM16_X1_HW2_PLT_PCREL = 71
except:
    pass

# /usr/include/elf.h: 3758
try:
    R_TILEGX_IMM16_X0_HW0_LAST_GOT = 72
except:
    pass

# /usr/include/elf.h: 3759
try:
    R_TILEGX_IMM16_X1_HW0_LAST_GOT = 73
except:
    pass

# /usr/include/elf.h: 3760
try:
    R_TILEGX_IMM16_X0_HW1_LAST_GOT = 74
except:
    pass

# /usr/include/elf.h: 3761
try:
    R_TILEGX_IMM16_X1_HW1_LAST_GOT = 75
except:
    pass

# /usr/include/elf.h: 3762
try:
    R_TILEGX_IMM16_X0_HW3_PLT_PCREL = 76
except:
    pass

# /usr/include/elf.h: 3763
try:
    R_TILEGX_IMM16_X1_HW3_PLT_PCREL = 77
except:
    pass

# /usr/include/elf.h: 3764
try:
    R_TILEGX_IMM16_X0_HW0_TLS_GD = 78
except:
    pass

# /usr/include/elf.h: 3765
try:
    R_TILEGX_IMM16_X1_HW0_TLS_GD = 79
except:
    pass

# /usr/include/elf.h: 3766
try:
    R_TILEGX_IMM16_X0_HW0_TLS_LE = 80
except:
    pass

# /usr/include/elf.h: 3767
try:
    R_TILEGX_IMM16_X1_HW0_TLS_LE = 81
except:
    pass

# /usr/include/elf.h: 3768
try:
    R_TILEGX_IMM16_X0_HW0_LAST_TLS_LE = 82
except:
    pass

# /usr/include/elf.h: 3769
try:
    R_TILEGX_IMM16_X1_HW0_LAST_TLS_LE = 83
except:
    pass

# /usr/include/elf.h: 3770
try:
    R_TILEGX_IMM16_X0_HW1_LAST_TLS_LE = 84
except:
    pass

# /usr/include/elf.h: 3771
try:
    R_TILEGX_IMM16_X1_HW1_LAST_TLS_LE = 85
except:
    pass

# /usr/include/elf.h: 3772
try:
    R_TILEGX_IMM16_X0_HW0_LAST_TLS_GD = 86
except:
    pass

# /usr/include/elf.h: 3773
try:
    R_TILEGX_IMM16_X1_HW0_LAST_TLS_GD = 87
except:
    pass

# /usr/include/elf.h: 3774
try:
    R_TILEGX_IMM16_X0_HW1_LAST_TLS_GD = 88
except:
    pass

# /usr/include/elf.h: 3775
try:
    R_TILEGX_IMM16_X1_HW1_LAST_TLS_GD = 89
except:
    pass

# /usr/include/elf.h: 3777
try:
    R_TILEGX_IMM16_X0_HW0_TLS_IE = 92
except:
    pass

# /usr/include/elf.h: 3778
try:
    R_TILEGX_IMM16_X1_HW0_TLS_IE = 93
except:
    pass

# /usr/include/elf.h: 3779
try:
    R_TILEGX_IMM16_X0_HW0_LAST_PLT_PCREL = 94
except:
    pass

# /usr/include/elf.h: 3780
try:
    R_TILEGX_IMM16_X1_HW0_LAST_PLT_PCREL = 95
except:
    pass

# /usr/include/elf.h: 3781
try:
    R_TILEGX_IMM16_X0_HW1_LAST_PLT_PCREL = 96
except:
    pass

# /usr/include/elf.h: 3782
try:
    R_TILEGX_IMM16_X1_HW1_LAST_PLT_PCREL = 97
except:
    pass

# /usr/include/elf.h: 3783
try:
    R_TILEGX_IMM16_X0_HW2_LAST_PLT_PCREL = 98
except:
    pass

# /usr/include/elf.h: 3784
try:
    R_TILEGX_IMM16_X1_HW2_LAST_PLT_PCREL = 99
except:
    pass

# /usr/include/elf.h: 3785
try:
    R_TILEGX_IMM16_X0_HW0_LAST_TLS_IE = 100
except:
    pass

# /usr/include/elf.h: 3786
try:
    R_TILEGX_IMM16_X1_HW0_LAST_TLS_IE = 101
except:
    pass

# /usr/include/elf.h: 3787
try:
    R_TILEGX_IMM16_X0_HW1_LAST_TLS_IE = 102
except:
    pass

# /usr/include/elf.h: 3788
try:
    R_TILEGX_IMM16_X1_HW1_LAST_TLS_IE = 103
except:
    pass

# /usr/include/elf.h: 3790
try:
    R_TILEGX_TLS_DTPMOD64 = 106
except:
    pass

# /usr/include/elf.h: 3791
try:
    R_TILEGX_TLS_DTPOFF64 = 107
except:
    pass

# /usr/include/elf.h: 3792
try:
    R_TILEGX_TLS_TPOFF64 = 108
except:
    pass

# /usr/include/elf.h: 3793
try:
    R_TILEGX_TLS_DTPMOD32 = 109
except:
    pass

# /usr/include/elf.h: 3794
try:
    R_TILEGX_TLS_DTPOFF32 = 110
except:
    pass

# /usr/include/elf.h: 3795
try:
    R_TILEGX_TLS_TPOFF32 = 111
except:
    pass

# /usr/include/elf.h: 3796
try:
    R_TILEGX_TLS_GD_CALL = 112
except:
    pass

# /usr/include/elf.h: 3797
try:
    R_TILEGX_IMM8_X0_TLS_GD_ADD = 113
except:
    pass

# /usr/include/elf.h: 3798
try:
    R_TILEGX_IMM8_X1_TLS_GD_ADD = 114
except:
    pass

# /usr/include/elf.h: 3799
try:
    R_TILEGX_IMM8_Y0_TLS_GD_ADD = 115
except:
    pass

# /usr/include/elf.h: 3800
try:
    R_TILEGX_IMM8_Y1_TLS_GD_ADD = 116
except:
    pass

# /usr/include/elf.h: 3801
try:
    R_TILEGX_TLS_IE_LOAD = 117
except:
    pass

# /usr/include/elf.h: 3802
try:
    R_TILEGX_IMM8_X0_TLS_ADD = 118
except:
    pass

# /usr/include/elf.h: 3803
try:
    R_TILEGX_IMM8_X1_TLS_ADD = 119
except:
    pass

# /usr/include/elf.h: 3804
try:
    R_TILEGX_IMM8_Y0_TLS_ADD = 120
except:
    pass

# /usr/include/elf.h: 3805
try:
    R_TILEGX_IMM8_Y1_TLS_ADD = 121
except:
    pass

# /usr/include/elf.h: 3807
try:
    R_TILEGX_GNU_VTINHERIT = 128
except:
    pass

# /usr/include/elf.h: 3808
try:
    R_TILEGX_GNU_VTENTRY = 129
except:
    pass

# /usr/include/elf.h: 3810
try:
    R_TILEGX_NUM = 130
except:
    pass

# /usr/include/elf.h: 3813
try:
    EF_RISCV_RVC = 0x0001
except:
    pass

# /usr/include/elf.h: 3814
try:
    EF_RISCV_FLOAT_ABI = 0x0006
except:
    pass

# /usr/include/elf.h: 3815
try:
    EF_RISCV_FLOAT_ABI_SOFT = 0x0000
except:
    pass

# /usr/include/elf.h: 3816
try:
    EF_RISCV_FLOAT_ABI_SINGLE = 0x0002
except:
    pass

# /usr/include/elf.h: 3817
try:
    EF_RISCV_FLOAT_ABI_DOUBLE = 0x0004
except:
    pass

# /usr/include/elf.h: 3818
try:
    EF_RISCV_FLOAT_ABI_QUAD = 0x0006
except:
    pass

# /usr/include/elf.h: 3821
try:
    R_RISCV_NONE = 0
except:
    pass

# /usr/include/elf.h: 3822
try:
    R_RISCV_32 = 1
except:
    pass

# /usr/include/elf.h: 3823
try:
    R_RISCV_64 = 2
except:
    pass

# /usr/include/elf.h: 3824
try:
    R_RISCV_RELATIVE = 3
except:
    pass

# /usr/include/elf.h: 3825
try:
    R_RISCV_COPY = 4
except:
    pass

# /usr/include/elf.h: 3826
try:
    R_RISCV_JUMP_SLOT = 5
except:
    pass

# /usr/include/elf.h: 3827
try:
    R_RISCV_TLS_DTPMOD32 = 6
except:
    pass

# /usr/include/elf.h: 3828
try:
    R_RISCV_TLS_DTPMOD64 = 7
except:
    pass

# /usr/include/elf.h: 3829
try:
    R_RISCV_TLS_DTPREL32 = 8
except:
    pass

# /usr/include/elf.h: 3830
try:
    R_RISCV_TLS_DTPREL64 = 9
except:
    pass

# /usr/include/elf.h: 3831
try:
    R_RISCV_TLS_TPREL32 = 10
except:
    pass

# /usr/include/elf.h: 3832
try:
    R_RISCV_TLS_TPREL64 = 11
except:
    pass

# /usr/include/elf.h: 3833
try:
    R_RISCV_BRANCH = 16
except:
    pass

# /usr/include/elf.h: 3834
try:
    R_RISCV_JAL = 17
except:
    pass

# /usr/include/elf.h: 3835
try:
    R_RISCV_CALL = 18
except:
    pass

# /usr/include/elf.h: 3836
try:
    R_RISCV_CALL_PLT = 19
except:
    pass

# /usr/include/elf.h: 3837
try:
    R_RISCV_GOT_HI20 = 20
except:
    pass

# /usr/include/elf.h: 3838
try:
    R_RISCV_TLS_GOT_HI20 = 21
except:
    pass

# /usr/include/elf.h: 3839
try:
    R_RISCV_TLS_GD_HI20 = 22
except:
    pass

# /usr/include/elf.h: 3840
try:
    R_RISCV_PCREL_HI20 = 23
except:
    pass

# /usr/include/elf.h: 3841
try:
    R_RISCV_PCREL_LO12_I = 24
except:
    pass

# /usr/include/elf.h: 3842
try:
    R_RISCV_PCREL_LO12_S = 25
except:
    pass

# /usr/include/elf.h: 3843
try:
    R_RISCV_HI20 = 26
except:
    pass

# /usr/include/elf.h: 3844
try:
    R_RISCV_LO12_I = 27
except:
    pass

# /usr/include/elf.h: 3845
try:
    R_RISCV_LO12_S = 28
except:
    pass

# /usr/include/elf.h: 3846
try:
    R_RISCV_TPREL_HI20 = 29
except:
    pass

# /usr/include/elf.h: 3847
try:
    R_RISCV_TPREL_LO12_I = 30
except:
    pass

# /usr/include/elf.h: 3848
try:
    R_RISCV_TPREL_LO12_S = 31
except:
    pass

# /usr/include/elf.h: 3849
try:
    R_RISCV_TPREL_ADD = 32
except:
    pass

# /usr/include/elf.h: 3850
try:
    R_RISCV_ADD8 = 33
except:
    pass

# /usr/include/elf.h: 3851
try:
    R_RISCV_ADD16 = 34
except:
    pass

# /usr/include/elf.h: 3852
try:
    R_RISCV_ADD32 = 35
except:
    pass

# /usr/include/elf.h: 3853
try:
    R_RISCV_ADD64 = 36
except:
    pass

# /usr/include/elf.h: 3854
try:
    R_RISCV_SUB8 = 37
except:
    pass

# /usr/include/elf.h: 3855
try:
    R_RISCV_SUB16 = 38
except:
    pass

# /usr/include/elf.h: 3856
try:
    R_RISCV_SUB32 = 39
except:
    pass

# /usr/include/elf.h: 3857
try:
    R_RISCV_SUB64 = 40
except:
    pass

# /usr/include/elf.h: 3858
try:
    R_RISCV_GNU_VTINHERIT = 41
except:
    pass

# /usr/include/elf.h: 3859
try:
    R_RISCV_GNU_VTENTRY = 42
except:
    pass

# /usr/include/elf.h: 3860
try:
    R_RISCV_ALIGN = 43
except:
    pass

# /usr/include/elf.h: 3861
try:
    R_RISCV_RVC_BRANCH = 44
except:
    pass

# /usr/include/elf.h: 3862
try:
    R_RISCV_RVC_JUMP = 45
except:
    pass

# /usr/include/elf.h: 3863
try:
    R_RISCV_RVC_LUI = 46
except:
    pass

# /usr/include/elf.h: 3864
try:
    R_RISCV_GPREL_I = 47
except:
    pass

# /usr/include/elf.h: 3865
try:
    R_RISCV_GPREL_S = 48
except:
    pass

# /usr/include/elf.h: 3866
try:
    R_RISCV_TPREL_I = 49
except:
    pass

# /usr/include/elf.h: 3867
try:
    R_RISCV_TPREL_S = 50
except:
    pass

# /usr/include/elf.h: 3868
try:
    R_RISCV_RELAX = 51
except:
    pass

# /usr/include/elf.h: 3869
try:
    R_RISCV_SUB6 = 52
except:
    pass

# /usr/include/elf.h: 3870
try:
    R_RISCV_SET6 = 53
except:
    pass

# /usr/include/elf.h: 3871
try:
    R_RISCV_SET8 = 54
except:
    pass

# /usr/include/elf.h: 3872
try:
    R_RISCV_SET16 = 55
except:
    pass

# /usr/include/elf.h: 3873
try:
    R_RISCV_SET32 = 56
except:
    pass

# /usr/include/elf.h: 3874
try:
    R_RISCV_32_PCREL = 57
except:
    pass

# /usr/include/elf.h: 3876
try:
    R_RISCV_NUM = 58
except:
    pass

# /usr/include/elf.h: 3880
try:
    R_BPF_NONE = 0
except:
    pass

# /usr/include/elf.h: 3881
try:
    R_BPF_64_64 = 1
except:
    pass

# /usr/include/elf.h: 3882
try:
    R_BPF_64_32 = 10
except:
    pass

# /usr/include/elf.h: 3886
try:
    R_METAG_HIADDR16 = 0
except:
    pass

# /usr/include/elf.h: 3887
try:
    R_METAG_LOADDR16 = 1
except:
    pass

# /usr/include/elf.h: 3888
try:
    R_METAG_ADDR32 = 2
except:
    pass

# /usr/include/elf.h: 3889
try:
    R_METAG_NONE = 3
except:
    pass

# /usr/include/elf.h: 3890
try:
    R_METAG_RELBRANCH = 4
except:
    pass

# /usr/include/elf.h: 3891
try:
    R_METAG_GETSETOFF = 5
except:
    pass

# /usr/include/elf.h: 3894
try:
    R_METAG_REG32OP1 = 6
except:
    pass

# /usr/include/elf.h: 3895
try:
    R_METAG_REG32OP2 = 7
except:
    pass

# /usr/include/elf.h: 3896
try:
    R_METAG_REG32OP3 = 8
except:
    pass

# /usr/include/elf.h: 3897
try:
    R_METAG_REG16OP1 = 9
except:
    pass

# /usr/include/elf.h: 3898
try:
    R_METAG_REG16OP2 = 10
except:
    pass

# /usr/include/elf.h: 3899
try:
    R_METAG_REG16OP3 = 11
except:
    pass

# /usr/include/elf.h: 3900
try:
    R_METAG_REG32OP4 = 12
except:
    pass

# /usr/include/elf.h: 3902
try:
    R_METAG_HIOG = 13
except:
    pass

# /usr/include/elf.h: 3903
try:
    R_METAG_LOOG = 14
except:
    pass

# /usr/include/elf.h: 3905
try:
    R_METAG_REL8 = 15
except:
    pass

# /usr/include/elf.h: 3906
try:
    R_METAG_REL16 = 16
except:
    pass

# /usr/include/elf.h: 3909
try:
    R_METAG_GNU_VTINHERIT = 30
except:
    pass

# /usr/include/elf.h: 3910
try:
    R_METAG_GNU_VTENTRY = 31
except:
    pass

# /usr/include/elf.h: 3913
try:
    R_METAG_HI16_GOTOFF = 32
except:
    pass

# /usr/include/elf.h: 3914
try:
    R_METAG_LO16_GOTOFF = 33
except:
    pass

# /usr/include/elf.h: 3915
try:
    R_METAG_GETSET_GOTOFF = 34
except:
    pass

# /usr/include/elf.h: 3916
try:
    R_METAG_GETSET_GOT = 35
except:
    pass

# /usr/include/elf.h: 3917
try:
    R_METAG_HI16_GOTPC = 36
except:
    pass

# /usr/include/elf.h: 3918
try:
    R_METAG_LO16_GOTPC = 37
except:
    pass

# /usr/include/elf.h: 3919
try:
    R_METAG_HI16_PLT = 38
except:
    pass

# /usr/include/elf.h: 3920
try:
    R_METAG_LO16_PLT = 39
except:
    pass

# /usr/include/elf.h: 3921
try:
    R_METAG_RELBRANCH_PLT = 40
except:
    pass

# /usr/include/elf.h: 3922
try:
    R_METAG_GOTOFF = 41
except:
    pass

# /usr/include/elf.h: 3923
try:
    R_METAG_PLT = 42
except:
    pass

# /usr/include/elf.h: 3924
try:
    R_METAG_COPY = 43
except:
    pass

# /usr/include/elf.h: 3925
try:
    R_METAG_JMP_SLOT = 44
except:
    pass

# /usr/include/elf.h: 3926
try:
    R_METAG_RELATIVE = 45
except:
    pass

# /usr/include/elf.h: 3927
try:
    R_METAG_GLOB_DAT = 46
except:
    pass

# /usr/include/elf.h: 3930
try:
    R_METAG_TLS_GD = 47
except:
    pass

# /usr/include/elf.h: 3931
try:
    R_METAG_TLS_LDM = 48
except:
    pass

# /usr/include/elf.h: 3932
try:
    R_METAG_TLS_LDO_HI16 = 49
except:
    pass

# /usr/include/elf.h: 3933
try:
    R_METAG_TLS_LDO_LO16 = 50
except:
    pass

# /usr/include/elf.h: 3934
try:
    R_METAG_TLS_LDO = 51
except:
    pass

# /usr/include/elf.h: 3935
try:
    R_METAG_TLS_IE = 52
except:
    pass

# /usr/include/elf.h: 3936
try:
    R_METAG_TLS_IENONPIC = 53
except:
    pass

# /usr/include/elf.h: 3937
try:
    R_METAG_TLS_IENONPIC_HI16 = 54
except:
    pass

# /usr/include/elf.h: 3938
try:
    R_METAG_TLS_IENONPIC_LO16 = 55
except:
    pass

# /usr/include/elf.h: 3939
try:
    R_METAG_TLS_TPOFF = 56
except:
    pass

# /usr/include/elf.h: 3940
try:
    R_METAG_TLS_DTPMOD = 57
except:
    pass

# /usr/include/elf.h: 3941
try:
    R_METAG_TLS_DTPOFF = 58
except:
    pass

# /usr/include/elf.h: 3942
try:
    R_METAG_TLS_LE = 59
except:
    pass

# /usr/include/elf.h: 3943
try:
    R_METAG_TLS_LE_HI16 = 60
except:
    pass

# /usr/include/elf.h: 3944
try:
    R_METAG_TLS_LE_LO16 = 61
except:
    pass

# /usr/include/elf.h: 3947
try:
    R_NDS32_NONE = 0
except:
    pass

# /usr/include/elf.h: 3948
try:
    R_NDS32_32_RELA = 20
except:
    pass

# /usr/include/elf.h: 3949
try:
    R_NDS32_COPY = 39
except:
    pass

# /usr/include/elf.h: 3950
try:
    R_NDS32_GLOB_DAT = 40
except:
    pass

# /usr/include/elf.h: 3951
try:
    R_NDS32_JMP_SLOT = 41
except:
    pass

# /usr/include/elf.h: 3952
try:
    R_NDS32_RELATIVE = 42
except:
    pass

# /usr/include/elf.h: 3953
try:
    R_NDS32_TLS_TPOFF = 102
except:
    pass

# /usr/include/elf.h: 3954
try:
    R_NDS32_TLS_DESC = 119
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 20
try:
    AT_NULL = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 21
try:
    AT_IGNORE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 22
try:
    AT_EXECFD = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 23
try:
    AT_PHDR = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 24
try:
    AT_PHENT = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 25
try:
    AT_PHNUM = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 26
try:
    AT_PAGESZ = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 27
try:
    AT_BASE = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 28
try:
    AT_FLAGS = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 29
try:
    AT_ENTRY = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 30
try:
    AT_NOTELF = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 31
try:
    AT_UID = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 32
try:
    AT_EUID = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 33
try:
    AT_GID = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 34
try:
    AT_EGID = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 35
try:
    AT_CLKTCK = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 38
try:
    AT_PLATFORM = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 39
try:
    AT_HWCAP = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 44
try:
    AT_FPUCW = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 47
try:
    AT_DCACHEBSIZE = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 48
try:
    AT_ICACHEBSIZE = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 49
try:
    AT_UCACHEBSIZE = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 53
try:
    AT_IGNOREPPC = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 55
try:
    AT_SECURE = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 57
try:
    AT_BASE_PLATFORM = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 59
try:
    AT_RANDOM = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 61
try:
    AT_HWCAP2 = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 64
try:
    AT_EXECFN = 31
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 68
try:
    AT_SYSINFO = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 69
try:
    AT_SYSINFO_EHDR = 33
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 73
try:
    AT_L1I_CACHESHAPE = 34
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 74
try:
    AT_L1D_CACHESHAPE = 35
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 75
try:
    AT_L2_CACHESHAPE = 36
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 76
try:
    AT_L3_CACHESHAPE = 37
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 81
try:
    AT_L1I_CACHESIZE = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 82
try:
    AT_L1I_CACHEGEOMETRY = 41
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 83
try:
    AT_L1D_CACHESIZE = 42
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 84
try:
    AT_L1D_CACHEGEOMETRY = 43
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 85
try:
    AT_L2_CACHESIZE = 44
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 86
try:
    AT_L2_CACHEGEOMETRY = 45
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 87
try:
    AT_L3_CACHESIZE = 46
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 88
try:
    AT_L3_CACHEGEOMETRY = 47
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/auxv.h: 90
try:
    AT_MINSIGSTKSZ = 51
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 19
try:
    _SYS_DEBUGREG_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 23
try:
    DR_FIRSTADDR = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 24
try:
    DR_LASTADDR = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 26
try:
    DR_STATUS = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 27
try:
    DR_CONTROL = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 33
try:
    DR_TRAP0 = 0x1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 34
try:
    DR_TRAP1 = 0x2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 35
try:
    DR_TRAP2 = 0x4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 36
try:
    DR_TRAP3 = 0x8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 38
try:
    DR_STEP = 0x4000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 39
try:
    DR_SWITCH = 0x8000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 47
try:
    DR_CONTROL_SHIFT = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 48
try:
    DR_CONTROL_SIZE = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 50
try:
    DR_RW_EXECUTE = 0x0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 51
try:
    DR_RW_WRITE = 0x1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 52
try:
    DR_RW_READ = 0x3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 54
try:
    DR_LEN_1 = 0x0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 55
try:
    DR_LEN_2 = 0x4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 56
try:
    DR_LEN_4 = 0xC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 58
try:
    DR_LEN_8 = 0x8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 68
try:
    DR_LOCAL_ENABLE_SHIFT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 69
try:
    DR_GLOBAL_ENABLE_SHIFT = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 70
try:
    DR_ENABLE_SIZE = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 72
try:
    DR_LOCAL_ENABLE_MASK = 0x55
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 73
try:
    DR_GLOBAL_ENABLE_MASK = 0xAA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 81
try:
    DR_CONTROL_RESERVED = 0xFFFFFFFF0000FC00
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 85
try:
    DR_LOCAL_SLOWDOWN = 0x100
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/debugreg.h: 86
try:
    DR_GLOBAL_SLOWDOWN = 0x200
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/dir.h: 19
try:
    _SYS_DIR_H = 1
except:
    pass

# /usr/include/linux/limits.h: 7
try:
    NGROUPS_MAX = 65536
except:
    pass

# /usr/include/linux/limits.h: 10
try:
    MAX_CANON = 255
except:
    pass

# /usr/include/linux/limits.h: 13
try:
    PATH_MAX = 4096
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/elf.h: 19
try:
    _SYS_ELF_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 19
try:
    _SYS_EPOLL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/epoll.h: 26
try:
    EPOLL_CLOEXEC = EPOLL_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 37
try:
    EPOLLIN = EPOLLIN
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 39
try:
    EPOLLPRI = EPOLLPRI
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 41
try:
    EPOLLOUT = EPOLLOUT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 43
try:
    EPOLLRDNORM = EPOLLRDNORM
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 45
try:
    EPOLLRDBAND = EPOLLRDBAND
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 47
try:
    EPOLLWRNORM = EPOLLWRNORM
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 49
try:
    EPOLLWRBAND = EPOLLWRBAND
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 51
try:
    EPOLLMSG = EPOLLMSG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 53
try:
    EPOLLERR = EPOLLERR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 55
try:
    EPOLLHUP = EPOLLHUP
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 57
try:
    EPOLLRDHUP = EPOLLRDHUP
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 59
try:
    EPOLLEXCLUSIVE = EPOLLEXCLUSIVE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 61
try:
    EPOLLWAKEUP = EPOLLWAKEUP
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 63
try:
    EPOLLONESHOT = EPOLLONESHOT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 65
try:
    EPOLLET = EPOLLET
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 70
try:
    EPOLL_CTL_ADD = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 71
try:
    EPOLL_CTL_DEL = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/epoll.h: 72
try:
    EPOLL_CTL_MOD = 3
except:
    pass

# /usr/include/errno.h: 23
try:
    _ERRNO_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/errno.h: 20
try:
    _BITS_ERRNO_H = 1
except:
    pass

# /usr/include/asm-generic/errno-base.h: 15
try:
    EAGAIN = 11
except:
    pass

# /usr/include/asm-generic/errno.h: 7
try:
    EDEADLK = 35
except:
    pass

# /usr/include/asm-generic/errno.h: 8
try:
    ENAMETOOLONG = 36
except:
    pass

# /usr/include/asm-generic/errno.h: 9
try:
    ENOLCK = 37
except:
    pass

# /usr/include/asm-generic/errno.h: 18
try:
    ENOSYS = 38
except:
    pass

# /usr/include/asm-generic/errno.h: 20
try:
    ENOTEMPTY = 39
except:
    pass

# /usr/include/asm-generic/errno.h: 21
try:
    ELOOP = 40
except:
    pass

# /usr/include/asm-generic/errno.h: 22
try:
    EWOULDBLOCK = EAGAIN
except:
    pass

# /usr/include/asm-generic/errno.h: 23
try:
    ENOMSG = 42
except:
    pass

# /usr/include/asm-generic/errno.h: 24
try:
    EIDRM = 43
except:
    pass

# /usr/include/asm-generic/errno.h: 25
try:
    ECHRNG = 44
except:
    pass

# /usr/include/asm-generic/errno.h: 26
try:
    EL2NSYNC = 45
except:
    pass

# /usr/include/asm-generic/errno.h: 27
try:
    EL3HLT = 46
except:
    pass

# /usr/include/asm-generic/errno.h: 28
try:
    EL3RST = 47
except:
    pass

# /usr/include/asm-generic/errno.h: 29
try:
    ELNRNG = 48
except:
    pass

# /usr/include/asm-generic/errno.h: 30
try:
    EUNATCH = 49
except:
    pass

# /usr/include/asm-generic/errno.h: 31
try:
    ENOCSI = 50
except:
    pass

# /usr/include/asm-generic/errno.h: 32
try:
    EL2HLT = 51
except:
    pass

# /usr/include/asm-generic/errno.h: 33
try:
    EBADE = 52
except:
    pass

# /usr/include/asm-generic/errno.h: 34
try:
    EBADR = 53
except:
    pass

# /usr/include/asm-generic/errno.h: 35
try:
    EXFULL = 54
except:
    pass

# /usr/include/asm-generic/errno.h: 36
try:
    ENOANO = 55
except:
    pass

# /usr/include/asm-generic/errno.h: 37
try:
    EBADRQC = 56
except:
    pass

# /usr/include/asm-generic/errno.h: 38
try:
    EBADSLT = 57
except:
    pass

# /usr/include/asm-generic/errno.h: 40
try:
    EDEADLOCK = EDEADLK
except:
    pass

# /usr/include/asm-generic/errno.h: 42
try:
    EBFONT = 59
except:
    pass

# /usr/include/asm-generic/errno.h: 43
try:
    ENOSTR = 60
except:
    pass

# /usr/include/asm-generic/errno.h: 44
try:
    ENODATA = 61
except:
    pass

# /usr/include/asm-generic/errno.h: 45
try:
    ETIME = 62
except:
    pass

# /usr/include/asm-generic/errno.h: 46
try:
    ENOSR = 63
except:
    pass

# /usr/include/asm-generic/errno.h: 47
try:
    ENONET = 64
except:
    pass

# /usr/include/asm-generic/errno.h: 48
try:
    ENOPKG = 65
except:
    pass

# /usr/include/asm-generic/errno.h: 49
try:
    EREMOTE = 66
except:
    pass

# /usr/include/asm-generic/errno.h: 50
try:
    ENOLINK = 67
except:
    pass

# /usr/include/asm-generic/errno.h: 51
try:
    EADV = 68
except:
    pass

# /usr/include/asm-generic/errno.h: 52
try:
    ESRMNT = 69
except:
    pass

# /usr/include/asm-generic/errno.h: 53
try:
    ECOMM = 70
except:
    pass

# /usr/include/asm-generic/errno.h: 54
try:
    EPROTO = 71
except:
    pass

# /usr/include/asm-generic/errno.h: 55
try:
    EMULTIHOP = 72
except:
    pass

# /usr/include/asm-generic/errno.h: 56
try:
    EDOTDOT = 73
except:
    pass

# /usr/include/asm-generic/errno.h: 57
try:
    EBADMSG = 74
except:
    pass

# /usr/include/asm-generic/errno.h: 58
try:
    EOVERFLOW = 75
except:
    pass

# /usr/include/asm-generic/errno.h: 59
try:
    ENOTUNIQ = 76
except:
    pass

# /usr/include/asm-generic/errno.h: 60
try:
    EBADFD = 77
except:
    pass

# /usr/include/asm-generic/errno.h: 61
try:
    EREMCHG = 78
except:
    pass

# /usr/include/asm-generic/errno.h: 62
try:
    ELIBACC = 79
except:
    pass

# /usr/include/asm-generic/errno.h: 63
try:
    ELIBBAD = 80
except:
    pass

# /usr/include/asm-generic/errno.h: 64
try:
    ELIBSCN = 81
except:
    pass

# /usr/include/asm-generic/errno.h: 65
try:
    ELIBMAX = 82
except:
    pass

# /usr/include/asm-generic/errno.h: 66
try:
    ELIBEXEC = 83
except:
    pass

# /usr/include/asm-generic/errno.h: 67
try:
    EILSEQ = 84
except:
    pass

# /usr/include/asm-generic/errno.h: 68
try:
    ERESTART = 85
except:
    pass

# /usr/include/asm-generic/errno.h: 69
try:
    ESTRPIPE = 86
except:
    pass

# /usr/include/asm-generic/errno.h: 70
try:
    EUSERS = 87
except:
    pass

# /usr/include/asm-generic/errno.h: 71
try:
    ENOTSOCK = 88
except:
    pass

# /usr/include/asm-generic/errno.h: 72
try:
    EDESTADDRREQ = 89
except:
    pass

# /usr/include/asm-generic/errno.h: 73
try:
    EMSGSIZE = 90
except:
    pass

# /usr/include/asm-generic/errno.h: 74
try:
    EPROTOTYPE = 91
except:
    pass

# /usr/include/asm-generic/errno.h: 75
try:
    ENOPROTOOPT = 92
except:
    pass

# /usr/include/asm-generic/errno.h: 76
try:
    EPROTONOSUPPORT = 93
except:
    pass

# /usr/include/asm-generic/errno.h: 77
try:
    ESOCKTNOSUPPORT = 94
except:
    pass

# /usr/include/asm-generic/errno.h: 78
try:
    EOPNOTSUPP = 95
except:
    pass

# /usr/include/asm-generic/errno.h: 79
try:
    EPFNOSUPPORT = 96
except:
    pass

# /usr/include/asm-generic/errno.h: 80
try:
    EAFNOSUPPORT = 97
except:
    pass

# /usr/include/asm-generic/errno.h: 81
try:
    EADDRINUSE = 98
except:
    pass

# /usr/include/asm-generic/errno.h: 82
try:
    EADDRNOTAVAIL = 99
except:
    pass

# /usr/include/asm-generic/errno.h: 83
try:
    ENETDOWN = 100
except:
    pass

# /usr/include/asm-generic/errno.h: 84
try:
    ENETUNREACH = 101
except:
    pass

# /usr/include/asm-generic/errno.h: 85
try:
    ENETRESET = 102
except:
    pass

# /usr/include/asm-generic/errno.h: 86
try:
    ECONNABORTED = 103
except:
    pass

# /usr/include/asm-generic/errno.h: 87
try:
    ECONNRESET = 104
except:
    pass

# /usr/include/asm-generic/errno.h: 88
try:
    ENOBUFS = 105
except:
    pass

# /usr/include/asm-generic/errno.h: 89
try:
    EISCONN = 106
except:
    pass

# /usr/include/asm-generic/errno.h: 90
try:
    ENOTCONN = 107
except:
    pass

# /usr/include/asm-generic/errno.h: 91
try:
    ESHUTDOWN = 108
except:
    pass

# /usr/include/asm-generic/errno.h: 92
try:
    ETOOMANYREFS = 109
except:
    pass

# /usr/include/asm-generic/errno.h: 93
try:
    ETIMEDOUT = 110
except:
    pass

# /usr/include/asm-generic/errno.h: 94
try:
    ECONNREFUSED = 111
except:
    pass

# /usr/include/asm-generic/errno.h: 95
try:
    EHOSTDOWN = 112
except:
    pass

# /usr/include/asm-generic/errno.h: 96
try:
    EHOSTUNREACH = 113
except:
    pass

# /usr/include/asm-generic/errno.h: 97
try:
    EALREADY = 114
except:
    pass

# /usr/include/asm-generic/errno.h: 98
try:
    EINPROGRESS = 115
except:
    pass

# /usr/include/asm-generic/errno.h: 99
try:
    ESTALE = 116
except:
    pass

# /usr/include/asm-generic/errno.h: 100
try:
    EUCLEAN = 117
except:
    pass

# /usr/include/asm-generic/errno.h: 101
try:
    ENOTNAM = 118
except:
    pass

# /usr/include/asm-generic/errno.h: 102
try:
    ENAVAIL = 119
except:
    pass

# /usr/include/asm-generic/errno.h: 103
try:
    EISNAM = 120
except:
    pass

# /usr/include/asm-generic/errno.h: 104
try:
    EREMOTEIO = 121
except:
    pass

# /usr/include/asm-generic/errno.h: 105
try:
    EDQUOT = 122
except:
    pass

# /usr/include/asm-generic/errno.h: 107
try:
    ENOMEDIUM = 123
except:
    pass

# /usr/include/asm-generic/errno.h: 108
try:
    EMEDIUMTYPE = 124
except:
    pass

# /usr/include/asm-generic/errno.h: 109
try:
    ECANCELED = 125
except:
    pass

# /usr/include/asm-generic/errno.h: 110
try:
    ENOKEY = 126
except:
    pass

# /usr/include/asm-generic/errno.h: 111
try:
    EKEYEXPIRED = 127
except:
    pass

# /usr/include/asm-generic/errno.h: 112
try:
    EKEYREVOKED = 128
except:
    pass

# /usr/include/asm-generic/errno.h: 113
try:
    EKEYREJECTED = 129
except:
    pass

# /usr/include/asm-generic/errno.h: 116
try:
    EOWNERDEAD = 130
except:
    pass

# /usr/include/asm-generic/errno.h: 117
try:
    ENOTRECOVERABLE = 131
except:
    pass

# /usr/include/asm-generic/errno.h: 119
try:
    ERFKILL = 132
except:
    pass

# /usr/include/asm-generic/errno.h: 121
try:
    EHWPOISON = 133
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/errno.h: 30
try:
    ENOTSUP = EOPNOTSUPP
except:
    pass

# /usr/include/errno.h: 38
try:
    errno = ((__errno_location ())[0])
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/eventfd.h: 19
try:
    _SYS_EVENTFD_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 26
try:
    EFD_SEMAPHORE = EFD_SEMAPHORE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 28
try:
    EFD_CLOEXEC = EFD_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/eventfd.h: 30
try:
    EFD_NONBLOCK = EFD_NONBLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/fanotify.h: 19
try:
    _SYS_FANOTIFY_H = 1
except:
    pass

# /usr/include/linux/posix_types.h: 22
# #undef __FD_SETSIZE
try:
    del __FD_SETSIZE
except NameError:
    pass

__aligned_u64 = __u64# /usr/include/linux/types.h: 43

__aligned_be64 = __be64# /usr/include/linux/types.h: 44

__aligned_le64 = __le64# /usr/include/linux/types.h: 45

# /usr/include/linux/fanotify.h: 8
try:
    FAN_ACCESS = 0x00000001
except:
    pass

# /usr/include/linux/fanotify.h: 9
try:
    FAN_MODIFY = 0x00000002
except:
    pass

# /usr/include/linux/fanotify.h: 10
try:
    FAN_ATTRIB = 0x00000004
except:
    pass

# /usr/include/linux/fanotify.h: 11
try:
    FAN_CLOSE_WRITE = 0x00000008
except:
    pass

# /usr/include/linux/fanotify.h: 12
try:
    FAN_CLOSE_NOWRITE = 0x00000010
except:
    pass

# /usr/include/linux/fanotify.h: 13
try:
    FAN_OPEN = 0x00000020
except:
    pass

# /usr/include/linux/fanotify.h: 14
try:
    FAN_MOVED_FROM = 0x00000040
except:
    pass

# /usr/include/linux/fanotify.h: 15
try:
    FAN_MOVED_TO = 0x00000080
except:
    pass

# /usr/include/linux/fanotify.h: 16
try:
    FAN_CREATE = 0x00000100
except:
    pass

# /usr/include/linux/fanotify.h: 17
try:
    FAN_DELETE = 0x00000200
except:
    pass

# /usr/include/linux/fanotify.h: 18
try:
    FAN_DELETE_SELF = 0x00000400
except:
    pass

# /usr/include/linux/fanotify.h: 19
try:
    FAN_MOVE_SELF = 0x00000800
except:
    pass

# /usr/include/linux/fanotify.h: 20
try:
    FAN_OPEN_EXEC = 0x00001000
except:
    pass

# /usr/include/linux/fanotify.h: 22
try:
    FAN_Q_OVERFLOW = 0x00004000
except:
    pass

# /usr/include/linux/fanotify.h: 24
try:
    FAN_OPEN_PERM = 0x00010000
except:
    pass

# /usr/include/linux/fanotify.h: 25
try:
    FAN_ACCESS_PERM = 0x00020000
except:
    pass

# /usr/include/linux/fanotify.h: 26
try:
    FAN_OPEN_EXEC_PERM = 0x00040000
except:
    pass

# /usr/include/linux/fanotify.h: 28
try:
    FAN_ONDIR = 0x40000000
except:
    pass

# /usr/include/linux/fanotify.h: 30
try:
    FAN_EVENT_ON_CHILD = 0x08000000
except:
    pass

# /usr/include/linux/fanotify.h: 33
try:
    FAN_CLOSE = (FAN_CLOSE_WRITE | FAN_CLOSE_NOWRITE)
except:
    pass

# /usr/include/linux/fanotify.h: 34
try:
    FAN_MOVE = (FAN_MOVED_FROM | FAN_MOVED_TO)
except:
    pass

# /usr/include/linux/fanotify.h: 37
try:
    FAN_CLOEXEC = 0x00000001
except:
    pass

# /usr/include/linux/fanotify.h: 38
try:
    FAN_NONBLOCK = 0x00000002
except:
    pass

# /usr/include/linux/fanotify.h: 41
try:
    FAN_CLASS_NOTIF = 0x00000000
except:
    pass

# /usr/include/linux/fanotify.h: 42
try:
    FAN_CLASS_CONTENT = 0x00000004
except:
    pass

# /usr/include/linux/fanotify.h: 43
try:
    FAN_CLASS_PRE_CONTENT = 0x00000008
except:
    pass

# /usr/include/linux/fanotify.h: 46
try:
    FAN_ALL_CLASS_BITS = ((FAN_CLASS_NOTIF | FAN_CLASS_CONTENT) | FAN_CLASS_PRE_CONTENT)
except:
    pass

# /usr/include/linux/fanotify.h: 49
try:
    FAN_UNLIMITED_QUEUE = 0x00000010
except:
    pass

# /usr/include/linux/fanotify.h: 50
try:
    FAN_UNLIMITED_MARKS = 0x00000020
except:
    pass

# /usr/include/linux/fanotify.h: 51
try:
    FAN_ENABLE_AUDIT = 0x00000040
except:
    pass

# /usr/include/linux/fanotify.h: 54
try:
    FAN_REPORT_TID = 0x00000100
except:
    pass

# /usr/include/linux/fanotify.h: 55
try:
    FAN_REPORT_FID = 0x00000200
except:
    pass

# /usr/include/linux/fanotify.h: 58
try:
    FAN_ALL_INIT_FLAGS = ((((FAN_CLOEXEC | FAN_NONBLOCK) | FAN_ALL_CLASS_BITS) | FAN_UNLIMITED_QUEUE) | FAN_UNLIMITED_MARKS)
except:
    pass

# /usr/include/linux/fanotify.h: 63
try:
    FAN_MARK_ADD = 0x00000001
except:
    pass

# /usr/include/linux/fanotify.h: 64
try:
    FAN_MARK_REMOVE = 0x00000002
except:
    pass

# /usr/include/linux/fanotify.h: 65
try:
    FAN_MARK_DONT_FOLLOW = 0x00000004
except:
    pass

# /usr/include/linux/fanotify.h: 66
try:
    FAN_MARK_ONLYDIR = 0x00000008
except:
    pass

# /usr/include/linux/fanotify.h: 68
try:
    FAN_MARK_IGNORED_MASK = 0x00000020
except:
    pass

# /usr/include/linux/fanotify.h: 69
try:
    FAN_MARK_IGNORED_SURV_MODIFY = 0x00000040
except:
    pass

# /usr/include/linux/fanotify.h: 70
try:
    FAN_MARK_FLUSH = 0x00000080
except:
    pass

# /usr/include/linux/fanotify.h: 74
try:
    FAN_MARK_INODE = 0x00000000
except:
    pass

# /usr/include/linux/fanotify.h: 75
try:
    FAN_MARK_MOUNT = 0x00000010
except:
    pass

# /usr/include/linux/fanotify.h: 76
try:
    FAN_MARK_FILESYSTEM = 0x00000100
except:
    pass

# /usr/include/linux/fanotify.h: 79
try:
    FAN_ALL_MARK_FLAGS = (((((((FAN_MARK_ADD | FAN_MARK_REMOVE) | FAN_MARK_DONT_FOLLOW) | FAN_MARK_ONLYDIR) | FAN_MARK_MOUNT) | FAN_MARK_IGNORED_MASK) | FAN_MARK_IGNORED_SURV_MODIFY) | FAN_MARK_FLUSH)
except:
    pass

# /usr/include/linux/fanotify.h: 89
try:
    FAN_ALL_EVENTS = (((FAN_ACCESS | FAN_MODIFY) | FAN_CLOSE) | FAN_OPEN)
except:
    pass

# /usr/include/linux/fanotify.h: 98
try:
    FAN_ALL_PERM_EVENTS = (FAN_OPEN_PERM | FAN_ACCESS_PERM)
except:
    pass

# /usr/include/linux/fanotify.h: 102
try:
    FAN_ALL_OUTGOING_EVENTS = ((FAN_ALL_EVENTS | FAN_ALL_PERM_EVENTS) | FAN_Q_OVERFLOW)
except:
    pass

# /usr/include/linux/fanotify.h: 106
try:
    FANOTIFY_METADATA_VERSION = 3
except:
    pass

# /usr/include/linux/fanotify.h: 118
try:
    FAN_EVENT_INFO_TYPE_FID = 1
except:
    pass

# /usr/include/linux/fanotify.h: 144
try:
    FAN_ALLOW = 0x01
except:
    pass

# /usr/include/linux/fanotify.h: 145
try:
    FAN_DENY = 0x02
except:
    pass

# /usr/include/linux/fanotify.h: 146
try:
    FAN_AUDIT = 0x10
except:
    pass

# /usr/include/linux/fanotify.h: 149
try:
    FAN_NOFD = (-1)
except:
    pass

# /usr/include/linux/fanotify.h: 152
class struct_fanotify_event_metadata(Structure):
    pass

# /usr/include/linux/fanotify.h: 152
try:
    FAN_EVENT_METADATA_LEN = sizeof(struct_fanotify_event_metadata)
except:
    pass

# /usr/include/linux/fanotify.h: 154
def FAN_EVENT_NEXT(meta, len):
    return (len - (meta.contents.event_len))

# /usr/include/linux/fanotify.h: 158
def FAN_EVENT_OK(meta, len):
    return ((((c_long (ord_if_char(len))).value >= (c_long (ord_if_char(FAN_EVENT_METADATA_LEN))).value) and ((c_long (ord_if_char(((meta.contents.event_len).value)))).value >= (c_long (ord_if_char(FAN_EVENT_METADATA_LEN))).value)) and ((c_long (ord_if_char(((meta.contents.event_len).value)))).value <= (c_long (ord_if_char(len))).value))

# /usr/include/fcntl.h: 23
try:
    _FCNTL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 24
try:
    __O_LARGEFILE = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 29
try:
    F_GETLK64 = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 30
try:
    F_SETLK64 = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 31
try:
    F_SETLKW64 = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl-linux.h: 47
try:
    O_CREAT = 0o100
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl-linux.h: 79
try:
    __O_DIRECTORY = 0o200000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/fcntl-linux.h: 100
try:
    __O_TMPFILE = (0o20000000 | __O_DIRECTORY)
except:
    pass

# /usr/include/fcntl.h: 40
def __OPEN_NEEDS_MODE(oflag):
    return (((oflag & O_CREAT) != 0) or ((oflag & __O_TMPFILE) == __O_TMPFILE))

# /usr/include/x86_64-linux-gnu/bits/stat.h: 23
try:
    _BITS_STAT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 37
try:
    _STAT_VER_KERNEL = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 38
try:
    _STAT_VER_LINUX = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 41
try:
    _MKNOD_VER_LINUX = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 44
try:
    _STAT_VER = _STAT_VER_LINUX
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 179
try:
    __S_IFMT = 0o170000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 182
try:
    __S_IFDIR = 0o040000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 183
try:
    __S_IFCHR = 0o020000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 184
try:
    __S_IFBLK = 0o060000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 185
try:
    __S_IFREG = 0o100000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 186
try:
    __S_IFIFO = 0o010000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 187
try:
    __S_IFLNK = 0o120000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 188
try:
    __S_IFSOCK = 0o140000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 192
def __S_TYPEISMQ(buf):
    return (((buf.contents.st_mode).value) - ((buf.contents.st_mode).value))

# /usr/include/x86_64-linux-gnu/bits/stat.h: 193
def __S_TYPEISSEM(buf):
    return (((buf.contents.st_mode).value) - ((buf.contents.st_mode).value))

# /usr/include/x86_64-linux-gnu/bits/stat.h: 194
def __S_TYPEISSHM(buf):
    return (((buf.contents.st_mode).value) - ((buf.contents.st_mode).value))

# /usr/include/x86_64-linux-gnu/bits/stat.h: 198
try:
    __S_ISUID = 0o4000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 199
try:
    __S_ISGID = 0o2000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 200
try:
    __S_ISVTX = 0o1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 201
try:
    __S_IREAD = 0o400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 202
try:
    __S_IWRITE = 0o200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 203
try:
    __S_IEXEC = 0o100
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 206
try:
    UTIME_NOW = ((1 << 30) - 1)
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stat.h: 207
try:
    UTIME_OMIT = ((1 << 30) - 2)
except:
    pass

# /usr/include/fcntl.h: 80
try:
    S_IFMT = __S_IFMT
except:
    pass

# /usr/include/fcntl.h: 81
try:
    S_IFDIR = __S_IFDIR
except:
    pass

# /usr/include/fcntl.h: 82
try:
    S_IFCHR = __S_IFCHR
except:
    pass

# /usr/include/fcntl.h: 83
try:
    S_IFBLK = __S_IFBLK
except:
    pass

# /usr/include/fcntl.h: 84
try:
    S_IFREG = __S_IFREG
except:
    pass

# /usr/include/fcntl.h: 86
try:
    S_IFIFO = __S_IFIFO
except:
    pass

# /usr/include/fcntl.h: 89
try:
    S_IFLNK = __S_IFLNK
except:
    pass

# /usr/include/fcntl.h: 92
try:
    S_IFSOCK = __S_IFSOCK
except:
    pass

# /usr/include/fcntl.h: 97
try:
    S_ISUID = __S_ISUID
except:
    pass

# /usr/include/fcntl.h: 98
try:
    S_ISGID = __S_ISGID
except:
    pass

# /usr/include/fcntl.h: 102
try:
    S_ISVTX = __S_ISVTX
except:
    pass

# /usr/include/fcntl.h: 105
try:
    S_IRUSR = __S_IREAD
except:
    pass

# /usr/include/fcntl.h: 106
try:
    S_IWUSR = __S_IWRITE
except:
    pass

# /usr/include/fcntl.h: 107
try:
    S_IXUSR = __S_IEXEC
except:
    pass

# /usr/include/fcntl.h: 109
try:
    S_IRWXU = ((__S_IREAD | __S_IWRITE) | __S_IEXEC)
except:
    pass

# /usr/include/fcntl.h: 111
try:
    S_IRGRP = (S_IRUSR >> 3)
except:
    pass

# /usr/include/fcntl.h: 112
try:
    S_IWGRP = (S_IWUSR >> 3)
except:
    pass

# /usr/include/fcntl.h: 113
try:
    S_IXGRP = (S_IXUSR >> 3)
except:
    pass

# /usr/include/fcntl.h: 115
try:
    S_IRWXG = (S_IRWXU >> 3)
except:
    pass

# /usr/include/fcntl.h: 117
try:
    S_IROTH = (S_IRGRP >> 3)
except:
    pass

# /usr/include/fcntl.h: 118
try:
    S_IWOTH = (S_IWGRP >> 3)
except:
    pass

# /usr/include/fcntl.h: 119
try:
    S_IXOTH = (S_IXGRP >> 3)
except:
    pass

# /usr/include/fcntl.h: 121
try:
    S_IRWXO = (S_IRWXG >> 3)
except:
    pass

# /usr/include/fcntl.h: 128
try:
    R_OK = 4
except:
    pass

# /usr/include/fcntl.h: 129
try:
    W_OK = 2
except:
    pass

# /usr/include/fcntl.h: 130
try:
    X_OK = 1
except:
    pass

# /usr/include/fcntl.h: 131
try:
    F_OK = 0
except:
    pass

# /usr/include/fcntl.h: 137
try:
    SEEK_SET = 0
except:
    pass

# /usr/include/fcntl.h: 138
try:
    SEEK_CUR = 1
except:
    pass

# /usr/include/fcntl.h: 139
try:
    SEEK_END = 2
except:
    pass

# /usr/include/fcntl.h: 237
try:
    F_ULOCK = 0
except:
    pass

# /usr/include/fcntl.h: 238
try:
    F_LOCK = 1
except:
    pass

# /usr/include/fcntl.h: 239
try:
    F_TLOCK = 2
except:
    pass

# /usr/include/fcntl.h: 240
try:
    F_TEST = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 19
try:
    _SYS_FILE_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 33
try:
    L_SET = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 34
try:
    L_INCR = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 35
try:
    L_XTND = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 40
try:
    LOCK_SH = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 41
try:
    LOCK_EX = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 42
try:
    LOCK_UN = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/file.h: 45
try:
    LOCK_NB = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/fsuid.h: 19
try:
    _SYS_FSUID_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 33
try:
    _SYS_GMON_H = 1
except:
    pass

HISTCOUNTER = c_ushort# /usr/include/x86_64-linux-gnu/sys/gmon.h: 61

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 66
try:
    HISTFRACTION = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 96
try:
    HASHFRACTION = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 108
try:
    ARCDENSITY = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 115
try:
    MINARCS = 50
except:
    pass

ARCINDEX = c_ulong# /usr/include/x86_64-linux-gnu/sys/gmon.h: 120

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 130
try:
    MAXARCS = (1 << 20)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 151
def ROUNDDOWN(x, y):
    return ((x / y) * y)

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 152
def ROUNDUP(x, y):
    return ((((x + y) - 1) / y) * y)

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 176
try:
    GMON_PROF_ON = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 177
try:
    GMON_PROF_BUSY = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 178
try:
    GMON_PROF_ERROR = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 179
try:
    GMON_PROF_OFF = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 184
try:
    GPROF_STATE = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 185
try:
    GPROF_COUNT = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 186
try:
    GPROF_FROMS = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 187
try:
    GPROF_TOS = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon.h: 188
try:
    GPROF_GMONPARAM = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 28
try:
    _SYS_GMON_OUT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 32
try:
    GMON_MAGIC = 'gmon'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 33
try:
    GMON_VERSION = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 36
try:
    GMON_SHOBJ_VERSION = 0x1ffff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 19
try:
    _SYS_INOTIFY_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/inotify.h: 26
try:
    IN_CLOEXEC = IN_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/inotify.h: 28
try:
    IN_NONBLOCK = IN_NONBLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 39
try:
    IN_ACCESS = 0x00000001
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 40
try:
    IN_MODIFY = 0x00000002
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 41
try:
    IN_ATTRIB = 0x00000004
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 42
try:
    IN_CLOSE_WRITE = 0x00000008
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 43
try:
    IN_CLOSE_NOWRITE = 0x00000010
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 44
try:
    IN_CLOSE = (IN_CLOSE_WRITE | IN_CLOSE_NOWRITE)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 45
try:
    IN_OPEN = 0x00000020
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 46
try:
    IN_MOVED_FROM = 0x00000040
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 47
try:
    IN_MOVED_TO = 0x00000080
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 48
try:
    IN_MOVE = (IN_MOVED_FROM | IN_MOVED_TO)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 49
try:
    IN_CREATE = 0x00000100
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 50
try:
    IN_DELETE = 0x00000200
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 51
try:
    IN_DELETE_SELF = 0x00000400
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 52
try:
    IN_MOVE_SELF = 0x00000800
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 55
try:
    IN_UNMOUNT = 0x00002000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 56
try:
    IN_Q_OVERFLOW = 0x00004000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 57
try:
    IN_IGNORED = 0x00008000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 60
try:
    IN_CLOSE = (IN_CLOSE_WRITE | IN_CLOSE_NOWRITE)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 61
try:
    IN_MOVE = (IN_MOVED_FROM | IN_MOVED_TO)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 64
try:
    IN_ONLYDIR = 0x01000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 66
try:
    IN_DONT_FOLLOW = 0x02000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 67
try:
    IN_EXCL_UNLINK = 0x04000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 69
try:
    IN_MASK_CREATE = 0x10000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 70
try:
    IN_MASK_ADD = 0x20000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 72
try:
    IN_ISDIR = 0x40000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 73
try:
    IN_ONESHOT = 0x80000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/inotify.h: 76
try:
    IN_ALL_EVENTS = (((((((((((IN_ACCESS | IN_MODIFY) | IN_ATTRIB) | IN_CLOSE_WRITE) | IN_CLOSE_NOWRITE) | IN_OPEN) | IN_MOVED_FROM) | IN_MOVED_TO) | IN_CREATE) | IN_DELETE) | IN_DELETE_SELF) | IN_MOVE_SELF)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/io.h: 19
try:
    _SYS_IO_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ioctl.h: 19
try:
    _SYS_IOCTL_H = 1
except:
    pass

# /usr/include/asm-generic/ioctl.h: 23
try:
    _IOC_NRBITS = 8
except:
    pass

# /usr/include/asm-generic/ioctl.h: 24
try:
    _IOC_TYPEBITS = 8
except:
    pass

# /usr/include/asm-generic/ioctl.h: 32
try:
    _IOC_SIZEBITS = 14
except:
    pass

# /usr/include/asm-generic/ioctl.h: 36
try:
    _IOC_DIRBITS = 2
except:
    pass

# /usr/include/asm-generic/ioctl.h: 39
try:
    _IOC_NRMASK = ((1 << _IOC_NRBITS) - 1)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 40
try:
    _IOC_TYPEMASK = ((1 << _IOC_TYPEBITS) - 1)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 41
try:
    _IOC_SIZEMASK = ((1 << _IOC_SIZEBITS) - 1)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 42
try:
    _IOC_DIRMASK = ((1 << _IOC_DIRBITS) - 1)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 44
try:
    _IOC_NRSHIFT = 0
except:
    pass

# /usr/include/asm-generic/ioctl.h: 45
try:
    _IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 46
try:
    _IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 47
try:
    _IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 58
try:
    _IOC_NONE = 0
except:
    pass

# /usr/include/asm-generic/ioctl.h: 62
try:
    _IOC_WRITE = 1
except:
    pass

# /usr/include/asm-generic/ioctl.h: 66
try:
    _IOC_READ = 2
except:
    pass

# /usr/include/asm-generic/ioctl.h: 69
def _IOC(dir, type, nr, size):
    return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))

# /usr/include/asm-generic/ioctl.h: 75
def _IOC_TYPECHECK(t):
    return sizeof(t)

# /usr/include/asm-generic/ioctl.h: 83
def _IO(type, nr):
    return (_IOC (_IOC_NONE, type, nr, 0))

# /usr/include/asm-generic/ioctl.h: 84
def _IOR(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, (_IOC_TYPECHECK (size))))

# /usr/include/asm-generic/ioctl.h: 85
def _IOW(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, (_IOC_TYPECHECK (size))))

# /usr/include/asm-generic/ioctl.h: 86
def _IOWR(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, (_IOC_TYPECHECK (size))))

# /usr/include/asm-generic/ioctl.h: 87
def _IOR_BAD(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, sizeof(size)))

# /usr/include/asm-generic/ioctl.h: 88
def _IOW_BAD(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, sizeof(size)))

# /usr/include/asm-generic/ioctl.h: 89
def _IOWR_BAD(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, sizeof(size)))

# /usr/include/asm-generic/ioctl.h: 92
def _IOC_DIR(nr):
    return ((nr >> _IOC_DIRSHIFT) & _IOC_DIRMASK)

# /usr/include/asm-generic/ioctl.h: 93
def _IOC_TYPE(nr):
    return ((nr >> _IOC_TYPESHIFT) & _IOC_TYPEMASK)

# /usr/include/asm-generic/ioctl.h: 94
def _IOC_NR(nr):
    return ((nr >> _IOC_NRSHIFT) & _IOC_NRMASK)

# /usr/include/asm-generic/ioctl.h: 95
def _IOC_SIZE(nr):
    return ((nr >> _IOC_SIZESHIFT) & _IOC_SIZEMASK)

# /usr/include/asm-generic/ioctl.h: 99
try:
    IOC_IN = (_IOC_WRITE << _IOC_DIRSHIFT)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 100
try:
    IOC_OUT = (_IOC_READ << _IOC_DIRSHIFT)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 101
try:
    IOC_INOUT = ((_IOC_WRITE | _IOC_READ) << _IOC_DIRSHIFT)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 102
try:
    IOCSIZE_MASK = (_IOC_SIZEMASK << _IOC_SIZESHIFT)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 103
try:
    IOCSIZE_SHIFT = _IOC_SIZESHIFT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 46
try:
    TTYDEF_IFLAG = (((((BRKINT | ISTRIP) | ICRNL) | IMAXBEL) | IXON) | IXANY)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 47
try:
    TTYDEF_OFLAG = ((OPOST | ONLCR) | XTABS)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 48
try:
    TTYDEF_LFLAG = ((((((ECHO | ICANON) | ISIG) | IEXTEN) | ECHOE) | ECHOKE) | ECHOCTL)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 49
try:
    TTYDEF_CFLAG = (((CREAD | CS7) | PARENB) | HUPCL)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 50
try:
    TTYDEF_SPEED = B9600
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 55
def CTRL(x):
    return (x & 0o37)

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 56
try:
    CEOF = (CTRL ('d'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 60
try:
    CEOL = '\\0'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 62
try:
    CERASE = 0o177
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 63
try:
    CINTR = (CTRL ('c'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 67
try:
    CSTATUS = '\\0'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 69
try:
    CKILL = (CTRL ('u'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 70
try:
    CMIN = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 71
try:
    CQUIT = 0o34
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 72
try:
    CSUSP = (CTRL ('z'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 73
try:
    CTIME = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 74
try:
    CDSUSP = (CTRL ('y'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 75
try:
    CSTART = (CTRL ('q'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 76
try:
    CSTOP = (CTRL ('s'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 77
try:
    CLNEXT = (CTRL ('v'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 78
try:
    CDISCARD = (CTRL ('o'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 79
try:
    CWERASE = (CTRL ('w'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 80
try:
    CREPRINT = (CTRL ('r'))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 81
try:
    CEOT = CEOF
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 83
try:
    CBRK = CEOL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 84
try:
    CRPRNT = CREPRINT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttydefaults.h: 85
try:
    CFLUSH = CDISCARD
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ipc.h: 19
try:
    _SYS_IPC_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 25
try:
    IPC_CREAT = 0o1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 26
try:
    IPC_EXCL = 0o2000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 27
try:
    IPC_NOWAIT = 0o4000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 30
try:
    IPC_RMID = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 31
try:
    IPC_SET = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 32
try:
    IPC_STAT = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/ipc.h: 38
try:
    IPC_PRIVATE = (__key_t (ord_if_char(0))).value
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/kd.h: 19
try:
    _SYS_KD_H = 1
except:
    pass

# /usr/include/linux/kd.h: 9
try:
    GIO_FONT = 0x4B60
except:
    pass

# /usr/include/linux/kd.h: 10
try:
    PIO_FONT = 0x4B61
except:
    pass

# /usr/include/linux/kd.h: 12
try:
    GIO_FONTX = 0x4B6B
except:
    pass

# /usr/include/linux/kd.h: 13
try:
    PIO_FONTX = 0x4B6C
except:
    pass

# /usr/include/linux/kd.h: 20
try:
    PIO_FONTRESET = 0x4B6D
except:
    pass

# /usr/include/linux/kd.h: 22
try:
    GIO_CMAP = 0x4B70
except:
    pass

# /usr/include/linux/kd.h: 23
try:
    PIO_CMAP = 0x4B71
except:
    pass

# /usr/include/linux/kd.h: 25
try:
    KIOCSOUND = 0x4B2F
except:
    pass

# /usr/include/linux/kd.h: 26
try:
    KDMKTONE = 0x4B30
except:
    pass

# /usr/include/linux/kd.h: 28
try:
    KDGETLED = 0x4B31
except:
    pass

# /usr/include/linux/kd.h: 29
try:
    KDSETLED = 0x4B32
except:
    pass

# /usr/include/linux/kd.h: 30
try:
    LED_SCR = 0x01
except:
    pass

# /usr/include/linux/kd.h: 31
try:
    LED_NUM = 0x02
except:
    pass

# /usr/include/linux/kd.h: 32
try:
    LED_CAP = 0x04
except:
    pass

# /usr/include/linux/kd.h: 34
try:
    KDGKBTYPE = 0x4B33
except:
    pass

# /usr/include/linux/kd.h: 35
try:
    KB_84 = 0x01
except:
    pass

# /usr/include/linux/kd.h: 36
try:
    KB_101 = 0x02
except:
    pass

# /usr/include/linux/kd.h: 37
try:
    KB_OTHER = 0x03
except:
    pass

# /usr/include/linux/kd.h: 39
try:
    KDADDIO = 0x4B34
except:
    pass

# /usr/include/linux/kd.h: 40
try:
    KDDELIO = 0x4B35
except:
    pass

# /usr/include/linux/kd.h: 41
try:
    KDENABIO = 0x4B36
except:
    pass

# /usr/include/linux/kd.h: 42
try:
    KDDISABIO = 0x4B37
except:
    pass

# /usr/include/linux/kd.h: 44
try:
    KDSETMODE = 0x4B3A
except:
    pass

# /usr/include/linux/kd.h: 45
try:
    KD_TEXT = 0x00
except:
    pass

# /usr/include/linux/kd.h: 46
try:
    KD_GRAPHICS = 0x01
except:
    pass

# /usr/include/linux/kd.h: 47
try:
    KD_TEXT0 = 0x02
except:
    pass

# /usr/include/linux/kd.h: 48
try:
    KD_TEXT1 = 0x03
except:
    pass

# /usr/include/linux/kd.h: 49
try:
    KD_TRANSPARENT = 0x04
except:
    pass

# /usr/include/linux/kd.h: 51
try:
    KDGETMODE = 0x4B3B
except:
    pass

# /usr/include/linux/kd.h: 53
try:
    KDMAPDISP = 0x4B3C
except:
    pass

# /usr/include/linux/kd.h: 54
try:
    KDUNMAPDISP = 0x4B3D
except:
    pass

# /usr/include/linux/kd.h: 57
try:
    E_TABSZ = 256
except:
    pass

# /usr/include/linux/kd.h: 58
try:
    GIO_SCRNMAP = 0x4B40
except:
    pass

# /usr/include/linux/kd.h: 59
try:
    PIO_SCRNMAP = 0x4B41
except:
    pass

# /usr/include/linux/kd.h: 60
try:
    GIO_UNISCRNMAP = 0x4B69
except:
    pass

# /usr/include/linux/kd.h: 61
try:
    PIO_UNISCRNMAP = 0x4B6A
except:
    pass

# /usr/include/linux/kd.h: 63
try:
    GIO_UNIMAP = 0x4B66
except:
    pass

# /usr/include/linux/kd.h: 72
try:
    PIO_UNIMAP = 0x4B67
except:
    pass

# /usr/include/linux/kd.h: 73
try:
    PIO_UNIMAPCLR = 0x4B68
except:
    pass

# /usr/include/linux/kd.h: 80
try:
    UNI_DIRECT_BASE = 0xF000
except:
    pass

# /usr/include/linux/kd.h: 81
try:
    UNI_DIRECT_MASK = 0x01FF
except:
    pass

# /usr/include/linux/kd.h: 83
try:
    K_RAW = 0x00
except:
    pass

# /usr/include/linux/kd.h: 84
try:
    K_XLATE = 0x01
except:
    pass

# /usr/include/linux/kd.h: 85
try:
    K_MEDIUMRAW = 0x02
except:
    pass

# /usr/include/linux/kd.h: 86
try:
    K_UNICODE = 0x03
except:
    pass

# /usr/include/linux/kd.h: 87
try:
    K_OFF = 0x04
except:
    pass

# /usr/include/linux/kd.h: 88
try:
    KDGKBMODE = 0x4B44
except:
    pass

# /usr/include/linux/kd.h: 89
try:
    KDSKBMODE = 0x4B45
except:
    pass

# /usr/include/linux/kd.h: 91
try:
    K_METABIT = 0x03
except:
    pass

# /usr/include/linux/kd.h: 92
try:
    K_ESCPREFIX = 0x04
except:
    pass

# /usr/include/linux/kd.h: 93
try:
    KDGKBMETA = 0x4B62
except:
    pass

# /usr/include/linux/kd.h: 94
try:
    KDSKBMETA = 0x4B63
except:
    pass

# /usr/include/linux/kd.h: 96
try:
    K_SCROLLLOCK = 0x01
except:
    pass

# /usr/include/linux/kd.h: 97
try:
    K_NUMLOCK = 0x02
except:
    pass

# /usr/include/linux/kd.h: 98
try:
    K_CAPSLOCK = 0x04
except:
    pass

# /usr/include/linux/kd.h: 99
try:
    KDGKBLED = 0x4B64
except:
    pass

# /usr/include/linux/kd.h: 100
try:
    KDSKBLED = 0x4B65
except:
    pass

# /usr/include/linux/kd.h: 107
try:
    K_NORMTAB = 0x00
except:
    pass

# /usr/include/linux/kd.h: 108
try:
    K_SHIFTTAB = 0x01
except:
    pass

# /usr/include/linux/kd.h: 109
try:
    K_ALTTAB = 0x02
except:
    pass

# /usr/include/linux/kd.h: 110
try:
    K_ALTSHIFTTAB = 0x03
except:
    pass

# /usr/include/linux/kd.h: 112
try:
    KDGKBENT = 0x4B46
except:
    pass

# /usr/include/linux/kd.h: 113
try:
    KDSKBENT = 0x4B47
except:
    pass

# /usr/include/linux/kd.h: 119
try:
    KDGKBSENT = 0x4B48
except:
    pass

# /usr/include/linux/kd.h: 120
try:
    KDSKBSENT = 0x4B49
except:
    pass

# /usr/include/linux/kd.h: 129
try:
    KDGKBDIACR = 0x4B4A
except:
    pass

# /usr/include/linux/kd.h: 130
try:
    KDSKBDIACR = 0x4B4B
except:
    pass

# /usr/include/linux/kd.h: 139
try:
    KDGKBDIACRUC = 0x4BFA
except:
    pass

# /usr/include/linux/kd.h: 140
try:
    KDSKBDIACRUC = 0x4BFB
except:
    pass

# /usr/include/linux/kd.h: 145
try:
    KDGETKEYCODE = 0x4B4C
except:
    pass

# /usr/include/linux/kd.h: 146
try:
    KDSETKEYCODE = 0x4B4D
except:
    pass

# /usr/include/linux/kd.h: 148
try:
    KDSIGACCEPT = 0x4B4E
except:
    pass

# /usr/include/linux/kd.h: 156
try:
    KDKBDREP = 0x4B52
except:
    pass

# /usr/include/linux/kd.h: 159
try:
    KDFONTOP = 0x4B72
except:
    pass

# /usr/include/linux/kd.h: 175
try:
    KD_FONT_OP_SET = 0
except:
    pass

# /usr/include/linux/kd.h: 176
try:
    KD_FONT_OP_GET = 1
except:
    pass

# /usr/include/linux/kd.h: 177
try:
    KD_FONT_OP_SET_DEFAULT = 2
except:
    pass

# /usr/include/linux/kd.h: 178
try:
    KD_FONT_OP_COPY = 3
except:
    pass

# /usr/include/linux/kd.h: 180
try:
    KD_FONT_FLAG_DONT_RECALC = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/klog.h: 20
try:
    _SYS_KLOG_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mman.h: 20
try:
    _SYS_MMAN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/mman.h: 28
try:
    MAP_32BIT = 0x40
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mman.h: 44
try:
    MAP_FAILED = cast((-1), POINTER(None))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 22
try:
    _SYS_MOUNT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 27
try:
    BLOCK_SIZE = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 28
try:
    BLOCK_SIZE_BITS = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 36
try:
    MS_RDONLY = MS_RDONLY
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 38
try:
    MS_NOSUID = MS_NOSUID
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 40
try:
    MS_NODEV = MS_NODEV
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 42
try:
    MS_NOEXEC = MS_NOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 44
try:
    MS_SYNCHRONOUS = MS_SYNCHRONOUS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 46
try:
    MS_REMOUNT = MS_REMOUNT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 48
try:
    MS_MANDLOCK = MS_MANDLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 50
try:
    MS_DIRSYNC = MS_DIRSYNC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 52
try:
    MS_NOATIME = MS_NOATIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 54
try:
    MS_NODIRATIME = MS_NODIRATIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 56
try:
    MS_BIND = MS_BIND
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 58
try:
    MS_MOVE = MS_MOVE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 60
try:
    MS_REC = MS_REC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 62
try:
    MS_SILENT = MS_SILENT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 64
try:
    MS_POSIXACL = MS_POSIXACL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 66
try:
    MS_UNBINDABLE = MS_UNBINDABLE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 68
try:
    MS_PRIVATE = MS_PRIVATE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 70
try:
    MS_SLAVE = MS_SLAVE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 72
try:
    MS_SHARED = MS_SHARED
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 74
try:
    MS_RELATIME = MS_RELATIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 76
try:
    MS_KERNMOUNT = MS_KERNMOUNT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 78
try:
    MS_I_VERSION = MS_I_VERSION
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 80
try:
    MS_STRICTATIME = MS_STRICTATIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 82
try:
    MS_LAZYTIME = MS_LAZYTIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 84
try:
    MS_ACTIVE = MS_ACTIVE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 86
try:
    MS_NOUSER = MS_NOUSER
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 90
try:
    MS_RMT_MASK = ((((MS_RDONLY | MS_SYNCHRONOUS) | MS_MANDLOCK) | MS_I_VERSION) | MS_LAZYTIME)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 96
try:
    MS_MGC_VAL = 0xc0ed0000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 97
try:
    MS_MGC_MSK = 0xffff0000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 104
try:
    BLKROSET = (_IO (0x12, 93))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 105
try:
    BLKROGET = (_IO (0x12, 94))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 106
try:
    BLKRRPART = (_IO (0x12, 95))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 107
try:
    BLKGETSIZE = (_IO (0x12, 96))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 108
try:
    BLKFLSBUF = (_IO (0x12, 97))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 109
try:
    BLKRASET = (_IO (0x12, 98))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 110
try:
    BLKRAGET = (_IO (0x12, 99))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 111
try:
    BLKFRASET = (_IO (0x12, 100))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 112
try:
    BLKFRAGET = (_IO (0x12, 101))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 113
try:
    BLKSECTSET = (_IO (0x12, 102))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 114
try:
    BLKSECTGET = (_IO (0x12, 103))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 115
try:
    BLKSSZGET = (_IO (0x12, 104))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 116
try:
    BLKBSZGET = (_IOR (0x12, 112, c_size_t))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 117
try:
    BLKBSZSET = (_IOW (0x12, 113, c_size_t))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 118
try:
    BLKGETSIZE64 = (_IOR (0x12, 114, c_size_t))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 125
try:
    MNT_FORCE = MNT_FORCE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 127
try:
    MNT_DETACH = MNT_DETACH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 129
try:
    MNT_EXPIRE = MNT_EXPIRE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mount.h: 131
try:
    UMOUNT_NOFOLLOW = UMOUNT_NOFOLLOW
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 22
try:
    _SYS_MTIO_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 39
try:
    MTRESET = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 40
try:
    MTFSF = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 42
try:
    MTBSF = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 43
try:
    MTFSR = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 44
try:
    MTBSR = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 45
try:
    MTWEOF = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 46
try:
    MTREW = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 47
try:
    MTOFFL = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 48
try:
    MTNOP = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 49
try:
    MTRETEN = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 50
try:
    MTBSFM = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 51
try:
    MTFSFM = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 52
try:
    MTEOM = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 55
try:
    MTERASE = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 57
try:
    MTRAS1 = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 58
try:
    MTRAS2 = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 59
try:
    MTRAS3 = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 61
try:
    MTSETBLK = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 62
try:
    MTSETDENSITY = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 63
try:
    MTSEEK = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 64
try:
    MTTELL = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 65
try:
    MTSETDRVBUFFER = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 67
try:
    MTFSS = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 68
try:
    MTBSS = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 69
try:
    MTWSM = 27
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 71
try:
    MTLOCK = 28
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 72
try:
    MTUNLOCK = 29
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 73
try:
    MTLOAD = 30
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 74
try:
    MTUNLOAD = 31
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 75
try:
    MTCOMPRESSION = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 76
try:
    MTSETPART = 33
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 77
try:
    MTMKPART = 34
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 102
try:
    MT_ISUNKNOWN = 0x01
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 103
try:
    MT_ISQIC02 = 0x02
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 104
try:
    MT_ISWT5150 = 0x03
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 105
try:
    MT_ISARCHIVE_5945L2 = 0x04
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 106
try:
    MT_ISCMSJ500 = 0x05
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 107
try:
    MT_ISTDC3610 = 0x06
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 108
try:
    MT_ISARCHIVE_VP60I = 0x07
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 109
try:
    MT_ISARCHIVE_2150L = 0x08
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 110
try:
    MT_ISARCHIVE_2060L = 0x09
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 111
try:
    MT_ISARCHIVESC499 = 0x0A
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 112
try:
    MT_ISQIC02_ALL_FEATURES = 0x0F
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 113
try:
    MT_ISWT5099EEN24 = 0x11
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 114
try:
    MT_ISTEAC_MT2ST = 0x12
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 116
try:
    MT_ISEVEREX_FT40A = 0x32
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 117
try:
    MT_ISDDS1 = 0x51
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 118
try:
    MT_ISDDS2 = 0x52
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 119
try:
    MT_ISSCSI1 = 0x71
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 120
try:
    MT_ISSCSI2 = 0x72
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 124
try:
    MT_ISFTAPE_UNKNOWN = 0x800000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 125
try:
    MT_ISFTAPE_FLAG = 0x800000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 197
try:
    MTIOCTOP = (_IOW ('m', 1, struct_mtop))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 198
try:
    MTIOCGET = (_IOR ('m', 2, struct_mtget))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 199
try:
    MTIOCPOS = (_IOR ('m', 3, struct_mtpos))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 203
try:
    MTIOCGETCONFIG = (_IOR ('m', 4, struct_mtconfiginfo))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 204
try:
    MTIOCSETCONFIG = (_IOW ('m', 5, struct_mtconfiginfo))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 211
def GMT_EOF(x):
    return (x & 0x80000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 212
def GMT_BOT(x):
    return (x & 0x40000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 213
def GMT_EOT(x):
    return (x & 0x20000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 214
def GMT_SM(x):
    return (x & 0x10000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 215
def GMT_EOD(x):
    return (x & 0x08000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 216
def GMT_WR_PROT(x):
    return (x & 0x04000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 218
def GMT_ONLINE(x):
    return (x & 0x01000000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 219
def GMT_D_6250(x):
    return (x & 0x00800000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 220
def GMT_D_1600(x):
    return (x & 0x00400000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 221
def GMT_D_800(x):
    return (x & 0x00200000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 224
def GMT_DR_OPEN(x):
    return (x & 0x00040000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 226
def GMT_IM_REP_EN(x):
    return (x & 0x00010000)

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 231
try:
    MT_ST_BLKSIZE_SHIFT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 232
try:
    MT_ST_BLKSIZE_MASK = 0xffffff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 233
try:
    MT_ST_DENSITY_SHIFT = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 234
try:
    MT_ST_DENSITY_MASK = 0xff000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 236
try:
    MT_ST_SOFTERR_SHIFT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 237
try:
    MT_ST_SOFTERR_MASK = 0xffff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 240
try:
    MT_ST_OPTIONS = 0xf0000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 241
try:
    MT_ST_BOOLEANS = 0x10000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 242
try:
    MT_ST_SETBOOLEANS = 0x30000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 243
try:
    MT_ST_CLEARBOOLEANS = 0x40000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 244
try:
    MT_ST_WRITE_THRESHOLD = 0x20000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 245
try:
    MT_ST_DEF_BLKSIZE = 0x50000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 246
try:
    MT_ST_DEF_OPTIONS = 0x60000000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 248
try:
    MT_ST_BUFFER_WRITES = 0x1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 249
try:
    MT_ST_ASYNC_WRITES = 0x2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 250
try:
    MT_ST_READ_AHEAD = 0x4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 251
try:
    MT_ST_DEBUGGING = 0x8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 252
try:
    MT_ST_TWO_FM = 0x10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 253
try:
    MT_ST_FAST_MTEOM = 0x20
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 254
try:
    MT_ST_AUTO_LOCK = 0x40
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 255
try:
    MT_ST_DEF_WRITES = 0x80
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 256
try:
    MT_ST_CAN_BSR = 0x100
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 257
try:
    MT_ST_NO_BLKLIMS = 0x200
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 258
try:
    MT_ST_CAN_PARTITIONS = 0x400
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 259
try:
    MT_ST_SCSI2LOGICAL = 0x800
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 262
try:
    MT_ST_CLEAR_DEFAULT = 0xfffff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 263
try:
    MT_ST_DEF_DENSITY = (MT_ST_DEF_OPTIONS | 0x100000)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 264
try:
    MT_ST_DEF_COMPRESSION = (MT_ST_DEF_OPTIONS | 0x200000)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 265
try:
    MT_ST_DEF_DRVBUFFER = (MT_ST_DEF_OPTIONS | 0x300000)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 268
try:
    MT_ST_HPLOADER_OFFSET = 10000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/mtio.h: 273
try:
    DEFTAPE = '/dev/tape'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 20
try:
    _SYS_PARAM_H = 1
except:
    pass

# /usr/include/limits.h: 54
try:
    CHAR_BIT = 8
except:
    pass

# /usr/lib/gcc/x86_64-linux-gnu/9/include/limits.h: 63
# #undef CHAR_BIT
try:
    del CHAR_BIT
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/signum-generic.h: 96
try:
    __SIGRTMIN = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/signum-generic.h: 97
try:
    __SIGRTMAX = __SIGRTMIN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/signum-generic.h: 100
try:
    _NSIG = (__SIGRTMAX + 1)
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/signum.h: 55
# #undef __SIGRTMAX
try:
    del __SIGRTMAX
except NameError:
    pass

# /usr/include/signal.h: 167
def sigmask(sig):
    return (c_int (ord_if_char((1 << (sig - 1))))).value

# /usr/include/signal.h: 181
try:
    NSIG = _NSIG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 19
try:
    _SYS_UCONTEXT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 29
def __ctx(fld):
    return fld

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 40
try:
    __NGREG = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 42
try:
    NGREG = __NGREG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 260
# #undef __ctx
try:
    del __ctx
except NameError:
    pass

# /usr/include/signal.h: 370
try:
    SIGRTMIN = (__libc_current_sigrtmin ())
except:
    pass

# /usr/include/signal.h: 371
try:
    SIGRTMAX = (__libc_current_sigrtmax ())
except:
    pass

# /usr/include/asm-generic/param.h: 6
try:
    HZ = 100
except:
    pass

# /usr/include/asm-generic/param.h: 10
try:
    EXEC_PAGESIZE = 4096
except:
    pass

# /usr/include/asm-generic/param.h: 14
try:
    NOGROUP = (-1)
except:
    pass

# /usr/include/asm-generic/param.h: 17
try:
    MAXHOSTNAMELEN = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/param.h: 36
try:
    MAXSYMLINKS = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/param.h: 41
try:
    NOFILE = 256
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/param.h: 42
try:
    NCARGS = 131072
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 36
try:
    NBBY = CHAR_BIT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 39
try:
    NGROUPS = NGROUPS_MAX
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 45
try:
    CANBSIZ = MAX_CANON
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 48
try:
    MAXPATHLEN = PATH_MAX
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 72
try:
    NODEV = (dev_t (ord_if_char((-1)))).value
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 78
try:
    DEV_BSIZE = 512
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/param.h: 83
def setbit(a, i):
    return ((a [(i / NBBY)]) | (1 << (i % NBBY)))

# /usr/include/x86_64-linux-gnu/sys/param.h: 84
def clrbit(a, i):
    return ((a [(i / NBBY)]) & (~(1 << (i % NBBY))))

# /usr/include/x86_64-linux-gnu/sys/param.h: 85
def isset(a, i):
    return ((a [(i / NBBY)]) & (1 << (i % NBBY)))

# /usr/include/x86_64-linux-gnu/sys/param.h: 86
def isclr(a, i):
    return (((a [(i / NBBY)]) & (1 << (i % NBBY))) == 0)

# /usr/include/x86_64-linux-gnu/sys/param.h: 90
def howmany(x, y):
    return ((x + (y - 1)) / y)

# /usr/include/x86_64-linux-gnu/sys/param.h: 97
def roundup(x, y):
    return (((x + (y - 1)) / y) * y)

# /usr/include/x86_64-linux-gnu/sys/param.h: 99
def powerof2(x):
    return (((x - 1) & x) == 0)

# /usr/include/x86_64-linux-gnu/sys/param.h: 102
def MIN(a, b):
    return (a < b) and a or b

# /usr/include/x86_64-linux-gnu/sys/param.h: 103
def MAX(a, b):
    return (a > b) and a or b

# /usr/include/x86_64-linux-gnu/sys/pci.h: 19
try:
    _SYS_PCI_H = 1
except:
    pass

# /usr/include/linux/pci.h: 31
def PCI_DEVFN(slot, func):
    return (((slot & 0x1f) << 3) | (func & 0x07))

# /usr/include/linux/pci.h: 32
def PCI_SLOT(devfn):
    return ((devfn >> 3) & 0x1f)

# /usr/include/linux/pci.h: 33
def PCI_FUNC(devfn):
    return (devfn & 0x07)

# /usr/include/linux/pci.h: 36
try:
    PCIIOC_BASE = ((('P' << 24) | ('C' << 16)) | ('I' << 8))
except:
    pass

# /usr/include/linux/pci.h: 37
try:
    PCIIOC_CONTROLLER = (PCIIOC_BASE | 0x00)
except:
    pass

# /usr/include/linux/pci.h: 38
try:
    PCIIOC_MMAP_IS_IO = (PCIIOC_BASE | 0x01)
except:
    pass

# /usr/include/linux/pci.h: 39
try:
    PCIIOC_MMAP_IS_MEM = (PCIIOC_BASE | 0x02)
except:
    pass

# /usr/include/linux/pci.h: 40
try:
    PCIIOC_WRITE_COMBINE = (PCIIOC_BASE | 0x03)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/perm.h: 20
try:
    _SYS_PERM_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/personality.h: 21
try:
    _SYS_PERSONALITY_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/poll.h: 20
try:
    _SYS_POLL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 25
try:
    POLLIN = 0x001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 26
try:
    POLLPRI = 0x002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 27
try:
    POLLOUT = 0x004
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 31
try:
    POLLRDNORM = 0x040
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 32
try:
    POLLRDBAND = 0x080
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 33
try:
    POLLWRNORM = 0x100
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 34
try:
    POLLWRBAND = 0x200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 47
try:
    POLLERR = 0x008
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 48
try:
    POLLHUP = 0x010
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/poll.h: 49
try:
    POLLNVAL = 0x020
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/prctl.h: 19
try:
    _SYS_PRCTL_H = 1
except:
    pass

# /usr/include/linux/prctl.h: 9
try:
    PR_SET_PDEATHSIG = 1
except:
    pass

# /usr/include/linux/prctl.h: 10
try:
    PR_GET_PDEATHSIG = 2
except:
    pass

# /usr/include/linux/prctl.h: 13
try:
    PR_GET_DUMPABLE = 3
except:
    pass

# /usr/include/linux/prctl.h: 14
try:
    PR_SET_DUMPABLE = 4
except:
    pass

# /usr/include/linux/prctl.h: 17
try:
    PR_GET_UNALIGN = 5
except:
    pass

# /usr/include/linux/prctl.h: 18
try:
    PR_SET_UNALIGN = 6
except:
    pass

# /usr/include/linux/prctl.h: 19
try:
    PR_UNALIGN_NOPRINT = 1
except:
    pass

# /usr/include/linux/prctl.h: 20
try:
    PR_UNALIGN_SIGBUS = 2
except:
    pass

# /usr/include/linux/prctl.h: 24
try:
    PR_GET_KEEPCAPS = 7
except:
    pass

# /usr/include/linux/prctl.h: 25
try:
    PR_SET_KEEPCAPS = 8
except:
    pass

# /usr/include/linux/prctl.h: 28
try:
    PR_GET_FPEMU = 9
except:
    pass

# /usr/include/linux/prctl.h: 29
try:
    PR_SET_FPEMU = 10
except:
    pass

# /usr/include/linux/prctl.h: 30
try:
    PR_FPEMU_NOPRINT = 1
except:
    pass

# /usr/include/linux/prctl.h: 31
try:
    PR_FPEMU_SIGFPE = 2
except:
    pass

# /usr/include/linux/prctl.h: 34
try:
    PR_GET_FPEXC = 11
except:
    pass

# /usr/include/linux/prctl.h: 35
try:
    PR_SET_FPEXC = 12
except:
    pass

# /usr/include/linux/prctl.h: 36
try:
    PR_FP_EXC_SW_ENABLE = 0x80
except:
    pass

# /usr/include/linux/prctl.h: 37
try:
    PR_FP_EXC_DIV = 0x010000
except:
    pass

# /usr/include/linux/prctl.h: 38
try:
    PR_FP_EXC_OVF = 0x020000
except:
    pass

# /usr/include/linux/prctl.h: 39
try:
    PR_FP_EXC_UND = 0x040000
except:
    pass

# /usr/include/linux/prctl.h: 40
try:
    PR_FP_EXC_RES = 0x080000
except:
    pass

# /usr/include/linux/prctl.h: 41
try:
    PR_FP_EXC_INV = 0x100000
except:
    pass

# /usr/include/linux/prctl.h: 42
try:
    PR_FP_EXC_DISABLED = 0
except:
    pass

# /usr/include/linux/prctl.h: 43
try:
    PR_FP_EXC_NONRECOV = 1
except:
    pass

# /usr/include/linux/prctl.h: 44
try:
    PR_FP_EXC_ASYNC = 2
except:
    pass

# /usr/include/linux/prctl.h: 45
try:
    PR_FP_EXC_PRECISE = 3
except:
    pass

# /usr/include/linux/prctl.h: 49
try:
    PR_GET_TIMING = 13
except:
    pass

# /usr/include/linux/prctl.h: 50
try:
    PR_SET_TIMING = 14
except:
    pass

# /usr/include/linux/prctl.h: 51
try:
    PR_TIMING_STATISTICAL = 0
except:
    pass

# /usr/include/linux/prctl.h: 53
try:
    PR_TIMING_TIMESTAMP = 1
except:
    pass

# /usr/include/linux/prctl.h: 56
try:
    PR_SET_NAME = 15
except:
    pass

# /usr/include/linux/prctl.h: 57
try:
    PR_GET_NAME = 16
except:
    pass

# /usr/include/linux/prctl.h: 60
try:
    PR_GET_ENDIAN = 19
except:
    pass

# /usr/include/linux/prctl.h: 61
try:
    PR_SET_ENDIAN = 20
except:
    pass

# /usr/include/linux/prctl.h: 62
try:
    PR_ENDIAN_BIG = 0
except:
    pass

# /usr/include/linux/prctl.h: 63
try:
    PR_ENDIAN_LITTLE = 1
except:
    pass

# /usr/include/linux/prctl.h: 64
try:
    PR_ENDIAN_PPC_LITTLE = 2
except:
    pass

# /usr/include/linux/prctl.h: 67
try:
    PR_GET_SECCOMP = 21
except:
    pass

# /usr/include/linux/prctl.h: 68
try:
    PR_SET_SECCOMP = 22
except:
    pass

# /usr/include/linux/prctl.h: 71
try:
    PR_CAPBSET_READ = 23
except:
    pass

# /usr/include/linux/prctl.h: 72
try:
    PR_CAPBSET_DROP = 24
except:
    pass

# /usr/include/linux/prctl.h: 75
try:
    PR_GET_TSC = 25
except:
    pass

# /usr/include/linux/prctl.h: 76
try:
    PR_SET_TSC = 26
except:
    pass

# /usr/include/linux/prctl.h: 77
try:
    PR_TSC_ENABLE = 1
except:
    pass

# /usr/include/linux/prctl.h: 78
try:
    PR_TSC_SIGSEGV = 2
except:
    pass

# /usr/include/linux/prctl.h: 81
try:
    PR_GET_SECUREBITS = 27
except:
    pass

# /usr/include/linux/prctl.h: 82
try:
    PR_SET_SECUREBITS = 28
except:
    pass

# /usr/include/linux/prctl.h: 88
try:
    PR_SET_TIMERSLACK = 29
except:
    pass

# /usr/include/linux/prctl.h: 89
try:
    PR_GET_TIMERSLACK = 30
except:
    pass

# /usr/include/linux/prctl.h: 91
try:
    PR_TASK_PERF_EVENTS_DISABLE = 31
except:
    pass

# /usr/include/linux/prctl.h: 92
try:
    PR_TASK_PERF_EVENTS_ENABLE = 32
except:
    pass

# /usr/include/linux/prctl.h: 98
try:
    PR_MCE_KILL = 33
except:
    pass

# /usr/include/linux/prctl.h: 99
try:
    PR_MCE_KILL_CLEAR = 0
except:
    pass

# /usr/include/linux/prctl.h: 100
try:
    PR_MCE_KILL_SET = 1
except:
    pass

# /usr/include/linux/prctl.h: 102
try:
    PR_MCE_KILL_LATE = 0
except:
    pass

# /usr/include/linux/prctl.h: 103
try:
    PR_MCE_KILL_EARLY = 1
except:
    pass

# /usr/include/linux/prctl.h: 104
try:
    PR_MCE_KILL_DEFAULT = 2
except:
    pass

# /usr/include/linux/prctl.h: 106
try:
    PR_MCE_KILL_GET = 34
except:
    pass

# /usr/include/linux/prctl.h: 111
try:
    PR_SET_MM = 35
except:
    pass

# /usr/include/linux/prctl.h: 112
try:
    PR_SET_MM_START_CODE = 1
except:
    pass

# /usr/include/linux/prctl.h: 113
try:
    PR_SET_MM_END_CODE = 2
except:
    pass

# /usr/include/linux/prctl.h: 114
try:
    PR_SET_MM_START_DATA = 3
except:
    pass

# /usr/include/linux/prctl.h: 115
try:
    PR_SET_MM_END_DATA = 4
except:
    pass

# /usr/include/linux/prctl.h: 116
try:
    PR_SET_MM_START_STACK = 5
except:
    pass

# /usr/include/linux/prctl.h: 117
try:
    PR_SET_MM_START_BRK = 6
except:
    pass

# /usr/include/linux/prctl.h: 118
try:
    PR_SET_MM_BRK = 7
except:
    pass

# /usr/include/linux/prctl.h: 119
try:
    PR_SET_MM_ARG_START = 8
except:
    pass

# /usr/include/linux/prctl.h: 120
try:
    PR_SET_MM_ARG_END = 9
except:
    pass

# /usr/include/linux/prctl.h: 121
try:
    PR_SET_MM_ENV_START = 10
except:
    pass

# /usr/include/linux/prctl.h: 122
try:
    PR_SET_MM_ENV_END = 11
except:
    pass

# /usr/include/linux/prctl.h: 123
try:
    PR_SET_MM_AUXV = 12
except:
    pass

# /usr/include/linux/prctl.h: 124
try:
    PR_SET_MM_EXE_FILE = 13
except:
    pass

# /usr/include/linux/prctl.h: 125
try:
    PR_SET_MM_MAP = 14
except:
    pass

# /usr/include/linux/prctl.h: 126
try:
    PR_SET_MM_MAP_SIZE = 15
except:
    pass

# /usr/include/linux/prctl.h: 155
try:
    PR_SET_PTRACER = 0x59616d61
except:
    pass

# /usr/include/linux/prctl.h: 156
try:
    PR_SET_PTRACER_ANY = (c_ulong (ord_if_char((-1)))).value
except:
    pass

# /usr/include/linux/prctl.h: 158
try:
    PR_SET_CHILD_SUBREAPER = 36
except:
    pass

# /usr/include/linux/prctl.h: 159
try:
    PR_GET_CHILD_SUBREAPER = 37
except:
    pass

# /usr/include/linux/prctl.h: 175
try:
    PR_SET_NO_NEW_PRIVS = 38
except:
    pass

# /usr/include/linux/prctl.h: 176
try:
    PR_GET_NO_NEW_PRIVS = 39
except:
    pass

# /usr/include/linux/prctl.h: 178
try:
    PR_GET_TID_ADDRESS = 40
except:
    pass

# /usr/include/linux/prctl.h: 180
try:
    PR_SET_THP_DISABLE = 41
except:
    pass

# /usr/include/linux/prctl.h: 181
try:
    PR_GET_THP_DISABLE = 42
except:
    pass

# /usr/include/linux/prctl.h: 186
try:
    PR_MPX_ENABLE_MANAGEMENT = 43
except:
    pass

# /usr/include/linux/prctl.h: 187
try:
    PR_MPX_DISABLE_MANAGEMENT = 44
except:
    pass

# /usr/include/linux/prctl.h: 189
try:
    PR_SET_FP_MODE = 45
except:
    pass

# /usr/include/linux/prctl.h: 190
try:
    PR_GET_FP_MODE = 46
except:
    pass

# /usr/include/linux/prctl.h: 191
try:
    PR_FP_MODE_FR = (1 << 0)
except:
    pass

# /usr/include/linux/prctl.h: 192
try:
    PR_FP_MODE_FRE = (1 << 1)
except:
    pass

# /usr/include/linux/prctl.h: 195
try:
    PR_CAP_AMBIENT = 47
except:
    pass

# /usr/include/linux/prctl.h: 196
try:
    PR_CAP_AMBIENT_IS_SET = 1
except:
    pass

# /usr/include/linux/prctl.h: 197
try:
    PR_CAP_AMBIENT_RAISE = 2
except:
    pass

# /usr/include/linux/prctl.h: 198
try:
    PR_CAP_AMBIENT_LOWER = 3
except:
    pass

# /usr/include/linux/prctl.h: 199
try:
    PR_CAP_AMBIENT_CLEAR_ALL = 4
except:
    pass

# /usr/include/linux/prctl.h: 203
try:
    PR_SVE_SET_VL = 50
except:
    pass

# /usr/include/linux/prctl.h: 204
try:
    PR_SVE_SET_VL_ONEXEC = (1 << 18)
except:
    pass

# /usr/include/linux/prctl.h: 205
try:
    PR_SVE_GET_VL = 51
except:
    pass

# /usr/include/linux/prctl.h: 207
try:
    PR_SVE_VL_LEN_MASK = 0xffff
except:
    pass

# /usr/include/linux/prctl.h: 208
try:
    PR_SVE_VL_INHERIT = (1 << 17)
except:
    pass

# /usr/include/linux/prctl.h: 211
try:
    PR_GET_SPECULATION_CTRL = 52
except:
    pass

# /usr/include/linux/prctl.h: 212
try:
    PR_SET_SPECULATION_CTRL = 53
except:
    pass

# /usr/include/linux/prctl.h: 214
try:
    PR_SPEC_STORE_BYPASS = 0
except:
    pass

# /usr/include/linux/prctl.h: 215
try:
    PR_SPEC_INDIRECT_BRANCH = 1
except:
    pass

# /usr/include/linux/prctl.h: 217
try:
    PR_SPEC_NOT_AFFECTED = 0
except:
    pass

# /usr/include/linux/prctl.h: 218
try:
    PR_SPEC_PRCTL = (1 << 0)
except:
    pass

# /usr/include/linux/prctl.h: 219
try:
    PR_SPEC_ENABLE = (1 << 1)
except:
    pass

# /usr/include/linux/prctl.h: 220
try:
    PR_SPEC_DISABLE = (1 << 2)
except:
    pass

# /usr/include/linux/prctl.h: 221
try:
    PR_SPEC_FORCE_DISABLE = (1 << 3)
except:
    pass

# /usr/include/linux/prctl.h: 222
try:
    PR_SPEC_DISABLE_NOEXEC = (1 << 4)
except:
    pass

# /usr/include/linux/prctl.h: 225
try:
    PR_PAC_RESET_KEYS = 54
except:
    pass

# /usr/include/linux/prctl.h: 226
try:
    PR_PAC_APIAKEY = (1 << 0)
except:
    pass

# /usr/include/linux/prctl.h: 227
try:
    PR_PAC_APIBKEY = (1 << 1)
except:
    pass

# /usr/include/linux/prctl.h: 228
try:
    PR_PAC_APDAKEY = (1 << 2)
except:
    pass

# /usr/include/linux/prctl.h: 229
try:
    PR_PAC_APDBKEY = (1 << 3)
except:
    pass

# /usr/include/linux/prctl.h: 230
try:
    PR_PAC_APGAKEY = (1 << 4)
except:
    pass

# /usr/include/linux/prctl.h: 233
try:
    PR_SET_TAGGED_ADDR_CTRL = 55
except:
    pass

# /usr/include/linux/prctl.h: 234
try:
    PR_GET_TAGGED_ADDR_CTRL = 56
except:
    pass

# /usr/include/linux/prctl.h: 235
try:
    PR_TAGGED_ADDR_ENABLE = (1 << 0)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/procfs.h: 21
try:
    _SYS_PROCFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/time.h: 19
try:
    _SYS_TIME_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/time.h: 93
try:
    ITIMER_REAL = ITIMER_REAL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/time.h: 96
try:
    ITIMER_VIRTUAL = ITIMER_VIRTUAL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/time.h: 100
try:
    ITIMER_PROF = ITIMER_PROF
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/time.h: 160
def timerisset(tvp):
    return ((tvp.contents.tv_sec) or (tvp.contents.tv_usec))

# /usr/include/x86_64-linux-gnu/sys/time.h: 161
def timerclear(tvp):
    return 0

# /usr/include/x86_64-linux-gnu/sys/user.h: 19
try:
    _SYS_USER_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/user.h: 172
try:
    PAGE_SHIFT = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/user.h: 173
try:
    PAGE_SIZE = (1 << PAGE_SHIFT)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/user.h: 174
try:
    PAGE_MASK = (~(PAGE_SIZE - 1))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/user.h: 175
try:
    NBPG = PAGE_SIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/user.h: 176
try:
    UPAGES = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/procfs.h: 34
try:
    ELF_NGREG = (sizeof(struct_user_regs_struct) / sizeof(elf_greg_t))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/procfs.h: 82
try:
    ELF_PRARGSZ = 80
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/profil.h: 19
try:
    _PROFIL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 21
try:
    _SYS_PTRACE_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 35
try:
    PT_TRACE_ME = PTRACE_TRACEME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 39
try:
    PT_READ_I = PTRACE_PEEKTEXT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 43
try:
    PT_READ_D = PTRACE_PEEKDATA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 47
try:
    PT_READ_U = PTRACE_PEEKUSER
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 51
try:
    PT_WRITE_I = PTRACE_POKETEXT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 55
try:
    PT_WRITE_D = PTRACE_POKEDATA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 59
try:
    PT_WRITE_U = PTRACE_POKEUSER
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 63
try:
    PT_CONTINUE = PTRACE_CONT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 67
try:
    PT_KILL = PTRACE_KILL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 71
try:
    PT_STEP = PTRACE_SINGLESTEP
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 75
try:
    PT_GETREGS = PTRACE_GETREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 79
try:
    PT_SETREGS = PTRACE_SETREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 83
try:
    PT_GETFPREGS = PTRACE_GETFPREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 87
try:
    PT_SETFPREGS = PTRACE_SETFPREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 91
try:
    PT_ATTACH = PTRACE_ATTACH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 95
try:
    PT_DETACH = PTRACE_DETACH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 99
try:
    PT_GETFPXREGS = PTRACE_GETFPXREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 103
try:
    PT_SETFPXREGS = PTRACE_SETFPXREGS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 107
try:
    PT_SYSCALL = PTRACE_SYSCALL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 111
try:
    PT_GET_THREAD_AREA = PTRACE_GET_THREAD_AREA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 115
try:
    PT_SET_THREAD_AREA = PTRACE_SET_THREAD_AREA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 120
try:
    PT_ARCH_PRCTL = PTRACE_ARCH_PRCTL
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 125
try:
    PT_SYSEMU = PTRACE_SYSEMU
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 129
try:
    PT_SYSEMU_SINGLESTEP = PTRACE_SYSEMU_SINGLESTEP
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 133
try:
    PT_STEPBLOCK = PTRACE_SINGLEBLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 137
try:
    PT_SETOPTIONS = PTRACE_SETOPTIONS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 141
try:
    PT_GETEVENTMSG = PTRACE_GETEVENTMSG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 145
try:
    PT_GETSIGINFO = PTRACE_GETSIGINFO
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 149
try:
    PT_SETSIGINFO = PTRACE_SETSIGINFO
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 153
try:
    PTRACE_GETREGSET = PTRACE_GETREGSET
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 157
try:
    PTRACE_SETREGSET = PTRACE_SETREGSET
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 162
try:
    PTRACE_SEIZE = PTRACE_SEIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 166
try:
    PTRACE_INTERRUPT = PTRACE_INTERRUPT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 170
try:
    PTRACE_LISTEN = PTRACE_LISTEN
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 174
try:
    PTRACE_PEEKSIGINFO = PTRACE_PEEKSIGINFO
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 178
try:
    PTRACE_GETSIGMASK = PTRACE_GETSIGMASK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 182
try:
    PTRACE_SETSIGMASK = PTRACE_SETSIGMASK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 186
try:
    PTRACE_SECCOMP_GET_FILTER = PTRACE_SECCOMP_GET_FILTER
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 190
try:
    PTRACE_SECCOMP_GET_METADATA = PTRACE_SECCOMP_GET_METADATA
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ptrace.h: 194
try:
    PTRACE_GET_SYSCALL_INFO = PTRACE_GET_SYSCALL_INFO
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/queue.h: 143
def LIST_FIRST(head):
    return (head.contents.lh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 204
def SLIST_FIRST(head):
    return (head.contents.slh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 286
def STAILQ_FIRST(head):
    return (head.contents.stqh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 360
def SIMPLEQ_FIRST(head):
    return (head.contents.sqh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 458
def TAILQ_FIRST(head):
    return (head.contents.tqh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 559
def CIRCLEQ_EMPTY(head):
    return (((head.contents.cqh_first).value) == cast(head, POINTER(None)))

# /usr/include/x86_64-linux-gnu/sys/queue.h: 560
def CIRCLEQ_FIRST(head):
    return (head.contents.cqh_first)

# /usr/include/x86_64-linux-gnu/sys/queue.h: 561
def CIRCLEQ_LAST(head):
    return (head.contents.cqh_last)

# /usr/include/x86_64-linux-gnu/sys/quota.h: 52
try:
    _SYS_QUOTA_H = 1
except:
    pass

# /usr/include/linux/quota.h: 38
try:
    __DQUOT_VERSION__ = 'dquot_6.6.0'
except:
    pass

# /usr/include/linux/quota.h: 40
try:
    MAXQUOTAS = 3
except:
    pass

# /usr/include/linux/quota.h: 41
try:
    USRQUOTA = 0
except:
    pass

# /usr/include/linux/quota.h: 42
try:
    GRPQUOTA = 1
except:
    pass

# /usr/include/linux/quota.h: 43
try:
    PRJQUOTA = 2
except:
    pass

# /usr/include/linux/quota.h: 61
try:
    SUBCMDMASK = 0x00ff
except:
    pass

# /usr/include/linux/quota.h: 62
try:
    SUBCMDSHIFT = 8
except:
    pass

# /usr/include/linux/quota.h: 63
def QCMD(cmd, type):
    return ((cmd << SUBCMDSHIFT) | (type & SUBCMDMASK))

# /usr/include/linux/quota.h: 65
try:
    Q_SYNC = 0x800001
except:
    pass

# /usr/include/linux/quota.h: 66
try:
    Q_QUOTAON = 0x800002
except:
    pass

# /usr/include/linux/quota.h: 67
try:
    Q_QUOTAOFF = 0x800003
except:
    pass

# /usr/include/linux/quota.h: 68
try:
    Q_GETFMT = 0x800004
except:
    pass

# /usr/include/linux/quota.h: 69
try:
    Q_GETINFO = 0x800005
except:
    pass

# /usr/include/linux/quota.h: 70
try:
    Q_SETINFO = 0x800006
except:
    pass

# /usr/include/linux/quota.h: 71
try:
    Q_GETQUOTA = 0x800007
except:
    pass

# /usr/include/linux/quota.h: 72
try:
    Q_SETQUOTA = 0x800008
except:
    pass

# /usr/include/linux/quota.h: 73
try:
    Q_GETNEXTQUOTA = 0x800009
except:
    pass

# /usr/include/linux/quota.h: 76
try:
    QFMT_VFS_OLD = 1
except:
    pass

# /usr/include/linux/quota.h: 77
try:
    QFMT_VFS_V0 = 2
except:
    pass

# /usr/include/linux/quota.h: 78
try:
    QFMT_OCFS2 = 3
except:
    pass

# /usr/include/linux/quota.h: 79
try:
    QFMT_VFS_V1 = 4
except:
    pass

# /usr/include/linux/quota.h: 83
try:
    QIF_DQBLKSIZE_BITS = 10
except:
    pass

# /usr/include/linux/quota.h: 84
try:
    QIF_DQBLKSIZE = (1 << QIF_DQBLKSIZE_BITS)
except:
    pass

# /usr/include/linux/quota.h: 99
try:
    QIF_BLIMITS = (1 << QIF_BLIMITS_B)
except:
    pass

# /usr/include/linux/quota.h: 100
try:
    QIF_SPACE = (1 << QIF_SPACE_B)
except:
    pass

# /usr/include/linux/quota.h: 101
try:
    QIF_ILIMITS = (1 << QIF_ILIMITS_B)
except:
    pass

# /usr/include/linux/quota.h: 102
try:
    QIF_INODES = (1 << QIF_INODES_B)
except:
    pass

# /usr/include/linux/quota.h: 103
try:
    QIF_BTIME = (1 << QIF_BTIME_B)
except:
    pass

# /usr/include/linux/quota.h: 104
try:
    QIF_ITIME = (1 << QIF_ITIME_B)
except:
    pass

# /usr/include/linux/quota.h: 105
try:
    QIF_LIMITS = (QIF_BLIMITS | QIF_ILIMITS)
except:
    pass

# /usr/include/linux/quota.h: 106
try:
    QIF_USAGE = (QIF_SPACE | QIF_INODES)
except:
    pass

# /usr/include/linux/quota.h: 107
try:
    QIF_TIMES = (QIF_BTIME | QIF_ITIME)
except:
    pass

# /usr/include/linux/quota.h: 108
try:
    QIF_ALL = ((QIF_LIMITS | QIF_USAGE) | QIF_TIMES)
except:
    pass

# /usr/include/linux/quota.h: 139
try:
    IIF_BGRACE = 1
except:
    pass

# /usr/include/linux/quota.h: 140
try:
    IIF_IGRACE = 2
except:
    pass

# /usr/include/linux/quota.h: 141
try:
    IIF_FLAGS = 4
except:
    pass

# /usr/include/linux/quota.h: 142
try:
    IIF_ALL = ((IIF_BGRACE | IIF_IGRACE) | IIF_FLAGS)
except:
    pass

# /usr/include/linux/quota.h: 152
try:
    DQF_ROOT_SQUASH = (1 << DQF_ROOT_SQUASH_B)
except:
    pass

# /usr/include/linux/quota.h: 154
try:
    DQF_SYS_FILE = (1 << DQF_SYS_FILE_B)
except:
    pass

# /usr/include/linux/quota.h: 166
try:
    QUOTA_NL_NOWARN = 0
except:
    pass

# /usr/include/linux/quota.h: 167
try:
    QUOTA_NL_IHARDWARN = 1
except:
    pass

# /usr/include/linux/quota.h: 168
try:
    QUOTA_NL_ISOFTLONGWARN = 2
except:
    pass

# /usr/include/linux/quota.h: 169
try:
    QUOTA_NL_ISOFTWARN = 3
except:
    pass

# /usr/include/linux/quota.h: 170
try:
    QUOTA_NL_BHARDWARN = 4
except:
    pass

# /usr/include/linux/quota.h: 171
try:
    QUOTA_NL_BSOFTLONGWARN = 5
except:
    pass

# /usr/include/linux/quota.h: 172
try:
    QUOTA_NL_BSOFTWARN = 6
except:
    pass

# /usr/include/linux/quota.h: 173
try:
    QUOTA_NL_IHARDBELOW = 7
except:
    pass

# /usr/include/linux/quota.h: 174
try:
    QUOTA_NL_ISOFTBELOW = 8
except:
    pass

# /usr/include/linux/quota.h: 175
try:
    QUOTA_NL_BHARDBELOW = 9
except:
    pass

# /usr/include/linux/quota.h: 176
try:
    QUOTA_NL_BSOFTBELOW = 10
except:
    pass

# /usr/include/linux/quota.h: 183
try:
    QUOTA_NL_C_MAX = (__QUOTA_NL_C_MAX - 1)
except:
    pass

# /usr/include/linux/quota.h: 196
try:
    QUOTA_NL_A_MAX = (__QUOTA_NL_A_MAX - 1)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 63
def dbtob(num):
    return (num << 10)

# /usr/include/x86_64-linux-gnu/sys/quota.h: 64
def btodb(num):
    return (num >> 10)

# /usr/include/x86_64-linux-gnu/sys/quota.h: 70
def fs_to_dq_blocks(num, blksize):
    return ((num * blksize) / 1024)

# /usr/include/x86_64-linux-gnu/sys/quota.h: 81
try:
    MAX_IQ_TIME = 604800
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 82
try:
    MAX_DQ_TIME = 604800
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 84
try:
    QUOTAFILENAME = 'quota'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 85
try:
    QUOTAGROUP = 'staff'
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 87
try:
    NR_DQHASH = 43
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 88
try:
    NR_DQUOTS = 256
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/quota.h: 117
def dqoff(UID):
    return (__loff_t (ord_if_char((UID * sizeof(struct_dqblk))))).value

# /usr/include/x86_64-linux-gnu/sys/random.h: 20
try:
    _SYS_RANDOM_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/random.h: 26
try:
    GRND_NONBLOCK = 0x01
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/random.h: 27
try:
    GRND_RANDOM = 0x02
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/raw.h: 19
try:
    _SYS_RAW_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/raw.h: 25
try:
    RAW_MAJOR = 162
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/raw.h: 28
try:
    RAW_SETBIND = (_IO (0xac, 0))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/raw.h: 29
try:
    RAW_GETBIND = (_IO (0xac, 1))
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 22
try:
    _SYS_REBOOT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 27
try:
    RB_AUTOBOOT = 0x01234567
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 30
try:
    RB_HALT_SYSTEM = 0xcdef0123
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 33
try:
    RB_ENABLE_CAD = 0x89abcdef
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 36
try:
    RB_DISABLE_CAD = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 39
try:
    RB_POWER_OFF = 0x4321fedc
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 42
try:
    RB_SW_SUSPEND = 0xd000fce2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reboot.h: 45
try:
    RB_KEXEC = 0x45584543
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 19
try:
    _SYS_REG_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 26
try:
    R15 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 27
try:
    R14 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 28
try:
    R13 = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 29
try:
    R12 = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 30
try:
    RBP = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 31
try:
    RBX = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 32
try:
    R11 = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 33
try:
    R10 = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 34
try:
    R9 = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 35
try:
    R8 = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 36
try:
    RAX = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 37
try:
    RCX = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 38
try:
    RDX = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 39
try:
    RSI = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 40
try:
    RDI = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 41
try:
    ORIG_RAX = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 42
try:
    RIP = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 43
try:
    CS = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 44
try:
    EFLAGS = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 45
try:
    RSP = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 46
try:
    SS = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 47
try:
    FS_BASE = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 48
try:
    GS_BASE = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 49
try:
    DS = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 50
try:
    ES = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 51
try:
    FS = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/reg.h: 52
try:
    GS = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/resource.h: 19
try:
    _SYS_RESOURCE_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 35
try:
    RLIMIT_CPU = RLIMIT_CPU
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 39
try:
    RLIMIT_FSIZE = RLIMIT_FSIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 43
try:
    RLIMIT_DATA = RLIMIT_DATA
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 47
try:
    RLIMIT_STACK = RLIMIT_STACK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 51
try:
    RLIMIT_CORE = RLIMIT_CORE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 58
try:
    RLIMIT_RSS = __RLIMIT_RSS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 63
try:
    RLIMIT_NOFILE = RLIMIT_NOFILE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 64
try:
    RLIMIT_OFILE = __RLIMIT_OFILE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 68
try:
    RLIMIT_AS = RLIMIT_AS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 72
try:
    RLIMIT_NPROC = __RLIMIT_NPROC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 76
try:
    RLIMIT_MEMLOCK = __RLIMIT_MEMLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 80
try:
    RLIMIT_LOCKS = __RLIMIT_LOCKS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 84
try:
    RLIMIT_SIGPENDING = __RLIMIT_SIGPENDING
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 88
try:
    RLIMIT_MSGQUEUE = __RLIMIT_MSGQUEUE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 94
try:
    RLIMIT_NICE = __RLIMIT_NICE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 99
try:
    RLIMIT_RTPRIO = __RLIMIT_RTPRIO
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 105
try:
    RLIMIT_RTTIME = __RLIMIT_RTTIME
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 109
try:
    RLIMIT_NLIMITS = __RLIMIT_NLIMITS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 110
try:
    RLIM_NLIMITS = __RLIM_NLIMITS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 115
try:
    RLIM_INFINITY = (__rlim_t (ord_if_char((-1)))).value
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 125
try:
    RLIM_SAVED_MAX = RLIM_INFINITY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 126
try:
    RLIM_SAVED_CUR = RLIM_INFINITY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 162
try:
    RUSAGE_SELF = RUSAGE_SELF
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 166
try:
    RUSAGE_CHILDREN = RUSAGE_CHILDREN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 182
try:
    PRIO_MIN = (-20)
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 183
try:
    PRIO_MAX = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 190
try:
    PRIO_PROCESS = PRIO_PROCESS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 192
try:
    PRIO_PGRP = PRIO_PGRP
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/resource.h: 194
try:
    PRIO_USER = PRIO_USER
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sem.h: 19
try:
    _SYS_SEM_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 26
try:
    SEM_UNDO = 0x1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 29
try:
    GETPID = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 30
try:
    GETVAL = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 31
try:
    GETALL = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 32
try:
    GETNCNT = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 33
try:
    GETZCNT = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 34
try:
    SETVAL = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 35
try:
    SETALL = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 74
try:
    _SEM_SEMUN_UNDEFINED = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 79
try:
    SEM_STAT = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 80
try:
    SEM_INFO = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sem.h: 81
try:
    SEM_STAT_ANY = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sendfile.h: 20
try:
    _SYS_SENDFILE_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/shm.h: 19
try:
    _SYS_SHM_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 28
try:
    SHM_R = 0o400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 29
try:
    SHM_W = 0o200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 32
try:
    SHM_RDONLY = 0o10000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 33
try:
    SHM_RND = 0o20000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 34
try:
    SHM_REMAP = 0o40000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 35
try:
    SHM_EXEC = 0o100000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 38
try:
    SHM_LOCK = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 39
try:
    SHM_UNLOCK = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 83
try:
    SHM_STAT = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 84
try:
    SHM_INFO = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 85
try:
    SHM_STAT_ANY = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 88
try:
    SHM_DEST = 0o1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 89
try:
    SHM_LOCKED = 0o2000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 90
try:
    SHM_HUGETLB = 0o4000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/shm.h: 91
try:
    SHM_NORESERVE = 0o10000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/signalfd.h: 19
try:
    _SYS_SIGNALFD_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/signalfd.h: 26
try:
    SFD_CLOEXEC = SFD_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/signalfd.h: 28
try:
    SFD_NONBLOCK = SFD_NONBLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/socket.h: 20
try:
    _SYS_SOCKET_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 41
try:
    PF_UNSPEC = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 42
try:
    PF_LOCAL = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 43
try:
    PF_UNIX = PF_LOCAL
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 44
try:
    PF_FILE = PF_LOCAL
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 45
try:
    PF_INET = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 46
try:
    PF_AX25 = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 47
try:
    PF_IPX = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 48
try:
    PF_APPLETALK = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 49
try:
    PF_NETROM = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 50
try:
    PF_BRIDGE = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 51
try:
    PF_ATMPVC = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 52
try:
    PF_X25 = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 53
try:
    PF_INET6 = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 54
try:
    PF_ROSE = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 55
try:
    PF_DECnet = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 56
try:
    PF_NETBEUI = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 57
try:
    PF_SECURITY = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 58
try:
    PF_KEY = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 59
try:
    PF_NETLINK = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 60
try:
    PF_ROUTE = PF_NETLINK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 61
try:
    PF_PACKET = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 62
try:
    PF_ASH = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 63
try:
    PF_ECONET = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 64
try:
    PF_ATMSVC = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 65
try:
    PF_RDS = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 66
try:
    PF_SNA = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 67
try:
    PF_IRDA = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 68
try:
    PF_PPPOX = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 69
try:
    PF_WANPIPE = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 70
try:
    PF_LLC = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 71
try:
    PF_IB = 27
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 72
try:
    PF_MPLS = 28
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 73
try:
    PF_CAN = 29
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 74
try:
    PF_TIPC = 30
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 75
try:
    PF_BLUETOOTH = 31
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 76
try:
    PF_IUCV = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 77
try:
    PF_RXRPC = 33
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 78
try:
    PF_ISDN = 34
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 79
try:
    PF_PHONET = 35
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 80
try:
    PF_IEEE802154 = 36
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 81
try:
    PF_CAIF = 37
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 82
try:
    PF_ALG = 38
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 83
try:
    PF_NFC = 39
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 84
try:
    PF_VSOCK = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 85
try:
    PF_KCM = 41
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 86
try:
    PF_QIPCRTR = 42
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 87
try:
    PF_SMC = 43
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 88
try:
    PF_XDP = 44
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 89
try:
    PF_MAX = 45
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 92
try:
    AF_UNSPEC = PF_UNSPEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 93
try:
    AF_LOCAL = PF_LOCAL
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 94
try:
    AF_UNIX = PF_UNIX
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 95
try:
    AF_FILE = PF_FILE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 96
try:
    AF_INET = PF_INET
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 97
try:
    AF_AX25 = PF_AX25
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 98
try:
    AF_IPX = PF_IPX
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 99
try:
    AF_APPLETALK = PF_APPLETALK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 100
try:
    AF_NETROM = PF_NETROM
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 101
try:
    AF_BRIDGE = PF_BRIDGE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 102
try:
    AF_ATMPVC = PF_ATMPVC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 103
try:
    AF_X25 = PF_X25
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 104
try:
    AF_INET6 = PF_INET6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 105
try:
    AF_ROSE = PF_ROSE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 106
try:
    AF_DECnet = PF_DECnet
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 107
try:
    AF_NETBEUI = PF_NETBEUI
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 108
try:
    AF_SECURITY = PF_SECURITY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 109
try:
    AF_KEY = PF_KEY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 110
try:
    AF_NETLINK = PF_NETLINK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 111
try:
    AF_ROUTE = PF_ROUTE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 112
try:
    AF_PACKET = PF_PACKET
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 113
try:
    AF_ASH = PF_ASH
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 114
try:
    AF_ECONET = PF_ECONET
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 115
try:
    AF_ATMSVC = PF_ATMSVC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 116
try:
    AF_RDS = PF_RDS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 117
try:
    AF_SNA = PF_SNA
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 118
try:
    AF_IRDA = PF_IRDA
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 119
try:
    AF_PPPOX = PF_PPPOX
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 120
try:
    AF_WANPIPE = PF_WANPIPE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 121
try:
    AF_LLC = PF_LLC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 122
try:
    AF_IB = PF_IB
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 123
try:
    AF_MPLS = PF_MPLS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 124
try:
    AF_CAN = PF_CAN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 125
try:
    AF_TIPC = PF_TIPC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 126
try:
    AF_BLUETOOTH = PF_BLUETOOTH
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 127
try:
    AF_IUCV = PF_IUCV
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 128
try:
    AF_RXRPC = PF_RXRPC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 129
try:
    AF_ISDN = PF_ISDN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 130
try:
    AF_PHONET = PF_PHONET
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 131
try:
    AF_IEEE802154 = PF_IEEE802154
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 132
try:
    AF_CAIF = PF_CAIF
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 133
try:
    AF_ALG = PF_ALG
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 134
try:
    AF_NFC = PF_NFC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 135
try:
    AF_VSOCK = PF_VSOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 136
try:
    AF_KCM = PF_KCM
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 137
try:
    AF_QIPCRTR = PF_QIPCRTR
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 138
try:
    AF_SMC = PF_SMC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 139
try:
    AF_XDP = PF_XDP
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 140
try:
    AF_MAX = PF_MAX
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 146
try:
    SOL_RAW = 255
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 147
try:
    SOL_DECNET = 261
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 148
try:
    SOL_X25 = 262
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 149
try:
    SOL_PACKET = 263
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 150
try:
    SOL_ATM = 264
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 151
try:
    SOL_AAL = 265
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 152
try:
    SOL_IRDA = 266
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 153
try:
    SOL_NETBEUI = 267
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 154
try:
    SOL_LLC = 268
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 155
try:
    SOL_DCCP = 269
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 156
try:
    SOL_NETLINK = 270
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 157
try:
    SOL_TIPC = 271
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 158
try:
    SOL_RXRPC = 272
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 159
try:
    SOL_PPPOL2TP = 273
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 160
try:
    SOL_BLUETOOTH = 274
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 161
try:
    SOL_PNPIPE = 275
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 162
try:
    SOL_RDS = 276
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 163
try:
    SOL_IUCV = 277
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 164
try:
    SOL_CAIF = 278
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 165
try:
    SOL_ALG = 279
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 166
try:
    SOL_NFC = 280
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 167
try:
    SOL_KCM = 281
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 168
try:
    SOL_TLS = 282
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 169
try:
    SOL_XDP = 283
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 172
try:
    SOMAXCONN = 4096
except:
    pass

__ss_aligntype = c_ulong# /usr/include/x86_64-linux-gnu/bits/socket.h: 187

# /usr/include/x86_64-linux-gnu/bits/socket.h: 203
try:
    MSG_OOB = MSG_OOB
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 205
try:
    MSG_PEEK = MSG_PEEK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 207
try:
    MSG_DONTROUTE = MSG_DONTROUTE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 214
try:
    MSG_CTRUNC = MSG_CTRUNC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 216
try:
    MSG_PROXY = MSG_PROXY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 218
try:
    MSG_TRUNC = MSG_TRUNC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 220
try:
    MSG_DONTWAIT = MSG_DONTWAIT
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 222
try:
    MSG_EOR = MSG_EOR
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 224
try:
    MSG_WAITALL = MSG_WAITALL
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 226
try:
    MSG_FIN = MSG_FIN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 228
try:
    MSG_SYN = MSG_SYN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 230
try:
    MSG_CONFIRM = MSG_CONFIRM
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 232
try:
    MSG_RST = MSG_RST
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 234
try:
    MSG_ERRQUEUE = MSG_ERRQUEUE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 236
try:
    MSG_NOSIGNAL = MSG_NOSIGNAL
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 238
try:
    MSG_MORE = MSG_MORE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 240
try:
    MSG_WAITFORONE = MSG_WAITFORONE
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 242
try:
    MSG_BATCH = MSG_BATCH
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 244
try:
    MSG_ZEROCOPY = MSG_ZEROCOPY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 246
try:
    MSG_FASTOPEN = MSG_FASTOPEN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 251
try:
    MSG_CMSG_CLOEXEC = MSG_CMSG_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/socket.h: 291
def CMSG_DATA(cmsg):
    return (cmsg.contents.__cmsg_data)

# /usr/include/x86_64-linux-gnu/bits/socket.h: 295
def CMSG_NXTHDR(mhdr, cmsg):
    return (__cmsg_nxthdr (mhdr, cmsg))

# /usr/include/x86_64-linux-gnu/bits/socket.h: 296
def CMSG_FIRSTHDR(mhdr):
    return ((c_size_t (ord_if_char(((mhdr.contents.msg_controllen).value)))).value >= sizeof(struct_cmsghdr)) and cast((mhdr.contents.msg_control), POINTER(struct_cmsghdr)) or cast(0, POINTER(struct_cmsghdr))

# /usr/include/x86_64-linux-gnu/bits/socket.h: 299
def CMSG_ALIGN(len):
    return (((len + sizeof(c_size_t)) - 1) & (c_size_t (ord_if_char((~(sizeof(c_size_t) - 1))))).value)

# /usr/include/x86_64-linux-gnu/bits/socket.h: 301
def CMSG_SPACE(len):
    return ((CMSG_ALIGN (len)) + (CMSG_ALIGN (sizeof(struct_cmsghdr))))

# /usr/include/x86_64-linux-gnu/bits/socket.h: 303
def CMSG_LEN(len):
    return ((CMSG_ALIGN (sizeof(struct_cmsghdr))) + len)

# /usr/include/x86_64-linux-gnu/bits/socket.h: 335
try:
    SCM_RIGHTS = SCM_RIGHTS
except:
    pass

# /usr/include/asm-generic/socket.h: 9
try:
    SOL_SOCKET = 1
except:
    pass

# /usr/include/asm-generic/socket.h: 11
try:
    SO_DEBUG = 1
except:
    pass

# /usr/include/asm-generic/socket.h: 12
try:
    SO_REUSEADDR = 2
except:
    pass

# /usr/include/asm-generic/socket.h: 13
try:
    SO_TYPE = 3
except:
    pass

# /usr/include/asm-generic/socket.h: 14
try:
    SO_ERROR = 4
except:
    pass

# /usr/include/asm-generic/socket.h: 15
try:
    SO_DONTROUTE = 5
except:
    pass

# /usr/include/asm-generic/socket.h: 16
try:
    SO_BROADCAST = 6
except:
    pass

# /usr/include/asm-generic/socket.h: 17
try:
    SO_SNDBUF = 7
except:
    pass

# /usr/include/asm-generic/socket.h: 18
try:
    SO_RCVBUF = 8
except:
    pass

# /usr/include/asm-generic/socket.h: 19
try:
    SO_SNDBUFFORCE = 32
except:
    pass

# /usr/include/asm-generic/socket.h: 20
try:
    SO_RCVBUFFORCE = 33
except:
    pass

# /usr/include/asm-generic/socket.h: 21
try:
    SO_KEEPALIVE = 9
except:
    pass

# /usr/include/asm-generic/socket.h: 22
try:
    SO_OOBINLINE = 10
except:
    pass

# /usr/include/asm-generic/socket.h: 23
try:
    SO_NO_CHECK = 11
except:
    pass

# /usr/include/asm-generic/socket.h: 24
try:
    SO_PRIORITY = 12
except:
    pass

# /usr/include/asm-generic/socket.h: 25
try:
    SO_LINGER = 13
except:
    pass

# /usr/include/asm-generic/socket.h: 26
try:
    SO_BSDCOMPAT = 14
except:
    pass

# /usr/include/asm-generic/socket.h: 27
try:
    SO_REUSEPORT = 15
except:
    pass

# /usr/include/asm-generic/socket.h: 29
try:
    SO_PASSCRED = 16
except:
    pass

# /usr/include/asm-generic/socket.h: 30
try:
    SO_PEERCRED = 17
except:
    pass

# /usr/include/asm-generic/socket.h: 31
try:
    SO_RCVLOWAT = 18
except:
    pass

# /usr/include/asm-generic/socket.h: 32
try:
    SO_SNDLOWAT = 19
except:
    pass

# /usr/include/asm-generic/socket.h: 33
try:
    SO_RCVTIMEO_OLD = 20
except:
    pass

# /usr/include/asm-generic/socket.h: 34
try:
    SO_SNDTIMEO_OLD = 21
except:
    pass

# /usr/include/asm-generic/socket.h: 38
try:
    SO_SECURITY_AUTHENTICATION = 22
except:
    pass

# /usr/include/asm-generic/socket.h: 39
try:
    SO_SECURITY_ENCRYPTION_TRANSPORT = 23
except:
    pass

# /usr/include/asm-generic/socket.h: 40
try:
    SO_SECURITY_ENCRYPTION_NETWORK = 24
except:
    pass

# /usr/include/asm-generic/socket.h: 42
try:
    SO_BINDTODEVICE = 25
except:
    pass

# /usr/include/asm-generic/socket.h: 45
try:
    SO_ATTACH_FILTER = 26
except:
    pass

# /usr/include/asm-generic/socket.h: 46
try:
    SO_DETACH_FILTER = 27
except:
    pass

# /usr/include/asm-generic/socket.h: 47
try:
    SO_GET_FILTER = SO_ATTACH_FILTER
except:
    pass

# /usr/include/asm-generic/socket.h: 49
try:
    SO_PEERNAME = 28
except:
    pass

# /usr/include/asm-generic/socket.h: 51
try:
    SO_ACCEPTCONN = 30
except:
    pass

# /usr/include/asm-generic/socket.h: 53
try:
    SO_PEERSEC = 31
except:
    pass

# /usr/include/asm-generic/socket.h: 54
try:
    SO_PASSSEC = 34
except:
    pass

# /usr/include/asm-generic/socket.h: 56
try:
    SO_MARK = 36
except:
    pass

# /usr/include/asm-generic/socket.h: 58
try:
    SO_PROTOCOL = 38
except:
    pass

# /usr/include/asm-generic/socket.h: 59
try:
    SO_DOMAIN = 39
except:
    pass

# /usr/include/asm-generic/socket.h: 61
try:
    SO_RXQ_OVFL = 40
except:
    pass

# /usr/include/asm-generic/socket.h: 63
try:
    SO_WIFI_STATUS = 41
except:
    pass

# /usr/include/asm-generic/socket.h: 64
try:
    SCM_WIFI_STATUS = SO_WIFI_STATUS
except:
    pass

# /usr/include/asm-generic/socket.h: 65
try:
    SO_PEEK_OFF = 42
except:
    pass

# /usr/include/asm-generic/socket.h: 68
try:
    SO_NOFCS = 43
except:
    pass

# /usr/include/asm-generic/socket.h: 70
try:
    SO_LOCK_FILTER = 44
except:
    pass

# /usr/include/asm-generic/socket.h: 72
try:
    SO_SELECT_ERR_QUEUE = 45
except:
    pass

# /usr/include/asm-generic/socket.h: 74
try:
    SO_BUSY_POLL = 46
except:
    pass

# /usr/include/asm-generic/socket.h: 76
try:
    SO_MAX_PACING_RATE = 47
except:
    pass

# /usr/include/asm-generic/socket.h: 78
try:
    SO_BPF_EXTENSIONS = 48
except:
    pass

# /usr/include/asm-generic/socket.h: 80
try:
    SO_INCOMING_CPU = 49
except:
    pass

# /usr/include/asm-generic/socket.h: 82
try:
    SO_ATTACH_BPF = 50
except:
    pass

# /usr/include/asm-generic/socket.h: 83
try:
    SO_DETACH_BPF = SO_DETACH_FILTER
except:
    pass

# /usr/include/asm-generic/socket.h: 85
try:
    SO_ATTACH_REUSEPORT_CBPF = 51
except:
    pass

# /usr/include/asm-generic/socket.h: 86
try:
    SO_ATTACH_REUSEPORT_EBPF = 52
except:
    pass

# /usr/include/asm-generic/socket.h: 88
try:
    SO_CNX_ADVICE = 53
except:
    pass

# /usr/include/asm-generic/socket.h: 90
try:
    SCM_TIMESTAMPING_OPT_STATS = 54
except:
    pass

# /usr/include/asm-generic/socket.h: 92
try:
    SO_MEMINFO = 55
except:
    pass

# /usr/include/asm-generic/socket.h: 94
try:
    SO_INCOMING_NAPI_ID = 56
except:
    pass

# /usr/include/asm-generic/socket.h: 96
try:
    SO_COOKIE = 57
except:
    pass

# /usr/include/asm-generic/socket.h: 98
try:
    SCM_TIMESTAMPING_PKTINFO = 58
except:
    pass

# /usr/include/asm-generic/socket.h: 100
try:
    SO_PEERGROUPS = 59
except:
    pass

# /usr/include/asm-generic/socket.h: 102
try:
    SO_ZEROCOPY = 60
except:
    pass

# /usr/include/asm-generic/socket.h: 104
try:
    SO_TXTIME = 61
except:
    pass

# /usr/include/asm-generic/socket.h: 105
try:
    SCM_TXTIME = SO_TXTIME
except:
    pass

# /usr/include/asm-generic/socket.h: 107
try:
    SO_BINDTOIFINDEX = 62
except:
    pass

# /usr/include/asm-generic/socket.h: 109
try:
    SO_TIMESTAMP_OLD = 29
except:
    pass

# /usr/include/asm-generic/socket.h: 110
try:
    SO_TIMESTAMPNS_OLD = 35
except:
    pass

# /usr/include/asm-generic/socket.h: 111
try:
    SO_TIMESTAMPING_OLD = 37
except:
    pass

# /usr/include/asm-generic/socket.h: 113
try:
    SO_TIMESTAMP_NEW = 63
except:
    pass

# /usr/include/asm-generic/socket.h: 114
try:
    SO_TIMESTAMPNS_NEW = 64
except:
    pass

# /usr/include/asm-generic/socket.h: 115
try:
    SO_TIMESTAMPING_NEW = 65
except:
    pass

# /usr/include/asm-generic/socket.h: 117
try:
    SO_RCVTIMEO_NEW = 66
except:
    pass

# /usr/include/asm-generic/socket.h: 118
try:
    SO_SNDTIMEO_NEW = 67
except:
    pass

# /usr/include/asm-generic/socket.h: 120
try:
    SO_DETACH_REUSEPORT_BPF = 68
except:
    pass

# /usr/include/asm-generic/socket.h: 125
try:
    SO_TIMESTAMP = SO_TIMESTAMP_OLD
except:
    pass

# /usr/include/asm-generic/socket.h: 126
try:
    SO_TIMESTAMPNS = SO_TIMESTAMPNS_OLD
except:
    pass

# /usr/include/asm-generic/socket.h: 127
try:
    SO_TIMESTAMPING = SO_TIMESTAMPING_OLD
except:
    pass

# /usr/include/asm-generic/socket.h: 129
try:
    SO_RCVTIMEO = SO_RCVTIMEO_OLD
except:
    pass

# /usr/include/asm-generic/socket.h: 130
try:
    SO_SNDTIMEO = SO_SNDTIMEO_OLD
except:
    pass

# /usr/include/asm-generic/socket.h: 140
try:
    SCM_TIMESTAMP = SO_TIMESTAMP
except:
    pass

# /usr/include/asm-generic/socket.h: 141
try:
    SCM_TIMESTAMPNS = SO_TIMESTAMPNS
except:
    pass

# /usr/include/asm-generic/socket.h: 142
try:
    SCM_TIMESTAMPING = SO_TIMESTAMPING
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/socket.h: 44
try:
    SHUT_RD = SHUT_RD
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/socket.h: 46
try:
    SHUT_WR = SHUT_WR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/socket.h: 48
try:
    SHUT_RDWR = SHUT_RDWR
except:
    pass

__SOCKADDR_ARG = POINTER(struct_sockaddr)# /usr/include/x86_64-linux-gnu/sys/socket.h: 58

__CONST_SOCKADDR_ARG = POINTER(struct_sockaddr)# /usr/include/x86_64-linux-gnu/sys/socket.h: 59

# /usr/include/linux/soundcard.h: 36
try:
    SOUND_VERSION = 0x030802
except:
    pass

# /usr/include/linux/soundcard.h: 49
try:
    SNDCARD_ADLIB = 1
except:
    pass

# /usr/include/linux/soundcard.h: 50
try:
    SNDCARD_SB = 2
except:
    pass

# /usr/include/linux/soundcard.h: 51
try:
    SNDCARD_PAS = 3
except:
    pass

# /usr/include/linux/soundcard.h: 52
try:
    SNDCARD_GUS = 4
except:
    pass

# /usr/include/linux/soundcard.h: 53
try:
    SNDCARD_MPU401 = 5
except:
    pass

# /usr/include/linux/soundcard.h: 54
try:
    SNDCARD_SB16 = 6
except:
    pass

# /usr/include/linux/soundcard.h: 55
try:
    SNDCARD_SB16MIDI = 7
except:
    pass

# /usr/include/linux/soundcard.h: 56
try:
    SNDCARD_UART6850 = 8
except:
    pass

# /usr/include/linux/soundcard.h: 57
try:
    SNDCARD_GUS16 = 9
except:
    pass

# /usr/include/linux/soundcard.h: 58
try:
    SNDCARD_MSS = 10
except:
    pass

# /usr/include/linux/soundcard.h: 59
try:
    SNDCARD_PSS = 11
except:
    pass

# /usr/include/linux/soundcard.h: 60
try:
    SNDCARD_SSCAPE = 12
except:
    pass

# /usr/include/linux/soundcard.h: 61
try:
    SNDCARD_PSS_MPU = 13
except:
    pass

# /usr/include/linux/soundcard.h: 62
try:
    SNDCARD_PSS_MSS = 14
except:
    pass

# /usr/include/linux/soundcard.h: 63
try:
    SNDCARD_SSCAPE_MSS = 15
except:
    pass

# /usr/include/linux/soundcard.h: 64
try:
    SNDCARD_TRXPRO = 16
except:
    pass

# /usr/include/linux/soundcard.h: 65
try:
    SNDCARD_TRXPRO_SB = 17
except:
    pass

# /usr/include/linux/soundcard.h: 66
try:
    SNDCARD_TRXPRO_MPU = 18
except:
    pass

# /usr/include/linux/soundcard.h: 67
try:
    SNDCARD_MAD16 = 19
except:
    pass

# /usr/include/linux/soundcard.h: 68
try:
    SNDCARD_MAD16_MPU = 20
except:
    pass

# /usr/include/linux/soundcard.h: 69
try:
    SNDCARD_CS4232 = 21
except:
    pass

# /usr/include/linux/soundcard.h: 70
try:
    SNDCARD_CS4232_MPU = 22
except:
    pass

# /usr/include/linux/soundcard.h: 71
try:
    SNDCARD_MAUI = 23
except:
    pass

# /usr/include/linux/soundcard.h: 72
try:
    SNDCARD_PSEUDO_MSS = 24
except:
    pass

# /usr/include/linux/soundcard.h: 73
try:
    SNDCARD_GUSPNP = 25
except:
    pass

# /usr/include/linux/soundcard.h: 74
try:
    SNDCARD_UART401 = 26
except:
    pass

# /usr/include/linux/soundcard.h: 86
try:
    SIOC_OUT = IOC_OUT
except:
    pass

# /usr/include/linux/soundcard.h: 87
try:
    SIOC_IN = IOC_IN
except:
    pass

# /usr/include/linux/soundcard.h: 88
try:
    SIOC_INOUT = IOC_INOUT
except:
    pass

# /usr/include/linux/soundcard.h: 89
try:
    _SIOC_SIZE = _IOC_SIZE
except:
    pass

# /usr/include/linux/soundcard.h: 90
try:
    _SIOC_DIR = _IOC_DIR
except:
    pass

# /usr/include/linux/soundcard.h: 91
try:
    _SIOC_NONE = _IOC_NONE
except:
    pass

# /usr/include/linux/soundcard.h: 92
try:
    _SIOC_READ = _IOC_READ
except:
    pass

# /usr/include/linux/soundcard.h: 93
try:
    _SIOC_WRITE = _IOC_WRITE
except:
    pass

# /usr/include/linux/soundcard.h: 94
try:
    _SIO = _IO
except:
    pass

# /usr/include/linux/soundcard.h: 95
try:
    _SIOR = _IOR
except:
    pass

# /usr/include/linux/soundcard.h: 96
try:
    _SIOW = _IOW
except:
    pass

# /usr/include/linux/soundcard.h: 97
try:
    _SIOWR = _IOWR
except:
    pass

# /usr/include/linux/soundcard.h: 126
try:
    SNDCTL_SEQ_RESET = (_SIO ('Q', 0))
except:
    pass

# /usr/include/linux/soundcard.h: 127
try:
    SNDCTL_SEQ_SYNC = (_SIO ('Q', 1))
except:
    pass

# /usr/include/linux/soundcard.h: 128
try:
    SNDCTL_SYNTH_INFO = (_SIOWR ('Q', 2, struct_synth_info))
except:
    pass

# /usr/include/linux/soundcard.h: 129
try:
    SNDCTL_SEQ_CTRLRATE = (_SIOWR ('Q', 3, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 130
try:
    SNDCTL_SEQ_GETOUTCOUNT = (_SIOR ('Q', 4, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 131
try:
    SNDCTL_SEQ_GETINCOUNT = (_SIOR ('Q', 5, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 132
try:
    SNDCTL_SEQ_PERCMODE = (_SIOW ('Q', 6, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 133
try:
    SNDCTL_FM_LOAD_INSTR = (_SIOW ('Q', 7, struct_sbi_instrument))
except:
    pass

# /usr/include/linux/soundcard.h: 134
try:
    SNDCTL_SEQ_TESTMIDI = (_SIOW ('Q', 8, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 135
try:
    SNDCTL_SEQ_RESETSAMPLES = (_SIOW ('Q', 9, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 136
try:
    SNDCTL_SEQ_NRSYNTHS = (_SIOR ('Q', 10, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 137
try:
    SNDCTL_SEQ_NRMIDIS = (_SIOR ('Q', 11, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 138
try:
    SNDCTL_MIDI_INFO = (_SIOWR ('Q', 12, struct_midi_info))
except:
    pass

# /usr/include/linux/soundcard.h: 139
try:
    SNDCTL_SEQ_THRESHOLD = (_SIOW ('Q', 13, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 140
try:
    SNDCTL_SYNTH_MEMAVL = (_SIOWR ('Q', 14, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 141
try:
    SNDCTL_FM_4OP_ENABLE = (_SIOW ('Q', 15, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 142
try:
    SNDCTL_SEQ_PANIC = (_SIO ('Q', 17))
except:
    pass

# /usr/include/linux/soundcard.h: 143
try:
    SNDCTL_SEQ_OUTOFBAND = (_SIOW ('Q', 18, struct_seq_event_rec))
except:
    pass

# /usr/include/linux/soundcard.h: 144
try:
    SNDCTL_SEQ_GETTIME = (_SIOR ('Q', 19, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 145
try:
    SNDCTL_SYNTH_ID = (_SIOWR ('Q', 20, struct_synth_info))
except:
    pass

# /usr/include/linux/soundcard.h: 146
try:
    SNDCTL_SYNTH_CONTROL = (_SIOWR ('Q', 21, struct_synth_control))
except:
    pass

# /usr/include/linux/soundcard.h: 147
try:
    SNDCTL_SYNTH_REMOVESAMPLE = (_SIOWR ('Q', 22, struct_remove_sample))
except:
    pass

# /usr/include/linux/soundcard.h: 166
try:
    SNDCTL_TMR_TIMEBASE = (_SIOWR ('T', 1, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 167
try:
    SNDCTL_TMR_START = (_SIO ('T', 2))
except:
    pass

# /usr/include/linux/soundcard.h: 168
try:
    SNDCTL_TMR_STOP = (_SIO ('T', 3))
except:
    pass

# /usr/include/linux/soundcard.h: 169
try:
    SNDCTL_TMR_CONTINUE = (_SIO ('T', 4))
except:
    pass

# /usr/include/linux/soundcard.h: 170
try:
    SNDCTL_TMR_TEMPO = (_SIOWR ('T', 5, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 171
try:
    SNDCTL_TMR_SOURCE = (_SIOWR ('T', 6, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 172
try:
    TMR_INTERNAL = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 173
try:
    TMR_EXTERNAL = 0x00000002
except:
    pass

# /usr/include/linux/soundcard.h: 174
try:
    TMR_MODE_MIDI = 0x00000010
except:
    pass

# /usr/include/linux/soundcard.h: 175
try:
    TMR_MODE_FSK = 0x00000020
except:
    pass

# /usr/include/linux/soundcard.h: 176
try:
    TMR_MODE_CLS = 0x00000040
except:
    pass

# /usr/include/linux/soundcard.h: 177
try:
    TMR_MODE_SMPTE = 0x00000080
except:
    pass

# /usr/include/linux/soundcard.h: 178
try:
    SNDCTL_TMR_METRONOME = (_SIOW ('T', 7, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 179
try:
    SNDCTL_TMR_SELECT = (_SIOW ('T', 8, c_int))
except:
    pass

# /usr/include/linux/patchkey.h: 28
def _PATCHKEY(id):
    return ((id << 8) | 0x00fd)

# /usr/include/linux/soundcard.h: 193
try:
    AFMT_S16_NE = AFMT_S16_LE
except:
    pass

# /usr/include/linux/soundcard.h: 211
try:
    WAVE_PATCH = (_PATCHKEY (0x04))
except:
    pass

# /usr/include/linux/soundcard.h: 212
try:
    GUS_PATCH = WAVE_PATCH
except:
    pass

# /usr/include/linux/soundcard.h: 213
try:
    WAVEFRONT_PATCH = (_PATCHKEY (0x06))
except:
    pass

# /usr/include/linux/soundcard.h: 223
try:
    WAVE_16_BITS = 0x01
except:
    pass

# /usr/include/linux/soundcard.h: 224
try:
    WAVE_UNSIGNED = 0x02
except:
    pass

# /usr/include/linux/soundcard.h: 225
try:
    WAVE_LOOPING = 0x04
except:
    pass

# /usr/include/linux/soundcard.h: 226
try:
    WAVE_BIDIR_LOOP = 0x08
except:
    pass

# /usr/include/linux/soundcard.h: 227
try:
    WAVE_LOOP_BACK = 0x10
except:
    pass

# /usr/include/linux/soundcard.h: 228
try:
    WAVE_SUSTAIN_ON = 0x20
except:
    pass

# /usr/include/linux/soundcard.h: 229
try:
    WAVE_ENVELOPES = 0x40
except:
    pass

# /usr/include/linux/soundcard.h: 230
try:
    WAVE_FAST_RELEASE = 0x80
except:
    pass

# /usr/include/linux/soundcard.h: 233
try:
    WAVE_VIBRATO = 0x00010000
except:
    pass

# /usr/include/linux/soundcard.h: 234
try:
    WAVE_TREMOLO = 0x00020000
except:
    pass

# /usr/include/linux/soundcard.h: 235
try:
    WAVE_SCALE = 0x00040000
except:
    pass

# /usr/include/linux/soundcard.h: 236
try:
    WAVE_FRACTIONS = 0x00080000
except:
    pass

# /usr/include/linux/soundcard.h: 238
try:
    WAVE_ROM = 0x40000000
except:
    pass

# /usr/include/linux/soundcard.h: 239
try:
    WAVE_MULAW = 0x20000000
except:
    pass

# /usr/include/linux/soundcard.h: 300
try:
    SYSEX_PATCH = (_PATCHKEY (0x05))
except:
    pass

# /usr/include/linux/soundcard.h: 301
try:
    MAUI_PATCH = (_PATCHKEY (0x06))
except:
    pass

# /usr/include/linux/soundcard.h: 327
try:
    SEQ_NOTEOFF = 0
except:
    pass

# /usr/include/linux/soundcard.h: 328
try:
    SEQ_FMNOTEOFF = SEQ_NOTEOFF
except:
    pass

# /usr/include/linux/soundcard.h: 329
try:
    SEQ_NOTEON = 1
except:
    pass

# /usr/include/linux/soundcard.h: 330
try:
    SEQ_FMNOTEON = SEQ_NOTEON
except:
    pass

# /usr/include/linux/soundcard.h: 331
try:
    SEQ_WAIT = TMR_WAIT_ABS
except:
    pass

# /usr/include/linux/soundcard.h: 332
try:
    SEQ_PGMCHANGE = 3
except:
    pass

# /usr/include/linux/soundcard.h: 333
try:
    SEQ_FMPGMCHANGE = SEQ_PGMCHANGE
except:
    pass

# /usr/include/linux/soundcard.h: 334
try:
    SEQ_SYNCTIMER = TMR_START
except:
    pass

# /usr/include/linux/soundcard.h: 335
try:
    SEQ_MIDIPUTC = 5
except:
    pass

# /usr/include/linux/soundcard.h: 336
try:
    SEQ_DRUMON = 6
except:
    pass

# /usr/include/linux/soundcard.h: 337
try:
    SEQ_DRUMOFF = 7
except:
    pass

# /usr/include/linux/soundcard.h: 338
try:
    SEQ_ECHO = TMR_ECHO
except:
    pass

# /usr/include/linux/soundcard.h: 339
try:
    SEQ_AFTERTOUCH = 9
except:
    pass

# /usr/include/linux/soundcard.h: 340
try:
    SEQ_CONTROLLER = 10
except:
    pass

# /usr/include/linux/soundcard.h: 354
try:
    CTL_BANK_SELECT = 0x00
except:
    pass

# /usr/include/linux/soundcard.h: 355
try:
    CTL_MODWHEEL = 0x01
except:
    pass

# /usr/include/linux/soundcard.h: 356
try:
    CTL_BREATH = 0x02
except:
    pass

# /usr/include/linux/soundcard.h: 358
try:
    CTL_FOOT = 0x04
except:
    pass

# /usr/include/linux/soundcard.h: 359
try:
    CTL_PORTAMENTO_TIME = 0x05
except:
    pass

# /usr/include/linux/soundcard.h: 360
try:
    CTL_DATA_ENTRY = 0x06
except:
    pass

# /usr/include/linux/soundcard.h: 361
try:
    CTL_MAIN_VOLUME = 0x07
except:
    pass

# /usr/include/linux/soundcard.h: 362
try:
    CTL_BALANCE = 0x08
except:
    pass

# /usr/include/linux/soundcard.h: 364
try:
    CTL_PAN = 0x0a
except:
    pass

# /usr/include/linux/soundcard.h: 365
try:
    CTL_EXPRESSION = 0x0b
except:
    pass

# /usr/include/linux/soundcard.h: 370
try:
    CTL_GENERAL_PURPOSE1 = 0x10
except:
    pass

# /usr/include/linux/soundcard.h: 371
try:
    CTL_GENERAL_PURPOSE2 = 0x11
except:
    pass

# /usr/include/linux/soundcard.h: 372
try:
    CTL_GENERAL_PURPOSE3 = 0x12
except:
    pass

# /usr/include/linux/soundcard.h: 373
try:
    CTL_GENERAL_PURPOSE4 = 0x13
except:
    pass

# /usr/include/linux/soundcard.h: 383
try:
    CTL_DAMPER_PEDAL = 0x40
except:
    pass

# /usr/include/linux/soundcard.h: 384
try:
    CTL_SUSTAIN = 0x40
except:
    pass

# /usr/include/linux/soundcard.h: 385
try:
    CTL_HOLD = 0x40
except:
    pass

# /usr/include/linux/soundcard.h: 386
try:
    CTL_PORTAMENTO = 0x41
except:
    pass

# /usr/include/linux/soundcard.h: 387
try:
    CTL_SOSTENUTO = 0x42
except:
    pass

# /usr/include/linux/soundcard.h: 388
try:
    CTL_SOFT_PEDAL = 0x43
except:
    pass

# /usr/include/linux/soundcard.h: 390
try:
    CTL_HOLD2 = 0x45
except:
    pass

# /usr/include/linux/soundcard.h: 393
try:
    CTL_GENERAL_PURPOSE5 = 0x50
except:
    pass

# /usr/include/linux/soundcard.h: 394
try:
    CTL_GENERAL_PURPOSE6 = 0x51
except:
    pass

# /usr/include/linux/soundcard.h: 395
try:
    CTL_GENERAL_PURPOSE7 = 0x52
except:
    pass

# /usr/include/linux/soundcard.h: 396
try:
    CTL_GENERAL_PURPOSE8 = 0x53
except:
    pass

# /usr/include/linux/soundcard.h: 398
try:
    CTL_EXT_EFF_DEPTH = 0x5b
except:
    pass

# /usr/include/linux/soundcard.h: 399
try:
    CTL_TREMOLO_DEPTH = 0x5c
except:
    pass

# /usr/include/linux/soundcard.h: 400
try:
    CTL_CHORUS_DEPTH = 0x5d
except:
    pass

# /usr/include/linux/soundcard.h: 401
try:
    CTL_DETUNE_DEPTH = 0x5e
except:
    pass

# /usr/include/linux/soundcard.h: 402
try:
    CTL_CELESTE_DEPTH = 0x5e
except:
    pass

# /usr/include/linux/soundcard.h: 403
try:
    CTL_PHASER_DEPTH = 0x5f
except:
    pass

# /usr/include/linux/soundcard.h: 404
try:
    CTL_DATA_INCREMENT = 0x60
except:
    pass

# /usr/include/linux/soundcard.h: 405
try:
    CTL_DATA_DECREMENT = 0x61
except:
    pass

# /usr/include/linux/soundcard.h: 406
try:
    CTL_NONREG_PARM_NUM_LSB = 0x62
except:
    pass

# /usr/include/linux/soundcard.h: 407
try:
    CTL_NONREG_PARM_NUM_MSB = 0x63
except:
    pass

# /usr/include/linux/soundcard.h: 408
try:
    CTL_REGIST_PARM_NUM_LSB = 0x64
except:
    pass

# /usr/include/linux/soundcard.h: 409
try:
    CTL_REGIST_PARM_NUM_MSB = 0x65
except:
    pass

# /usr/include/linux/soundcard.h: 414
try:
    CTRL_PITCH_BENDER = 255
except:
    pass

# /usr/include/linux/soundcard.h: 415
try:
    CTRL_PITCH_BENDER_RANGE = 254
except:
    pass

# /usr/include/linux/soundcard.h: 416
try:
    CTRL_EXPRESSION = 253
except:
    pass

# /usr/include/linux/soundcard.h: 417
try:
    CTRL_MAIN_VOLUME = 252
except:
    pass

# /usr/include/linux/soundcard.h: 418
try:
    SEQ_BALANCE = 11
except:
    pass

# /usr/include/linux/soundcard.h: 419
try:
    SEQ_VOLMODE = 12
except:
    pass

# /usr/include/linux/soundcard.h: 425
try:
    VOL_METHOD_ADAGIO = 1
except:
    pass

# /usr/include/linux/soundcard.h: 426
try:
    VOL_METHOD_LINEAR = 2
except:
    pass

# /usr/include/linux/soundcard.h: 437
try:
    SEQ_FULLSIZE = 0xfd
except:
    pass

# /usr/include/linux/soundcard.h: 458
try:
    SEQ_PRIVATE = 0xfe
except:
    pass

# /usr/include/linux/soundcard.h: 459
try:
    SEQ_EXTENDED = 0xff
except:
    pass

# /usr/include/linux/soundcard.h: 469
try:
    FM_PATCH = (_PATCHKEY (0x01))
except:
    pass

# /usr/include/linux/soundcard.h: 470
try:
    OPL3_PATCH = (_PATCHKEY (0x03))
except:
    pass

# /usr/include/linux/soundcard.h: 480
try:
    SYNTH_TYPE_FM = 0
except:
    pass

# /usr/include/linux/soundcard.h: 481
try:
    SYNTH_TYPE_SAMPLE = 1
except:
    pass

# /usr/include/linux/soundcard.h: 482
try:
    SYNTH_TYPE_MIDI = 2
except:
    pass

# /usr/include/linux/soundcard.h: 485
try:
    FM_TYPE_ADLIB = 0x00
except:
    pass

# /usr/include/linux/soundcard.h: 486
try:
    FM_TYPE_OPL3 = 0x01
except:
    pass

# /usr/include/linux/soundcard.h: 487
try:
    MIDI_TYPE_MPU401 = 0x401
except:
    pass

# /usr/include/linux/soundcard.h: 489
try:
    SAMPLE_TYPE_BASIC = 0x10
except:
    pass

# /usr/include/linux/soundcard.h: 490
try:
    SAMPLE_TYPE_GUS = SAMPLE_TYPE_BASIC
except:
    pass

# /usr/include/linux/soundcard.h: 491
try:
    SAMPLE_TYPE_WAVEFRONT = 0x11
except:
    pass

# /usr/include/linux/soundcard.h: 498
try:
    SYNTH_CAP_PERCMODE = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 499
try:
    SYNTH_CAP_OPL3 = 0x00000002
except:
    pass

# /usr/include/linux/soundcard.h: 500
try:
    SYNTH_CAP_INPUT = 0x00000004
except:
    pass

# /usr/include/linux/soundcard.h: 509
try:
    MIDI_CAP_MPU401 = 1
except:
    pass

# /usr/include/linux/soundcard.h: 528
try:
    SNDCTL_MIDI_PRETIME = (_SIOWR ('m', 0, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 529
try:
    SNDCTL_MIDI_MPUMODE = (_SIOWR ('m', 1, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 530
try:
    SNDCTL_MIDI_MPUCMD = (_SIOWR ('m', 2, mpu_command_rec))
except:
    pass

# /usr/include/linux/soundcard.h: 536
try:
    SNDCTL_DSP_RESET = (_SIO ('P', 0))
except:
    pass

# /usr/include/linux/soundcard.h: 537
try:
    SNDCTL_DSP_SYNC = (_SIO ('P', 1))
except:
    pass

# /usr/include/linux/soundcard.h: 538
try:
    SNDCTL_DSP_SPEED = (_SIOWR ('P', 2, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 539
try:
    SNDCTL_DSP_STEREO = (_SIOWR ('P', 3, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 540
try:
    SNDCTL_DSP_GETBLKSIZE = (_SIOWR ('P', 4, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 541
try:
    SNDCTL_DSP_SAMPLESIZE = SNDCTL_DSP_SETFMT
except:
    pass

# /usr/include/linux/soundcard.h: 542
try:
    SNDCTL_DSP_CHANNELS = (_SIOWR ('P', 6, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 543
try:
    SOUND_PCM_WRITE_CHANNELS = SNDCTL_DSP_CHANNELS
except:
    pass

# /usr/include/linux/soundcard.h: 544
try:
    SOUND_PCM_WRITE_FILTER = (_SIOWR ('P', 7, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 545
try:
    SNDCTL_DSP_POST = (_SIO ('P', 8))
except:
    pass

# /usr/include/linux/soundcard.h: 546
try:
    SNDCTL_DSP_SUBDIVIDE = (_SIOWR ('P', 9, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 547
try:
    SNDCTL_DSP_SETFRAGMENT = (_SIOWR ('P', 10, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 550
try:
    SNDCTL_DSP_GETFMTS = (_SIOR ('P', 11, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 551
try:
    SNDCTL_DSP_SETFMT = (_SIOWR ('P', 5, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 552
try:
    AFMT_QUERY = 0x00000000
except:
    pass

# /usr/include/linux/soundcard.h: 553
try:
    AFMT_MU_LAW = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 554
try:
    AFMT_A_LAW = 0x00000002
except:
    pass

# /usr/include/linux/soundcard.h: 555
try:
    AFMT_IMA_ADPCM = 0x00000004
except:
    pass

# /usr/include/linux/soundcard.h: 556
try:
    AFMT_U8 = 0x00000008
except:
    pass

# /usr/include/linux/soundcard.h: 557
try:
    AFMT_S16_LE = 0x00000010
except:
    pass

# /usr/include/linux/soundcard.h: 558
try:
    AFMT_S16_BE = 0x00000020
except:
    pass

# /usr/include/linux/soundcard.h: 559
try:
    AFMT_S8 = 0x00000040
except:
    pass

# /usr/include/linux/soundcard.h: 560
try:
    AFMT_U16_LE = 0x00000080
except:
    pass

# /usr/include/linux/soundcard.h: 561
try:
    AFMT_U16_BE = 0x00000100
except:
    pass

# /usr/include/linux/soundcard.h: 562
try:
    AFMT_MPEG = 0x00000200
except:
    pass

# /usr/include/linux/soundcard.h: 563
try:
    AFMT_AC3 = 0x00000400
except:
    pass

# /usr/include/linux/soundcard.h: 577
try:
    SNDCTL_DSP_GETOSPACE = (_SIOR ('P', 12, audio_buf_info))
except:
    pass

# /usr/include/linux/soundcard.h: 578
try:
    SNDCTL_DSP_GETISPACE = (_SIOR ('P', 13, audio_buf_info))
except:
    pass

# /usr/include/linux/soundcard.h: 579
try:
    SNDCTL_DSP_NONBLOCK = (_SIO ('P', 14))
except:
    pass

# /usr/include/linux/soundcard.h: 580
try:
    SNDCTL_DSP_GETCAPS = (_SIOR ('P', 15, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 581
try:
    DSP_CAP_REVISION = 0x000000ff
except:
    pass

# /usr/include/linux/soundcard.h: 582
try:
    DSP_CAP_DUPLEX = 0x00000100
except:
    pass

# /usr/include/linux/soundcard.h: 583
try:
    DSP_CAP_REALTIME = 0x00000200
except:
    pass

# /usr/include/linux/soundcard.h: 584
try:
    DSP_CAP_BATCH = 0x00000400
except:
    pass

# /usr/include/linux/soundcard.h: 588
try:
    DSP_CAP_COPROC = 0x00000800
except:
    pass

# /usr/include/linux/soundcard.h: 591
try:
    DSP_CAP_TRIGGER = 0x00001000
except:
    pass

# /usr/include/linux/soundcard.h: 592
try:
    DSP_CAP_MMAP = 0x00002000
except:
    pass

# /usr/include/linux/soundcard.h: 593
try:
    DSP_CAP_MULTI = 0x00004000
except:
    pass

# /usr/include/linux/soundcard.h: 594
try:
    DSP_CAP_BIND = 0x00008000
except:
    pass

# /usr/include/linux/soundcard.h: 597
try:
    SNDCTL_DSP_GETTRIGGER = (_SIOR ('P', 16, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 598
try:
    SNDCTL_DSP_SETTRIGGER = (_SIOW ('P', 16, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 599
try:
    PCM_ENABLE_INPUT = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 600
try:
    PCM_ENABLE_OUTPUT = 0x00000002
except:
    pass

# /usr/include/linux/soundcard.h: 608
try:
    SNDCTL_DSP_GETIPTR = (_SIOR ('P', 17, count_info))
except:
    pass

# /usr/include/linux/soundcard.h: 609
try:
    SNDCTL_DSP_GETOPTR = (_SIOR ('P', 18, count_info))
except:
    pass

# /usr/include/linux/soundcard.h: 615
try:
    SNDCTL_DSP_MAPINBUF = (_SIOR ('P', 19, buffmem_desc))
except:
    pass

# /usr/include/linux/soundcard.h: 616
try:
    SNDCTL_DSP_MAPOUTBUF = (_SIOR ('P', 20, buffmem_desc))
except:
    pass

# /usr/include/linux/soundcard.h: 617
try:
    SNDCTL_DSP_SETSYNCRO = (_SIO ('P', 21))
except:
    pass

# /usr/include/linux/soundcard.h: 618
try:
    SNDCTL_DSP_SETDUPLEX = (_SIO ('P', 22))
except:
    pass

# /usr/include/linux/soundcard.h: 619
try:
    SNDCTL_DSP_GETODELAY = (_SIOR ('P', 23, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 621
try:
    SNDCTL_DSP_GETCHANNELMASK = (_SIOWR ('P', 64, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 622
try:
    SNDCTL_DSP_BIND_CHANNEL = (_SIOWR ('P', 65, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 623
try:
    DSP_BIND_QUERY = 0x00000000
except:
    pass

# /usr/include/linux/soundcard.h: 624
try:
    DSP_BIND_FRONT = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 625
try:
    DSP_BIND_SURR = 0x00000002
except:
    pass

# /usr/include/linux/soundcard.h: 626
try:
    DSP_BIND_CENTER_LFE = 0x00000004
except:
    pass

# /usr/include/linux/soundcard.h: 627
try:
    DSP_BIND_HANDSET = 0x00000008
except:
    pass

# /usr/include/linux/soundcard.h: 628
try:
    DSP_BIND_MIC = 0x00000010
except:
    pass

# /usr/include/linux/soundcard.h: 629
try:
    DSP_BIND_MODEM1 = 0x00000020
except:
    pass

# /usr/include/linux/soundcard.h: 630
try:
    DSP_BIND_MODEM2 = 0x00000040
except:
    pass

# /usr/include/linux/soundcard.h: 631
try:
    DSP_BIND_I2S = 0x00000080
except:
    pass

# /usr/include/linux/soundcard.h: 632
try:
    DSP_BIND_SPDIF = 0x00000100
except:
    pass

# /usr/include/linux/soundcard.h: 634
try:
    SNDCTL_DSP_SETSPDIF = (_SIOW ('P', 66, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 635
try:
    SNDCTL_DSP_GETSPDIF = (_SIOR ('P', 67, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 636
try:
    SPDIF_PRO = 0x0001
except:
    pass

# /usr/include/linux/soundcard.h: 637
try:
    SPDIF_N_AUD = 0x0002
except:
    pass

# /usr/include/linux/soundcard.h: 638
try:
    SPDIF_COPY = 0x0004
except:
    pass

# /usr/include/linux/soundcard.h: 639
try:
    SPDIF_PRE = 0x0008
except:
    pass

# /usr/include/linux/soundcard.h: 640
try:
    SPDIF_CC = 0x07f0
except:
    pass

# /usr/include/linux/soundcard.h: 641
try:
    SPDIF_L = 0x0800
except:
    pass

# /usr/include/linux/soundcard.h: 642
try:
    SPDIF_DRS = 0x4000
except:
    pass

# /usr/include/linux/soundcard.h: 643
try:
    SPDIF_V = 0x8000
except:
    pass

# /usr/include/linux/soundcard.h: 656
try:
    SNDCTL_DSP_PROFILE = (_SIOW ('P', 23, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 657
try:
    APF_NORMAL = 0
except:
    pass

# /usr/include/linux/soundcard.h: 658
try:
    APF_NETWORK = 1
except:
    pass

# /usr/include/linux/soundcard.h: 659
try:
    APF_CPUINTENS = 2
except:
    pass

# /usr/include/linux/soundcard.h: 661
try:
    SOUND_PCM_READ_RATE = (_SIOR ('P', 2, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 662
try:
    SOUND_PCM_READ_CHANNELS = (_SIOR ('P', 6, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 663
try:
    SOUND_PCM_READ_BITS = (_SIOR ('P', 5, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 664
try:
    SOUND_PCM_READ_FILTER = (_SIOR ('P', 7, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 667
try:
    SOUND_PCM_WRITE_BITS = SNDCTL_DSP_SETFMT
except:
    pass

# /usr/include/linux/soundcard.h: 668
try:
    SOUND_PCM_WRITE_RATE = SNDCTL_DSP_SPEED
except:
    pass

# /usr/include/linux/soundcard.h: 669
try:
    SOUND_PCM_POST = SNDCTL_DSP_POST
except:
    pass

# /usr/include/linux/soundcard.h: 670
try:
    SOUND_PCM_RESET = SNDCTL_DSP_RESET
except:
    pass

# /usr/include/linux/soundcard.h: 671
try:
    SOUND_PCM_SYNC = SNDCTL_DSP_SYNC
except:
    pass

# /usr/include/linux/soundcard.h: 672
try:
    SOUND_PCM_SUBDIVIDE = SNDCTL_DSP_SUBDIVIDE
except:
    pass

# /usr/include/linux/soundcard.h: 673
try:
    SOUND_PCM_SETFRAGMENT = SNDCTL_DSP_SETFRAGMENT
except:
    pass

# /usr/include/linux/soundcard.h: 674
try:
    SOUND_PCM_GETFMTS = SNDCTL_DSP_GETFMTS
except:
    pass

# /usr/include/linux/soundcard.h: 675
try:
    SOUND_PCM_SETFMT = SNDCTL_DSP_SETFMT
except:
    pass

# /usr/include/linux/soundcard.h: 676
try:
    SOUND_PCM_GETOSPACE = SNDCTL_DSP_GETOSPACE
except:
    pass

# /usr/include/linux/soundcard.h: 677
try:
    SOUND_PCM_GETISPACE = SNDCTL_DSP_GETISPACE
except:
    pass

# /usr/include/linux/soundcard.h: 678
try:
    SOUND_PCM_NONBLOCK = SNDCTL_DSP_NONBLOCK
except:
    pass

# /usr/include/linux/soundcard.h: 679
try:
    SOUND_PCM_GETCAPS = SNDCTL_DSP_GETCAPS
except:
    pass

# /usr/include/linux/soundcard.h: 680
try:
    SOUND_PCM_GETTRIGGER = SNDCTL_DSP_GETTRIGGER
except:
    pass

# /usr/include/linux/soundcard.h: 681
try:
    SOUND_PCM_SETTRIGGER = SNDCTL_DSP_SETTRIGGER
except:
    pass

# /usr/include/linux/soundcard.h: 682
try:
    SOUND_PCM_SETSYNCRO = SNDCTL_DSP_SETSYNCRO
except:
    pass

# /usr/include/linux/soundcard.h: 683
try:
    SOUND_PCM_GETIPTR = SNDCTL_DSP_GETIPTR
except:
    pass

# /usr/include/linux/soundcard.h: 684
try:
    SOUND_PCM_GETOPTR = SNDCTL_DSP_GETOPTR
except:
    pass

# /usr/include/linux/soundcard.h: 685
try:
    SOUND_PCM_MAPINBUF = SNDCTL_DSP_MAPINBUF
except:
    pass

# /usr/include/linux/soundcard.h: 686
try:
    SOUND_PCM_MAPOUTBUF = SNDCTL_DSP_MAPOUTBUF
except:
    pass

# /usr/include/linux/soundcard.h: 696
try:
    CPF_NONE = 0x0000
except:
    pass

# /usr/include/linux/soundcard.h: 697
try:
    CPF_FIRST = 0x0001
except:
    pass

# /usr/include/linux/soundcard.h: 698
try:
    CPF_LAST = 0x0002
except:
    pass

# /usr/include/linux/soundcard.h: 718
try:
    SNDCTL_COPR_RESET = (_SIO ('C', 0))
except:
    pass

# /usr/include/linux/soundcard.h: 719
try:
    SNDCTL_COPR_LOAD = (_SIOWR ('C', 1, copr_buffer))
except:
    pass

# /usr/include/linux/soundcard.h: 720
try:
    SNDCTL_COPR_RDATA = (_SIOWR ('C', 2, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 721
try:
    SNDCTL_COPR_RCODE = (_SIOWR ('C', 3, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 722
try:
    SNDCTL_COPR_WDATA = (_SIOW ('C', 4, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 723
try:
    SNDCTL_COPR_WCODE = (_SIOW ('C', 5, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 724
try:
    SNDCTL_COPR_RUN = (_SIOWR ('C', 6, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 725
try:
    SNDCTL_COPR_HALT = (_SIOWR ('C', 7, copr_debug_buf))
except:
    pass

# /usr/include/linux/soundcard.h: 726
try:
    SNDCTL_COPR_SENDMSG = (_SIOWR ('C', 8, copr_msg))
except:
    pass

# /usr/include/linux/soundcard.h: 727
try:
    SNDCTL_COPR_RCVMSG = (_SIOR ('C', 9, copr_msg))
except:
    pass

# /usr/include/linux/soundcard.h: 742
try:
    SOUND_MIXER_NRDEVICES = 25
except:
    pass

# /usr/include/linux/soundcard.h: 743
try:
    SOUND_MIXER_VOLUME = 0
except:
    pass

# /usr/include/linux/soundcard.h: 744
try:
    SOUND_MIXER_BASS = 1
except:
    pass

# /usr/include/linux/soundcard.h: 745
try:
    SOUND_MIXER_TREBLE = 2
except:
    pass

# /usr/include/linux/soundcard.h: 746
try:
    SOUND_MIXER_SYNTH = 3
except:
    pass

# /usr/include/linux/soundcard.h: 747
try:
    SOUND_MIXER_PCM = 4
except:
    pass

# /usr/include/linux/soundcard.h: 748
try:
    SOUND_MIXER_SPEAKER = 5
except:
    pass

# /usr/include/linux/soundcard.h: 749
try:
    SOUND_MIXER_LINE = 6
except:
    pass

# /usr/include/linux/soundcard.h: 750
try:
    SOUND_MIXER_MIC = 7
except:
    pass

# /usr/include/linux/soundcard.h: 751
try:
    SOUND_MIXER_CD = 8
except:
    pass

# /usr/include/linux/soundcard.h: 752
try:
    SOUND_MIXER_IMIX = 9
except:
    pass

# /usr/include/linux/soundcard.h: 753
try:
    SOUND_MIXER_ALTPCM = 10
except:
    pass

# /usr/include/linux/soundcard.h: 754
try:
    SOUND_MIXER_RECLEV = 11
except:
    pass

# /usr/include/linux/soundcard.h: 755
try:
    SOUND_MIXER_IGAIN = 12
except:
    pass

# /usr/include/linux/soundcard.h: 756
try:
    SOUND_MIXER_OGAIN = 13
except:
    pass

# /usr/include/linux/soundcard.h: 763
try:
    SOUND_MIXER_LINE1 = 14
except:
    pass

# /usr/include/linux/soundcard.h: 764
try:
    SOUND_MIXER_LINE2 = 15
except:
    pass

# /usr/include/linux/soundcard.h: 765
try:
    SOUND_MIXER_LINE3 = 16
except:
    pass

# /usr/include/linux/soundcard.h: 766
try:
    SOUND_MIXER_DIGITAL1 = 17
except:
    pass

# /usr/include/linux/soundcard.h: 767
try:
    SOUND_MIXER_DIGITAL2 = 18
except:
    pass

# /usr/include/linux/soundcard.h: 768
try:
    SOUND_MIXER_DIGITAL3 = 19
except:
    pass

# /usr/include/linux/soundcard.h: 769
try:
    SOUND_MIXER_PHONEIN = 20
except:
    pass

# /usr/include/linux/soundcard.h: 770
try:
    SOUND_MIXER_PHONEOUT = 21
except:
    pass

# /usr/include/linux/soundcard.h: 771
try:
    SOUND_MIXER_VIDEO = 22
except:
    pass

# /usr/include/linux/soundcard.h: 772
try:
    SOUND_MIXER_RADIO = 23
except:
    pass

# /usr/include/linux/soundcard.h: 773
try:
    SOUND_MIXER_MONITOR = 24
except:
    pass

# /usr/include/linux/soundcard.h: 777
try:
    SOUND_ONOFF_MIN = 28
except:
    pass

# /usr/include/linux/soundcard.h: 778
try:
    SOUND_ONOFF_MAX = 30
except:
    pass

# /usr/include/linux/soundcard.h: 781
try:
    SOUND_MIXER_NONE = 31
except:
    pass

# /usr/include/linux/soundcard.h: 787
try:
    SOUND_MIXER_ENHANCE = SOUND_MIXER_NONE
except:
    pass

# /usr/include/linux/soundcard.h: 788
try:
    SOUND_MIXER_MUTE = SOUND_MIXER_NONE
except:
    pass

# /usr/include/linux/soundcard.h: 789
try:
    SOUND_MIXER_LOUD = SOUND_MIXER_NONE
except:
    pass

# /usr/include/linux/soundcard.h: 804
try:
    SOUND_MIXER_RECSRC = 0xff
except:
    pass

# /usr/include/linux/soundcard.h: 805
try:
    SOUND_MIXER_DEVMASK = 0xfe
except:
    pass

# /usr/include/linux/soundcard.h: 806
try:
    SOUND_MIXER_RECMASK = 0xfd
except:
    pass

# /usr/include/linux/soundcard.h: 807
try:
    SOUND_MIXER_CAPS = 0xfc
except:
    pass

# /usr/include/linux/soundcard.h: 808
try:
    SOUND_CAP_EXCL_INPUT = 0x00000001
except:
    pass

# /usr/include/linux/soundcard.h: 809
try:
    SOUND_MIXER_STEREODEVS = 0xfb
except:
    pass

# /usr/include/linux/soundcard.h: 810
try:
    SOUND_MIXER_OUTSRC = 0xfa
except:
    pass

# /usr/include/linux/soundcard.h: 811
try:
    SOUND_MIXER_OUTMASK = 0xf9
except:
    pass

# /usr/include/linux/soundcard.h: 815
try:
    SOUND_MASK_VOLUME = (1 << SOUND_MIXER_VOLUME)
except:
    pass

# /usr/include/linux/soundcard.h: 816
try:
    SOUND_MASK_BASS = (1 << SOUND_MIXER_BASS)
except:
    pass

# /usr/include/linux/soundcard.h: 817
try:
    SOUND_MASK_TREBLE = (1 << SOUND_MIXER_TREBLE)
except:
    pass

# /usr/include/linux/soundcard.h: 818
try:
    SOUND_MASK_SYNTH = (1 << SOUND_MIXER_SYNTH)
except:
    pass

# /usr/include/linux/soundcard.h: 819
try:
    SOUND_MASK_PCM = (1 << SOUND_MIXER_PCM)
except:
    pass

# /usr/include/linux/soundcard.h: 820
try:
    SOUND_MASK_SPEAKER = (1 << SOUND_MIXER_SPEAKER)
except:
    pass

# /usr/include/linux/soundcard.h: 821
try:
    SOUND_MASK_LINE = (1 << SOUND_MIXER_LINE)
except:
    pass

# /usr/include/linux/soundcard.h: 822
try:
    SOUND_MASK_MIC = (1 << SOUND_MIXER_MIC)
except:
    pass

# /usr/include/linux/soundcard.h: 823
try:
    SOUND_MASK_CD = (1 << SOUND_MIXER_CD)
except:
    pass

# /usr/include/linux/soundcard.h: 824
try:
    SOUND_MASK_IMIX = (1 << SOUND_MIXER_IMIX)
except:
    pass

# /usr/include/linux/soundcard.h: 825
try:
    SOUND_MASK_ALTPCM = (1 << SOUND_MIXER_ALTPCM)
except:
    pass

# /usr/include/linux/soundcard.h: 826
try:
    SOUND_MASK_RECLEV = (1 << SOUND_MIXER_RECLEV)
except:
    pass

# /usr/include/linux/soundcard.h: 827
try:
    SOUND_MASK_IGAIN = (1 << SOUND_MIXER_IGAIN)
except:
    pass

# /usr/include/linux/soundcard.h: 828
try:
    SOUND_MASK_OGAIN = (1 << SOUND_MIXER_OGAIN)
except:
    pass

# /usr/include/linux/soundcard.h: 829
try:
    SOUND_MASK_LINE1 = (1 << SOUND_MIXER_LINE1)
except:
    pass

# /usr/include/linux/soundcard.h: 830
try:
    SOUND_MASK_LINE2 = (1 << SOUND_MIXER_LINE2)
except:
    pass

# /usr/include/linux/soundcard.h: 831
try:
    SOUND_MASK_LINE3 = (1 << SOUND_MIXER_LINE3)
except:
    pass

# /usr/include/linux/soundcard.h: 832
try:
    SOUND_MASK_DIGITAL1 = (1 << SOUND_MIXER_DIGITAL1)
except:
    pass

# /usr/include/linux/soundcard.h: 833
try:
    SOUND_MASK_DIGITAL2 = (1 << SOUND_MIXER_DIGITAL2)
except:
    pass

# /usr/include/linux/soundcard.h: 834
try:
    SOUND_MASK_DIGITAL3 = (1 << SOUND_MIXER_DIGITAL3)
except:
    pass

# /usr/include/linux/soundcard.h: 835
try:
    SOUND_MASK_PHONEIN = (1 << SOUND_MIXER_PHONEIN)
except:
    pass

# /usr/include/linux/soundcard.h: 836
try:
    SOUND_MASK_PHONEOUT = (1 << SOUND_MIXER_PHONEOUT)
except:
    pass

# /usr/include/linux/soundcard.h: 837
try:
    SOUND_MASK_RADIO = (1 << SOUND_MIXER_RADIO)
except:
    pass

# /usr/include/linux/soundcard.h: 838
try:
    SOUND_MASK_VIDEO = (1 << SOUND_MIXER_VIDEO)
except:
    pass

# /usr/include/linux/soundcard.h: 839
try:
    SOUND_MASK_MONITOR = (1 << SOUND_MIXER_MONITOR)
except:
    pass

# /usr/include/linux/soundcard.h: 842
try:
    SOUND_MASK_MUTE = (1 << SOUND_MIXER_MUTE)
except:
    pass

# /usr/include/linux/soundcard.h: 843
try:
    SOUND_MASK_ENHANCE = (1 << SOUND_MIXER_ENHANCE)
except:
    pass

# /usr/include/linux/soundcard.h: 844
try:
    SOUND_MASK_LOUD = (1 << SOUND_MIXER_LOUD)
except:
    pass

# /usr/include/linux/soundcard.h: 846
def MIXER_READ(dev):
    return (_SIOR ('M', dev, c_int))

# /usr/include/linux/soundcard.h: 847
try:
    SOUND_MIXER_READ_VOLUME = (MIXER_READ (SOUND_MIXER_VOLUME))
except:
    pass

# /usr/include/linux/soundcard.h: 848
try:
    SOUND_MIXER_READ_BASS = (MIXER_READ (SOUND_MIXER_BASS))
except:
    pass

# /usr/include/linux/soundcard.h: 849
try:
    SOUND_MIXER_READ_TREBLE = (MIXER_READ (SOUND_MIXER_TREBLE))
except:
    pass

# /usr/include/linux/soundcard.h: 850
try:
    SOUND_MIXER_READ_SYNTH = (MIXER_READ (SOUND_MIXER_SYNTH))
except:
    pass

# /usr/include/linux/soundcard.h: 851
try:
    SOUND_MIXER_READ_PCM = (MIXER_READ (SOUND_MIXER_PCM))
except:
    pass

# /usr/include/linux/soundcard.h: 852
try:
    SOUND_MIXER_READ_SPEAKER = (MIXER_READ (SOUND_MIXER_SPEAKER))
except:
    pass

# /usr/include/linux/soundcard.h: 853
try:
    SOUND_MIXER_READ_LINE = (MIXER_READ (SOUND_MIXER_LINE))
except:
    pass

# /usr/include/linux/soundcard.h: 854
try:
    SOUND_MIXER_READ_MIC = (MIXER_READ (SOUND_MIXER_MIC))
except:
    pass

# /usr/include/linux/soundcard.h: 855
try:
    SOUND_MIXER_READ_CD = (MIXER_READ (SOUND_MIXER_CD))
except:
    pass

# /usr/include/linux/soundcard.h: 856
try:
    SOUND_MIXER_READ_IMIX = (MIXER_READ (SOUND_MIXER_IMIX))
except:
    pass

# /usr/include/linux/soundcard.h: 857
try:
    SOUND_MIXER_READ_ALTPCM = (MIXER_READ (SOUND_MIXER_ALTPCM))
except:
    pass

# /usr/include/linux/soundcard.h: 858
try:
    SOUND_MIXER_READ_RECLEV = (MIXER_READ (SOUND_MIXER_RECLEV))
except:
    pass

# /usr/include/linux/soundcard.h: 859
try:
    SOUND_MIXER_READ_IGAIN = (MIXER_READ (SOUND_MIXER_IGAIN))
except:
    pass

# /usr/include/linux/soundcard.h: 860
try:
    SOUND_MIXER_READ_OGAIN = (MIXER_READ (SOUND_MIXER_OGAIN))
except:
    pass

# /usr/include/linux/soundcard.h: 861
try:
    SOUND_MIXER_READ_LINE1 = (MIXER_READ (SOUND_MIXER_LINE1))
except:
    pass

# /usr/include/linux/soundcard.h: 862
try:
    SOUND_MIXER_READ_LINE2 = (MIXER_READ (SOUND_MIXER_LINE2))
except:
    pass

# /usr/include/linux/soundcard.h: 863
try:
    SOUND_MIXER_READ_LINE3 = (MIXER_READ (SOUND_MIXER_LINE3))
except:
    pass

# /usr/include/linux/soundcard.h: 866
try:
    SOUND_MIXER_READ_MUTE = (MIXER_READ (SOUND_MIXER_MUTE))
except:
    pass

# /usr/include/linux/soundcard.h: 867
try:
    SOUND_MIXER_READ_ENHANCE = (MIXER_READ (SOUND_MIXER_ENHANCE))
except:
    pass

# /usr/include/linux/soundcard.h: 868
try:
    SOUND_MIXER_READ_LOUD = (MIXER_READ (SOUND_MIXER_LOUD))
except:
    pass

# /usr/include/linux/soundcard.h: 870
try:
    SOUND_MIXER_READ_RECSRC = (MIXER_READ (SOUND_MIXER_RECSRC))
except:
    pass

# /usr/include/linux/soundcard.h: 871
try:
    SOUND_MIXER_READ_DEVMASK = (MIXER_READ (SOUND_MIXER_DEVMASK))
except:
    pass

# /usr/include/linux/soundcard.h: 872
try:
    SOUND_MIXER_READ_RECMASK = (MIXER_READ (SOUND_MIXER_RECMASK))
except:
    pass

# /usr/include/linux/soundcard.h: 873
try:
    SOUND_MIXER_READ_STEREODEVS = (MIXER_READ (SOUND_MIXER_STEREODEVS))
except:
    pass

# /usr/include/linux/soundcard.h: 874
try:
    SOUND_MIXER_READ_CAPS = (MIXER_READ (SOUND_MIXER_CAPS))
except:
    pass

# /usr/include/linux/soundcard.h: 876
def MIXER_WRITE(dev):
    return (_SIOWR ('M', dev, c_int))

# /usr/include/linux/soundcard.h: 877
try:
    SOUND_MIXER_WRITE_VOLUME = (MIXER_WRITE (SOUND_MIXER_VOLUME))
except:
    pass

# /usr/include/linux/soundcard.h: 878
try:
    SOUND_MIXER_WRITE_BASS = (MIXER_WRITE (SOUND_MIXER_BASS))
except:
    pass

# /usr/include/linux/soundcard.h: 879
try:
    SOUND_MIXER_WRITE_TREBLE = (MIXER_WRITE (SOUND_MIXER_TREBLE))
except:
    pass

# /usr/include/linux/soundcard.h: 880
try:
    SOUND_MIXER_WRITE_SYNTH = (MIXER_WRITE (SOUND_MIXER_SYNTH))
except:
    pass

# /usr/include/linux/soundcard.h: 881
try:
    SOUND_MIXER_WRITE_PCM = (MIXER_WRITE (SOUND_MIXER_PCM))
except:
    pass

# /usr/include/linux/soundcard.h: 882
try:
    SOUND_MIXER_WRITE_SPEAKER = (MIXER_WRITE (SOUND_MIXER_SPEAKER))
except:
    pass

# /usr/include/linux/soundcard.h: 883
try:
    SOUND_MIXER_WRITE_LINE = (MIXER_WRITE (SOUND_MIXER_LINE))
except:
    pass

# /usr/include/linux/soundcard.h: 884
try:
    SOUND_MIXER_WRITE_MIC = (MIXER_WRITE (SOUND_MIXER_MIC))
except:
    pass

# /usr/include/linux/soundcard.h: 885
try:
    SOUND_MIXER_WRITE_CD = (MIXER_WRITE (SOUND_MIXER_CD))
except:
    pass

# /usr/include/linux/soundcard.h: 886
try:
    SOUND_MIXER_WRITE_IMIX = (MIXER_WRITE (SOUND_MIXER_IMIX))
except:
    pass

# /usr/include/linux/soundcard.h: 887
try:
    SOUND_MIXER_WRITE_ALTPCM = (MIXER_WRITE (SOUND_MIXER_ALTPCM))
except:
    pass

# /usr/include/linux/soundcard.h: 888
try:
    SOUND_MIXER_WRITE_RECLEV = (MIXER_WRITE (SOUND_MIXER_RECLEV))
except:
    pass

# /usr/include/linux/soundcard.h: 889
try:
    SOUND_MIXER_WRITE_IGAIN = (MIXER_WRITE (SOUND_MIXER_IGAIN))
except:
    pass

# /usr/include/linux/soundcard.h: 890
try:
    SOUND_MIXER_WRITE_OGAIN = (MIXER_WRITE (SOUND_MIXER_OGAIN))
except:
    pass

# /usr/include/linux/soundcard.h: 891
try:
    SOUND_MIXER_WRITE_LINE1 = (MIXER_WRITE (SOUND_MIXER_LINE1))
except:
    pass

# /usr/include/linux/soundcard.h: 892
try:
    SOUND_MIXER_WRITE_LINE2 = (MIXER_WRITE (SOUND_MIXER_LINE2))
except:
    pass

# /usr/include/linux/soundcard.h: 893
try:
    SOUND_MIXER_WRITE_LINE3 = (MIXER_WRITE (SOUND_MIXER_LINE3))
except:
    pass

# /usr/include/linux/soundcard.h: 896
try:
    SOUND_MIXER_WRITE_MUTE = (MIXER_WRITE (SOUND_MIXER_MUTE))
except:
    pass

# /usr/include/linux/soundcard.h: 897
try:
    SOUND_MIXER_WRITE_ENHANCE = (MIXER_WRITE (SOUND_MIXER_ENHANCE))
except:
    pass

# /usr/include/linux/soundcard.h: 898
try:
    SOUND_MIXER_WRITE_LOUD = (MIXER_WRITE (SOUND_MIXER_LOUD))
except:
    pass

# /usr/include/linux/soundcard.h: 900
try:
    SOUND_MIXER_WRITE_RECSRC = (MIXER_WRITE (SOUND_MIXER_RECSRC))
except:
    pass

# /usr/include/linux/soundcard.h: 916
try:
    SOUND_MIXER_INFO = (_SIOR ('M', 101, mixer_info))
except:
    pass

# /usr/include/linux/soundcard.h: 917
try:
    SOUND_OLD_MIXER_INFO = (_SIOR ('M', 101, _old_mixer_info))
except:
    pass

# /usr/include/linux/soundcard.h: 927
try:
    SOUND_MIXER_ACCESS = (_SIOWR ('M', 102, mixer_record))
except:
    pass

# /usr/include/linux/soundcard.h: 932
try:
    SOUND_MIXER_AGC = (_SIOWR ('M', 103, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 933
try:
    SOUND_MIXER_3DSE = (_SIOWR ('M', 104, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 939
try:
    SOUND_MIXER_PRIVATE1 = (_SIOWR ('M', 111, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 940
try:
    SOUND_MIXER_PRIVATE2 = (_SIOWR ('M', 112, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 941
try:
    SOUND_MIXER_PRIVATE3 = (_SIOWR ('M', 113, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 942
try:
    SOUND_MIXER_PRIVATE4 = (_SIOWR ('M', 114, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 943
try:
    SOUND_MIXER_PRIVATE5 = (_SIOWR ('M', 115, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 959
try:
    SOUND_MIXER_GETLEVELS = (_SIOWR ('M', 116, mixer_vol_table))
except:
    pass

# /usr/include/linux/soundcard.h: 960
try:
    SOUND_MIXER_SETLEVELS = (_SIOWR ('M', 117, mixer_vol_table))
except:
    pass

# /usr/include/linux/soundcard.h: 968
try:
    OSS_GETVERSION = (_SIOR ('M', 118, c_int))
except:
    pass

# /usr/include/linux/soundcard.h: 988
try:
    EV_SEQ_LOCAL = 0x80
except:
    pass

# /usr/include/linux/soundcard.h: 989
try:
    EV_TIMING = 0x81
except:
    pass

# /usr/include/linux/soundcard.h: 990
try:
    EV_CHN_COMMON = 0x92
except:
    pass

# /usr/include/linux/soundcard.h: 991
try:
    EV_CHN_VOICE = 0x93
except:
    pass

# /usr/include/linux/soundcard.h: 992
try:
    EV_SYSEX = 0x94
except:
    pass

# /usr/include/linux/soundcard.h: 1002
try:
    MIDI_NOTEOFF = 0x80
except:
    pass

# /usr/include/linux/soundcard.h: 1003
try:
    MIDI_NOTEON = 0x90
except:
    pass

# /usr/include/linux/soundcard.h: 1004
try:
    MIDI_KEY_PRESSURE = 0xA0
except:
    pass

# /usr/include/linux/soundcard.h: 1010
try:
    MIDI_CTL_CHANGE = 0xB0
except:
    pass

# /usr/include/linux/soundcard.h: 1011
try:
    MIDI_PGM_CHANGE = 0xC0
except:
    pass

# /usr/include/linux/soundcard.h: 1012
try:
    MIDI_CHN_PRESSURE = 0xD0
except:
    pass

# /usr/include/linux/soundcard.h: 1013
try:
    MIDI_PITCH_BEND = 0xE0
except:
    pass

# /usr/include/linux/soundcard.h: 1015
try:
    MIDI_SYSTEM_PREFIX = 0xF0
except:
    pass

# /usr/include/linux/soundcard.h: 1020
try:
    TMR_WAIT_REL = 1
except:
    pass

# /usr/include/linux/soundcard.h: 1021
try:
    TMR_WAIT_ABS = 2
except:
    pass

# /usr/include/linux/soundcard.h: 1022
try:
    TMR_STOP = 3
except:
    pass

# /usr/include/linux/soundcard.h: 1023
try:
    TMR_START = 4
except:
    pass

# /usr/include/linux/soundcard.h: 1024
try:
    TMR_CONTINUE = 5
except:
    pass

# /usr/include/linux/soundcard.h: 1025
try:
    TMR_TEMPO = 6
except:
    pass

# /usr/include/linux/soundcard.h: 1026
try:
    TMR_ECHO = 8
except:
    pass

# /usr/include/linux/soundcard.h: 1027
try:
    TMR_CLOCK = 9
except:
    pass

# /usr/include/linux/soundcard.h: 1028
try:
    TMR_SPP = 10
except:
    pass

# /usr/include/linux/soundcard.h: 1029
try:
    TMR_TIMESIG = 11
except:
    pass

# /usr/include/linux/soundcard.h: 1034
try:
    LOCL_STARTAUDIO = 1
except:
    pass

# /usr/include/linux/soundcard.h: 1089
try:
    SEQ_DUMPBUF = seqbuf_dump
except:
    pass

# /usr/include/linux/soundcard.h: 1273
def SEQ_WRPATCH2(patchx, len):
    return (SEQ_DUMPBUF ())

# /usr/include/x86_64-linux-gnu/sys/stat.h: 23
try:
    _SYS_STAT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 104
try:
    S_IFMT = __S_IFMT
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 105
try:
    S_IFDIR = __S_IFDIR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 106
try:
    S_IFCHR = __S_IFCHR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 107
try:
    S_IFBLK = __S_IFBLK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 108
try:
    S_IFREG = __S_IFREG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 110
try:
    S_IFIFO = __S_IFIFO
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 113
try:
    S_IFLNK = __S_IFLNK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 117
try:
    S_IFSOCK = __S_IFSOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 123
def __S_ISTYPE(mode, mask):
    return ((mode & __S_IFMT) == mask)

# /usr/include/x86_64-linux-gnu/sys/stat.h: 125
def S_ISDIR(mode):
    return (__S_ISTYPE (mode, __S_IFDIR))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 126
def S_ISCHR(mode):
    return (__S_ISTYPE (mode, __S_IFCHR))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 127
def S_ISBLK(mode):
    return (__S_ISTYPE (mode, __S_IFBLK))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 128
def S_ISREG(mode):
    return (__S_ISTYPE (mode, __S_IFREG))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 130
def S_ISFIFO(mode):
    return (__S_ISTYPE (mode, __S_IFIFO))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 133
def S_ISLNK(mode):
    return (__S_ISTYPE (mode, __S_IFLNK))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 142
def S_ISSOCK(mode):
    return (__S_ISTYPE (mode, __S_IFSOCK))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 152
def S_TYPEISMQ(buf):
    return (__S_TYPEISMQ (buf))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 153
def S_TYPEISSEM(buf):
    return (__S_TYPEISSEM (buf))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 154
def S_TYPEISSHM(buf):
    return (__S_TYPEISSHM (buf))

# /usr/include/x86_64-linux-gnu/sys/stat.h: 160
try:
    S_ISUID = __S_ISUID
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 161
try:
    S_ISGID = __S_ISGID
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 165
try:
    S_ISVTX = __S_ISVTX
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 168
try:
    S_IRUSR = __S_IREAD
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 169
try:
    S_IWUSR = __S_IWRITE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 170
try:
    S_IXUSR = __S_IEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 172
try:
    S_IRWXU = ((__S_IREAD | __S_IWRITE) | __S_IEXEC)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 175
try:
    S_IREAD = S_IRUSR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 176
try:
    S_IWRITE = S_IWUSR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 177
try:
    S_IEXEC = S_IXUSR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 180
try:
    S_IRGRP = (S_IRUSR >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 181
try:
    S_IWGRP = (S_IWUSR >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 182
try:
    S_IXGRP = (S_IXUSR >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 184
try:
    S_IRWXG = (S_IRWXU >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 186
try:
    S_IROTH = (S_IRGRP >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 187
try:
    S_IWOTH = (S_IWGRP >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 188
try:
    S_IXOTH = (S_IXGRP >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 190
try:
    S_IRWXO = (S_IRWXG >> 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 195
try:
    ACCESSPERMS = ((S_IRWXU | S_IRWXG) | S_IRWXO)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 196
try:
    ALLPERMS = (((((S_ISUID | S_ISGID) | S_ISVTX) | S_IRWXU) | S_IRWXG) | S_IRWXO)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 197
try:
    DEFFILEMODE = (((((S_IRUSR | S_IWUSR) | S_IRGRP) | S_IWGRP) | S_IROTH) | S_IWOTH)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 199
try:
    S_BLKSIZE = 512
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/stat.h: 390
try:
    _MKNOD_VER = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/statfs.h: 20
try:
    _SYS_STATFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/statvfs.h: 20
try:
    _SYS_STATVFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 83
try:
    ST_RDONLY = ST_RDONLY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 85
try:
    ST_NOSUID = ST_NOSUID
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/swap.h: 21
try:
    _SYS_SWAP_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/swap.h: 27
try:
    SWAP_FLAG_PREFER = 0x8000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/swap.h: 28
try:
    SWAP_FLAG_PRIO_MASK = 0x7fff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/swap.h: 29
try:
    SWAP_FLAG_PRIO_SHIFT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/swap.h: 30
try:
    SWAP_FLAG_DISCARD = 0x10000
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syscall.h: 19
try:
    _SYSCALL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd.h: 13
try:
    __X32_SYSCALL_BIT = 0x40000000
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 4
try:
    __NR_read = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 5
try:
    __NR_write = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 6
try:
    __NR_open = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 7
try:
    __NR_close = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 8
try:
    __NR_stat = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 9
try:
    __NR_fstat = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 10
try:
    __NR_lstat = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 11
try:
    __NR_poll = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 12
try:
    __NR_lseek = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 13
try:
    __NR_mmap = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 14
try:
    __NR_mprotect = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 15
try:
    __NR_munmap = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 16
try:
    __NR_brk = 12
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 17
try:
    __NR_rt_sigaction = 13
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 18
try:
    __NR_rt_sigprocmask = 14
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 19
try:
    __NR_rt_sigreturn = 15
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 20
try:
    __NR_ioctl = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 21
try:
    __NR_pread64 = 17
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 22
try:
    __NR_pwrite64 = 18
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 23
try:
    __NR_readv = 19
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 24
try:
    __NR_writev = 20
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 25
try:
    __NR_access = 21
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 26
try:
    __NR_pipe = 22
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 27
try:
    __NR_select = 23
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 28
try:
    __NR_sched_yield = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 29
try:
    __NR_mremap = 25
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 30
try:
    __NR_msync = 26
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 31
try:
    __NR_mincore = 27
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 32
try:
    __NR_madvise = 28
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 33
try:
    __NR_shmget = 29
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 34
try:
    __NR_shmat = 30
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 35
try:
    __NR_shmctl = 31
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 36
try:
    __NR_dup = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 37
try:
    __NR_dup2 = 33
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 38
try:
    __NR_pause = 34
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 39
try:
    __NR_nanosleep = 35
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 40
try:
    __NR_getitimer = 36
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 41
try:
    __NR_alarm = 37
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 42
try:
    __NR_setitimer = 38
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 43
try:
    __NR_getpid = 39
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 44
try:
    __NR_sendfile = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 45
try:
    __NR_socket = 41
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 46
try:
    __NR_connect = 42
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 47
try:
    __NR_accept = 43
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 48
try:
    __NR_sendto = 44
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 49
try:
    __NR_recvfrom = 45
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 50
try:
    __NR_sendmsg = 46
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 51
try:
    __NR_recvmsg = 47
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 52
try:
    __NR_shutdown = 48
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 53
try:
    __NR_bind = 49
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 54
try:
    __NR_listen = 50
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 55
try:
    __NR_getsockname = 51
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 56
try:
    __NR_getpeername = 52
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 57
try:
    __NR_socketpair = 53
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 58
try:
    __NR_setsockopt = 54
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 59
try:
    __NR_getsockopt = 55
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 60
try:
    __NR_clone = 56
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 61
try:
    __NR_fork = 57
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 62
try:
    __NR_vfork = 58
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 63
try:
    __NR_execve = 59
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 64
try:
    __NR_exit = 60
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 65
try:
    __NR_wait4 = 61
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 66
try:
    __NR_kill = 62
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 67
try:
    __NR_uname = 63
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 68
try:
    __NR_semget = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 69
try:
    __NR_semop = 65
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 70
try:
    __NR_semctl = 66
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 71
try:
    __NR_shmdt = 67
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 72
try:
    __NR_msgget = 68
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 73
try:
    __NR_msgsnd = 69
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 74
try:
    __NR_msgrcv = 70
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 75
try:
    __NR_msgctl = 71
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 76
try:
    __NR_fcntl = 72
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 77
try:
    __NR_flock = 73
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 78
try:
    __NR_fsync = 74
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 79
try:
    __NR_fdatasync = 75
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 80
try:
    __NR_truncate = 76
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 81
try:
    __NR_ftruncate = 77
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 82
try:
    __NR_getdents = 78
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 83
try:
    __NR_getcwd = 79
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 84
try:
    __NR_chdir = 80
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 85
try:
    __NR_fchdir = 81
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 86
try:
    __NR_rename = 82
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 87
try:
    __NR_mkdir = 83
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 88
try:
    __NR_rmdir = 84
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 89
try:
    __NR_creat = 85
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 90
try:
    __NR_link = 86
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 91
try:
    __NR_unlink = 87
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 92
try:
    __NR_symlink = 88
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 93
try:
    __NR_readlink = 89
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 94
try:
    __NR_chmod = 90
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 95
try:
    __NR_fchmod = 91
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 96
try:
    __NR_chown = 92
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 97
try:
    __NR_fchown = 93
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 98
try:
    __NR_lchown = 94
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 99
try:
    __NR_umask = 95
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 100
try:
    __NR_gettimeofday = 96
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 101
try:
    __NR_getrlimit = 97
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 102
try:
    __NR_getrusage = 98
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 103
try:
    __NR_sysinfo = 99
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 104
try:
    __NR_times = 100
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 105
try:
    __NR_ptrace = 101
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 106
try:
    __NR_getuid = 102
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 107
try:
    __NR_syslog = 103
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 108
try:
    __NR_getgid = 104
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 109
try:
    __NR_setuid = 105
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 110
try:
    __NR_setgid = 106
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 111
try:
    __NR_geteuid = 107
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 112
try:
    __NR_getegid = 108
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 113
try:
    __NR_setpgid = 109
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 114
try:
    __NR_getppid = 110
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 115
try:
    __NR_getpgrp = 111
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 116
try:
    __NR_setsid = 112
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 117
try:
    __NR_setreuid = 113
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 118
try:
    __NR_setregid = 114
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 119
try:
    __NR_getgroups = 115
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 120
try:
    __NR_setgroups = 116
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 121
try:
    __NR_setresuid = 117
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 122
try:
    __NR_getresuid = 118
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 123
try:
    __NR_setresgid = 119
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 124
try:
    __NR_getresgid = 120
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 125
try:
    __NR_getpgid = 121
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 126
try:
    __NR_setfsuid = 122
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 127
try:
    __NR_setfsgid = 123
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 128
try:
    __NR_getsid = 124
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 129
try:
    __NR_capget = 125
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 130
try:
    __NR_capset = 126
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 131
try:
    __NR_rt_sigpending = 127
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 132
try:
    __NR_rt_sigtimedwait = 128
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 133
try:
    __NR_rt_sigqueueinfo = 129
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 134
try:
    __NR_rt_sigsuspend = 130
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 135
try:
    __NR_sigaltstack = 131
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 136
try:
    __NR_utime = 132
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 137
try:
    __NR_mknod = 133
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 138
try:
    __NR_uselib = 134
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 139
try:
    __NR_personality = 135
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 140
try:
    __NR_ustat = 136
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 141
try:
    __NR_statfs = 137
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 142
try:
    __NR_fstatfs = 138
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 143
try:
    __NR_sysfs = 139
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 144
try:
    __NR_getpriority = 140
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 145
try:
    __NR_setpriority = 141
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 146
try:
    __NR_sched_setparam = 142
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 147
try:
    __NR_sched_getparam = 143
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 148
try:
    __NR_sched_setscheduler = 144
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 149
try:
    __NR_sched_getscheduler = 145
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 150
try:
    __NR_sched_get_priority_max = 146
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 151
try:
    __NR_sched_get_priority_min = 147
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 152
try:
    __NR_sched_rr_get_interval = 148
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 153
try:
    __NR_mlock = 149
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 154
try:
    __NR_munlock = 150
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 155
try:
    __NR_mlockall = 151
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 156
try:
    __NR_munlockall = 152
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 157
try:
    __NR_vhangup = 153
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 158
try:
    __NR_modify_ldt = 154
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 159
try:
    __NR_pivot_root = 155
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 160
try:
    __NR__sysctl = 156
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 161
try:
    __NR_prctl = 157
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 162
try:
    __NR_arch_prctl = 158
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 163
try:
    __NR_adjtimex = 159
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 164
try:
    __NR_setrlimit = 160
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 165
try:
    __NR_chroot = 161
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 166
try:
    __NR_sync = 162
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 167
try:
    __NR_acct = 163
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 168
try:
    __NR_settimeofday = 164
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 169
try:
    __NR_mount = 165
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 170
try:
    __NR_umount2 = 166
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 171
try:
    __NR_swapon = 167
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 172
try:
    __NR_swapoff = 168
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 173
try:
    __NR_reboot = 169
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 174
try:
    __NR_sethostname = 170
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 175
try:
    __NR_setdomainname = 171
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 176
try:
    __NR_iopl = 172
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 177
try:
    __NR_ioperm = 173
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 178
try:
    __NR_create_module = 174
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 179
try:
    __NR_init_module = 175
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 180
try:
    __NR_delete_module = 176
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 181
try:
    __NR_get_kernel_syms = 177
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 182
try:
    __NR_query_module = 178
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 183
try:
    __NR_quotactl = 179
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 184
try:
    __NR_nfsservctl = 180
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 185
try:
    __NR_getpmsg = 181
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 186
try:
    __NR_putpmsg = 182
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 187
try:
    __NR_afs_syscall = 183
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 188
try:
    __NR_tuxcall = 184
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 189
try:
    __NR_security = 185
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 190
try:
    __NR_gettid = 186
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 191
try:
    __NR_readahead = 187
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 192
try:
    __NR_setxattr = 188
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 193
try:
    __NR_lsetxattr = 189
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 194
try:
    __NR_fsetxattr = 190
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 195
try:
    __NR_getxattr = 191
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 196
try:
    __NR_lgetxattr = 192
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 197
try:
    __NR_fgetxattr = 193
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 198
try:
    __NR_listxattr = 194
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 199
try:
    __NR_llistxattr = 195
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 200
try:
    __NR_flistxattr = 196
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 201
try:
    __NR_removexattr = 197
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 202
try:
    __NR_lremovexattr = 198
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 203
try:
    __NR_fremovexattr = 199
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 204
try:
    __NR_tkill = 200
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 205
try:
    __NR_time = 201
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 206
try:
    __NR_futex = 202
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 207
try:
    __NR_sched_setaffinity = 203
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 208
try:
    __NR_sched_getaffinity = 204
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 209
try:
    __NR_set_thread_area = 205
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 210
try:
    __NR_io_setup = 206
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 211
try:
    __NR_io_destroy = 207
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 212
try:
    __NR_io_getevents = 208
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 213
try:
    __NR_io_submit = 209
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 214
try:
    __NR_io_cancel = 210
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 215
try:
    __NR_get_thread_area = 211
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 216
try:
    __NR_lookup_dcookie = 212
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 217
try:
    __NR_epoll_create = 213
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 218
try:
    __NR_epoll_ctl_old = 214
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 219
try:
    __NR_epoll_wait_old = 215
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 220
try:
    __NR_remap_file_pages = 216
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 221
try:
    __NR_getdents64 = 217
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 222
try:
    __NR_set_tid_address = 218
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 223
try:
    __NR_restart_syscall = 219
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 224
try:
    __NR_semtimedop = 220
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 225
try:
    __NR_fadvise64 = 221
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 226
try:
    __NR_timer_create = 222
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 227
try:
    __NR_timer_settime = 223
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 228
try:
    __NR_timer_gettime = 224
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 229
try:
    __NR_timer_getoverrun = 225
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 230
try:
    __NR_timer_delete = 226
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 231
try:
    __NR_clock_settime = 227
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 232
try:
    __NR_clock_gettime = 228
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 233
try:
    __NR_clock_getres = 229
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 234
try:
    __NR_clock_nanosleep = 230
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 235
try:
    __NR_exit_group = 231
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 236
try:
    __NR_epoll_wait = 232
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 237
try:
    __NR_epoll_ctl = 233
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 238
try:
    __NR_tgkill = 234
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 239
try:
    __NR_utimes = 235
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 240
try:
    __NR_vserver = 236
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 241
try:
    __NR_mbind = 237
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 242
try:
    __NR_set_mempolicy = 238
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 243
try:
    __NR_get_mempolicy = 239
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 244
try:
    __NR_mq_open = 240
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 245
try:
    __NR_mq_unlink = 241
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 246
try:
    __NR_mq_timedsend = 242
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 247
try:
    __NR_mq_timedreceive = 243
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 248
try:
    __NR_mq_notify = 244
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 249
try:
    __NR_mq_getsetattr = 245
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 250
try:
    __NR_kexec_load = 246
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 251
try:
    __NR_waitid = 247
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 252
try:
    __NR_add_key = 248
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 253
try:
    __NR_request_key = 249
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 254
try:
    __NR_keyctl = 250
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 255
try:
    __NR_ioprio_set = 251
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 256
try:
    __NR_ioprio_get = 252
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 257
try:
    __NR_inotify_init = 253
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 258
try:
    __NR_inotify_add_watch = 254
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 259
try:
    __NR_inotify_rm_watch = 255
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 260
try:
    __NR_migrate_pages = 256
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 261
try:
    __NR_openat = 257
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 262
try:
    __NR_mkdirat = 258
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 263
try:
    __NR_mknodat = 259
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 264
try:
    __NR_fchownat = 260
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 265
try:
    __NR_futimesat = 261
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 266
try:
    __NR_newfstatat = 262
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 267
try:
    __NR_unlinkat = 263
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 268
try:
    __NR_renameat = 264
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 269
try:
    __NR_linkat = 265
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 270
try:
    __NR_symlinkat = 266
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 271
try:
    __NR_readlinkat = 267
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 272
try:
    __NR_fchmodat = 268
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 273
try:
    __NR_faccessat = 269
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 274
try:
    __NR_pselect6 = 270
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 275
try:
    __NR_ppoll = 271
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 276
try:
    __NR_unshare = 272
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 277
try:
    __NR_set_robust_list = 273
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 278
try:
    __NR_get_robust_list = 274
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 279
try:
    __NR_splice = 275
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 280
try:
    __NR_tee = 276
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 281
try:
    __NR_sync_file_range = 277
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 282
try:
    __NR_vmsplice = 278
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 283
try:
    __NR_move_pages = 279
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 284
try:
    __NR_utimensat = 280
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 285
try:
    __NR_epoll_pwait = 281
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 286
try:
    __NR_signalfd = 282
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 287
try:
    __NR_timerfd_create = 283
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 288
try:
    __NR_eventfd = 284
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 289
try:
    __NR_fallocate = 285
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 290
try:
    __NR_timerfd_settime = 286
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 291
try:
    __NR_timerfd_gettime = 287
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 292
try:
    __NR_accept4 = 288
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 293
try:
    __NR_signalfd4 = 289
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 294
try:
    __NR_eventfd2 = 290
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 295
try:
    __NR_epoll_create1 = 291
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 296
try:
    __NR_dup3 = 292
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 297
try:
    __NR_pipe2 = 293
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 298
try:
    __NR_inotify_init1 = 294
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 299
try:
    __NR_preadv = 295
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 300
try:
    __NR_pwritev = 296
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 301
try:
    __NR_rt_tgsigqueueinfo = 297
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 302
try:
    __NR_perf_event_open = 298
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 303
try:
    __NR_recvmmsg = 299
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 304
try:
    __NR_fanotify_init = 300
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 305
try:
    __NR_fanotify_mark = 301
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 306
try:
    __NR_prlimit64 = 302
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 307
try:
    __NR_name_to_handle_at = 303
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 308
try:
    __NR_open_by_handle_at = 304
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 309
try:
    __NR_clock_adjtime = 305
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 310
try:
    __NR_syncfs = 306
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 311
try:
    __NR_sendmmsg = 307
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 312
try:
    __NR_setns = 308
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 313
try:
    __NR_getcpu = 309
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 314
try:
    __NR_process_vm_readv = 310
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 315
try:
    __NR_process_vm_writev = 311
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 316
try:
    __NR_kcmp = 312
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 317
try:
    __NR_finit_module = 313
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 318
try:
    __NR_sched_setattr = 314
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 319
try:
    __NR_sched_getattr = 315
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 320
try:
    __NR_renameat2 = 316
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 321
try:
    __NR_seccomp = 317
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 322
try:
    __NR_getrandom = 318
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 323
try:
    __NR_memfd_create = 319
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 324
try:
    __NR_kexec_file_load = 320
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 325
try:
    __NR_bpf = 321
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 326
try:
    __NR_execveat = 322
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 327
try:
    __NR_userfaultfd = 323
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 328
try:
    __NR_membarrier = 324
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 329
try:
    __NR_mlock2 = 325
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 330
try:
    __NR_copy_file_range = 326
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 331
try:
    __NR_preadv2 = 327
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 332
try:
    __NR_pwritev2 = 328
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 333
try:
    __NR_pkey_mprotect = 329
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 334
try:
    __NR_pkey_alloc = 330
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 335
try:
    __NR_pkey_free = 331
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 336
try:
    __NR_statx = 332
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 337
try:
    __NR_io_pgetevents = 333
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 338
try:
    __NR_rseq = 334
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 339
try:
    __NR_pidfd_send_signal = 424
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 340
try:
    __NR_io_uring_setup = 425
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 341
try:
    __NR_io_uring_enter = 426
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 342
try:
    __NR_io_uring_register = 427
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 343
try:
    __NR_open_tree = 428
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 344
try:
    __NR_move_mount = 429
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 345
try:
    __NR_fsopen = 430
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 346
try:
    __NR_fsconfig = 431
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 347
try:
    __NR_fsmount = 432
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 348
try:
    __NR_fspick = 433
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 349
try:
    __NR_pidfd_open = 434
except:
    pass

# /usr/include/x86_64-linux-gnu/asm/unistd_64.h: 350
try:
    __NR_clone3 = 435
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 8
try:
    __GLIBC_LINUX_VERSION_CODE = 328960
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 31
try:
    SYS__sysctl = __NR__sysctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 35
try:
    SYS_accept = __NR_accept
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 39
try:
    SYS_accept4 = __NR_accept4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 43
try:
    SYS_access = __NR_access
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 47
try:
    SYS_acct = __NR_acct
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 59
try:
    SYS_add_key = __NR_add_key
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 63
try:
    SYS_adjtimex = __NR_adjtimex
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 67
try:
    SYS_afs_syscall = __NR_afs_syscall
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 71
try:
    SYS_alarm = __NR_alarm
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 79
try:
    SYS_arch_prctl = __NR_arch_prctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 107
try:
    SYS_bind = __NR_bind
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 111
try:
    SYS_bpf = __NR_bpf
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 123
try:
    SYS_brk = __NR_brk
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 135
try:
    SYS_capget = __NR_capget
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 139
try:
    SYS_capset = __NR_capset
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 143
try:
    SYS_chdir = __NR_chdir
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 147
try:
    SYS_chmod = __NR_chmod
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 151
try:
    SYS_chown = __NR_chown
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 159
try:
    SYS_chroot = __NR_chroot
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 163
try:
    SYS_clock_adjtime = __NR_clock_adjtime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 171
try:
    SYS_clock_getres = __NR_clock_getres
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 179
try:
    SYS_clock_gettime = __NR_clock_gettime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 187
try:
    SYS_clock_nanosleep = __NR_clock_nanosleep
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 195
try:
    SYS_clock_settime = __NR_clock_settime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 203
try:
    SYS_clone = __NR_clone
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 211
try:
    SYS_clone3 = __NR_clone3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 215
try:
    SYS_close = __NR_close
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 223
try:
    SYS_connect = __NR_connect
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 227
try:
    SYS_copy_file_range = __NR_copy_file_range
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 231
try:
    SYS_creat = __NR_creat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 235
try:
    SYS_create_module = __NR_create_module
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 239
try:
    SYS_delete_module = __NR_delete_module
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 247
try:
    SYS_dup = __NR_dup
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 251
try:
    SYS_dup2 = __NR_dup2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 255
try:
    SYS_dup3 = __NR_dup3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 259
try:
    SYS_epoll_create = __NR_epoll_create
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 263
try:
    SYS_epoll_create1 = __NR_epoll_create1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 267
try:
    SYS_epoll_ctl = __NR_epoll_ctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 271
try:
    SYS_epoll_ctl_old = __NR_epoll_ctl_old
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 275
try:
    SYS_epoll_pwait = __NR_epoll_pwait
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 279
try:
    SYS_epoll_wait = __NR_epoll_wait
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 283
try:
    SYS_epoll_wait_old = __NR_epoll_wait_old
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 287
try:
    SYS_eventfd = __NR_eventfd
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 291
try:
    SYS_eventfd2 = __NR_eventfd2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 303
try:
    SYS_execve = __NR_execve
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 307
try:
    SYS_execveat = __NR_execveat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 311
try:
    SYS_exit = __NR_exit
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 315
try:
    SYS_exit_group = __NR_exit_group
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 319
try:
    SYS_faccessat = __NR_faccessat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 323
try:
    SYS_fadvise64 = __NR_fadvise64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 331
try:
    SYS_fallocate = __NR_fallocate
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 335
try:
    SYS_fanotify_init = __NR_fanotify_init
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 339
try:
    SYS_fanotify_mark = __NR_fanotify_mark
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 343
try:
    SYS_fchdir = __NR_fchdir
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 347
try:
    SYS_fchmod = __NR_fchmod
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 351
try:
    SYS_fchmodat = __NR_fchmodat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 355
try:
    SYS_fchown = __NR_fchown
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 363
try:
    SYS_fchownat = __NR_fchownat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 367
try:
    SYS_fcntl = __NR_fcntl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 375
try:
    SYS_fdatasync = __NR_fdatasync
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 379
try:
    SYS_fgetxattr = __NR_fgetxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 383
try:
    SYS_finit_module = __NR_finit_module
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 387
try:
    SYS_flistxattr = __NR_flistxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 391
try:
    SYS_flock = __NR_flock
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 395
try:
    SYS_fork = __NR_fork
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 407
try:
    SYS_fremovexattr = __NR_fremovexattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 411
try:
    SYS_fsconfig = __NR_fsconfig
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 415
try:
    SYS_fsetxattr = __NR_fsetxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 419
try:
    SYS_fsmount = __NR_fsmount
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 423
try:
    SYS_fsopen = __NR_fsopen
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 427
try:
    SYS_fspick = __NR_fspick
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 431
try:
    SYS_fstat = __NR_fstat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 443
try:
    SYS_fstatfs = __NR_fstatfs
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 451
try:
    SYS_fsync = __NR_fsync
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 459
try:
    SYS_ftruncate = __NR_ftruncate
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 467
try:
    SYS_futex = __NR_futex
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 475
try:
    SYS_futimesat = __NR_futimesat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 479
try:
    SYS_get_kernel_syms = __NR_get_kernel_syms
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 483
try:
    SYS_get_mempolicy = __NR_get_mempolicy
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 487
try:
    SYS_get_robust_list = __NR_get_robust_list
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 491
try:
    SYS_get_thread_area = __NR_get_thread_area
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 499
try:
    SYS_getcpu = __NR_getcpu
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 503
try:
    SYS_getcwd = __NR_getcwd
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 507
try:
    SYS_getdents = __NR_getdents
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 511
try:
    SYS_getdents64 = __NR_getdents64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 523
try:
    SYS_getegid = __NR_getegid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 531
try:
    SYS_geteuid = __NR_geteuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 539
try:
    SYS_getgid = __NR_getgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 547
try:
    SYS_getgroups = __NR_getgroups
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 559
try:
    SYS_getitimer = __NR_getitimer
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 567
try:
    SYS_getpeername = __NR_getpeername
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 571
try:
    SYS_getpgid = __NR_getpgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 575
try:
    SYS_getpgrp = __NR_getpgrp
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 579
try:
    SYS_getpid = __NR_getpid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 583
try:
    SYS_getpmsg = __NR_getpmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 587
try:
    SYS_getppid = __NR_getppid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 591
try:
    SYS_getpriority = __NR_getpriority
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 595
try:
    SYS_getrandom = __NR_getrandom
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 599
try:
    SYS_getresgid = __NR_getresgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 607
try:
    SYS_getresuid = __NR_getresuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 615
try:
    SYS_getrlimit = __NR_getrlimit
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 619
try:
    SYS_getrusage = __NR_getrusage
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 623
try:
    SYS_getsid = __NR_getsid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 627
try:
    SYS_getsockname = __NR_getsockname
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 631
try:
    SYS_getsockopt = __NR_getsockopt
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 635
try:
    SYS_gettid = __NR_gettid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 639
try:
    SYS_gettimeofday = __NR_gettimeofday
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 643
try:
    SYS_getuid = __NR_getuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 655
try:
    SYS_getxattr = __NR_getxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 679
try:
    SYS_init_module = __NR_init_module
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 683
try:
    SYS_inotify_add_watch = __NR_inotify_add_watch
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 687
try:
    SYS_inotify_init = __NR_inotify_init
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 691
try:
    SYS_inotify_init1 = __NR_inotify_init1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 695
try:
    SYS_inotify_rm_watch = __NR_inotify_rm_watch
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 699
try:
    SYS_io_cancel = __NR_io_cancel
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 703
try:
    SYS_io_destroy = __NR_io_destroy
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 707
try:
    SYS_io_getevents = __NR_io_getevents
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 711
try:
    SYS_io_pgetevents = __NR_io_pgetevents
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 719
try:
    SYS_io_setup = __NR_io_setup
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 723
try:
    SYS_io_submit = __NR_io_submit
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 727
try:
    SYS_io_uring_enter = __NR_io_uring_enter
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 731
try:
    SYS_io_uring_register = __NR_io_uring_register
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 735
try:
    SYS_io_uring_setup = __NR_io_uring_setup
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 739
try:
    SYS_ioctl = __NR_ioctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 743
try:
    SYS_ioperm = __NR_ioperm
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 747
try:
    SYS_iopl = __NR_iopl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 751
try:
    SYS_ioprio_get = __NR_ioprio_get
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 755
try:
    SYS_ioprio_set = __NR_ioprio_set
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 763
try:
    SYS_kcmp = __NR_kcmp
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 771
try:
    SYS_kexec_file_load = __NR_kexec_file_load
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 775
try:
    SYS_kexec_load = __NR_kexec_load
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 779
try:
    SYS_keyctl = __NR_keyctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 783
try:
    SYS_kill = __NR_kill
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 787
try:
    SYS_lchown = __NR_lchown
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 795
try:
    SYS_lgetxattr = __NR_lgetxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 799
try:
    SYS_link = __NR_link
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 803
try:
    SYS_linkat = __NR_linkat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 807
try:
    SYS_listen = __NR_listen
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 811
try:
    SYS_listxattr = __NR_listxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 815
try:
    SYS_llistxattr = __NR_llistxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 827
try:
    SYS_lookup_dcookie = __NR_lookup_dcookie
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 831
try:
    SYS_lremovexattr = __NR_lremovexattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 835
try:
    SYS_lseek = __NR_lseek
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 839
try:
    SYS_lsetxattr = __NR_lsetxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 843
try:
    SYS_lstat = __NR_lstat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 851
try:
    SYS_madvise = __NR_madvise
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 855
try:
    SYS_mbind = __NR_mbind
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 859
try:
    SYS_membarrier = __NR_membarrier
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 863
try:
    SYS_memfd_create = __NR_memfd_create
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 871
try:
    SYS_migrate_pages = __NR_migrate_pages
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 875
try:
    SYS_mincore = __NR_mincore
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 879
try:
    SYS_mkdir = __NR_mkdir
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 883
try:
    SYS_mkdirat = __NR_mkdirat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 887
try:
    SYS_mknod = __NR_mknod
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 891
try:
    SYS_mknodat = __NR_mknodat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 895
try:
    SYS_mlock = __NR_mlock
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 899
try:
    SYS_mlock2 = __NR_mlock2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 903
try:
    SYS_mlockall = __NR_mlockall
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 907
try:
    SYS_mmap = __NR_mmap
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 915
try:
    SYS_modify_ldt = __NR_modify_ldt
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 919
try:
    SYS_mount = __NR_mount
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 923
try:
    SYS_move_mount = __NR_move_mount
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 927
try:
    SYS_move_pages = __NR_move_pages
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 931
try:
    SYS_mprotect = __NR_mprotect
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 939
try:
    SYS_mq_getsetattr = __NR_mq_getsetattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 943
try:
    SYS_mq_notify = __NR_mq_notify
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 947
try:
    SYS_mq_open = __NR_mq_open
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 951
try:
    SYS_mq_timedreceive = __NR_mq_timedreceive
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 959
try:
    SYS_mq_timedsend = __NR_mq_timedsend
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 967
try:
    SYS_mq_unlink = __NR_mq_unlink
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 971
try:
    SYS_mremap = __NR_mremap
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 975
try:
    SYS_msgctl = __NR_msgctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 979
try:
    SYS_msgget = __NR_msgget
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 983
try:
    SYS_msgrcv = __NR_msgrcv
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 987
try:
    SYS_msgsnd = __NR_msgsnd
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 991
try:
    SYS_msync = __NR_msync
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 999
try:
    SYS_munlock = __NR_munlock
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1003
try:
    SYS_munlockall = __NR_munlockall
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1007
try:
    SYS_munmap = __NR_munmap
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1011
try:
    SYS_name_to_handle_at = __NR_name_to_handle_at
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1015
try:
    SYS_nanosleep = __NR_nanosleep
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1019
try:
    SYS_newfstatat = __NR_newfstatat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1023
try:
    SYS_nfsservctl = __NR_nfsservctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1067
try:
    SYS_open = __NR_open
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1071
try:
    SYS_open_by_handle_at = __NR_open_by_handle_at
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1075
try:
    SYS_open_tree = __NR_open_tree
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1079
try:
    SYS_openat = __NR_openat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1523
try:
    SYS_pause = __NR_pause
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1539
try:
    SYS_perf_event_open = __NR_perf_event_open
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1551
try:
    SYS_personality = __NR_personality
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1555
try:
    SYS_pidfd_open = __NR_pidfd_open
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1559
try:
    SYS_pidfd_send_signal = __NR_pidfd_send_signal
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1563
try:
    SYS_pipe = __NR_pipe
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1567
try:
    SYS_pipe2 = __NR_pipe2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1571
try:
    SYS_pivot_root = __NR_pivot_root
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1575
try:
    SYS_pkey_alloc = __NR_pkey_alloc
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1579
try:
    SYS_pkey_free = __NR_pkey_free
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1583
try:
    SYS_pkey_mprotect = __NR_pkey_mprotect
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1587
try:
    SYS_poll = __NR_poll
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1591
try:
    SYS_ppoll = __NR_ppoll
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1599
try:
    SYS_prctl = __NR_prctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1603
try:
    SYS_pread64 = __NR_pread64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1607
try:
    SYS_preadv = __NR_preadv
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1611
try:
    SYS_preadv2 = __NR_preadv2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1615
try:
    SYS_prlimit64 = __NR_prlimit64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1619
try:
    SYS_process_vm_readv = __NR_process_vm_readv
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1623
try:
    SYS_process_vm_writev = __NR_process_vm_writev
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1635
try:
    SYS_pselect6 = __NR_pselect6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1643
try:
    SYS_ptrace = __NR_ptrace
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1647
try:
    SYS_putpmsg = __NR_putpmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1651
try:
    SYS_pwrite64 = __NR_pwrite64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1655
try:
    SYS_pwritev = __NR_pwritev
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1659
try:
    SYS_pwritev2 = __NR_pwritev2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1663
try:
    SYS_query_module = __NR_query_module
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1667
try:
    SYS_quotactl = __NR_quotactl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1671
try:
    SYS_read = __NR_read
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1675
try:
    SYS_readahead = __NR_readahead
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1683
try:
    SYS_readlink = __NR_readlink
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1687
try:
    SYS_readlinkat = __NR_readlinkat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1691
try:
    SYS_readv = __NR_readv
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1695
try:
    SYS_reboot = __NR_reboot
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1703
try:
    SYS_recvfrom = __NR_recvfrom
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1707
try:
    SYS_recvmmsg = __NR_recvmmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1715
try:
    SYS_recvmsg = __NR_recvmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1719
try:
    SYS_remap_file_pages = __NR_remap_file_pages
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1723
try:
    SYS_removexattr = __NR_removexattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1727
try:
    SYS_rename = __NR_rename
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1731
try:
    SYS_renameat = __NR_renameat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1735
try:
    SYS_renameat2 = __NR_renameat2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1739
try:
    SYS_request_key = __NR_request_key
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1743
try:
    SYS_restart_syscall = __NR_restart_syscall
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1751
try:
    SYS_rmdir = __NR_rmdir
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1755
try:
    SYS_rseq = __NR_rseq
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1759
try:
    SYS_rt_sigaction = __NR_rt_sigaction
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1763
try:
    SYS_rt_sigpending = __NR_rt_sigpending
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1767
try:
    SYS_rt_sigprocmask = __NR_rt_sigprocmask
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1771
try:
    SYS_rt_sigqueueinfo = __NR_rt_sigqueueinfo
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1775
try:
    SYS_rt_sigreturn = __NR_rt_sigreturn
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1779
try:
    SYS_rt_sigsuspend = __NR_rt_sigsuspend
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1783
try:
    SYS_rt_sigtimedwait = __NR_rt_sigtimedwait
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1791
try:
    SYS_rt_tgsigqueueinfo = __NR_rt_tgsigqueueinfo
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1823
try:
    SYS_sched_get_priority_max = __NR_sched_get_priority_max
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1827
try:
    SYS_sched_get_priority_min = __NR_sched_get_priority_min
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1831
try:
    SYS_sched_getaffinity = __NR_sched_getaffinity
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1835
try:
    SYS_sched_getattr = __NR_sched_getattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1839
try:
    SYS_sched_getparam = __NR_sched_getparam
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1843
try:
    SYS_sched_getscheduler = __NR_sched_getscheduler
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1847
try:
    SYS_sched_rr_get_interval = __NR_sched_rr_get_interval
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1859
try:
    SYS_sched_setaffinity = __NR_sched_setaffinity
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1863
try:
    SYS_sched_setattr = __NR_sched_setattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1867
try:
    SYS_sched_setparam = __NR_sched_setparam
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1871
try:
    SYS_sched_setscheduler = __NR_sched_setscheduler
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1875
try:
    SYS_sched_yield = __NR_sched_yield
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1879
try:
    SYS_seccomp = __NR_seccomp
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1883
try:
    SYS_security = __NR_security
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1887
try:
    SYS_select = __NR_select
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1891
try:
    SYS_semctl = __NR_semctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1895
try:
    SYS_semget = __NR_semget
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1899
try:
    SYS_semop = __NR_semop
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1903
try:
    SYS_semtimedop = __NR_semtimedop
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1915
try:
    SYS_sendfile = __NR_sendfile
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1923
try:
    SYS_sendmmsg = __NR_sendmmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1927
try:
    SYS_sendmsg = __NR_sendmsg
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1931
try:
    SYS_sendto = __NR_sendto
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1935
try:
    SYS_set_mempolicy = __NR_set_mempolicy
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1939
try:
    SYS_set_robust_list = __NR_set_robust_list
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1943
try:
    SYS_set_thread_area = __NR_set_thread_area
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1947
try:
    SYS_set_tid_address = __NR_set_tid_address
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1955
try:
    SYS_setdomainname = __NR_setdomainname
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1959
try:
    SYS_setfsgid = __NR_setfsgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1967
try:
    SYS_setfsuid = __NR_setfsuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1975
try:
    SYS_setgid = __NR_setgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1983
try:
    SYS_setgroups = __NR_setgroups
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1995
try:
    SYS_sethostname = __NR_sethostname
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 1999
try:
    SYS_setitimer = __NR_setitimer
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2003
try:
    SYS_setns = __NR_setns
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2007
try:
    SYS_setpgid = __NR_setpgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2015
try:
    SYS_setpriority = __NR_setpriority
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2019
try:
    SYS_setregid = __NR_setregid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2027
try:
    SYS_setresgid = __NR_setresgid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2035
try:
    SYS_setresuid = __NR_setresuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2043
try:
    SYS_setreuid = __NR_setreuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2051
try:
    SYS_setrlimit = __NR_setrlimit
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2055
try:
    SYS_setsid = __NR_setsid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2059
try:
    SYS_setsockopt = __NR_setsockopt
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2063
try:
    SYS_settimeofday = __NR_settimeofday
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2067
try:
    SYS_setuid = __NR_setuid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2075
try:
    SYS_setxattr = __NR_setxattr
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2083
try:
    SYS_shmat = __NR_shmat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2087
try:
    SYS_shmctl = __NR_shmctl
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2091
try:
    SYS_shmdt = __NR_shmdt
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2095
try:
    SYS_shmget = __NR_shmget
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2099
try:
    SYS_shutdown = __NR_shutdown
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2107
try:
    SYS_sigaltstack = __NR_sigaltstack
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2115
try:
    SYS_signalfd = __NR_signalfd
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2119
try:
    SYS_signalfd4 = __NR_signalfd4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2139
try:
    SYS_socket = __NR_socket
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2147
try:
    SYS_socketpair = __NR_socketpair
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2151
try:
    SYS_splice = __NR_splice
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2167
try:
    SYS_stat = __NR_stat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2175
try:
    SYS_statfs = __NR_statfs
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2183
try:
    SYS_statx = __NR_statx
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2203
try:
    SYS_swapoff = __NR_swapoff
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2207
try:
    SYS_swapon = __NR_swapon
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2215
try:
    SYS_symlink = __NR_symlink
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2219
try:
    SYS_symlinkat = __NR_symlinkat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2223
try:
    SYS_sync = __NR_sync
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2227
try:
    SYS_sync_file_range = __NR_sync_file_range
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2235
try:
    SYS_syncfs = __NR_syncfs
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2259
try:
    SYS_sysfs = __NR_sysfs
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2263
try:
    SYS_sysinfo = __NR_sysinfo
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2267
try:
    SYS_syslog = __NR_syslog
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2275
try:
    SYS_tee = __NR_tee
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2279
try:
    SYS_tgkill = __NR_tgkill
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2283
try:
    SYS_time = __NR_time
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2287
try:
    SYS_timer_create = __NR_timer_create
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2291
try:
    SYS_timer_delete = __NR_timer_delete
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2295
try:
    SYS_timer_getoverrun = __NR_timer_getoverrun
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2299
try:
    SYS_timer_gettime = __NR_timer_gettime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2307
try:
    SYS_timer_settime = __NR_timer_settime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2319
try:
    SYS_timerfd_create = __NR_timerfd_create
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2323
try:
    SYS_timerfd_gettime = __NR_timerfd_gettime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2331
try:
    SYS_timerfd_settime = __NR_timerfd_settime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2339
try:
    SYS_times = __NR_times
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2343
try:
    SYS_tkill = __NR_tkill
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2347
try:
    SYS_truncate = __NR_truncate
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2355
try:
    SYS_tuxcall = __NR_tuxcall
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2371
try:
    SYS_umask = __NR_umask
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2379
try:
    SYS_umount2 = __NR_umount2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2383
try:
    SYS_uname = __NR_uname
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2387
try:
    SYS_unlink = __NR_unlink
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2391
try:
    SYS_unlinkat = __NR_unlinkat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2395
try:
    SYS_unshare = __NR_unshare
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2399
try:
    SYS_uselib = __NR_uselib
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2403
try:
    SYS_userfaultfd = __NR_userfaultfd
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2415
try:
    SYS_ustat = __NR_ustat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2419
try:
    SYS_utime = __NR_utime
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2423
try:
    SYS_utimensat = __NR_utimensat
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2431
try:
    SYS_utimes = __NR_utimes
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2439
try:
    SYS_vfork = __NR_vfork
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2443
try:
    SYS_vhangup = __NR_vhangup
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2455
try:
    SYS_vmsplice = __NR_vmsplice
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2459
try:
    SYS_vserver = __NR_vserver
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2463
try:
    SYS_wait4 = __NR_wait4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2467
try:
    SYS_waitid = __NR_waitid
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2475
try:
    SYS_write = __NR_write
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/syscall.h: 2479
try:
    SYS_writev = __NR_writev
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 19
try:
    _SYS_SYSCTL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 28
try:
    _LINUX_KERNEL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 36
try:
    _LINUX_LIST_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 40
try:
    __LINUX_COMPILER_H = 1
except:
    pass

# /usr/include/linux/sysctl.h: 30
try:
    CTL_MAXNAME = 10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 48
# #undef _LINUX_KERNEL_H
try:
    del _LINUX_KERNEL_H
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 56
# #undef _LINUX_LIST_H
try:
    del _LINUX_LIST_H
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysctl.h: 60
# #undef __LINUX_COMPILER_H
try:
    del __LINUX_COMPILER_H
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysinfo.h: 19
try:
    _SYS_SYSINFO_H = 1
except:
    pass

# /usr/include/linux/sysinfo.h: 7
try:
    SI_LOAD_SHIFT = 16
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 33
try:
    _SYS_SYSLOG_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 51
try:
    LOG_EMERG = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 52
try:
    LOG_ALERT = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 53
try:
    LOG_CRIT = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 54
try:
    LOG_ERR = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 55
try:
    LOG_WARNING = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 56
try:
    LOG_NOTICE = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 57
try:
    LOG_INFO = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 58
try:
    LOG_DEBUG = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 60
try:
    LOG_PRIMASK = 0x07
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 62
def LOG_PRI(p):
    return (p & LOG_PRIMASK)

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 63
def LOG_MAKEPRI(fac, pri):
    return (fac | pri)

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 93
try:
    LOG_KERN = (0 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 94
try:
    LOG_USER = (1 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 95
try:
    LOG_MAIL = (2 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 96
try:
    LOG_DAEMON = (3 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 97
try:
    LOG_AUTH = (4 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 98
try:
    LOG_SYSLOG = (5 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 99
try:
    LOG_LPR = (6 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 100
try:
    LOG_NEWS = (7 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 101
try:
    LOG_UUCP = (8 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 102
try:
    LOG_CRON = (9 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 103
try:
    LOG_AUTHPRIV = (10 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 104
try:
    LOG_FTP = (11 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 107
try:
    LOG_LOCAL0 = (16 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 108
try:
    LOG_LOCAL1 = (17 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 109
try:
    LOG_LOCAL2 = (18 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 110
try:
    LOG_LOCAL3 = (19 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 111
try:
    LOG_LOCAL4 = (20 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 112
try:
    LOG_LOCAL5 = (21 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 113
try:
    LOG_LOCAL6 = (22 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 114
try:
    LOG_LOCAL7 = (23 << 3)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 116
try:
    LOG_NFACILITIES = 24
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 117
try:
    LOG_FACMASK = 0x03f8
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 119
def LOG_FAC(p):
    return ((p & LOG_FACMASK) >> 3)

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 153
def LOG_MASK(pri):
    return (1 << pri)

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 154
def LOG_UPTO(pri):
    return ((1 << (pri + 1)) - 1)

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 162
try:
    LOG_PID = 0x01
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 163
try:
    LOG_CONS = 0x02
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 164
try:
    LOG_ODELAY = 0x04
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 165
try:
    LOG_NDELAY = 0x08
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 166
try:
    LOG_NOWAIT = 0x10
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/syslog.h: 167
try:
    LOG_PERROR = 0x20
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 20
try:
    _SYS_SYSMACROS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/sysmacros.h: 20
try:
    _BITS_SYSMACROS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 60
def major(dev):
    return (gnu_dev_major (dev))

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 61
def minor(dev):
    return (gnu_dev_minor (dev))

# /usr/include/x86_64-linux-gnu/sys/sysmacros.h: 62
def makedev(maj, min):
    return (gnu_dev_makedev (maj, min))

# /usr/include/termios.h: 23
try:
    _TERMIOS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 25
try:
    BRKINT = 0o000002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 29
try:
    ISTRIP = 0o000040
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 32
try:
    ICRNL = 0o000400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 35
try:
    IXON = 0o002000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 36
try:
    IXANY = 0o004000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h: 38
try:
    IMAXBEL = 0o020000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_oflag.h: 24
try:
    OPOST = 0o000001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_oflag.h: 27
try:
    ONLCR = 0o000004
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_oflag.h: 60
try:
    XTABS = 0o014000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 33
try:
    B0 = 0o000000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 34
try:
    B50 = 0o000001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 35
try:
    B75 = 0o000002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 36
try:
    B110 = 0o000003
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 37
try:
    B134 = 0o000004
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 38
try:
    B150 = 0o000005
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 39
try:
    B200 = 0o000006
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 40
try:
    B300 = 0o000007
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 41
try:
    B600 = 0o000010
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 42
try:
    B1200 = 0o000011
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 43
try:
    B1800 = 0o000012
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 44
try:
    B2400 = 0o000013
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 45
try:
    B4800 = 0o000014
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 46
try:
    B9600 = 0o000015
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 47
try:
    B19200 = 0o000016
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 48
try:
    B38400 = 0o000017
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 50
try:
    EXTA = B19200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 51
try:
    EXTB = B38400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_cflag.h: 27
try:
    CS7 = 0o000040
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_cflag.h: 30
try:
    CREAD = 0o000200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_cflag.h: 31
try:
    PARENB = 0o000400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_cflag.h: 33
try:
    HUPCL = 0o002000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 24
try:
    ISIG = 0o000001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 25
try:
    ICANON = 0o000002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 29
try:
    ECHO = 0o000010
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 30
try:
    ECHOE = 0o000020
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 37
try:
    ECHOCTL = 0o001000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 45
try:
    ECHOKE = 0o004000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h: 54
try:
    IEXTEN = 0o100000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 60
try:
    TIOCSER_TEMT = 0x01
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 64
try:
    TCOOFF = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 65
try:
    TCOON = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 66
try:
    TCIOFF = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 67
try:
    TCION = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 70
try:
    TCIFLUSH = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 71
try:
    TCOFLUSH = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/termios.h: 72
try:
    TCIOFLUSH = 2
except:
    pass

# /usr/include/termios.h: 44
def CCEQ(val, c):
    return ((c == val) and (val != _POSIX_VDISABLE))

# /usr/include/x86_64-linux-gnu/sys/timeb.h: 19
try:
    _SYS_TIMEB_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 19
try:
    _SYS_TIMERFD_H = 1
except:
    pass

# /usr/include/time.h: 23
try:
    _TIME_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 24
try:
    _BITS_TIME_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 34
try:
    CLOCKS_PER_SEC = (__clock_t (ord_if_char(1000000))).value
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 46
try:
    CLOCK_REALTIME = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 48
try:
    CLOCK_MONOTONIC = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 50
try:
    CLOCK_PROCESS_CPUTIME_ID = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 52
try:
    CLOCK_THREAD_CPUTIME_ID = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 54
try:
    CLOCK_MONOTONIC_RAW = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 56
try:
    CLOCK_REALTIME_COARSE = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 58
try:
    CLOCK_MONOTONIC_COARSE = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 60
try:
    CLOCK_BOOTTIME = 7
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 62
try:
    CLOCK_REALTIME_ALARM = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 64
try:
    CLOCK_BOOTTIME_ALARM = 9
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 66
try:
    CLOCK_TAI = 11
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time.h: 69
try:
    TIMER_ABSTIME = 1
except:
    pass

# /usr/include/time.h: 65
try:
    TIME_UTC = 1
except:
    pass

# /usr/include/time.h: 181
def __isleap(year):
    return (((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0)))

# /usr/include/x86_64-linux-gnu/bits/timerfd.h: 26
try:
    TFD_CLOEXEC = TFD_CLOEXEC
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timerfd.h: 28
try:
    TFD_NONBLOCK = TFD_NONBLOCK
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 32
try:
    TFD_TIMER_ABSTIME = TFD_TIMER_ABSTIME
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timerfd.h: 34
try:
    TFD_TIMER_CANCEL_ON_SET = TFD_TIMER_CANCEL_ON_SET
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/times.h: 23
try:
    _SYS_TIMES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 19
try:
    _SYS_TIMEX_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 19
try:
    _BITS_TIMEX_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 57
try:
    ADJ_OFFSET = 0x0001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 58
try:
    ADJ_FREQUENCY = 0x0002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 59
try:
    ADJ_MAXERROR = 0x0004
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 60
try:
    ADJ_ESTERROR = 0x0008
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 61
try:
    ADJ_STATUS = 0x0010
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 62
try:
    ADJ_TIMECONST = 0x0020
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 63
try:
    ADJ_TAI = 0x0080
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 64
try:
    ADJ_SETOFFSET = 0x0100
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 65
try:
    ADJ_MICRO = 0x1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 66
try:
    ADJ_NANO = 0x2000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 67
try:
    ADJ_TICK = 0x4000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 68
try:
    ADJ_OFFSET_SINGLESHOT = 0x8001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 69
try:
    ADJ_OFFSET_SS_READ = 0xa001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 72
try:
    MOD_OFFSET = ADJ_OFFSET
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 73
try:
    MOD_FREQUENCY = ADJ_FREQUENCY
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 74
try:
    MOD_MAXERROR = ADJ_MAXERROR
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 75
try:
    MOD_ESTERROR = ADJ_ESTERROR
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 76
try:
    MOD_STATUS = ADJ_STATUS
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 77
try:
    MOD_TIMECONST = ADJ_TIMECONST
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 78
try:
    MOD_CLKB = ADJ_TICK
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 79
try:
    MOD_CLKA = ADJ_OFFSET_SINGLESHOT
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 80
try:
    MOD_TAI = ADJ_TAI
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 81
try:
    MOD_MICRO = ADJ_MICRO
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 82
try:
    MOD_NANO = ADJ_NANO
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 86
try:
    STA_PLL = 0x0001
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 87
try:
    STA_PPSFREQ = 0x0002
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 88
try:
    STA_PPSTIME = 0x0004
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 89
try:
    STA_FLL = 0x0008
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 91
try:
    STA_INS = 0x0010
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 92
try:
    STA_DEL = 0x0020
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 93
try:
    STA_UNSYNC = 0x0040
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 94
try:
    STA_FREQHOLD = 0x0080
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 96
try:
    STA_PPSSIGNAL = 0x0100
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 97
try:
    STA_PPSJITTER = 0x0200
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 98
try:
    STA_PPSWANDER = 0x0400
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 99
try:
    STA_PPSERROR = 0x0800
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 101
try:
    STA_CLOCKERR = 0x1000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 102
try:
    STA_NANO = 0x2000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 103
try:
    STA_MODE = 0x4000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 104
try:
    STA_CLK = 0x8000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timex.h: 107
try:
    STA_RONLY = (((((((STA_PPSSIGNAL | STA_PPSJITTER) | STA_PPSWANDER) | STA_PPSERROR) | STA_CLOCKERR) | STA_NANO) | STA_MODE) | STA_CLK)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 28
try:
    NTP_API = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 44
try:
    TIME_OK = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 45
try:
    TIME_INS = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 46
try:
    TIME_DEL = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 47
try:
    TIME_OOP = 3
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 48
try:
    TIME_WAIT = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 49
try:
    TIME_ERROR = 5
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 50
try:
    TIME_BAD = TIME_ERROR
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 53
try:
    MAXTC = 6
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/timex.h: 65
try:
    ntp_gettime = ntp_gettimex
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/ttychars.h: 38
try:
    _SYS_TTYCHARS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/uio.h: 19
try:
    _SYS_UIO_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/uio_lim.h: 30
try:
    __IOV_MAX = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/uio.h: 26
try:
    UIO_MAXIOV = __IOV_MAX
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/un.h: 19
try:
    _SYS_UN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/un.h: 40
def SUN_LEN(ptr):
    return ((c_size_t (ord_if_char(((cast(0, POINTER(struct_sockaddr_un)).contents.sun_path).value)))).value + (strlen (((ptr.contents.sun_path).value))))

# /usr/include/unistd.h: 23
try:
    _UNISTD_H = 1
except:
    pass

# /usr/include/unistd.h: 34
try:
    _POSIX_VERSION = 200809
except:
    pass

# /usr/include/unistd.h: 53
try:
    __POSIX2_THIS_VERSION = 200809
except:
    pass

# /usr/include/unistd.h: 67
try:
    _POSIX2_VERSION = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 70
try:
    _POSIX2_C_VERSION = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 74
try:
    _POSIX2_C_BIND = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 78
try:
    _POSIX2_C_DEV = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 82
try:
    _POSIX2_SW_DEV = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 86
try:
    _POSIX2_LOCALEDEF = __POSIX2_THIS_VERSION
except:
    pass

# /usr/include/unistd.h: 90
try:
    _XOPEN_VERSION = 700
except:
    pass

# /usr/include/unistd.h: 100
try:
    _XOPEN_XCU_VERSION = 4
except:
    pass

# /usr/include/unistd.h: 103
try:
    _XOPEN_XPG2 = 1
except:
    pass

# /usr/include/unistd.h: 104
try:
    _XOPEN_XPG3 = 1
except:
    pass

# /usr/include/unistd.h: 105
try:
    _XOPEN_XPG4 = 1
except:
    pass

# /usr/include/unistd.h: 108
try:
    _XOPEN_UNIX = 1
except:
    pass

# /usr/include/unistd.h: 112
try:
    _XOPEN_ENH_I18N = 1
except:
    pass

# /usr/include/unistd.h: 115
try:
    _XOPEN_LEGACY = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/posix_opt.h: 57
try:
    _POSIX_VDISABLE = '\\0'
except:
    pass

# /usr/include/unistd.h: 210
try:
    STDIN_FILENO = 0
except:
    pass

# /usr/include/unistd.h: 211
try:
    STDOUT_FILENO = 1
except:
    pass

# /usr/include/unistd.h: 212
try:
    STDERR_FILENO = 2
except:
    pass

# /usr/include/unistd.h: 281
try:
    R_OK = 4
except:
    pass

# /usr/include/unistd.h: 282
try:
    W_OK = 2
except:
    pass

# /usr/include/unistd.h: 283
try:
    X_OK = 1
except:
    pass

# /usr/include/unistd.h: 284
try:
    F_OK = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 23
try:
    _SYS_UTSNAME_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/utsname.h: 23
try:
    _UTSNAME_LENGTH = 65
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/utsname.h: 28
try:
    _UTSNAME_DOMAIN_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 32
try:
    _UTSNAME_SYSNAME_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 35
try:
    _UTSNAME_NODENAME_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 38
try:
    _UTSNAME_RELEASE_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 41
try:
    _UTSNAME_VERSION_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 44
try:
    _UTSNAME_MACHINE_LENGTH = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/utsname.h: 76
try:
    SYS_NMLN = _UTSNAME_LENGTH
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 19
try:
    _SYS_VLIMIT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/vlimit.h: 57
try:
    INFINITY = 0x7fffffff
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/vm86.h: 20
try:
    _SYS_VM86_H = 1
except:
    pass

# /usr/include/linux/vt.h: 10
try:
    MIN_NR_CONSOLES = 1
except:
    pass

# /usr/include/linux/vt.h: 11
try:
    MAX_NR_CONSOLES = 63
except:
    pass

# /usr/include/linux/vt.h: 17
try:
    VT_OPENQRY = 0x5600
except:
    pass

# /usr/include/linux/vt.h: 26
try:
    VT_GETMODE = 0x5601
except:
    pass

# /usr/include/linux/vt.h: 27
try:
    VT_SETMODE = 0x5602
except:
    pass

# /usr/include/linux/vt.h: 28
try:
    VT_AUTO = 0x00
except:
    pass

# /usr/include/linux/vt.h: 29
try:
    VT_PROCESS = 0x01
except:
    pass

# /usr/include/linux/vt.h: 30
try:
    VT_ACKACQ = 0x02
except:
    pass

# /usr/include/linux/vt.h: 37
try:
    VT_GETSTATE = 0x5603
except:
    pass

# /usr/include/linux/vt.h: 38
try:
    VT_SENDSIG = 0x5604
except:
    pass

# /usr/include/linux/vt.h: 40
try:
    VT_RELDISP = 0x5605
except:
    pass

# /usr/include/linux/vt.h: 42
try:
    VT_ACTIVATE = 0x5606
except:
    pass

# /usr/include/linux/vt.h: 43
try:
    VT_WAITACTIVE = 0x5607
except:
    pass

# /usr/include/linux/vt.h: 44
try:
    VT_DISALLOCATE = 0x5608
except:
    pass

# /usr/include/linux/vt.h: 51
try:
    VT_RESIZE = 0x5609
except:
    pass

# /usr/include/linux/vt.h: 61
try:
    VT_RESIZEX = 0x560A
except:
    pass

# /usr/include/linux/vt.h: 62
try:
    VT_LOCKSWITCH = 0x560B
except:
    pass

# /usr/include/linux/vt.h: 63
try:
    VT_UNLOCKSWITCH = 0x560C
except:
    pass

# /usr/include/linux/vt.h: 64
try:
    VT_GETHIFONTMASK = 0x560D
except:
    pass

# /usr/include/linux/vt.h: 68
try:
    VT_EVENT_SWITCH = 0x0001
except:
    pass

# /usr/include/linux/vt.h: 69
try:
    VT_EVENT_BLANK = 0x0002
except:
    pass

# /usr/include/linux/vt.h: 70
try:
    VT_EVENT_UNBLANK = 0x0004
except:
    pass

# /usr/include/linux/vt.h: 71
try:
    VT_EVENT_RESIZE = 0x0008
except:
    pass

# /usr/include/linux/vt.h: 72
try:
    VT_MAX_EVENT = 0x000F
except:
    pass

# /usr/include/linux/vt.h: 78
try:
    VT_WAITEVENT = 0x560E
except:
    pass

# /usr/include/linux/vt.h: 85
try:
    VT_SETACTIVATE = 0x560F
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/vtimes.h: 19
try:
    _SYS_VTIMES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/vtimes.h: 29
try:
    VTIMES_UNITS_PER_SECOND = 60
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/wait.h: 23
try:
    _SYS_WAIT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/wait.h: 66
try:
    WCOREFLAG = __WCOREFLAG
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/wait.h: 67
def WCOREDUMP(status):
    return (__WCOREDUMP (status))

# /usr/include/x86_64-linux-gnu/sys/wait.h: 68
def W_EXITCODE(ret, sig):
    return (__W_EXITCODE (ret, sig))

# /usr/include/x86_64-linux-gnu/sys/wait.h: 69
def W_STOPCODE(sig):
    return (__W_STOPCODE (sig))

# /usr/include/x86_64-linux-gnu/sys/wait.h: 81
try:
    WAIT_ANY = (-1)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/wait.h: 82
try:
    WAIT_MYPGRP = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 19
try:
    _SYS_XATTR_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 33
try:
    XATTR_CREATE = XATTR_CREATE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/xattr.h: 35
try:
    XATTR_REPLACE = XATTR_REPLACE
except:
    pass

random_data = struct_random_data# /usr/include/stdlib.h: 423

drand48_data = struct_drand48_data# /usr/include/stdlib.h: 490

exec = struct_exec# /usr/include/x86_64-linux-gnu/a.out.h: 8

nlist = struct_nlist# /usr/include/x86_64-linux-gnu/a.out.h: 90

relocation_info = struct_relocation_info# /usr/include/x86_64-linux-gnu/a.out.h: 127

ieee754_float = union_ieee754_float# /usr/include/x86_64-linux-gnu/ieee754.h: 27

ieee754_double = union_ieee754_double# /usr/include/x86_64-linux-gnu/ieee754.h: 67

ieee854_long_double = union_ieee854_long_double# /usr/include/x86_64-linux-gnu/ieee754.h: 129

acct = struct_acct# /usr/include/x86_64-linux-gnu/sys/acct.h: 38

acct_v3 = struct_acct_v3# /usr/include/x86_64-linux-gnu/sys/acct.h: 60

epoll_data = union_epoll_data# /usr/include/x86_64-linux-gnu/sys/epoll.h: 81

epoll_event = struct_epoll_event# /usr/include/x86_64-linux-gnu/sys/epoll.h: 83

fanotify_event_info_header = struct_fanotify_event_info_header# /usr/include/linux/fanotify.h: 121

fanotify_event_info_fid = struct_fanotify_event_info_fid# /usr/include/linux/fanotify.h: 128

flock = struct_flock# /usr/include/x86_64-linux-gnu/bits/fcntl.h: 35

stat = struct_stat# /usr/include/x86_64-linux-gnu/bits/stat.h: 46

__bb = struct___bb# /usr/include/x86_64-linux-gnu/sys/gmon.h: 46

tostruct = struct_tostruct# /usr/include/x86_64-linux-gnu/sys/gmon.h: 132

rawarc = struct_rawarc# /usr/include/x86_64-linux-gnu/sys/gmon.h: 142

gmonparam = struct_gmonparam# /usr/include/x86_64-linux-gnu/sys/gmon.h: 157

gmon_hdr = struct_gmon_hdr# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 45

gmon_hist_hdr = struct_gmon_hist_hdr# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 60

gmon_cg_arc_record = struct_gmon_cg_arc_record# /usr/include/x86_64-linux-gnu/sys/gmon_out.h: 70

inotify_event = struct_inotify_event# /usr/include/x86_64-linux-gnu/sys/inotify.h: 28

consolefontdesc = struct_consolefontdesc# /usr/include/linux/kd.h: 14

unipair = struct_unipair# /usr/include/linux/kd.h: 64

unimapdesc = struct_unimapdesc# /usr/include/linux/kd.h: 68

unimapinit = struct_unimapinit# /usr/include/linux/kd.h: 74

kbentry = struct_kbentry# /usr/include/linux/kd.h: 102

kbsentry = struct_kbsentry# /usr/include/linux/kd.h: 115

kbdiacr = struct_kbdiacr# /usr/include/linux/kd.h: 122

kbdiacrs = struct_kbdiacrs# /usr/include/linux/kd.h: 125

kbdiacruc = struct_kbdiacruc# /usr/include/linux/kd.h: 132

kbdiacrsuc = struct_kbdiacrsuc# /usr/include/linux/kd.h: 135

kbkeycode = struct_kbkeycode# /usr/include/linux/kd.h: 142

kbd_repeat = struct_kbd_repeat# /usr/include/linux/kd.h: 150

console_font_op = struct_console_font_op# /usr/include/linux/kd.h: 161

console_font = struct_console_font# /usr/include/linux/kd.h: 169

mtop = struct_mtop# /usr/include/x86_64-linux-gnu/sys/mtio.h: 30

mtget = struct_mtget# /usr/include/x86_64-linux-gnu/sys/mtio.h: 81

mt_tape_info = struct_mt_tape_info# /usr/include/x86_64-linux-gnu/sys/mtio.h: 127

mtpos = struct_mtpos# /usr/include/x86_64-linux-gnu/sys/mtio.h: 157

mtconfiginfo = struct_mtconfiginfo# /usr/include/x86_64-linux-gnu/sys/mtio.h: 167

_libc_fpxreg = struct__libc_fpxreg# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 101

_libc_xmmreg = struct__libc_xmmreg# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 108

_libc_fpstate = struct__libc_fpstate# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 113

ucontext_t = struct_ucontext_t# /usr/include/x86_64-linux-gnu/sys/ucontext.h: 142

pollfd = struct_pollfd# /usr/include/x86_64-linux-gnu/sys/poll.h: 36

prctl_mm_map = struct_prctl_mm_map# /usr/include/linux/prctl.h: 134

timezone = struct_timezone# /usr/include/x86_64-linux-gnu/sys/time.h: 52

itimerval = struct_itimerval# /usr/include/x86_64-linux-gnu/sys/time.h: 105

user_fpregs_struct = struct_user_fpregs_struct# /usr/include/x86_64-linux-gnu/sys/user.h: 27

user_regs_struct = struct_user_regs_struct# /usr/include/x86_64-linux-gnu/sys/user.h: 42

user = struct_user# /usr/include/x86_64-linux-gnu/sys/user.h: 73

elf_siginfo = struct_elf_siginfo# /usr/include/x86_64-linux-gnu/sys/procfs.h: 49

elf_prstatus = struct_elf_prstatus# /usr/include/x86_64-linux-gnu/sys/procfs.h: 63

elf_prpsinfo = struct_elf_prpsinfo# /usr/include/x86_64-linux-gnu/sys/procfs.h: 84

prof = struct_prof# /usr/include/x86_64-linux-gnu/sys/profil.h: 37

if_dqblk = struct_if_dqblk# /usr/include/linux/quota.h: 110

if_nextdqblk = struct_if_nextdqblk# /usr/include/linux/quota.h: 122

if_dqinfo = struct_if_dqinfo# /usr/include/linux/quota.h: 156

dqblk = struct_dqblk# /usr/include/x86_64-linux-gnu/sys/quota.h: 91

dqinfo = struct_dqinfo# /usr/include/x86_64-linux-gnu/sys/quota.h: 120

raw_config_request = struct_raw_config_request# /usr/include/x86_64-linux-gnu/sys/raw.h: 31

rlimit = struct_rlimit# /usr/include/x86_64-linux-gnu/bits/resource.h: 139

semid_ds = struct_semid_ds# /usr/include/x86_64-linux-gnu/bits/sem.h: 50

seminfo = struct_seminfo# /usr/include/x86_64-linux-gnu/bits/sem.h: 83

sembuf = struct_sembuf# /usr/include/x86_64-linux-gnu/sys/sem.h: 40

shmid_ds = struct_shmid_ds# /usr/include/x86_64-linux-gnu/bits/shm.h: 58

shminfo = struct_shminfo# /usr/include/x86_64-linux-gnu/bits/shm.h: 93

shm_info = struct_shm_info# /usr/include/x86_64-linux-gnu/bits/shm.h: 106

signalfd_siginfo = struct_signalfd_siginfo# /usr/include/x86_64-linux-gnu/sys/signalfd.h: 27

sockaddr = struct_sockaddr# /usr/include/x86_64-linux-gnu/bits/socket.h: 178

sockaddr_storage = struct_sockaddr_storage# /usr/include/x86_64-linux-gnu/bits/socket.h: 191

msghdr = struct_msghdr# /usr/include/x86_64-linux-gnu/bits/socket.h: 257

cmsghdr = struct_cmsghdr# /usr/include/x86_64-linux-gnu/bits/socket.h: 275

linger = struct_linger# /usr/include/x86_64-linux-gnu/bits/socket.h: 361

synth_control = struct_synth_control# /usr/include/linux/soundcard.h: 153

remove_sample = struct_remove_sample# /usr/include/linux/soundcard.h: 160

seq_event_rec = struct_seq_event_rec# /usr/include/linux/soundcard.h: 164

patch_info = struct_patch_info# /usr/include/linux/soundcard.h: 209

sysex_info = struct_sysex_info# /usr/include/linux/soundcard.h: 298

sbi_instrument = struct_sbi_instrument# /usr/include/linux/soundcard.h: 467

synth_info = struct_synth_info# /usr/include/linux/soundcard.h: 476

sound_timer_info = struct_sound_timer_info# /usr/include/linux/soundcard.h: 504

midi_info = struct_midi_info# /usr/include/linux/soundcard.h: 511

audio_buf_info = struct_audio_buf_info# /usr/include/linux/soundcard.h: 575

count_info = struct_count_info# /usr/include/linux/soundcard.h: 606

buffmem_desc = struct_buffmem_desc# /usr/include/linux/soundcard.h: 614

copr_buffer = struct_copr_buffer# /usr/include/linux/soundcard.h: 703

copr_debug_buf = struct_copr_debug_buf# /usr/include/linux/soundcard.h: 711

copr_msg = struct_copr_msg# /usr/include/linux/soundcard.h: 716

mixer_info = struct_mixer_info# /usr/include/linux/soundcard.h: 908

_old_mixer_info = struct__old_mixer_info# /usr/include/linux/soundcard.h: 914

mixer_vol_table = struct_mixer_vol_table# /usr/include/linux/soundcard.h: 957

statfs = struct_statfs# /usr/include/x86_64-linux-gnu/bits/statfs.h: 24

statvfs = struct_statvfs# /usr/include/x86_64-linux-gnu/bits/statvfs.h: 29

__sysctl_args = struct___sysctl_args# /usr/include/linux/sysctl.h: 35

sysinfo = struct_sysinfo# /usr/include/linux/sysinfo.h: 8

timeb = struct_timeb# /usr/include/x86_64-linux-gnu/sys/timeb.h: 29

tms = struct_tms# /usr/include/x86_64-linux-gnu/sys/times.h: 32

timex = struct_timex# /usr/include/x86_64-linux-gnu/bits/timex.h: 26

ntptimeval = struct_ntptimeval# /usr/include/x86_64-linux-gnu/sys/timex.h: 30

ttychars = struct_ttychars# /usr/include/x86_64-linux-gnu/sys/ttychars.h: 40

sockaddr_un = struct_sockaddr_un# /usr/include/x86_64-linux-gnu/sys/un.h: 29

utsname = struct_utsname# /usr/include/x86_64-linux-gnu/sys/utsname.h: 48

vt_mode = struct_vt_mode# /usr/include/linux/vt.h: 19

vt_stat = struct_vt_stat# /usr/include/linux/vt.h: 32

vt_sizes = struct_vt_sizes# /usr/include/linux/vt.h: 46

vt_consize = struct_vt_consize# /usr/include/linux/vt.h: 53

vt_event = struct_vt_event# /usr/include/linux/vt.h: 66

vt_setactivate = struct_vt_setactivate# /usr/include/linux/vt.h: 80

vtimes = struct_vtimes# /usr/include/x86_64-linux-gnu/sys/vtimes.h: 31

fanotify_event_metadata = struct_fanotify_event_metadata# /usr/include/linux/fanotify.h: 152

# No inserted files

# No prefix-stripping

