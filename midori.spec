Summary:	Web browser based on WebKitGtk
Name:		midori
Version:	0.0.17
Release:	%mkrel 1
Source:		http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Networking/WWW
URL:		http://software.twotoasts.de/?page=midori
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	WebKitGtk-devel
BuildRequires:	libsexy-devel
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libxslt-devel

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
rm -rf %{buildroot}
%makeinstall_std

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
