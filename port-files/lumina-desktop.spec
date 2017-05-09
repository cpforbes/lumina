%global srcname       lumina
%global srcurl        https://github.com/trueos/%{srcname}

%{!?rel: %global rel 1}

%if %{defined git_build}
%global commit0 %{git_build}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define release_version 1.2.1
%global relver %{rel}.%{shortcommit0}
%else
%define release_version 1.2.0
%global relver %{rel}
%endif

%define rpm_version %(echo %{release_version} | tr - .)

Summary:            A lightweight, portable desktop environment
Name:               lumina-desktop
Version:            %{rpm_version}
Release:            %{relver}%{?dist}
License:            BSD
Group:              User Interface/Desktops
URL:                http://lumina-desktop.org

# Formatted so spectool can fetch the source.
%if %{defined git_build}
Source0:            %{srcurl}/archive/%{commit0}.tar.gz#/lumina-%{shortcommit0}.tar.gz
%else
Source0:            %{srcurl}/archive/v%{release_version}.tar.gz#/lumina-%{release_version}.tar.gz
%endif

# Exclude IBM ESA/390 and ESA System/z architectures
ExcludeArch:        s390 s390x

# Compiler requirements
BuildRequires:      gcc, gcc-c++

# Qt requirements
BuildRequires:      qt5-qttools
BuildRequires:      qt5-qttools-devel
BuildRequires:      qt5-linguist
BuildRequires:      qt5-qtbase-devel
BuildRequires:      qt5-qtmultimedia-devel
BuildRequires:      qt5-qtdeclarative-devel
BuildRequires:      qt5-qtsvg-devel
BuildRequires:      qt5-qtx11extras-devel

# X component requirements
BuildRequires:      xcb-util-image
BuildRequires:      xcb-util-image-devel
BuildRequires:      xcb-util-wm-devel
BuildRequires:      libxcb-devel
BuildRequires:      xcb-util-devel
BuildRequires:      libXcomposite-devel
BuildRequires:      libXdamage-devel
BuildRequires:      libXrender-devel

# Runtime requirements
Requires:           alsa-utils
Requires:           acpi
Requires:           numlockx
Requires:           pavucontrol
Requires:           sysstat
Requires:           xscreensaver
Requires:           xbacklight
Requires:           xterm
Requires:           qt5-style-oxygen
Requires:           plasma-oxygen 
Requires:           fluxbox

# Desktop requirements
Requires:             %{name}-filesystem = %{version}-%{release}
Requires:             %{name}-data = %{version}-%{release}

# Fix for rhbz#1389486, unable to start applications in Lumina
Requires:             %{srcname}-open%{?_isa} = %{version}-%{release}

%if 0%{?fedora}
Suggests:           lumina-open = %{version}-%{release}
Suggests:           lumina-config = %{version}-%{release}
Suggests:           lumina-fm = %{version}-%{release}
Suggests:           lumina-screenshot = %{version}-%{release}
Suggests:           lumina-search = %{version}-%{release}
Suggests:           lumina-info = %{version}-%{release}
Suggests:           lumina-xconfig = %{version}-%{release}
Suggests:           lumina-fileinfo = %{version}-%{release}
Suggests:           lumina-textedit = %{version}-%{release}
Suggests:           lumina-calculator = %{version}-%{release}
Suggests:           lumina-archiver = %{version}-%{release}
%endif

%description
The Lumina Desktop Environment is a lightweight system interface
that is designed for use on any Unix-like operating system.

%package data
Summary:              Data for Lumina Desktop
BuildArch:            noarch
Requires:             %{name} = %{version}-%{release}

%description data
This package provides the data files for the Lumina Desktop
Environment: Colors, desktop background, theme templates.

%package filesystem
Summary:              Common folders for Lumina Desktop
BuildArch:            noarch
Obsoletes:            %{name}-libs < 1.2.0

%description filesystem
This package provides the common folders for the Lumina Desktop Environment.

%package wallpapers
Summary:              Wallpapers for Lumina Desktop
BuildArch:            noarch
Requires:             kde-filesystem

%description wallpapers
Optional wallpapers recommended for Lumina Desktop.

%package -n lumina-open
Summary:            xdg-open style utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-open
This package provides lumina-open, which handles opening of
files and URLs according to the system-wide mimetype association.
It also provides an optional selector if more than one application
is assigned with the given url or file type.

%package -n lumina-config
Summary:            Configuration utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-config
This package provides lumina-config, which allows changing
various aspects of lumina and fluxbox, like the wallpaper being
used, theme, icons, panel (and plugins), startup and default
applications, desktop menu and more.

%package -n lumina-fm
Summary:            File manager for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-fm
This package provides lumina-fm, which is a simple file manager
with support for multiple view modes, tabbed browsing,
including an integrated slideshow-based picture viewer.


%package -n lumina-screenshot
Summary:            Screenshot utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-screenshot
This package provides lumina-screenshot, which is a simple
screenshot utility that allows to snapshot the whole desktop
or a single window after a configurable delay.

Optionally the window border can be hidden when taking a
screenshot of a single window.


%package -n lumina-search
Summary:            Search utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-search
This package provides lumina-search, which is a simple
search utility that allows to search for applications or
files and directories in the home directory and launch
or open them.


%package -n lumina-info
Summary:            Basic information utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-info
This package provides lumina-info, which is a simple
utility that displays various information about the Lumina
installation, like paths, contributors, license or version.


%package -n lumina-xconfig
Summary:            X server display configuration tool for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-xconfig
This package provides lumina-xconfig, which is a simple
multi-head aware display configuration tool for configuring
the X server.


%package -n lumina-fileinfo
Summary:            Desktop file editor for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-fileinfo
This package provides lumina-fileinfo, which is an
advanced desktop file (menu) editor.

%package -n lumina-textedit
Summary:            Text editor for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-textedit
This package provides lumina-textedit.

%package -n lumina-calculator
Summary:            Calculator for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-calculator
This package provides lumina-calculator

%package -n lumina-archiver
Summary:            Archiver for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-archiver
This package provides lumina-archiver

%package -n lumina-mediaplayer
Summary:            Media Player for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-mediaplayer
This package provides lumina-mediaplayer

%package -n lumina-xdg-entry
Summary:            xdg entry editor for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-xdg-entry
This package provides lumina-xdg-entry

%prep
%if %{defined git_build}
%setup -q -n lumina-%{commit0}
%else
%setup -q -n lumina-%{release_version}
%endif

%build
%if %{defined git_build}
git_version='DEFINES+=GIT_VERSION="\\\"%{shortcommit0}\\\""'
%else
git_version=''
%endif
echo %{?git_version}

%qmake_qt5 $git_version \
 QMAKE_CFLAGS_ISYSTEM= \
 CONFIG+="configure" \
 CONFIG+="WITH_I18N" \
 PREFIX="%{_prefix}" \
 LIBPREFIX="%{_libdir}" \
 QT5LIBDIR="%{_qt5_prefix}" \
 L_LIBDIR=%{_libdir} \
 L_MANDIR=%{_mandir}

make %{?_smp_mflags}


%install
# Install the desktop
make INSTALL_ROOT=%{buildroot} install

# Fix paths in desktop files
find %{buildroot}/ -name *.desktop -exec sed -i "s:/usr/local/:/usr/:g" {} \;

# Create proper config file
cp %{buildroot}%{_datadir}/lumina-desktop/luminaDesktop.conf %{buildroot}%{_sysconfdir}/luminaDesktop.conf
sed -i "s:/usr/local/share/applications/firefox.desktop:firefox:g" %{buildroot}%{_sysconfdir}/luminaDesktop.conf
sed -i "s:/usr/local/share/applications/thunderbird.desktop:thunderbird:g" %{buildroot}%{_sysconfdir}/luminaDesktop.conf


%files
%license LICENSE
%{_bindir}/lumina-desktop
%{_bindir}/start-lumina-desktop
%config(noreplace) %{_sysconfdir}/luminaDesktop.conf
%{_mandir}/man8/lumina-desktop.8.gz
%{_mandir}/man8/start-lumina-desktop.8.gz
%{_datadir}/%{name}/i18n/lumina-desktop*.qm
%{_sysconfdir}/luminaDesktop.conf.dist
%{_datadir}/pixmaps/Lumina-DE.png
%{_datadir}/xsessions/Lumina-DE.desktop
%{_datadir}/icons/material-design-dark
%{_datadir}/icons/material-design-light

%files data
%{_datadir}/%{name}/desktop-background.jpg
%{_datadir}/%{name}/luminaDesktop.conf
%{_datadir}/%{name}/compton.conf
%{_datadir}/%{name}/fluxbox-init-rc
%{_datadir}/%{name}/fluxbox-keys
%{_datadir}/%{name}/Login.ogg
%{_datadir}/%{name}/Logout.ogg
%{_datadir}/%{name}/low-battery.ogg
%{_datadir}/%{name}/colors/Lumina-Red.qss.colors
%{_datadir}/%{name}/colors/Lumina-Green.qss.colors
%{_datadir}/%{name}/colors/Lumina-Purple.qss.colors
%{_datadir}/%{name}/colors/Lumina-Gold.qss.colors
%{_datadir}/%{name}/colors/Lumina-Glass.qss.colors
%{_datadir}/%{name}/colors/PCBSD10-Default.qss.colors
%{_datadir}/%{name}/themes/Lumina-default.qss.template
%{_datadir}/%{name}/themes/None.qss.template
%{_datadir}/%{name}/themes/Glass.qss.template
%{_datadir}/%{name}/themes/DarkGlass.qss.template
%{_datadir}/%{name}/colors/Blue-Light.qss.colors
%{_datadir}/%{name}/colors/Grey-Dark.qss.colors
%{_datadir}/%{name}/colors/Solarized-Dark.qss.colors
%{_datadir}/%{name}/colors/Solarized-Light.qss.colors
%{_datadir}/%{name}/colors/Black.qss.colors
%{_datadir}/%{name}/menu-scripts/ls.json.sh
%{_datadir}/%{name}/globs2
%exclude %{_datadir}/%{name}/i18n

%files filesystem
%license LICENSE
# each binary expects its locale files in the common folder
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n

%files wallpapers
%license LICENSE
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_blue-grey-zoom.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_blue-grey.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_gold.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_green.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_grey-blue-zoom.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_grey-blue.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_purple.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_red.jpg

%files -n lumina-open
%license LICENSE
%{_bindir}/lumina-open
%{_datadir}/lumina-desktop/i18n/lumina-open*.qm
%{_mandir}/man1/lumina-open.1.gz

%files -n lumina-config
%license LICENSE
%{_bindir}/lumina-config
%{_datadir}/lumina-desktop/i18n/lumina-config*.qm
%{_datadir}/applications/lumina-config.desktop

%files -n lumina-fm
%license LICENSE
%{_bindir}/lumina-fm
%{_datadir}/lumina-desktop/i18n/lumina-fm*.qm
%{_datadir}/pixmaps/Insight-FileManager.png
%{_datadir}/applications/lumina-fm.desktop

%files -n lumina-screenshot
%license LICENSE
%{_bindir}/lumina-screenshot
%{_datadir}/lumina-desktop/i18n/l-screenshot*.qm
%{_datadir}/applications/lumina-screenshot.desktop

%files -n lumina-search
%license LICENSE
%{_bindir}/lumina-search
%{_datadir}/lumina-desktop/i18n/lumina-search*.qm
%{_datadir}/applications/lumina-search.desktop

%files -n lumina-info
%license LICENSE
%{_bindir}/lumina-info
%{_datadir}/lumina-desktop/i18n/lumina-info*.qm
%{_datadir}/applications/lumina-info.desktop
%{_datadir}/applications/lumina-support.desktop

%files -n lumina-xconfig
%license LICENSE
%{_bindir}/lumina-xconfig
%{_datadir}/lumina-desktop/i18n/lumina-xconfig*.qm
%{_datadir}/applications/lumina-xconfig.desktop

%files -n lumina-fileinfo
%license LICENSE
%{_bindir}/lumina-fileinfo
%{_datadir}/lumina-desktop/i18n/l-fileinfo*.qm
%{_datadir}/applications/lumina-fileinfo.desktop

%files -n lumina-textedit
%license LICENSE
%{_bindir}/lumina-textedit
%{_bindir}/lte
%{_datadir}/lumina-desktop/i18n/l-te*.qm
%{_datadir}/applications/lumina-textedit.desktop

%files -n lumina-calculator
%license LICENSE
%{_bindir}/lumina-calculator
%{_datadir}/lumina-desktop/i18n/l-calc_*.qm
%{_datadir}/applications/lumina-calculator.desktop

%files -n lumina-archiver
%license LICENSE
%{_bindir}/lumina-archiver
%{_datadir}/lumina-desktop/i18n/l-archiver_*.qm
%{_datadir}/applications/lumina-archiver.desktop

%files -n lumina-mediaplayer
%license LICENSE
%{_bindir}/lumina-mediaplayer
%{_datadir}/lumina-desktop/i18n/l-mediap_*.qm
%{_datadir}/applications/lumina-mediaplayer.desktop

%files -n lumina-xdg-entry
%license LICENSE
%{_bindir}/lumina-xdg-entry
%{_datadir}/applications/lumina-xdg-entry.desktop

%changelog
* Wed Jan  4 2017 Craig Forbes <cforbes@trustwave.com> - 1.2.0-1
- Updated to 1.2.0
- Removed devel and libs sub-packages
- Added lumina-archiver
- Fix qmake flags to work with gcc 6 (Fedora 25)

* Tue Nov 22 2016 Craig Forbes <cforbes@gmail.com> - 1.1.0.p1-1
- Updated to 1.1.0-p1

* Wed Dec 23 2015 Neal Gompa <ngompa13@gmail.com>
- Update to 0.8.8
- Bring it closer to Fedora guidelines
- Break out Lumina Desktop package into subpackages
- Unify 32-bit and 64-bit packaging

* Tue Oct 27 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Update to 0.8.7

* Thu Aug 20 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Updated for 32-bit

* Thu Jul 30 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Initial build
