%define git	0
%define rel	1

%define url_ver %(echo %{version} | cut -c 1-3)

%if %git
%define release		%mkrel 0.%git.%rel
%define distname	%name-%git.tar.lzma
%define dirname		%name
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.bz2
%define dirname		%name-%version
%endif

Summary:	Web browser based on WebKitGtk
Name:		midori
Version:	0.4.1
Release:	%{release}
License:	LGPLv2+
Group:		Networking/WWW
URL:		http://www.twotoasts.de/index.php?/pages/midori_summary.html
# For git: git clone http://software.twotoasts.de/media/midori.git
Source0:	http://archive.xfce.org/src/apps/midori/%{url_ver}/%{distname}
# (tpg) set default homepage
Patch0:		midori-0.2.4-default-homepage.patch
BuildRequires:	webkitgtk-devel >= 1.1.1
BuildRequires:	libsexy-devel
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	librsvg
BuildRequires:	unique-devel >= 0.9
BuildRequires:	libsoup-devel >= 2.25.2
BuildRequires:	libxml2-devel 
BuildRequires:	python-docutils
BuildRequires:	waf
BuildRequires:	vala
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libnotify-devel
Provides:	webclient
Requires:	indexhtml
Requires:	xdg-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%package vala
Group:   Networking/WWW
Summary: vala supported extensions for %{name}
Requires: %{name} = %{version}

%description vala
This package contains files needed when building vala supported extensions for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%serverbuild

# (tpg) fix module naming
sed -i -e 's/import UnitTest/import unittest/g' wscript

# (tpg) midori needs waf-1.5, so use internal one
./waf \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --enable-addons \
    --enable-libidn \
    configure

./waf build --want-rpath=0

%install
rm -rf %{buildroot}
./waf --destdir=%{buildroot} install

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}
%{_sysconfdir}/xdg/midori

%files vala
%defattr(-,root,root)
%{_includedir}/%{name}-0.4/extensions/history-list.h
%{_datadir}/vala/vapi/history-list.deps
%{_datadir}/vala/vapi/history-list.vapi
