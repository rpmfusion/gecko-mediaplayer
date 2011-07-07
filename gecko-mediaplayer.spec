Name:           gecko-mediaplayer
Version:        1.0.4
Release:        2%{?dist}
Summary:        Gnome MPlayer browser plugin

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://kdekorte.googlepages.com/gecko-mediaplayer
Source0:        http://gecko-mediaplayer.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         %{name}-applefix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  dbus-glib-devel
%if 0%{?fedora} < 15
BuildRequires:  GConf2-devel
%endif
BuildRequires:  gettext
BuildRequires:  libcurl-devel
BuildRequires:  libX11-devel
BuildRequires:  gecko-devel

Requires:       mozilla-filesystem
Requires:       gnome-mplayer-binary >= %{version}

%if 0%{?fedora} < 15
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2
%endif

Obsoletes:      mplayerplug-in < 3.50

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to play media in
a browser. It should work with all browsers on Unix-ish systems(Linux, BSD,
Solaris) and use the NS4 API (Mozilla, Firefox, Opera, etc.).


%prep
%setup -q
%patch0 -p0 -b .applefix


%build
%if 0%{?fedora} == 14
%configure --with-gconf
%else
%configure
%endif
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?fedora} < 15
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%endif
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

#remove intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gecko-mediaplayer


%pre
%if 0%{?fedora} < 15
%gconf_schema_prepare gecko-mediaplayer
%endif


%post
%if 0%{?fedora} < 15
%gconf_schema_upgrade gecko-mediaplayer
%endif


%preun
%if 0%{?fedora} < 15
%gconf_schema_remove gecko-mediaplayer
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%if 0%{?fedora} < 15
%{_sysconfdir}/gconf/schemas/gecko-mediaplayer.schemas
%endif
%{_libdir}/mozilla/plugins/gecko-mediaplayer-dvx.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-qt.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-rm.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-wmp.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer.so


%changelog
* Thu Jul 07 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.4-2
- Fixed apple.com regression using a patch from SVN

* Fri Jul 01 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.4-1
- Updated to 1.0.4

* Fri May 13 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.3-2
- Added explicit libcurl-devel to BuildRequires

* Mon Apr 25 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.3-1
- Dropped included patches
- Added logic to support gsettings/GConf
- Updated GConf scriptlets to the latest spec

* Sat Nov 06 2010 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.0-1
- Updated to 1.0.0
- Fixed xulrunner 2 detection

* Thu Feb 25 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.9.2-1
- Updated to 0.9.9.2

* Sat Feb 06 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.9-1
- Updated to 0.9.9

* Mon Nov 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.8-2
- Require mozilla-filesystem instead of %%{_libdir}/mozilla/plugins

* Sat Sep 19 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.8-1
- Updated to 0.9.8

* Fri Jul 21 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.7-1
- Updated to 0.9.7

* Sun Jun 05 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.6-1
- Updated to 0.9.6

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.5-2
- rebuild for new F11 features

* Fri Mar 13 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.5-1
- Updated to 0.9.5

* Wed Feb  4 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.4-1
- Updated to 0.9.4, no more xpt files
- Dropped the upsteamed patch
- Updated the URL

* Thu Jan  8 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.3-2
- Added patch fixing rpmfusion bug #290 from SVN

* Sat Jan  3 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.3-1
- Updated to 0.9.3

* Mon Nov 24 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.2-2
- s/gnome-mplayer-core-functionality/gnome-mplayer-binary

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
