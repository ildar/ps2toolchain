Name: ps2dev-newlib
Version: 0.1
Release: alt1
Summary: ps2dev project's patched libc based on newlib
License: GPL
Group: Development/Other
Url: https://github.com/ps2dev/ps2toolchain

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: https://github.com/ps2dev/ps2toolchain.tar
Source1: https://github.com/downloads/ps2dev/ps2toolchain/newlib-1.10.0.tar.gz

# Automatically added by buildreq on Mon Dec 03 2012 (-bi)
# optimized out: elfutils python-base
BuildRequires: git-core ps2dev-gcc-stage1 wget

BuildRequires: ps2dev-gcc-stage1 >= %version

%description
%name is the part of ps2dev toolchain.

This package provides libc headers and libraries for building Playstation2
applications. It is the lightly patched newlib for EE only.

%prep
%setup -n ps2toolchain
mkdir downloads
cp -al %SOURCE1 downloads/

%install
export _DESTDIR=%buildroot
./toolchain.sh 3
mv %buildroot%prefix/ps2dev/ee/ee/lib/crt0.o{,.fromNewlib}

%files
%prefix/ps2dev/ee/ee/include
%prefix/ps2dev/ee/ee/lib

%changelog
* Mon Dec 03 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- initial build for ALT Linux family
