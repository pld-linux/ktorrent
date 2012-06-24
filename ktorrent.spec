Summary:	Native KDE BitTorrent client
Summary(pl):	Natywny klient BitTorrenta dla KDE
Name:		ktorrent
Version:	1.2
Release:	0.rc1.1
License:	GPL
Group:		Applications/Networking
Source0:	http://ktorrent.pwsp.net/downloads/1.2rc1/%{name}-%{version}rc1.tar.gz
# Source0-md5:	c5dbd27aa19e2c8f8dbe210c9e36b469
URL:		http://ktorrent.pwsp.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
%setup -q -n %{name}-%{version}rc1

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
%attr(755,root,root) %{_bindir}/kttorinfo
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
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/ktorrent.kcfg
%{_datadir}/config.kcfg/ktinfowidgetplugin.kcfg
%{_datadir}/config.kcfg/ktipfilterplugin.kcfg
%{_datadir}/config.kcfg/ktsearchplugin.kcfg
%{_datadir}/config.kcfg/ktupnpplugin.kcfg
%{_datadir}/services/ktinfowidgetplugin.desktop
%{_datadir}/services/ktipfilterplugin.desktop
%{_datadir}/services/ktlogviewerplugin.desktop
%{_datadir}/services/ktpartfileimportplugin.desktop
%{_datadir}/services/ktsearchplugin.desktop
%{_datadir}/services/ktupnpplugin.desktop
%{_datadir}/servicetypes/ktorrentplugin.desktop
%{_desktopdir}/kde/ktorrent.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/ktorrent.svgz
