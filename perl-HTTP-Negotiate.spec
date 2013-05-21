%define upstream_name    HTTP-Negotiate
%define upstream_version 6.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	HTTP content negotiation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(HTTP::Headers)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in _draft-ietf-http-v11-spec-00.ps_ chapter
12. Content negotiation allows for the selection of a preferred content
representation based upon attributes of the negotiable variants and the
value of the various Accept* header fields in the request.

The variants are ordered by preference by calling the function choose().

The first parameter is reference to an array of the variants to choose
among. Each element in this array is an array with the values [$id, $qs,
$content_type, $content_encoding, $charset, $content_language,
$content_length] whose meanings are described below. The $content_encoding
and $content_language can be either a single scalar value or an array
reference if there are several values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-4mdv2012.0
+ Revision: 765365
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3
+ Revision: 763867
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-2
+ Revision: 763079
- rebuild

* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.0-1
+ Revision: 666390
- import perl-HTTP-Negotiate

