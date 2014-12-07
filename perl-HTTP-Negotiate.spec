%define modname	HTTP-Negotiate
%define modver 6.01

Summary:	HTTP content negotiation
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Negotiate-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(HTTP::Headers)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*


