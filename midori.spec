%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Web browser based on WebKitGtk
Name:		midori
Version:	0.5.5
Release:	1
License:	LGPLv2+
Group:		Networking/WWW
URL:		http://www.twotoasts.de/index.php?/pages/midori_summary.html
# For git: git clone http://software.twotoasts.de/media/midori.git
Source0:	http://www.midori-browser.org/downloads/%{name}_%{version}_all_.tar.bz2
# (tpg) set default homepage
#but why? google.com seems to be ok page for default
#Patch0:	midori-0.2.4-default-homepage.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	librsvg
BuildRequires:	python-docutils
BuildRequires:	waf
BuildRequires:	vala >= 0.13.2
BuildRequires:	pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.8.0
BuildRequires:	pkgconfig(gthread-2.0) >= 2.8.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libidn) >= 1.0
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6
BuildRequires:	pkgconfig(sqlite3) >= 3.0
BuildRequires:	pkgconfig(unique-3.0) >= 0.9
BuildRequires:	pkgconfig(webkitgtk-3.0) >= 1.1.17
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(zeitgeist-1.0)
Requires:	indexhtml
Requires:	xdg-utils
Requires:	glib-networking
Requires:	dbus-x11
Provides:	webclient

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%package vala
Group:		Networking/WWW
Summary:	vala supported extensions for %{name}
Requires:	%{name} = %{version}

%description vala
This package contains files needed when building vala supported extensions for
%{name}.

%package devel
Group:		Networking/WWW
Summary:	Development files for building Vala supported extensions for %{name}
Obsoletes:	%{name}-vala < 0.5.2-1

%description devel
This package contains files needed when building vala supported extensions
for %{name}.


%prep
%setup -q
%apply_patches

# (tpg) fix module naming
sed -i -e 's/import UnitTest/import unittest/g' wscript

%build
#% setup_compile_flags
#this macro fails build process
export CFLAGS="%{optflags} -fPIC"

# (tpg) midori needs waf-1.5, so use internal one
./waf configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--enable-gtk3 \
	--enable-addons

./waf build \
	--want-rpath=0

%install
./waf install \
	--destdir=%{buildroot}


#fix desktop file
desktop-file-install \
	--remove-not-show-in="Pantheon" \
	--dir %{buildroot}%{_datadir}/applications \
		 %{buildroot}%{_datadir}/applications/*.desktop


%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}
%{_sysconfdir}/xdg/midori

%files vala
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files devel
%{_includedir}/%{name}*
