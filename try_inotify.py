from linux_libc import inotify_init, inotify_add_watch, close, perror, String, IN_MODIFY, read, inotify_event
from ctypes import sizeof, pointer

def main():
    try:
        instance_fd = inotify_init()
        if instance_fd == -1:
            perror(String(b"inotify_init"))
            return
        test1_wd = inotify_add_watch(instance_fd, String(b"/home/tz-wsl1-2004/test1.txt"), IN_MODIFY)
        if test1_wd == -1:
            perror(String(b"test1_wd"))
            return
        test2_wd = inotify_add_watch(instance_fd, String(b"/home/tz-wsl1-2004/test2.txt"), IN_MODIFY)
        if test2_wd == -1:
            perror(String(b"test2_wd"))
            return
        event = inotify_event()
        while True:
            if read(instance_fd, pointer(event), sizeof(event)) < 0:
                perror(String(b"read"))
                return
            if event.wd == test1_wd: print("Test 1 File has been modified")
            elif event.wd == test2_wd: print("Test 2 File has been modified")
    except KeyboardInterrupt:
        print("User requested exit.")
    finally:
        print("Cleaning up: closing instance_fd")
        close(instance_fd)



if __name__=='__main__':
    main()

