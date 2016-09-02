#
%define         qtver   4.6.3
%define		kdever	4.5.0

Summary:	Native KDE BitTorrent client
Summary(de.UTF-8):	Ein nativer KDE BitTorrent Klient
Summary(pl.UTF-8):	Natywny klient BitTorrenta dla KDE
Name:		ktorrent
Version:	4.3.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	696852076315d3aa8ccc8745482872dd
# Patch0:		plasma_applet_remove_taskmanager.diff
Patch0:		Fix-compilation-of-ipblocklisttest-target.patch
URL:		http://ktorrent.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-tools
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	libktorrent-devel >= 1.3
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	taglib-devel
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

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# remove lib symlinks - devel subpackage is not needed anyway
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so

# remove unsupported langs
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavian*
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ar
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/eu
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/se

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktorrent
%attr(755,root,root) %{_bindir}/ktmagnetdownloader
%attr(755,root,root) %{_bindir}/ktupnptest
%attr(755,root,root) %{_libdir}/kde4/ktbwschedulerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktinfowidgetplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktipfilterplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktlogviewerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktscanfolderplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktsearchplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktstatsplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktupnpplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktwebinterfaceplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktmagnetgeneratorplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktmediaplayerplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktzeroconfplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktdownloadorderplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktshutdownplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktscriptingplugin.so
%attr(755,root,root) %{_libdir}/kde4/ktsyndicationplugin.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_ktorrent.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_ktorrent.so
%attr(755,root,root) %ghost %{_libdir}/libktcore.so.??
%attr(755,root,root) %{_libdir}/libktcore.so.*.*.*
%{_desktopdir}/kde4/ktorrent.desktop
%{_datadir}/apps/ktorrent
%{_datadir}/kde4/services/ktbwschedulerplugin.desktop
%{_datadir}/kde4/services/ktinfowidgetplugin.desktop
%{_datadir}/kde4/services/ktipfilterplugin.desktop
%{_datadir}/kde4/services/ktlogviewerplugin.desktop
%{_datadir}/kde4/services/ktscanfolderplugin.desktop
%{_datadir}/kde4/services/ktsearchplugin.desktop
%{_datadir}/kde4/services/ktstatsplugin.desktop
%{_datadir}/kde4/services/ktupnpplugin.desktop
%{_datadir}/kde4/services/ktwebinterfaceplugin.desktop
%{_datadir}/kde4/servicetypes/ktorrentplugin.desktop
%{_datadir}/kde4/services/ktmagnetgeneratorplugin.desktop
%{_datadir}/kde4/services/ktmediaplayerplugin.desktop
%{_datadir}/kde4/services/ktzeroconfplugin.desktop
%{_datadir}/kde4/services/ktdownloadorderplugin.desktop
%{_datadir}/kde4/services/ktscriptingplugin.desktop
%{_datadir}/kde4/services/ktshutdownplugin.desktop
%{_datadir}/kde4/services/ktsyndicationplugin.desktop
%{_datadir}/kde4/services/magnet.protocol
%{_datadir}/kde4/services/plasma-dataengine-ktorrent.desktop
%{_datadir}/kde4/services/plasma-applet-ktorrent.desktop
%{_iconsdir}/*/*/actions/kt-*.png
%{_iconsdir}/*/*/apps/ktorrent.png
%{_iconsdir}/*/*/actions/kt-*.svgz
