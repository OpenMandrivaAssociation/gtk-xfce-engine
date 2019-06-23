%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define gtk3binaryver 3.0.0
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Additional themes for Xfce desktop environment
Name:		gtk-xfce-engine
Version:	3.2.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/gtk-xfce-engine/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  xfce4-dev-tools

%description
A default Xfce GTK+ themes.

%files
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/libxfce.so
%{_libdir}/gtk-3.0/%{gtk3binaryver}/theming-engines/libxfce.so
%{_datadir}/themes/Xfce*

#---------------------------------------------------------------------------

%prep
%setup -q

%build
%xdt_autogen
%configure
%make_build

%install
%make_install
