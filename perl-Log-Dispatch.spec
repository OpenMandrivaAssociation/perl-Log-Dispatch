%define upstream_name    Log-Dispatch
%define upstream_version 2.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl modules for logging messages to multiple outputs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Dispatch-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Mail::Sender)
BuildRequires:	perl(Mail::Sendmail)
BuildRequires:	perl(MIME::Lite)
BuildArch:	noarch

%description 
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level.  It is
designed to be easily subclassed, both for creating a new dispatcher object and
particularly for creating new outputs.

%package ApacheLog
Summary: Apache mod_perl dispatcher for Log::Dispatch
Group:   Development/Perl

%description ApacheLog
Log::Dispatch::ApacheLog is a dispatcher for apache logging, used with
mod_perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Log
%exclude %{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%exclude %{_mandir}/*/Log::Dispatch::ApacheLog*
%{_mandir}/*/*

%files ApacheLog
%{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%{_mandir}/*/Log::Dispatch::ApacheLog*


%changelog
* Sat Mar 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.290.0-1mdv2011.0
+ Revision: 647009
- update to new version 2.29

* Sat Dec 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.280.0-1mdv2011.0
+ Revision: 622843
- update to new version 2.28

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.270.0-1mdv2011.0
+ Revision: 597077
- new version

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 2.260.0-1mdv2011.0
+ Revision: 447605
- update to 2.26

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 2.250.0-1mdv2010.0
+ Revision: 443473
- update to 2.25

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 2.240.0-1mdv2010.0
+ Revision: 439438
- update to 2.24

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.230.0-1mdv2010.0
+ Revision: 438655
- update to new version 2.23

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-1mdv2010.0
+ Revision: 403394
- rebuild using %%perl_convert_version

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.22-1mdv2009.1
+ Revision: 302849
- update to new version 2.22

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.21-4mdv2009.0
+ Revision: 257668
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.21-3mdv2009.0
+ Revision: 245706
- rebuild

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 2.21-1mdv2008.1
+ Revision: 163387
- update to new version 2.21

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.20-1mdv2008.1
+ Revision: 105553
- update to new version 2.20

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2008.0
+ Revision: 47694
- update to new version 2.18

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.17-1mdv2008.0
+ Revision: 20234
- 2.17
- kill patch0, no longer need


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2007.0
- new version
- Module::Build-based build

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 2.11-4mdk
- split Log::Dispatch::ApacheLog from main package, as it pulls 
  mod_perl, which pulls apache, which is a server.
- convert to new policy ( ie, use perl(Foo) for buildRequires )
- enhance summary

* Thu Dec 22 2005 Michael Scherer <misc@mandriva.org> 2.11-3mdk
- mkrel

* Tue Sep 27 2005 Oden Eriksson <oeriksson@mandriva.com> 2.11-2mdk
- fix deps

* Mon Aug 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.11-1mdk
- 2.11

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.10-1mdk
- 2.10
- fix install
- fix perms


