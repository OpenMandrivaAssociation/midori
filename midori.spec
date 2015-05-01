%define major	1
%define libname	%mklibname %{name}-core %{major}
%define devname	%mklibname %{name}-core -d

Summary:	Web browser based on WebKitGtk
Name:		midori
Version:	0.5.10
Release:	1
License:	LGPLv2+
Group:		Networking/WWW
URL:		http://www.midori-browser.org/
Source0:	http://www.midori-browser.org/downloads/%{name}_%{version}_all_.tar.bz2
BuildRequires:  vala
BuildRequires:  cmake
BuildRequires:  librsvg
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.8.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.8.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libidn) >= 1.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(sqlite3) >= 3.0
BuildRequires:  pkgconfig(unique-3.0) >= 0.9
BuildRequires:  pkgconfig(webkitgtk-3.0) >= 1.1.17
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(gcr-3)
Provides:	webclient
Requires:	indexhtml
Requires:	xdg-utils
Requires:	glib-networking
Requires:	gsettings-desktop-schemas

%description
Midori is a lightweight GTK+ 3 web browser based on WebKitGtk. It
features tabs, windows and session management, bookmarks stored with
XBEL, searchbox based on OpenSearch, and user scripts support.

%package -n %{libname}
Summary:	Core libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the core libraries for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 0.5.7

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q -c
%apply_patches

%build
%cmake -DUSE_APIDOCS=1 -DUSE_GTK3=ON -DUSE_ZEITGEIST=OFF
%make

%install
%makeinstall_std -C build

#fix desktop file
desktop-file-install \
	--remove-not-show-in="Pantheon" \
	--dir=%{buildroot}%{_datadir}/applications/ \
		 %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}
%{_sysconfdir}/xdg/midori
%{_datadir}/appdata/midori.appdata.xml

%files -n %{libname}
%{_libdir}/libmidori-core.so.%{major}
# wrongly named?!
%{_libdir}/libmidori-core.so.0.*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/%{name}*
%{_libdir}/libmidori-core.so
