#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-Pari
Summary:	Math::BigInt::Pari - use Math::Pari for Math::BigInt routines
Summary(pl.UTF-8):	Math::BigInt::Pari - wykorzystanie Math::Pari do funkcji Math::BigInt
Name:		perl-Math-BigInt-Pari
Version:	1.13
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64a336d15d0faed78587d411e4075363
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-Math-Pari >= 2.010602
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.87
Requires:	perl-Math-Pari >= 2.010709
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::Pari provides support for big integer calculations via
means of Math::Pari, an XS layer on top of the very fast PARI library.

%description -l pl.UTF-8
Math::BigInt::Pari dostarcza obsługę obliczeń na wielkich liczbach
całkowitych z wykorzystaniem funkcjonalności modułu Math::Pari -
warstwy XS będącej interfejsem do bardzo szybkiej biblioteki PARI.

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
%doc CHANGES README
%{perl_vendorlib}/Math/BigInt/Pari.pm
%{_mandir}/man3/*
