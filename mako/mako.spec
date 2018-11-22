%global provider        github
%global provider_tld    com
%global project         emersion
%global repo            mako
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          ce1978865935dbff1b3bf3065ff607a4178fe57b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           mako
Version:        1.1
Release:        3.git%{shortcommit}%{?dist}
Summary:        A lightweight Wayland notification daemon
License:        MIT
URL:            https://wayland.emersion.fr/mako
Source:         https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Requires:       cairo
Requires:       pango
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  scdoc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  systemd-devel

%description
%{summary}.

%prep
%setup -q -n %{repo}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README*.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1.gz
%{_mandir}/man1/makoctl.1.gz


%changelog
* Mon Nov 5 2018 Jarkko Oranen <oranenj@iki.fi> - 1.1.gitd1e6585
- Build from master
