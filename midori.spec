%define name midori
%define version 0.0.1
%define release %mkrel 1

Summary: Web browser based on GTK+ WebCore
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.bz2
# Fixes build against current GTK+ WebCore. By AdamW.
Patch0: midori-0.0.1-build.patch
License: GPL
Group: Networking/WWW
Url: http://software.twotoasts.de/?page=midori
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtk-webcore-nrcit-devel libsexy-devel
Requires: gtk-webcore-nrcore

%description
Midori is a lightweight GTK+ 2 web browser based on GTK+ WebCore. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q
%patch0 -p1 -b .build

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Midori
Comment=Lightweight web browser
Exec=%{_bindir}/%{name} 
Icon=web_browser_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Network;WebBrowser;X-MandrivaLinux-Internet-WebBrowsers;
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
