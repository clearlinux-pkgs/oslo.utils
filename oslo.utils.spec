#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : oslo.utils
Version  : 3.36.4
Release  : 46
URL      : http://tarballs.openstack.org/oslo.utils/oslo.utils-3.36.4.tar.gz
Source0  : http://tarballs.openstack.org/oslo.utils/oslo.utils-3.36.4.tar.gz
Source99 : http://tarballs.openstack.org/oslo.utils/oslo.utils-3.36.4.tar.gz.asc
Summary  : Oslo Utility library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.utils-python3
Requires: oslo.utils-license
Requires: oslo.utils-python
Requires: Sphinx
Requires: debtcollector
Requires: fixtures
Requires: funcsigs
Requires: iso8601
Requires: monotonic
Requires: netaddr
Requires: netifaces
Requires: oslo.i18n
Requires: pbr
Requires: pyparsing
Requires: pytz
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package license
Summary: license components for the oslo.utils package.
Group: Default

%description license
license components for the oslo.utils package.


%package python
Summary: python components for the oslo.utils package.
Group: Default
Requires: oslo.utils-python3

%description python
python components for the oslo.utils package.


%package python3
Summary: python3 components for the oslo.utils package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.utils package.


%prep
%setup -q -n oslo.utils-3.36.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532198980
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslo.utils
cp LICENSE %{buildroot}/usr/share/doc/oslo.utils/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/oslo.utils/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
