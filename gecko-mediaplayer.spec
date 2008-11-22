Name:           gecko-mediaplayer
Version:        0.9.2
Release:        1%{?dist}
Summary:        Gnome MPlayer browser plugin

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://code.google.com/p/gecko-mediaplayer/
Source0:        http://gecko-mediaplayer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  dbus-glib-devel
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  libX11-devel
BuildRequires:  gecko-devel

Requires:       %{_libdir}/mozilla/plugins
Requires:       gnome-mplayer-core-functionality >= %{version}

Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2

Obsoletes:      mplayerplug-in < 3.50

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to play media in
a browser. It should work with all browsers on Unix-ish systems(Linux, BSD,
Solaris) and use the NS4 API (Mozilla, Firefox, Opera, etc.).


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

#remove intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gecko-mediaplayer


%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/gecko-mediaplayer.schemas >/dev/null || :
    # If the schema file has ever been renamed::
    #gconftool-2 --makefile-uninstall-rule \
    #  %{_sysconfdir}/gconf/schemas/[OLDNAME].schemas > /dev/null || :
fi


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/gecko-mediaplayer.schemas > /dev/null || :


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/gecko-mediaplayer.schemas > /dev/null || :
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_sysconfdir}/gconf/schemas/gecko-mediaplayer.schemas
%{_libdir}/mozilla/plugins/gecko-mediaplayer-dvx.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-dvx.xpt
%{_libdir}/mozilla/plugins/gecko-mediaplayer-qt.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-qt.xpt
%{_libdir}/mozilla/plugins/gecko-mediaplayer-rm.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-rm.xpt
%{_libdir}/mozilla/plugins/gecko-mediaplayer-wmp.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-wmp.xpt
%{_libdir}/mozilla/plugins/gecko-mediaplayer.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer.xpt


%changelog
* Sat Nov 22 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.2-1
- Updated to 0.9.2
- Require gnome-mplayer-core-functionality instead of gnome-mplayer

* Fri Oct 31 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.0-1
- Updated to 0.9.0

* Mon Sep 29 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.0-1.1
- Updated to 0.8.0

* Sun Aug 17 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.0-1.1
- Updated to 0.7.0

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.6.3-3
- rebuild for buildsys cflags issue

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.6.3-2
- rebuild for buildsys cflags issue

* Sun Jul  6 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-1
- Updated to 0.6.3

* Wed May 28 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.2-1
- Updated to 0.6.2

* Thu Apr 17 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.1-1
- Updated to 0.6.1
- Updated URL and Source0
- Dropped upstreamed patch
- Dropped the rpmfusion-specific readme

* Fri Mar  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.0-3
- Added patch fixing unnecessary libxul-embedding.pc from SVN

* Fri Feb 29 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.0-2
- Switched to gecko-devel virtual provides
- Made the mplayerplug-in obsoletion versioned
- Ditto gnome-mplayer requirement

* Wed Feb 13 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.0-1
- Initial rpmfusion release
