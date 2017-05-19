#Fedora spec file based on the FreeBSD ports packaging
#lumina-desktop is lumina-core

%global srcname       lumina
%global srcurl        https://github.com/trueos/%{srcname}

%{!?rel: %global rel 1}

%if %{defined git_build}
%global commit0 %{git_build}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define release_version 1.2.2
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

Provides:       lumina-info = 1.2.1
Obsoletes:      lumina-info <= 1.2.1
Provides:       lumina-open = 1.2.1
Obsoletes:      lumina-open <= 1.2.1
Provides:       lumina-desktop-data = 1.2.1
Obsoletes:      lumina-desktop-data <= 1.2.1
Provides:       lumina-desktop-filesystem = 1.2.1
Obsoletes:      lumina-desktop-filesystem <= 1.2.1
Provides:       lumina-desktop-wallpapers = 1.2.1
Obsoletes:      lumina-desktop-wallpapers <= 1.2.1

%description
The Lumina Desktop Environment is a lightweight system interface that is 
designed for use on any Unix-like operating system. It takes a 
plugin-based approach, allowing the entire interface to be assembled or
arranged by each individual user as desired, with a system-wide default 
layout which can be customized by the system administrator. This allows 
every system (or user session) to be designed to maximize the individual 
user's productivity.


%package -n lumina-coreutils
Summary:        Core utilities for the Lumina Desktop.
Requires:       %{name} = %{version}-%{release}
Provides:       lumina-config = 1.2.1
Obsoletes:      lumina-config <= 1.2.1
Provides:       lumina-search = 1.2.1
Obsoletes:      lumina-search <= 1.2.1
Provides:       lumina-xconfig = 1.2.1
Obsoletes:      lumina-xconfig <= 1.2.1

%description -n lumina-coreutils
Core utilities for the Lumina Desktop.
This includes the following utilities:
* lumina-config (graphical interface for the desktop settings)
* lumina-xconfig (graphical interface for monitor settings)
* lumina-search (file/utility find and launch)


%package -n lumina-archiver
Summary:            Archiver for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-archiver
The archive manager from the Lumina desktop environment.
This is a graphical front-end to a couple base OS utilities:
* "tar" is used for all archive/file interactions
* "dd" is used for burning IMG files to removable devices.


%package -n lumina-calculator
Summary:            Calculator for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-calculator
Scientific calculator from the Lumina Desktop.


%package -n lumina-fileinfo
Summary:            Desktop file editor for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-fileinfo
The file information utility from the Lumina Desktop.
This can be used to view details about individual files in addition to
permitting the user to easily modify XDG *.desktop entries.


%package -n lumina-fm
Summary:            File manager for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-fm
The Insight file manager from the Lumina Desktop.
Capabilities:
* Standard File Manager Stuff (cut/copy/paste/move/rename files and directories)
* Bookmarks for commonly used locations on your system (great for saving 
    network shares accessed through /net)
* ZFS snapshot browsing - view/restore files from the past via a "time-slider"
* Multiple tab browser, with up to two side-by-side directories per tab
* Image slideshow - click through all the image files in a directory
* Multimedia Player - play multimedia files from a directory


%package -n lumina-mediaplayer
Summary:            Media Player for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-mediaplayer
Streaming media player from the Lumina Desktop.
Capabilities:
* Stream music from the Pandora online radio service (requires "pianobar")
* Find and play local audio/video file formats


%package -n lumina-screenshot
Summary:            Screenshot utility for Lumina Desktop
Group:              User Interface/Desktops

%description -n lumina-screenshot
Screenshot utility from the Lumina Desktop.
A simple screenshot utility that allows to snapshot the whole desktop or a
single window after a configurable delay.

Optionally the window border can be hidden when taking a screenshot of a
single window.


%package -n lumina-textedit
Summary:          Text editor for Lumina Desktop
Group:            User Interface/Desktops

%description -n lumina-textedit
Plaintext editor from the Lumina Desktop.
Capabilities:
* Syntax highlighting for various file formats
* Multiple file support via tabs.
* Find/replace support
* Line numbers and line wrap support


%package -n lumina-xdg-entry
Summary:            XDG desktop entry creator from the Lumina Desktop.
Group:              User Interface/Desktops

%description -n lumina-xdg-entry
XDG desktop entry creator from the Lumina Desktop.


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

ls %{buildroot}%{_sysconfdir}

# Create proper config file
cp %{buildroot}%{_datadir}/lumina-desktop/luminaDesktop.conf %{buildroot}%{_sysconfdir}/luminaDesktop.conf


%files
%license LICENSE
%{_bindir}/lumina-desktop
%{_bindir}/lumina-info
%{_bindir}/lumina-open
%{_bindir}/start-lumina-desktop
%{_sysconfdir}/luminaDesktop.conf.dist
%config(noreplace) %{_sysconfdir}/luminaDesktop.conf
%{_mandir}/man1/lumina-open.1.gz
%{_mandir}/man8/lumina-desktop.8.gz
%{_mandir}/man8/start-lumina-desktop.8.gz

%{_datadir}/applications/lumina-info.desktop
%{_datadir}/applications/lumina-support.desktop
%{_datadir}/icons/material-design-dark
%{_datadir}/icons/material-design-light

%{_datadir}/lumina-desktop/Login.ogg
%{_datadir}/lumina-desktop/Logout.ogg
%{_datadir}/lumina-desktop/colors/Black.qss.colors
%{_datadir}/lumina-desktop/colors/Blue-Light.qss.colors
%{_datadir}/lumina-desktop/colors/Grey-Dark.qss.colors
%{_datadir}/lumina-desktop/colors/Lumina-Glass.qss.colors
%{_datadir}/lumina-desktop/colors/Lumina-Gold.qss.colors
%{_datadir}/lumina-desktop/colors/Lumina-Green.qss.colors
%{_datadir}/lumina-desktop/colors/Lumina-Purple.qss.colors
%{_datadir}/lumina-desktop/colors/Lumina-Red.qss.colors
%{_datadir}/lumina-desktop/colors/PCBSD10-Default.qss.colors
%{_datadir}/lumina-desktop/colors/Solarized-Dark.qss.colors
%{_datadir}/lumina-desktop/colors/Solarized-Light.qss.colors
%{_datadir}/lumina-desktop/compton.conf
%{_datadir}/lumina-desktop/desktop-background.jpg
%{_datadir}/lumina-desktop/fluxbox-init-rc
%{_datadir}/lumina-desktop/fluxbox-keys
%{_datadir}/lumina-desktop/globs2
%{_datadir}/lumina-desktop/i18n/lumina-desktop_*.qm
%{_datadir}/lumina-desktop/i18n/lumina-info_*.qm
%{_datadir}/lumina-desktop/i18n/lumina-open_*.qm
%{_datadir}/lumina-desktop/low-battery.ogg
%{_datadir}/lumina-desktop/luminaDesktop.conf
%{_datadir}/lumina-desktop/menu-scripts/ls.json.sh
%{_datadir}/lumina-desktop/themes/DarkGlass.qss.template
%{_datadir}/lumina-desktop/themes/Glass.qss.template
%{_datadir}/lumina-desktop/themes/Lumina-default.qss.template
%{_datadir}/lumina-desktop/themes/None.qss.template
%{_datadir}/pixmaps/Lumina-DE.png
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_blue-grey-zoom.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_blue-grey.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_gold.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_green.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_grey-blue-zoom.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_grey-blue.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_purple.jpg
%{_datadir}/wallpapers/Lumina-DE/Lumina_Wispy_red.jpg
%{_datadir}/xsessions/Lumina-DE.desktop

%files -n lumina-coreutils
%{_bindir}/lumina-config
%{_bindir}/lumina-search
%{_bindir}/lumina-xconfig
%{_datadir}/applications/lumina-config.desktop
%{_datadir}/applications/lumina-search.desktop
%{_datadir}/applications/lumina-xconfig.desktop
%{_datadir}/lumina-desktop/i18n/lumina-config_*.qm
%{_datadir}/lumina-desktop/i18n/lumina-search_*.qm
%{_datadir}/lumina-desktop/i18n/lumina-xconfig_*.qm

%files -n lumina-archiver
%license LICENSE
%{_bindir}/lumina-archiver
%{_datadir}/lumina-desktop/i18n/l-archiver_*.qm
%{_datadir}/applications/lumina-archiver.desktop

%files -n lumina-calculator
%license LICENSE
%{_bindir}/lumina-calculator
%{_datadir}/lumina-desktop/i18n/l-calc_*.qm
%{_datadir}/applications/lumina-calculator.desktop

%files -n lumina-fileinfo
%license LICENSE
%{_bindir}/lumina-fileinfo
%{_datadir}/lumina-desktop/i18n/l-fileinfo*.qm
%{_datadir}/applications/lumina-fileinfo.desktop

%files -n lumina-fm
%license LICENSE
%{_bindir}/lumina-fm
%{_datadir}/lumina-desktop/i18n/lumina-fm*.qm
%{_datadir}/pixmaps/Insight-FileManager.png
%{_datadir}/applications/lumina-fm.desktop

%files -n lumina-mediaplayer
%license LICENSE
%{_bindir}/lumina-mediaplayer
%{_datadir}/lumina-desktop/i18n/l-mediap_*.qm
%{_datadir}/applications/lumina-mediaplayer.desktop

%files -n lumina-screenshot
%license LICENSE
%{_bindir}/lumina-screenshot
%{_datadir}/lumina-desktop/i18n/l-screenshot*.qm
%{_datadir}/applications/lumina-screenshot.desktop

%files -n lumina-textedit
%license LICENSE
%{_bindir}/lumina-textedit
%{_bindir}/lte
%{_datadir}/lumina-desktop/i18n/l-te*.qm
%{_datadir}/applications/lumina-textedit.desktop

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
