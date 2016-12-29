Name:           colm
Version:        0.13.0.4
Release:        1%{?dist}
Summary:        Programming language designed for the analysis of computer languages

# aapl/ and some headers from src/ are the LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://www.colm.net/open-source/colm/
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)

%description
Colm is a programming language designed for the analysis and transformation
of computer languages. Colm is influenced primarily by TXL. It is
in the family of program transformation languages.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
# Do not pollute with docs
sed -i -e "/dist_doc_DATA/d" Makefile.am

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -print -delete
install -p -m 0644 -D %{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_libdir}/lib%{name}-%{version}.so
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13.0.4-1
- Initial package
