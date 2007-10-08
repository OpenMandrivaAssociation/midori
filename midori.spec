%define name	midori
%define version	0.0.8
%define release	%mkrel 1

Summary:	Web browser based on GdkWebKit
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
Patch0:		midori-0.0.8-new_api.patch
License:	GPLv2+
Group:		Networking/WWW
URL:		http://software.twotoasts.de/?page=midori
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	WebKitGtk-devel libsexy-devel

%description
Midori is a lightweight GTK+ 2 web browser based on WebKitGdk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q
%patch0 -p0

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
