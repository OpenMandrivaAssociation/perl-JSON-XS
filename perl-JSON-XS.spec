%define upstream_name JSON-XS
%define upstream_version 4.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1
Summary:	JSON (JavaScript Object Notation) serialization
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/JSON/JSON-XS-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
%make_install


%files
%doc Changes README
%{_mandir}/*/*
%{_bindir}/json_xs
%{perl_vendorarch}/JSON*
%{perl_vendorarch}/auto/JSON/XS/*
