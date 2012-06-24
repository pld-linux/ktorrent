Summary:	Native KDE BitTorrent client
Summary(de):	Ein nativer KDE BitTorrent Klient
Summary(pl):	Natywny klient BitTorrenta dla KDE
Name:		ktorrent
Version:	2.0.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.pwsp.net/downloads/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6e6233e8f7104639f2929abeb7320333
Patch0:		kde-ac260.patch
URL:		http://ktorrent.pwsp.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
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

%description -l de
KTorrent ist ein BitTorrent Klient f�r KDE.

Hauptfunktionen sind:
- Torrent-Dateien Download
- Begr�nzung des Uploades, so dass Mehrheit der Leute nicht unerlaubt
  unbegr�nzte Datenfl�sse sendet
- Durchsuchung des Internets mit hilfe diverser Browser, man kann
  sogar den eigenen Browser dazu schreiben
- UDP Trackers

%description -l pl
KTorrent to klient BitTorrenta dla KDE.

G��wne cechy to:
- �ci�ganie plik�w torrent
- ograniczanie szybko�ci uploadu, bacz�ce �eby wi�kszo�� ludzi nie
  przesy�a�a nieograniczonej ilo�ci danych
- przeszukiwanie Internetu przy u�yciu r�nych wyszukiwarek, mo�na
  nawet doda� w�asn�
- trackery UDP

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-knetwork \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/ktorrent.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktcachecheck
%attr(755,root,root) %{_bindir}/ktorrent
%attr(755,root,root) %{_bindir}/ktshell
%attr(755,root,root) %{_bindir}/kttorinfo
%attr(755,root,root) %{_bindir}/ktupnptest
%attr(755,root,root) %{_libdir}/libktorrent.so.*.*.*
%{_libdir}/libktorrent.la
%{_libdir}/kde3/ktinfowidgetplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktinfowidgetplugin.so
%{_libdir}/kde3/ktipfilterplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktipfilterplugin.so
%{_libdir}/kde3/ktlogviewerplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktlogviewerplugin.so
%{_libdir}/kde3/ktpartfileimportplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktpartfileimportplugin.so
%{_libdir}/kde3/ktsearchplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktsearchplugin.so
%{_libdir}/kde3/ktupnpplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktupnpplugin.so
%{_libdir}/kde3/ktscanfolderplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktscanfolderplugin.so
%{_libdir}/kde3/ktschedulerplugin.la
%attr(755,root,root) %{_libdir}/kde3/ktschedulerplugin.so
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/ktorrent.kcfg
%{_datadir}/config.kcfg/ktinfowidgetplugin.kcfg
%{_datadir}/config.kcfg/ktipfilterplugin.kcfg
%{_datadir}/config.kcfg/ktsearchplugin.kcfg
%{_datadir}/config.kcfg/ktupnpplugin.kcfg
%{_datadir}/config.kcfg/ktscanfolderplugin.kcfg
%{_datadir}/config.kcfg/ktschedulerplugin.kcfg
%{_datadir}/config.kcfg/ktlogviewerplugin.kcfg
%{_datadir}/services/ktinfowidgetplugin.desktop
%{_datadir}/services/ktipfilterplugin.desktop
%{_datadir}/services/ktlogviewerplugin.desktop
%{_datadir}/services/ktpartfileimportplugin.desktop
%{_datadir}/services/ktsearchplugin.desktop
%{_datadir}/services/ktupnpplugin.desktop
%{_datadir}/services/ktscanfolderplugin.desktop
%{_datadir}/services/ktschedulerplugin.desktop
%{_datadir}/servicetypes/ktorrentplugin.desktop
%{_desktopdir}/kde/ktorrent.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/ktorrent.svgz
%{_iconsdir}/hicolor/128x128/mimetypes/torrent.png
%{_iconsdir}/hicolor/16x16/mimetypes/torrent.png
%{_iconsdir}/hicolor/22x22/mimetypes/torrent.png
%{_iconsdir}/hicolor/32x32/mimetypes/torrent.png
%{_iconsdir}/hicolor/48x48/mimetypes/torrent.png
%{_iconsdir}/hicolor/64x64/mimetypes/torrent.png
%{_iconsdir}/hicolor/scalable/mimetypes/torrent.svgz
