Summary:	Native KDE BitTorrent client
Name:		ktorrent
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.pwsp.net/downloads/1.1/%{name}-%{version}.tar.gz
# Source0-md5:	d282e2cef75f2e4cf4bf5a84e0f45d3c
URL:		http://ktorrent.pwsp.net/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTorrent is a BitTorrent program for KDE.

Its main features are:
- Downloads torrent files
- Upload speed capping, seeing that most people can't upload infinite
  amounts of data.
- Internet searching using various search engines, you can even add
  your own.
- UDP Trackers

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/ktorrent.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktcachecheck
%attr(755,root,root) %{_bindir}/ktorrent
%attr(755,root,root) %{_bindir}/kttorinfo
%{_desktopdir}/kde/ktorrent.desktop
%{_datadir}/apps/ktorrent/icons/hicolor/128x128/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/16x16/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/actions/ktremove.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/actions/ktstart.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/actions/ktstart_all.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/actions/ktstop.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/actions/ktstop_all.png
%{_datadir}/apps/ktorrent/icons/hicolor/22x22/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/32x32/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/48x48/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/64x64/apps/ktorrent.png
%{_datadir}/apps/ktorrent/icons/hicolor/64x64/filesystems/ktprefdownloads.png
%{_datadir}/apps/ktorrent/icons/hicolor/scalable/apps/ktorrent.svgz
%{_datadir}/apps/ktorrent/ktorrentui.rc
%{_datadir}/config.kcfg/ktorrent.kcfg
%{_iconsdir}/hicolor/128x128/apps/ktorrent.png
%{_iconsdir}/hicolor/16x16/apps/ktorrent.png
%{_iconsdir}/hicolor/22x22/apps/ktorrent.png
%{_iconsdir}/hicolor/32x32/apps/ktorrent.png
%{_iconsdir}/hicolor/48x48/apps/ktorrent.png
%{_iconsdir}/hicolor/64x64/apps/ktorrent.png
%{_iconsdir}/hicolor/scalable/apps/ktorrent.svgz
