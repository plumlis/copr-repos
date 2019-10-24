%global debug_package %{nil}

Name:           wl-clipboard-x11
Version:        4 
Release:        1%{?dist}
Summary:        wl-clipboard alternatives to X clipboard tools 

License:        GPL
URL:            https://github.com/brunelli/wl-clipboard-x11
Source0:        https://github.com/brunelli/wl-clipboard-x11/archive/v%{version}.tar.gz

BuildRequires:  make
Requires:       wl-clipboard
Provides:	xclip, xsel

%description
wl-clipboard alternatives to X clipboard tools


%prep
%autosetup


%build
echo "Nothing to do"


%install
%make_install
rm -f %{buildroot}/usr/bin/xclip
rm -f %{buildroot}/usr/bin/xsel
install -p %{buildroot}/usr/share/wl-clipboard-x11/wl-clipboard-x11 %{buildroot}/usr/bin/xclip
install -p %{buildroot}/usr/share/wl-clipboard-x11/wl-clipboard-x11 %{buildroot}/usr/bin/xsel

%files
/usr/bin/xclip
/usr/bin/xsel
/usr/share/man/man1/wl-clipboard-x11.1.gz
/usr/share/man/man1/xclip.1.gz
/usr/share/man/man1/xsel.1.gz
/usr/share/wl-clipboard-x11/wl-clipboard-x11





%changelog
* Mon Oct 14 2019 Jarkko Oranen
- Initial build
