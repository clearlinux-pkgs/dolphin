#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dolphin
Version  : 25.04.2
Release  : 106
URL      : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: dolphin-bin = %{version}-%{release}
Requires: dolphin-data = %{version}-%{release}
Requires: dolphin-lib = %{version}-%{release}
Requires: dolphin-license = %{version}-%{release}
Requires: dolphin-locales = %{version}-%{release}
Requires: dolphin-services = %{version}-%{release}
BuildRequires : baloo-dev
BuildRequires : baloo-widgets-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kfilemetadata-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : phonon-dev
BuildRequires : qt6base-dev
BuildRequires : ruby
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Dolphin
Dolphin is KDE's file manager that lets you navigate and browse the contents of your hard drives, USB sticks, SD cards, and more. Creating, moving, or deleting files and folders is simple and fast. See more information [on Dolphin's homepage](https://apps.kde.org/dolphin/).

%package bin
Summary: bin components for the dolphin package.
Group: Binaries
Requires: dolphin-data = %{version}-%{release}
Requires: dolphin-license = %{version}-%{release}
Requires: dolphin-services = %{version}-%{release}

%description bin
bin components for the dolphin package.


%package data
Summary: data components for the dolphin package.
Group: Data

%description data
data components for the dolphin package.


%package dev
Summary: dev components for the dolphin package.
Group: Development
Requires: dolphin-lib = %{version}-%{release}
Requires: dolphin-bin = %{version}-%{release}
Requires: dolphin-data = %{version}-%{release}
Provides: dolphin-devel = %{version}-%{release}
Requires: dolphin = %{version}-%{release}

%description dev
dev components for the dolphin package.


%package doc
Summary: doc components for the dolphin package.
Group: Documentation

%description doc
doc components for the dolphin package.


%package lib
Summary: lib components for the dolphin package.
Group: Libraries
Requires: dolphin-data = %{version}-%{release}
Requires: dolphin-license = %{version}-%{release}

%description lib
lib components for the dolphin package.


%package license
Summary: license components for the dolphin package.
Group: Default

%description license
license components for the dolphin package.


%package locales
Summary: locales components for the dolphin package.
Group: Default

%description locales
locales components for the dolphin package.


%package services
Summary: services components for the dolphin package.
Group: Systemd services
Requires: systemd

%description services
services components for the dolphin package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n dolphin-25.04.2
cd %{_builddir}/dolphin-25.04.2
pushd ..
cp -a dolphin-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749503026
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749503026
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dolphin
cp %{_builddir}/dolphin-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dolphin/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/dolphin-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/dolphin/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/dolphin/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/dolphin-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/dolphin/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/dolphin-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/dolphin/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/dolphin-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/dolphin/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/49e61f7864169f2e356c11a17422d7d20d74b40f || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/dolphin-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/dolphin/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang dolphin
%find_lang dolphin_servicemenuinstaller
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/kconf_update_bin/dolphin_25.04_update_statusandlocationbarssettings
/usr/lib64/kconf_update_bin/dolphin_25.04_update_statusandlocationbarssettings

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dolphin
/V3/usr/bin/servicemenuinstaller
/usr/bin/dolphin
/usr/bin/servicemenuinstaller

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.dolphin.desktop
/usr/share/config.kcfg/dolphin_compactmodesettings.kcfg
/usr/share/config.kcfg/dolphin_contentdisplaysettings.kcfg
/usr/share/config.kcfg/dolphin_contextmenusettings.kcfg
/usr/share/config.kcfg/dolphin_detailsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
/usr/share/config.kcfg/dolphin_generalsettings.kcfg
/usr/share/config.kcfg/dolphin_iconsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_versioncontrolsettings.kcfg
/usr/share/dbus-1/interfaces/org.freedesktop.FileManager1.xml
/usr/share/dbus-1/services/org.kde.dolphin.FileManager1.service
/usr/share/dolphin/dolphinpartactions.desktop
/usr/share/icons/hicolor/scalable/apps/org.kde.dolphin.svg
/usr/share/kconf_update/dolphin_detailsmodesettings.upd
/usr/share/kconf_update/dolphin_directorysizemode.py
/usr/share/kconf_update/dolphin_directorysizemode.upd
/usr/share/kconf_update/dolphin_statusandlocationbarssettings.upd
/usr/share/kglobalaccel/org.kde.dolphin.desktop
/usr/share/knsrcfiles/servicemenu.knsrc
/usr/share/metainfo/org.kde.dolphin.appdata.xml
/usr/share/qlogging-categories6/dolphin.categories
/usr/share/zsh/site-functions/_dolphin

%files dev
%defattr(-,root,root,-)
/usr/include/Dolphin/KVersionControlPlugin
/usr/include/Dolphin/dolphinvcs_version.h
/usr/include/Dolphin/kversioncontrolplugin.h
/usr/include/dolphin_export.h
/usr/include/dolphinvcs_export.h
/usr/lib64/cmake/DolphinVcs/DolphinVcsConfig.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsConfigVersion.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsTargets.cmake
/usr/lib64/libdolphinvcs.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/dolphin/default-ui.png
/usr/share/doc/HTML/ca/dolphin/grouping-view.png
/usr/share/doc/HTML/ca/dolphin/index.cache.bz2
/usr/share/doc/HTML/ca/dolphin/index.docbook
/usr/share/doc/HTML/ca/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/ca/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/ca/dolphin/locationbar-editable.png
/usr/share/doc/HTML/ca/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/ca/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/ca/dolphin/nepomuk-search-more-options.png
/usr/share/doc/HTML/ca/dolphin/nepomuk-search.png
/usr/share/doc/HTML/ca/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/ca/dolphin/preferences-navigation.png
/usr/share/doc/HTML/ca/dolphin/preferences-services.png
/usr/share/doc/HTML/ca/dolphin/preferences-trash.png
/usr/share/doc/HTML/ca/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/ca/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/ca/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/ca/dolphin/toolbar.png
/usr/share/doc/HTML/de/dolphin/default-ui.png
/usr/share/doc/HTML/de/dolphin/index.cache.bz2
/usr/share/doc/HTML/de/dolphin/index.docbook
/usr/share/doc/HTML/de/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/de/dolphin/locationbar-editable.png
/usr/share/doc/HTML/de/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/de/dolphin/preferences-navigation.png
/usr/share/doc/HTML/de/dolphin/preferences-startup.png
/usr/share/doc/HTML/de/dolphin/preferences-trash.png
/usr/share/doc/HTML/de/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/de/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/de/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/de/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/en/dolphin/baloo-search-more-options.png
/usr/share/doc/HTML/en/dolphin/baloo-search.png
/usr/share/doc/HTML/en/dolphin/default-ui.png
/usr/share/doc/HTML/en/dolphin/grouping-view.png
/usr/share/doc/HTML/en/dolphin/index.cache.bz2
/usr/share/doc/HTML/en/dolphin/index.docbook
/usr/share/doc/HTML/en/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/en/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/en/dolphin/locationbar-editable.png
/usr/share/doc/HTML/en/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/en/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/en/dolphin/preferences-context-menu.png
/usr/share/doc/HTML/en/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/en/dolphin/preferences-navigation.png
/usr/share/doc/HTML/en/dolphin/preferences-startup.png
/usr/share/doc/HTML/en/dolphin/preferences-trash.png
/usr/share/doc/HTML/en/dolphin/preferences-user-feedback.png
/usr/share/doc/HTML/en/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/en/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/en/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/en/dolphin/toolbar.png
/usr/share/doc/HTML/en/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/es/dolphin/index.cache.bz2
/usr/share/doc/HTML/es/dolphin/index.docbook
/usr/share/doc/HTML/id/dolphin/index.cache.bz2
/usr/share/doc/HTML/id/dolphin/index.docbook
/usr/share/doc/HTML/it/dolphin/default-ui.png
/usr/share/doc/HTML/it/dolphin/grouping-view.png
/usr/share/doc/HTML/it/dolphin/index.cache.bz2
/usr/share/doc/HTML/it/dolphin/index.docbook
/usr/share/doc/HTML/it/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/it/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/it/dolphin/locationbar-editable.png
/usr/share/doc/HTML/it/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/it/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/it/dolphin/nepomuk-search-more-options.png
/usr/share/doc/HTML/it/dolphin/nepomuk-search.png
/usr/share/doc/HTML/it/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/it/dolphin/preferences-navigation.png
/usr/share/doc/HTML/it/dolphin/preferences-services.png
/usr/share/doc/HTML/it/dolphin/preferences-startup.png
/usr/share/doc/HTML/it/dolphin/preferences-trash.png
/usr/share/doc/HTML/it/dolphin/preferences-user-feedback.png
/usr/share/doc/HTML/it/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/it/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/it/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/it/dolphin/toolbar.png
/usr/share/doc/HTML/it/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/nl/dolphin/default-ui.png
/usr/share/doc/HTML/nl/dolphin/index.cache.bz2
/usr/share/doc/HTML/nl/dolphin/index.docbook
/usr/share/doc/HTML/nl/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/nl/dolphin/locationbar-editable.png
/usr/share/doc/HTML/nl/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/nl/dolphin/preferences-navigation.png
/usr/share/doc/HTML/nl/dolphin/preferences-startup.png
/usr/share/doc/HTML/nl/dolphin/preferences-trash.png
/usr/share/doc/HTML/nl/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/nl/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/nl/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/nl/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/pt/dolphin/index.cache.bz2
/usr/share/doc/HTML/pt/dolphin/index.docbook
/usr/share/doc/HTML/pt_BR/dolphin/default-ui.png
/usr/share/doc/HTML/pt_BR/dolphin/grouping-view.png
/usr/share/doc/HTML/pt_BR/dolphin/index.cache.bz2
/usr/share/doc/HTML/pt_BR/dolphin/index.docbook
/usr/share/doc/HTML/pt_BR/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/pt_BR/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/pt_BR/dolphin/locationbar-editable.png
/usr/share/doc/HTML/pt_BR/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/pt_BR/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/pt_BR/dolphin/nepomuk-search-more-options.png
/usr/share/doc/HTML/pt_BR/dolphin/nepomuk-search.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-navigation.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-services.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-startup.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-trash.png
/usr/share/doc/HTML/pt_BR/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/pt_BR/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/pt_BR/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/pt_BR/dolphin/toolbar.png
/usr/share/doc/HTML/pt_BR/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/ru/dolphin/index.cache.bz2
/usr/share/doc/HTML/ru/dolphin/index.docbook
/usr/share/doc/HTML/sl/dolphin/index.cache.bz2
/usr/share/doc/HTML/sl/dolphin/index.docbook
/usr/share/doc/HTML/sr/dolphin/index.cache.bz2
/usr/share/doc/HTML/sr/dolphin/index.docbook
/usr/share/doc/HTML/sr@latin/dolphin/index.cache.bz2
/usr/share/doc/HTML/sr@latin/dolphin/index.docbook
/usr/share/doc/HTML/sv/dolphin/bookmarkbutton.png
/usr/share/doc/HTML/sv/dolphin/breadcrumb.png
/usr/share/doc/HTML/sv/dolphin/configurationwindow.png
/usr/share/doc/HTML/sv/dolphin/configurationwindow2.png
/usr/share/doc/HTML/sv/dolphin/directorypath.png
/usr/share/doc/HTML/sv/dolphin/dolphin.png
/usr/share/doc/HTML/sv/dolphin/hiddenfolder.png
/usr/share/doc/HTML/sv/dolphin/index.cache.bz2
/usr/share/doc/HTML/sv/dolphin/index.docbook
/usr/share/doc/HTML/sv/dolphin/split.png
/usr/share/doc/HTML/sv/dolphin/toolbarbuttons.png
/usr/share/doc/HTML/sv/dolphin/workspacebuttons.png
/usr/share/doc/HTML/tr/dolphin/baloo-search-more-options.png
/usr/share/doc/HTML/tr/dolphin/baloo-search.png
/usr/share/doc/HTML/tr/dolphin/default-ui.png
/usr/share/doc/HTML/tr/dolphin/grouping-view.png
/usr/share/doc/HTML/tr/dolphin/index.cache.bz2
/usr/share/doc/HTML/tr/dolphin/index.docbook
/usr/share/doc/HTML/tr/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/tr/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/tr/dolphin/locationbar-editable.png
/usr/share/doc/HTML/tr/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/tr/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/tr/dolphin/preferences-context-menu.png
/usr/share/doc/HTML/tr/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/tr/dolphin/preferences-navigation.png
/usr/share/doc/HTML/tr/dolphin/preferences-startup.png
/usr/share/doc/HTML/tr/dolphin/preferences-trash.png
/usr/share/doc/HTML/tr/dolphin/preferences-user-feedback.png
/usr/share/doc/HTML/tr/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/tr/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/tr/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/tr/dolphin/toolbar.png
/usr/share/doc/HTML/tr/dolphin/viewproperties-dialog.png
/usr/share/doc/HTML/uk/dolphin/default-ui.png
/usr/share/doc/HTML/uk/dolphin/grouping-view.png
/usr/share/doc/HTML/uk/dolphin/index.cache.bz2
/usr/share/doc/HTML/uk/dolphin/index.docbook
/usr/share/doc/HTML/uk/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/uk/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/uk/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/uk/dolphin/nepomuk-search-more-options.png
/usr/share/doc/HTML/uk/dolphin/nepomuk-search.png
/usr/share/doc/HTML/uk/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/uk/dolphin/preferences-navigation.png
/usr/share/doc/HTML/uk/dolphin/preferences-services.png
/usr/share/doc/HTML/uk/dolphin/preferences-startup.png
/usr/share/doc/HTML/uk/dolphin/preferences-trash.png
/usr/share/doc/HTML/uk/dolphin/preferences-user-feedback.png
/usr/share/doc/HTML/uk/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/uk/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/uk/dolphin/toolbar.png
/usr/share/doc/HTML/uk/dolphin/viewproperties-dialog.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdolphinprivate.so.25.04.2
/V3/usr/lib64/libdolphinvcs.so.25.04.2
/V3/usr/lib64/qt6/plugins/dolphin/kcms/kcm_dolphingeneral.so
/V3/usr/lib64/qt6/plugins/dolphin/kcms/kcm_dolphinviewmodes.so
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/movetonewfolderitemaction.so
/V3/usr/lib64/qt6/plugins/kf6/parts/dolphinpart.so
/usr/lib64/libdolphinprivate.so.25.04.2
/usr/lib64/libdolphinprivate.so.6
/usr/lib64/libdolphinvcs.so.25.04.2
/usr/lib64/libdolphinvcs.so.6
/usr/lib64/qt6/plugins/dolphin/kcms/kcm_dolphingeneral.so
/usr/lib64/qt6/plugins/dolphin/kcms/kcm_dolphinviewmodes.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/movetonewfolderitemaction.so
/usr/lib64/qt6/plugins/kf6/parts/dolphinpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/dolphin/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/dolphin/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/dolphin/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/dolphin/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/dolphin/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/dolphin/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/dolphin/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/dolphin/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/dolphin/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/dolphin/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/dolphin/fa05e58320cb7c64786b26396f4b992579a628bc

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-dolphin.service

%files locales -f dolphin.lang -f dolphin_servicemenuinstaller.lang
%defattr(-,root,root,-)

