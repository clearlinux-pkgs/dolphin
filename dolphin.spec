#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dolphin
Version  : 22.04.0
Release  : 62
URL      : https://download.kde.org/stable/release-service/22.04.0/src/dolphin-22.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.0/src/dolphin-22.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.0/src/dolphin-22.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : kactivities-dev
BuildRequires : kfilemetadata-dev
BuildRequires : phonon-dev
BuildRequires : ruby

%description
User Documentation
==================
See https://userbase.kde.org/Special:myLanguage/Dolphin

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

%description services
services components for the dolphin package.


%prep
%setup -q -n dolphin-22.04.0
cd %{_builddir}/dolphin-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650667416
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650667416
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dolphin
cp %{_builddir}/dolphin-22.04.0/COPYING %{buildroot}/usr/share/package-licenses/dolphin/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/dolphin-22.04.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/dolphin/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/dolphin-22.04.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/dolphin/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/dolphin-22.04.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/dolphin/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/dolphin-22.04.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/dolphin-22.04.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/dolphin-22.04.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/dolphin-22.04.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/dolphin-22.04.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/dolphin-22.04.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/dolphin/fa05e58320cb7c64786b26396f4b992579a628bc
cp %{_builddir}/dolphin-22.04.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dolphin/49e61f7864169f2e356c11a17422d7d20d74b40f
cp %{_builddir}/dolphin-22.04.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/dolphin-22.04.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/dolphin-22.04.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/dolphin-22.04.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang dolphin
%find_lang dolphin_servicemenuinstaller

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dolphin
/usr/bin/servicemenuinstaller

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.dolphin.desktop
/usr/share/config.kcfg/dolphin_compactmodesettings.kcfg
/usr/share/config.kcfg/dolphin_contextmenusettings.kcfg
/usr/share/config.kcfg/dolphin_detailsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
/usr/share/config.kcfg/dolphin_generalsettings.kcfg
/usr/share/config.kcfg/dolphin_iconsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_versioncontrolsettings.kcfg
/usr/share/dbus-1/interfaces/org.freedesktop.FileManager1.xml
/usr/share/dbus-1/services/org.kde.dolphin.FileManager1.service
/usr/share/kglobalaccel/org.kde.dolphin.desktop
/usr/share/knsrcfiles/servicemenu.knsrc
/usr/share/kservices5/dolphinpart.desktop
/usr/share/kservices5/kcmdolphingeneral.desktop
/usr/share/kservices5/kcmdolphinnavigation.desktop
/usr/share/kservices5/kcmdolphinviewmodes.desktop
/usr/share/kservicetypes5/fileviewversioncontrolplugin.desktop
/usr/share/locale/fi/LC_SCRIPTS/dolphin/dolphin.js
/usr/share/metainfo/org.kde.dolphin.appdata.xml
/usr/share/qlogging-categories5/dolphin.categories

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
/usr/share/doc/HTML/sr/dolphin/index.cache.bz2
/usr/share/doc/HTML/sr/dolphin/index.docbook
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
/usr/lib64/libdolphinprivate.so.5
/usr/lib64/libdolphinprivate.so.5.0.0
/usr/lib64/libdolphinvcs.so.5
/usr/lib64/libdolphinvcs.so.5.0.0
/usr/lib64/qt5/plugins/dolphin/kcms/libkcm_dolphingeneral.so
/usr/lib64/qt5/plugins/dolphin/kcms/libkcm_dolphinnavigation.so
/usr/lib64/qt5/plugins/dolphin/kcms/libkcm_dolphinviewmodes.so
/usr/lib64/qt5/plugins/kf5/parts/dolphinpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dolphin/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/dolphin/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/dolphin/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/dolphin/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/dolphin/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/dolphin/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/dolphin/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/dolphin/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/dolphin/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/dolphin/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/dolphin/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/dolphin/fa05e58320cb7c64786b26396f4b992579a628bc

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-dolphin.service

%files locales -f dolphin.lang -f dolphin_servicemenuinstaller.lang
%defattr(-,root,root,-)

