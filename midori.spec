Summary:	Web browser based on WebKitGtk
Name:		midori
Version:	0.0.17
Release:	%mkrel 2
Source:		http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
Patch0:		midori-0.0.17-middleclick.patch
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
Provides:	webclient

%description
Midori is a lightweight Gtk+ 2 web browser based on WebKitGtk. It 
features tabs, windows and session management, bookmarks stored with 
XBEL, searchbox based on OpenSearch, and user scripts support.

%prep
%setup -q
%patch0 -p1 -b .middle
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
