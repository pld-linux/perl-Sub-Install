#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Sub
%define	pnam	Install
Summary:	Sub::Install - install subroutines into packages easily
Summary(pl.UTF-8):	Sub::Install - łatwe instalowanie podprocedur do pakietów
Name:		perl-Sub-Install
Version:	0.928
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e1ce4f9cb6b2f6b8778b036c31afa5ab
URL:		http://search.cpan.org/dist/Sub-Install/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it easy to install subroutines into packages without
the unslightly mess of no strict or typeglobs lying about where just
anyone can see them.

%description -l pl.UTF-8
Ten moduł ułatwia instalowanie podprocedur do pakietów bez niemałego
bałaganu no strict lub typeglobów umieszczonych wszędzie, gdzie każdy
może je zobaczyć.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/Install.pm
%{_mandir}/man3/Sub::Install.3pm*
