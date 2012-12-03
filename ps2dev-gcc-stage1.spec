Name: ps2dev-gcc-stage1
Version: 0.1
Release: alt1
Summary: ps2dev project's patched cross-gcc, stage1 (not for production)
License: GPL
Group: Development/Other
Url: https://github.com/ps2dev/ps2toolchain

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: https://github.com/ps2dev/ps2toolchain.tar
Source1: https://github.com/downloads/ps2dev/ps2toolchain/gcc-3.2.2.tar.bz2

# Automatically added by buildreq on Mon Dec 03 2012 (-bi)
# optimized out: elfutils python-base
BuildRequires: git-core ps2dev-binutils wget

BuildRequires: ps2dev-binutils >= %version
Requires: ps2dev-binutils >= %version

%description
%name is the part of ps2dev toolchain.

This package provides the gcc-stage1 for building SDK.
It shouldn't be used for building applications, only SDK!

%prep
%setup -n ps2toolchain
mkdir downloads
cp -al %SOURCE1 downloads/

%install
export _DESTDIR=%buildroot
./toolchain.sh 2

# remove unnessesary files
rm -rf %buildroot$PS2DEV/{\
*/info/,\
*/man/,\
*/share/locale/,\
ps2sdk/,\
test.tmp\
}

%files
%prefix/ps2dev/ee/*/*
%exclude %prefix/ps2dev/ee/lib/libiberty.a

%package -n ps2dev-iop-gcc
Summary: ps2dev project's patched cross-gcc for IOP
Group: Development/Other
Requires: ps2dev-binutils >= %version
%description -n ps2dev-iop-gcc
ps2dev-iop-gcc is the part of ps2dev toolchain.

This package provides the IOP gcc.

%files -n ps2dev-iop-gcc
%prefix/ps2dev/iop/*/*
%exclude %prefix/ps2dev/iop/lib/libiberty.a

%changelog
* Mon Dec 03 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- initial build for ALT Linux family
