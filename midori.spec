%define git	20080906
%define rel	1

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
Version:	0.0.22
Release:	%{release}
# For git: git clone http://software.twotoasts.de/media/midori.git
Source0:	http://goodies.xfce.org/releases/midori/%{distname}
License:	GPLv2+
Group:		Networking/WWW
URL:		http://www.twotoasts.de/index.php?/pages/midori_summary.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	webkitgtk-devel
BuildRequires:	libsexy-devel
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	librsvg
Provides:	webclient

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q -n %{dirname}
# Fix files date in the future...
find -exec touch {} \;

%build
./waf configure --prefix=%{_prefix} --datadir=%{_datadir}
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./waf build %{_smp_mflags}

%install
rm -rf %{buildroot}
./waf install --destdir=%buildroot

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
