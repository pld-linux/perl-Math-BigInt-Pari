#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigInt-Pari
Summary:	Math::BigInt::Pari - use Math::Pari for Math::BigInt routines
Summary(pl):	Math::BigInt::Pari - wykorzystanie Math::Pari do funkcji Math::BigInt
Name:		perl-Math-BigInt-Pari
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0c2573c1e109e31b6e30acbbd90f2c15
Patch0:		%{name}-test.patch
BuildRequires:	perl-Math-BigInt >= 1.60
BuildRequires:	perl(Math::BigFloat) >= 1.35
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.60
Requires:	perl(Math::BigFloat) >= 1.35
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::Pari provides support for big integer calculations via
means of Math::Pari, an XS layer on top of the very fast PARI library.

%description -l pl
Math::BigInt::Pari dostarcza obs³ugê obliczeñ na wielkich liczbach
ca³kowitych z wykorzystaniem funkcjonalno¶ci modu³u Math::Pari -
warstwy XS bêd±cej interfejsem do bardzo szybkiej biblioteki PARI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# sqrt(+inf) == inf, not NaN
%patch -p1

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
