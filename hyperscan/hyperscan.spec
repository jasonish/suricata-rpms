%global commit0 d2e5089dc33c3f9d762898eefece67fe5ab323ea
%global gittag0 v4.3.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global _hardened_build 1

Name:		hyperscan
Version:	4.3.1
Release:	1%{?dist}
Summary:	High-performance regular expression matching library

License:	BSD
URL:		https://01.org/hyperscan
Source0:	https://github.com/01org/%{name}/archive/%{gittag0}.tar.gz#/%{name}-%{gittag0}.tar.gz
Patch1:		lib-suffix.patch
Patch2:         change-march-native.patch

BuildRequires:	boost-devel
BuildRequires:  cmake
BuildRequires:	pcre-devel
BuildRequires:	python
BuildRequires:  ragel

Requires:	pcre

#package requires SSE support and fails to build on non x86_64 archs
ExclusiveArch: x86_64

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
Summary:	Libraries and header files for the hyperscan library
Requires:	%{name}%{?_isa} = %{version}-%{release}

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
%patch2

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_AND_SHARED:BOOL=OFF .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc CHANGELOG.md
%doc README.md
%license COPYING
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhs.pc
%{_includedir}/hs/

%changelog
* Fri Sep 2 2016 Jason Taylor <jtfas90@gmail.com> - 4.3.1-1
- Updated to latest upstream release.

* Fri Jul 1 2016 Jason Ish <ish@unx.ca> - 4.2.0-1
- Initial package of Hyperscan.
