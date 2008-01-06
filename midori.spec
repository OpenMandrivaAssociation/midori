%define name	midori
%define version	0.0.16
%define release	%mkrel 1

Summary:	Web browser based on WebKitGtk
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Networking/WWW
URL:		http://software.twotoasts.de/?page=midori
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	WebKitGtk-devel libsexy-devel
BuildRequires:	icu-devel

%description
Midori is a lightweight Gtk+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q
# Fix files date in the future...
find -exec touch {} \;

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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
%_datadir/applications/%{name}.desktop
