#
# Conditional build:
%bcond_with	arts			# build with aRts support

Summary:	Native KDE BitTorrent client
Summary(de.UTF-8):	Ein nativer KDE BitTorrent Klient
Summary(pl.UTF-8):	Natywny klient BitTorrenta dla KDE
Name:		ktorrent
Version:	2.2.8
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c0bd753b27bbc3e404b6c59ceafb5f91
Patch0:		kde-common-LD_quote.patch
Patch1:		kde-ac260-lt.patch
Patch2:		%{name}-stl.patch
Patch3:		kde-am.patch
URL:		http://ktorrent.org/
BuildRequires:	autoconf
BuildRequires:	autoconf < 2.64
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# build broken with spaces in CC
%undefine	with_ccache

%description
KTorrent is a BitTorrent program for KDE.

Its main features are:
- Downloads torrent files
- Upload speed capping, seeing that most people can't upload infinite
  amounts of data.
- Internet searching using various search engines, you can even add
  your own.
- UDP Trackers

%description -l de.UTF-8
KTorrent ist ein BitTorrent Klient für KDE.

Hauptfunktionen sind:
- Torrent-Dateien Download
- Begränzung des Uploades, so dass Mehrheit der Leute nicht unerlaubt
  unbegränzte Datenflüsse sendet
- Durchsuchung des Internets mit hilfe diverser Browser, man kann
  sogar den eigenen Browser dazu schreiben
- UDP Trackers

%description -l pl.UTF-8
KTorrent to klient BitTorrenta dla KDE.

Główne cechy to:
- ściąganie plików torrent
- ograniczanie szybkości uploadu, baczące żeby większość ludzi nie
  przesyłała nieograniczonej ilości danych
- przeszukiwanie Internetu przy użyciu różnych wyszukiwarek, można
  nawet dodać własną
- trackery UDP

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-knetwork \
	--enable-mt \
	--disable-static \
	--with-pic \
	--with-gnu-ld \
	--disable-rpath \
	--disable-embedded \
	--enable-fast-install=yes \
	--with-xinerama \
	--disable-final \
	--with%{!?with_arts:out}-arts \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/ktorrent.desktop
rm -f $RPM_BUILD_ROOT%{_libdir}/{kde3/*.la,*.la}

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
%attr(755,root,root) %{_libdir}/libktorrent-*.*.*.so
%attr(755,root,root) %{_libdir}/libktorrent.so
%attr(755,root,root) %{_libdir}/kde3/ktinfowidgetplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktipfilterplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktlogviewerplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktpartfileimportplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktsearchplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktstatsplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktupnpplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktscanfolderplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktschedulerplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktrssfeedplugin.so
%attr(755,root,root) %{_libdir}/kde3/ktwebinterfaceplugin.so
#%attr(755,root,root) %{_libdir}/kde3/ktzeroconfplugin.so
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/ktorrent.kcfg
%{_datadir}/config.kcfg/ktinfowidgetplugin.kcfg
%{_datadir}/config.kcfg/ktipfilterplugin.kcfg
%{_datadir}/config.kcfg/ktsearchplugin.kcfg
%{_datadir}/config.kcfg/ktupnpplugin.kcfg
%{_datadir}/config.kcfg/ktscanfolderplugin.kcfg
%{_datadir}/config.kcfg/ktschedulerplugin.kcfg
%{_datadir}/config.kcfg/ktstatsplugin.kcfg
%{_datadir}/config.kcfg/ktlogviewerplugin.kcfg
%{_datadir}/config.kcfg/ktrssfeedplugin.kcfg
%{_datadir}/config.kcfg/ktwebinterfaceplugin.kcfg
%{_datadir}/services/ktinfowidgetplugin.desktop
%{_datadir}/services/ktipfilterplugin.desktop
%{_datadir}/services/ktlogviewerplugin.desktop
%{_datadir}/services/ktpartfileimportplugin.desktop
%{_datadir}/services/ktsearchplugin.desktop
%{_datadir}/services/ktstatsplugin.desktop
%{_datadir}/services/ktupnpplugin.desktop
%{_datadir}/services/ktscanfolderplugin.desktop
%{_datadir}/services/ktschedulerplugin.desktop
%{_datadir}/services/ktrssfeedplugin.desktop
%{_datadir}/services/ktwebinterfaceplugin.desktop
%{_datadir}/services/ktzeroconfplugin.desktop
%{_datadir}/servicetypes/ktorrentplugin.desktop
%{_desktopdir}/kde/ktorrent.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/ktorrent.svgz
%{_iconsdir}/hicolor/*x*/mimetypes/torrent.png
%{_iconsdir}/hicolor/scalable/mimetypes/torrent.svgz
