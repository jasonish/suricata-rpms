Name: suricata-beta-release-el
Version: 7
Release: 3%{?dist}
Summary: Suricata Beta Packages for Enterprise Linux and EL Like Systems
Group: Applications/Internet
License: Freeware
Source0: suricata-beta.repo
Source1: RPM-GPG-KEY-suricata-beta

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
Requires: redhat-release >= %{version} 
Requires: epel-release >= %{version}
Conflicts: fedora-release

%description 
This package contains the YUM repository information for Suricata beta
packages for Enterprise Linux.


%prep


%build


%install
rm -rf $RPM_BUILD_ROOT

# GPG key.
install -Dpm 644 %{SOURCE1} \
        $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-suricata-beta

# Create directories.
install -d -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# The yum repo file.
%{__install} -p -m0644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/


%clean
rm -rf $RPM_BUILD_ROOT


%post


%postun 


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg


%changelog
* Tue Jan 26 2016 Jason Ish <ish@unx.ca> - 7-3
- GPG key; new URL.

* Mon Dec 29 2014 Jason Ish <ish@unx.ca> - 7-1
- Initial package.
