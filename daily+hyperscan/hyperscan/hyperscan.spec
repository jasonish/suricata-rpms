Name:		hyperscan
Version:	4.2.0
Release:	1%{?dist}
Summary:	High-performance regular expression matching library

License:	BSD
URL:		https://01.org/hyperscan
Source0:	https://github.com/01org/hyperscan/archive/v%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake pcre-devel ragel
# Fedora has a recent enough version of boost.
%if 0%{?fedora}
BuildRequires:	boost-devel
%endif
BuildRequires:	python
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


%prep
%setup -q
%if 0%{?fedora} == 0
(cd include && tar zxf %{SOURCE1} boost_1_61_0/boost --strip-components=1)
%endif


%build
%cmake -DLIB_INSTALL_DIR:PATH=%{_libdir} -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DBUILD_STATIC_AND_SHARED:BOOL=ON .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}


%files
%doc CHANGELOG.md
%doc COPYING
%doc LICENSE
%doc README.md
%{_includedir}/hs/*
%{_libdir}/*


%changelog
* Tue Jun  7 2016 Jason Ish <ish@unx.ca> - 4.2.0-1
- Update to Hyperscan 4.2.0.

* Mon May 16 2016 Jason Ish <ish@unx.ca> - 4.1.0-1
- Initial package of Hyperscan.
