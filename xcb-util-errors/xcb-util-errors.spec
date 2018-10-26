%global libname xcb-errors

Name:           xcb-util-errors
Version:        1.0
Release:        0%{?dist}
Summary:        XCB utility functions for error handling

License:        MIT
URL:            https://cgit.freedesktop.org/xcb/util-errors/
Source0:        https://xcb.freedesktop.org/dist/xcb-util-errors-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(x11)

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/lib%{libname}.la

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/lib%{libname}.so.*

%files devel
%{_includedir}/xcb/%(n=%{libname}; echo ${n//-/_}).h
%{_libdir}/lib%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
* Sat Oct 26 2018 Jarkko Oranen <oranenj@iki.fi> - 1.0-0
- Initial build

