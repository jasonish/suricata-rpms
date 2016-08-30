%global _hardened_build 1

Name:		hyperscan
Version:	4.2.0
Release:	1%{?dist}
Summary:	High-performance regular expression matching library

License:	BSD
URL:		https://01.org/hyperscan
Source0:	https://github.com/01org/%{name}/archive/v%{version}.tar.gz
Patch1:		lib-suffix.patch

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	pcre-devel
BuildRequires:	python
BuildRequires:	ragel

Requires:	pcre

%description
Hyperscan is a high-performance multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.


%package devel
Summary:	Libraries and header files for the hyperscan library.
Requires:	%{name} = %{version}-%{release}

%description devel
Hyperscan is a high-performance multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

This package provides the libraries, include files and other resources
needed for developing Hyperscan applications.

%prep
%setup -q
%patch1 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -march=core2"
export CXXFLAGS="${CFLAGS}"
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_AND_SHARED:BOOL=ON .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_libdir}

%files
%doc CHANGELOG.md
%doc COPYING
%doc LICENSE
%doc README.md
%{_libdir}/libhs*

%files devel
%{_includedir}/hs/*
%{_libdir}/pkgconfig/libhs.pc

%changelog
* Fri Jul  1 2016 Jason Ish <ish@unx.ca> - 4.2.0-1
- Initial package of Hyperscan.
