%define name midori
%define version 0.0.5
%define release %mkrel 1

Summary: Web browser based on GdkWebKit
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
License: GPL
Group: Networking/WWW
Url: http://software.twotoasts.de/?page=midori
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: WebKitGdk-devel libsexy-devel

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGdk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Midori
Comment=Lightweight web browser
Exec=%{_bindir}/%{name} 
Icon=web_browser_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Network;WebBrowser;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/%{name}
%_datadir/applications/mandriva-%{name}.desktop
