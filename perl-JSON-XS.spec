%define upstream_name	 JSON-XS
%define upstream_version 2.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
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


%changelog
* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.300.0-1mdv2011.0
+ Revision: 572222
- update to 2.3

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.290.0-2mdv2011.0
+ Revision: 555970
- rebuild for perl 5.12

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.290.0-1mdv2010.1
+ Revision: 523434
- update to 2.29

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.280.0-1mdv2010.1
+ Revision: 518484
- update to 2.28

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.270.0-2mdv2010.1
+ Revision: 504859
- adding missing requires:

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.270.0-1mdv2010.1
+ Revision: 487049
- update to 2.27

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.260.0-1mdv2010.1
+ Revision: 461321
- update to 2.26

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.250.0-1mdv2010.0
+ Revision: 415039
- adding missing buildrequires:
- forgot to commit tarball
- update to 2.25

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.240.0-1mdv2010.0
+ Revision: 393298
- update to 2.24
- using %%perl_convert_version
- bumping epoch to make sure old (braindead) version scheme is forgotten

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2311-1mdv2009.1
+ Revision: 343258
- update to new version 2311

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2222-1mdv2009.1
+ Revision: 305734
- update to new version 2.2222

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.23-1mdv2009.1
+ Revision: 292193
- update to new version 2.23

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 238738
- new version

* Mon Jun 16 2008 Adam Williamson <awilliamson@mandriva.org> 2.21-1mdv2009.0
+ Revision: 220523
- import perl-JSON-XS


