%define module	JSON-XS
%define name		perl-%{module}
%define version     2.23
%define up_version  2.222
%define release		%mkrel 1

Summary:	JSON (JavaScript Object Notation) serialization
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/JSON/%{module}-%{up_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(CGI)
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
JSON serialising/deserialising, done correctly and fast.

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

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

