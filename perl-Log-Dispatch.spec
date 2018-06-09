%define upstream_name    Log-Dispatch
%define upstream_version 2.67

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl modules for logging messages to multiple outputs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Dispatch-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Mail::Sender)
BuildRequires:	perl(Mail::Sendmail)
BuildRequires:	perl(MIME::Lite)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Specio::Exporter)
BuildRequires:	perl(Params::ValidationCompiler)
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Devel::GlobalDestruction)
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
%doc Changes
%license LICENSE
%{perl_vendorlib}/Log
%exclude %{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%exclude %{_mandir}/*/Log::Dispatch::ApacheLog*
%{_mandir}/*/*

%files ApacheLog
%{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%{_mandir}/*/Log::Dispatch::ApacheLog*
