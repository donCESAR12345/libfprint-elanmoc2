Name:     libfprint-elanmoc2
Version:  1.94.5
Release:  %autorelease
Summary:  Toolkit for fingerprint scanner

License:  LGPLv2+
URL:      http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source:   https://github.com/agent0706/libfprint-elanmoc2/releases/download/release/libfprint-elanmoc2.tar.gz
ExcludeArch:  s390 s390x

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel

# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
	
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2

# Compatibility requirement
Requires:       fprintd-pam >= 1.94

# Conflict with standard libfprint package
Conflicts:      libfprint

%description
Library for fingerprint readers with patches 
for the support of the ELAN 0C4C and 0C00.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and
header files for developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-elanmoc2

%build
# Include the virtual image driver for integration tests
%meson -Ddrivers=all
%meson_build

%install
%meson_install
%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS THANKS AUTHORS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules
	
%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfprint-2.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/
	
%changelog
%autochangelog
