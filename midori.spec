%define git 	0
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
Version:	0.1.2
Release:	%{release}
# For git: git clone http://software.twotoasts.de/media/midori.git
Source0:	http://goodies.xfce.org/releases/midori/%{distname}
# Fix a 'format not a string literal and no format arguments' issue
# Will be fixed in next release / snapshot - AdamW 2008/12
Patch0:		midori-20081219-format.patch
License:	LGPLv2+
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
BuildRequires:	unique-devel
BuildRequires:	python-docutils
Provides:	webclient

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q -n %{dirname}
%patch0 -p1
# Fix files date in the future...
find -exec touch {} \;

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" ./waf configure --prefix=%{_prefix} --datadir=%{_datadir} --libdir=%{_libdir}
./waf build %{_smp_mflags}

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}

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
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}/*.png
