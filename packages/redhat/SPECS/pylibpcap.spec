Name:           pylibpcap
Version:        %{_version}
Release:        1
Summary:        Python interface to libpcap

License:        BSD
URL:            http://pylibpcap.sourceforge.net
Source0:        http://downloads.sourceforge.net/pylibpcap/pylibpcap-%{_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools libpcap-devel
Requires:       python

%description
Python interface to libpcap

%install
./setup.py install --root %{buildroot}

%files
%{buildroot}/*

%changelog
* Fri Aug 15 2014 Simon Cadman <src@niftiestsoftware.com> - 0.6.4-3
- Initial package creation