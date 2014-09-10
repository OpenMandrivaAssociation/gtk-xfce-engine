%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)
%define gtk3binaryver 3.0.0
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Additional themes for Xfce desktop environment
Name:		gtk-xfce-engine
Version:	3.0.1
Release:	2
License:	GPLv3
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/gtk-xfce-engine/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
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
