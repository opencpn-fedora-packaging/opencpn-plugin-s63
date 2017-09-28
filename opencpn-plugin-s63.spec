%global commit e3fab8b9f91cb12459fc7b9321b5a645f6f5b06a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner bdbcat
%global project s63_pi
%global plugin s63

Name: opencpn-plugin-s63
Summary: S-63 chart plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
S-63 is the encrypted distribution format for S-57 vector charts.
Today, hydrographical offices all over the world are producing their
official vector charts in the S-57 format.  Distribution is done under
the S-63 standard.  To use the encrypted charts, you must get a
license for your particular machine (called a Permit).  Visit
o-charts.org for more information and to get the permits.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_bindir}/OCPNsenc

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
