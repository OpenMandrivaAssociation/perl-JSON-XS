%define upstream_name	 JSON-XS
%define upstream_version 2.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
Epoch:      1

Summary:	JSON (JavaScript Object Notation) serialization
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(CGI)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(common::sense)
BuildRequires:	perl-devel

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:   perl(common::sense)

%description
JSON serialising/deserialising, done correctly and fast.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc Changes README
%{_mandir}/*/*
%{_bindir}/json_xs
%{perl_vendorarch}/JSON*
%{perl_vendorarch}/auto/JSON/XS/*
