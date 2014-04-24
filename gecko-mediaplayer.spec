Name:           gecko-mediaplayer
Version:        1.0.9
Release:        1%{?dist}
Summary:        Gnome MPlayer browser plugin

License:        GPLv2+
URL:            http://kdekorte.googlepages.com/gecko-mediaplayer
Source0:        http://gecko-mediaplayer.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  dbus-glib-devel
BuildRequires:  gettext
BuildRequires:  gmtk-devel == %{version}
BuildRequires:  libcurl-devel
BuildRequires:  libX11-devel
BuildRequires:  gecko-devel

Requires:       mozilla-filesystem
Requires:       gnome-mplayer-binary%{?_isa} >= %{version}

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
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

#remove intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gecko-mediaplayer


%files -f %{name}.lang
%doc COPYING ChangeLog
%{_libdir}/mozilla/plugins/gecko-mediaplayer-dvx.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-qt.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-rm.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer-wmp.so
%{_libdir}/mozilla/plugins/gecko-mediaplayer.so


%changelog
* Thu Apr 24 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.9-1
- Updated to 1.0.9

* Sun Mar 03 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.8-1
- Updated to 1.0.8

* Tue Oct 30 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.7-1
- Updated to 1.0.7

* Fri Apr 06 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.6-1
- Updated to 1.0.6

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.5-2
- Rebuilt for c++ ABI breakage

* Thu Dec 29 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.5-1
- Updated to 1.0.5
- Dropped the included apple.com fix
- Refactored to accomodate the gmtk split
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Removed GConf logic since F-14 is EOL
- Added %%{?_isa} to explicit dependencies

* Sat Jul 16 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.4-4
- Added an easy way to pick between GSettings and GConf2
- Rearranged the conditionals to avoid leaving empty %%pre et al.

* Fri Jul 08 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.4-3
- Updated the apple.com fix

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

* Tue Jul 21 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.7-1
- Updated to 0.9.7

* Fri Jun 05 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.6-1
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
