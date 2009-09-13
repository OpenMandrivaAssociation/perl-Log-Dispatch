%define upstream_name    Log-Dispatch
%define upstream_version 2.23

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Perl modules for logging messages to multiple outputs
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mail::Sender)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(MIME::Lite)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description 
%{upstream_name} module for Perl.  Log::Dispatch is a suite of OO modules for
logging messages to multiple outputs, each of which can have a minimum
and maximum log level.  It is designed to be easily subclassed, both
for creating a new dispatcher object and particularly for creating new
outputs.

%package ApacheLog
Summary: Apache mod_perl dispatcher for Log::Dispatch
Group:   Development/Perl

%description ApacheLog
Log::Dispatch::ApacheLog is a dispatcher for apache logging, used with
mod_perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/Log
%exclude %{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%exclude %{_mandir}/*/Log::Dispatch::ApacheLog*
%{_mandir}/*/*

%files ApacheLog
%{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%{_mandir}/*/Log::Dispatch::ApacheLog*
