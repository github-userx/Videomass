[Home](index.md)

# Known problems and solutions of Videomass
-------------------------------------------

## Common problems

- If you are using an earlier version of FFmpeg equal to or less than 3.1.5, the
_nlmeans_ filter it may not have been implemented yet, since it exists only in
the most recent versions of FFmpeg. Instead, use _hqdn3d_ or set Videomass to a
path with a newer version of FFmpeg.

- FFmpeg version 3.1 or higher is required for the _loudnorm_ filter (on EBU audio 
normalization). Versions earlier than ffmpeg 3.1 cause `No such filter: loudnorm` 
error on the Videomass 'Log viewing console' and the conversion process will fail.

- For VP9 encoder FFmpeg added support for row based multithreading in version
3.4, released on January 25th, 2018. As of libvpx version 1.7.0 this
multithreading enhancement is not enabled by default and needs be manually
activated with the `-row-mt 1` switch. Note that this feature is not available
if you are using an older version of the FFmpeg (eg Version 3.1.5) and should
be disabled when using this encoder.

- [Other issues](https://github.com/jeanslack/Videomass/issues)
  
 
## Videomass AppImage for Linux

**Very Important:**   
before to start latest version of Videomass AppImage, you should install 
*libsdl2-2.0-0* package which is not included on some Linux distributions, 
i.e all releases of **Ubuntu**. Alternatively, you can install the *ffmpeg* 
package which includes *libdsl2-2.0-0* as a dependency and is required by 
Videomass as it is not embedded in the AppImage itself.   
Thank you!  

to install *libsdl2-2.0-0* typing: `sudo apt install libsdl2-2.0-0`   

rather install *ffmpeg* which will also install *libsdl2-2.0-0*: `sudo apt install ffmpeg`   

----
Currently, two separate versions have been released for GTK2 and GTK3.   

Videomass AppImage for **GTK3** it has been successfully tested on the following Linux distributions:
* ~~Ubuntu 16.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)~~ NOT WORK
* Ubuntu 18.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)
* Xubuntu 18.04 x86_64 (by installing libsdl2 or ffmpeg first)
* Ubuntu 20.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)
* Linux Mint 19.3 x86_64 Cinnamon
* Debian 9 stretch x86_64
* Debian 10 buster x86_64
* SparkyLinux 5.11 lxqt x86_64 (stable edition)
* Sparkylinux 2020.06 xfce x86_64 (rolling edition)
* AV-Linux 2019.4.10 x86_64
* AV-Linux 2020.4.10 x86_64
* Fedora 32 (Workstation Edition) x86_64
* Manjaro Linux 20.0.3 (Lysia) x86_64

Videomass AppImage for **GTK2** it has been successfully tested on the following Linux distributions:
* Ubuntu 16.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)
* Ubuntu 18.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)
* Xubuntu 18.04 x86_64 (by installing libsdl2 or ffmpeg first)
* Ubuntu 20.04 LTS x86_64 (by installing libsdl2 or ffmpeg first)
* Linux Mint 19.3 x86_64 Cinnamon
* Debian 9 stretch x86_64
* Debian 10 buster x86_64
* SparkyLinux 5.11 lxqt x86_64 (stable edition)
* Sparkylinux 2020.06 xfce x86_64 (rolling edition)
* AV-Linux 2019.4.10 x86_64
* AV-Linux 2020.4.10 x86_64
* ~~Fedora 32 (Workstation Edition) x86_64~~ NOT WORK
* Manjaro Linux 20.0.3 (Lysia) x86_64

[Home](index.md)