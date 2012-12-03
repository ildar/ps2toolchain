Name: ps2dev-binutils
Version: 0.1
Release: alt1
Summary: ps2dev project's patched cross-binutils
License: GPL
Group: Development/Other
Url: https://github.com/ps2dev/ps2toolchain

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: https://github.com/ps2dev/ps2toolchain.tar
Source1: https://github.com/downloads/ps2dev/ps2toolchain/binutils-2.14.tar.bz2

# Automatically added by buildreq on Mon Dec 03 2012 (-bi)
# optimized out: elfutils perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators python-base tzdata
BuildRequires: flex git-core glibc-devel-static perl-Pod-Parser wget

%description
%name is the part of ps2dev toolchain.

This package provides the binutils part of the toolchain.

%prep
%setup -n ps2toolchain
mkdir downloads
cp -al %SOURCE1 downloads/

%install
cat > ps2dev_env.sh <<EOF
## Set up the environment.
export PS2DEV=%prefix/ps2dev
export PATH=\$PATH:\$PS2DEV/bin
export PATH=\$PATH:\$PS2DEV/ee/bin
export PATH=\$PATH:\$PS2DEV/iop/bin
export PATH=\$PATH:\$PS2DEV/dvp/bin
export PS2SDK=\$PS2DEV/ps2sdk
export PATH=\$PATH:\$PS2SDK/bin
EOF

. ps2dev_env.sh
export _DESTDIR=%buildroot
./toolchain.sh 1

mkdir -p %buildroot%_sysconfdir/profile.d/
install ps2dev_env.sh %buildroot%_sysconfdir/profile.d/

# remove unnessesary files
rm -rf %buildroot$PS2DEV/{\
*/info/,\
*/man/,\
*/share/locale/,\
ps2sdk/,\
test.tmp\
}

%files
%_sysconfdir/profile.d/ps2dev_env.sh
%prefix/ps2dev

%changelog
* Mon Dec 03 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- initial build for ALT Linux family
