#define _empty_manifest_terminate_build 0
%define upstream_name JSON-XS

Name:		perl-%{upstream_name}
Version:	4.04
Release:	1
Summary:	JSON (JavaScript Object Notation) serialization
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/JSON/JSON-XS-%{version}.tar.gz
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(common::sense)
BuildRequires:	perl-devel
BuildRequires:  perl(Canary::Stability)
Requires:	perl(common::sense)

%description
JSON serialising/deserialising, done correctly and fast.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{_mandir}/*/*
%{_bindir}/json_xs
%{perl_vendorarch}/JSON*
%{perl_vendorarch}/auto/JSON/XS/*
