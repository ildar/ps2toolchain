Name: ps2dev-sdk
Version: 0.1
Release: alt1
Summary: ps2dev project's SDK
License: GPL
Group: Development/Other
Url: https://github.com/ps2dev/ps2toolchain

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: https://github.com/ps2dev/ps2toolchain.tar
Source1: https://github.com/ps2dev/ps2sdk.tar
Source2: https://github.com/ps2dev/ps2client.tar

# Automatically added by buildreq on Mon Dec 03 2012 (-bi)
# optimized out: elfutils ps2dev-binutils ps2dev-newlib python-base
BuildRequires: git-core ps2dev-gcc ps2dev-iop-gcc wget

BuildRequires: ps2dev-gcc >= %version , ps2dev-iop-gcc >= %version
Requires: ps2dev-gcc >= %version , ps2dev-iop-gcc >= %version

%description
%name is the part of ps2dev toolchain.

This package provides SDK for building Playstation2 applications. It consists of:
* SDK itself
* ps2client

%prep
%setup -n ps2toolchain
mkdir downloads
tar xf %SOURCE1 -C downloads/
tar xf %SOURCE2 -C downloads/

%install
export _DESTDIR=%buildroot
./toolchain.sh 5 6

%files
%prefix/ps2dev/bin/*
%prefix/ps2dev/ee/lib/gcc-lib/ee/3.2.2/crt0.o
%prefix/ps2dev/ee/ee/lib/crt0.o
%prefix/ps2dev/ps2sdk

%changelog
* Mon Dec 03 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- initial build for ALT Linux family
