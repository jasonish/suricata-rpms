Name:		hyperscan
Version:	4.1.0
Release:	1%{?dist}
Summary:	High-performance regular expression matching library

License:	BSD
URL:		https://01.org/hyperscan
Source0:	https://github.com/01org/hyperscan/archive/v4.1.0.tar.gz
Source1:	http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake pcre-devel ragel
#BuildRequires:	boost-devel
BuildRequires:	python
Requires:	pcre

%description
High-performance regular expression matching library.


%prep
%setup -q
(cd include && tar zxf %{SOURCE1} boost_1_61_0/boost --strip-components=1)


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
* Mon May 16 2016 Jason Ish <ish@unx.ca> - 4.1.0-1
- Initial package of Hyperscan.
