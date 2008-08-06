Summary:	Native KDE BitTorrent client
Summary(de.UTF-8):	Ein nativer KDE BitTorrent Klient
Summary(pl.UTF-8):	Natywny klient BitTorrenta dla KDE
Name:		ktorrent
Version:	3.1.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	082c5fb35face3b7290044bc053411a6
URL:		http://ktorrent.org/
BuildRequires:	QtCore-devel >= 4.4.0
BuildRequires:	QtNetwork-devel >= 4.4.0
BuildRequires:	cmake
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	strigi-devel >= 0.5.5
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
- ograniczanie szybkości uploadu, baczące żeby większość ludzi
  nie przesyłała nieograniczonej ilości danych
- przeszukiwanie Internetu przy użyciu różnych wyszukiwarek, można
  nawet dodać własną
- trackery UDP

%package devel
Summary:        Header files for ktorrent
Summary(pl.UTF-8):      Pliki nag�~Bówkowe ktorrent
Group:          Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ktorrent.

%description devel -l pl.UTF-8
Pliki nag�~Bówkowe ktorrent.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktorrent
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
%attr(755,root,root) %{_libdir}/kde4/ktmediaplayerplugin.so
%attr(755,root,root) %ghost %{_libdir}/libbtcore.so.?
%attr(755,root,root) %{_libdir}/libbtcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libktcore.so.?
%attr(755,root,root) %{_libdir}/libktcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libktupnp.so.?
%attr(755,root,root) %{_libdir}/libktupnp.so.*.*.*
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
%{_datadir}/kde4/services/ktmediaplayerplugin.desktop
%{_iconsdir}/*/*/actions/kt-*.png
%{_iconsdir}/*/*/apps/ktorrent.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/libbtcore
%{_libdir}/libbtcore.so
%{_libdir}/libktcore.so
%{_libdir}/libktupnp.so
