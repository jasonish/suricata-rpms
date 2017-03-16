%global commit0 7aff6f6136e659f9dab48f2d383baa0fcb08bbc0
%global gittag0 v4.4.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global _hardened_build 1

Name:		hyperscan
Version:	4.4.1
Release:	1%{?dist}
Summary:	High-performance regular expression matching library

License:	BSD
URL:		https://01.org/hyperscan
Source0:	https://github.com/01org/%{name}/archive/%{gittag0}.tar.gz#/%{name}-%{gittag0}.tar.gz
Source1:	http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.gz
Patch1:		lib-suffix.patch
Patch2:         change-march-native.patch

BuildRequires:  cmake
BuildRequires:	pcre-devel
BuildRequires:	python
BuildRequires:  ragel
BuildRequires:	sqlite-devel

Requires:	pcre
Requires:	sqlite

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
%patch2 -p1
%if 0%{?fedora} == 0
(cd include && tar zxf %{SOURCE1} boost_1_61_0/boost --strip-components=1)
%endif


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
* Mon Jan 30 2017 Jason Ish <ish@unx.ca> - 4.4.0-1
- Update to 4.4.0.

* Fri Sep 2 2016 Jason Taylor <jtfas90@gmail.com> - 4.3.1-1
- Updated to latest upstream release.

* Fri Jul 1 2016 Jason Ish <ish@unx.ca> - 4.2.0-1
- Initial package of Hyperscan.
