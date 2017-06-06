Name:    hyperscan
Version: 4.4.1
Release: 1%{?dist}
Summary: High-performance regular expression matching library

License: BSD
URL:     https://01.org/hyperscan
Source0: https://github.com/01org/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:  honor-install-paths.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  pcre-devel
BuildRequires:  python
BuildRequires:  ragel
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  libpcap-devel

Requires:       pcre

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
Summary: Libraries and header files for the hyperscan library
Requires: %{name}%{?_isa} = %{version}-%{release}

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
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_AND_SHARED:BOOL=OFF .

%make_build

%install
%make_install

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
* Fri May 12 2017 Jason Taylor <jtfas90@gmail.com> - 4.4.1-1
- Update to latest upstream
- Add CMakeLists.txt path patch
- Spec file updates to meet packaging standards

* Mon Jan 30 2017 Jason Ish <ish@unx.ca> - 4.4.0-1
- Update to 4.4.0.

* Fri Sep 2 2016 Jason Taylor <jtfas90@gmail.com> - 4.3.1-1
- Updated to latest upstream release.

* Fri Jul 1 2016 Jason Ish <ish@unx.ca> - 4.2.0-1
- Initial package of Hyperscan.
