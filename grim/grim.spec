Name:           grim
Version:        1.2.0
Release:        1%{?dist}
Summary:        A screenshotting tool for Wayland compositors

License:        MIT
URL:            https://github.com/emersion/grim
Source0:        https://github.com/emersion/grim/releases/download/v%{version}/grim-%{version}.tar.gz

BuildRequires:  gcc, meson, libjpeg-turbo-devel, cairo-devel, wayland-devel, pkgconfig(wayland-protocols)

%description
A screenshotting tool for wayland


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
/usr/bin/grim

%changelog
* Tue Nov 19 2019 Jarkko Oranen
- 1.2.0
