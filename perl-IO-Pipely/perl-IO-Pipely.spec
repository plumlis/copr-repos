Name:           perl-IO-Pipely
Version:        0.005
Release:        1%{?dist}
Summary:        Portably create pipe() or pipe-like handles, one way or another
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Pipely/
Source0:        https://www.cpan.org/authors/id/R/RC/RCAPUTO/IO-Pipely-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.004
BuildRequires:  perl(base) >= 2.18
BuildRequires:  perl(Carp) >= 1.26
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl) >= 1.06
BuildRequires:  perl(IO::Socket) >= 1.31
BuildRequires:  perl(Scalar::Util) >= 1.29
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol) >= 1.06
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)
Requires:       perl(base) >= 2.18
Requires:       perl(Exporter) >= 5.68
Requires:       perl(Fcntl) >= 1.06
Requires:       perl(IO::Socket) >= 1.31
Requires:       perl(strict)
Requires:       perl(Symbol) >= 1.06
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
for detailed semantics and caveats.

%prep
%setup -q -n IO-Pipely-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES dist.ini LICENSE META.json README README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Nov 03 2018 Jarkko Oranen <oranenj@iki.fi> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
