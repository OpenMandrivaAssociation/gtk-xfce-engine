%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define gtk3binaryver 3.0.0
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Additional themes for Xfce desktop environment
Name:		gtk-xfce-engine
Version:	3.0.1
Release:	1
License:	GPLv3
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/gtk-xfce-engine/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel > 2.6.0
BuildRequires:	gtk+3-devel > 3.2.0
Conflicts:	gtk-engines2 < 2.18.1-2

%description
A default Xfce GTK+ themes.

%prep
%setup -q

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/libxfce.so
%{_libdir}/gtk-3.0/%{gtk3binaryver}/theming-engines/libxfce.so
%{_datadir}/themes/Xfce*


%changelog
* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.99.3-1
+ Revision: 791064
- update to new version 2.99.3

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.99.2-1
+ Revision: 789932
- update to new version 2.99.2

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.8.1-1
+ Revision: 644011
- update to new version 2.8.1

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-2mdv2011.0
+ Revision: 619284
- the mass rebuild of 2010.0 packages

* Sat May 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.6.0-1mdv2010.0
+ Revision: 376463
- add spec and source files
- create gtk-xfce-engine

