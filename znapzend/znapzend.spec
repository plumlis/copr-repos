Name: znapzend
Version: 0.19.1
Release: 1%{?dist}
Summary: zfs backup with remote capabilities and mbuffer integration
License: GPLv3+
URL: http://www.znapzend.org
Source: https://github.com/oetiker/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires: perl

%description
ZnapZend is a ZFS centric backup tool. It relies on snapshot, send and
receive to do its work. It has the built-in ability to manage both local
snapshots as well as remote copies by thinning them out as time
progresses.

%prep
%setup

%build
%configure
make

%install
%make_install

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
<init/znapzend.service perl -pe 's{NONE/bin}{%{_bindir}}' >$RPM_BUILD_ROOT/%{_unitdir}/znapzend.service

%files
%doc README.md LICENSE COPYRIGHT CHANGES
%{_bindir}/*
%{_mandir}/*/*
%{_unitdir}/*
