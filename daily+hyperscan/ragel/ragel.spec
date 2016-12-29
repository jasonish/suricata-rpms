%bcond_with bootstrap

Name:           ragel   
Version:        7.0.0.9
Release:        1%{?dist}
Summary:        Finite state machine compiler

# aapl/ is the LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://www.complang.org/%{name}/
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
%if %{with bootstrap}
BuildRequires:  kelbt
BuildRequires:  ragel
%endif
BuildRequires:  colm-devel

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)

%description
Ragel compiles executable finite state machines from regular languages.
Ragel targets C, C++ and ASM. Ragel state machines can not only recognize
byte sequences as regular expression machines do, but can also execute code
at arbitrary points in the recognition of a regular language. Code embedding
is done using inline operators that do not disrupt the regular language syntax.

%package devel
Summary:        Development libraries header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
# Do not pollute with docs
sed -i -e "/dist_doc_DATA/d" Makefile.am
# Put headers under subdir
sed -i -e "s/include_HEADERS/pkginclude_HEADERS/g" src/Makefile.am aapl/Makefile.am

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
%doc CREDITS ChangeLog
#doc doc/ragel-guide.pdf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_libdir}/lib%{name}.so.*
%{_libdir}/libfsm.so.*
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/libfsm.so
%{_includedir}/%{name}/

%changelog
* Fri Oct 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 7.0.0.9-1
- Fix FTBFS
- Update to 7.0.0.9
- Trivial fixes in spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.8-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 08 2013 Jeremy Hinegardner <jeremy@hinegardner.org> - 6.8-1
- Update to upstream 6.8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 6.6-6
- Fix build with gcc47
- Pass fedora cflags correctly

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 6.6-2
- rebuild to ensure F14 has higher NVR than F13

* Thu Feb 18 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.6-0
- update to 6.6
- remove patch, fix applied upstream

* Sun Aug 02 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.5-2
- fix build process 

* Sun Aug 02 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.5-1
- Update to 6.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> 6.4-3
-  remove main.cpp patch for testing

* Sat Apr 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> 6.4-2
-  add patch for main.cpp

* Sat Apr 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> 6.4-1
-  Update to 6.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.3-1
- update to 6.3

* Mon May 12 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.2-1
- update to 6.2

* Mon Apr 14 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.1-1
- update to 6.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.0-2
- Autorebuild for GCC 4.3

* Sat Jan 19 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 6.0-1
- update to 6.0

* Sun Jan 06 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 5.25-1
- update to 5.25

* Tue Sep 18 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.24-1
- update to 5.24
- update License tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 5.23-2
- Rebuild for selinux ppc32 issue.

* Tue Jul 24 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.23-1
- update to 5.23
- removed ragel-rlcodegen-replace.patch - it was applied upstream

* Mon Jun 18 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.22-1
- update to 5.22
- remove ragel-Makefile-in.patch - it was applied upstream
- update ragel-rlcodegen-replace.patch to apply cleanly

* Sat Mar 24 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-4
- further replacement of rlcodegen
- rework patches

* Fri Mar 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-3
- replace RPM_BUILD_ROOT in spec file with buildroot macro
- cleanup rpmlint errors for the src.rpm
- add ragel(1) man page patch

* Tue Mar 20 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-1
- Creation of spec file
