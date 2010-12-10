%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary:	Additional themes for Xfce desktop environment
Name:		gtk-xfce-engine
Version:	2.6.0
Release:	%mkrel 2
License:	GPLv3
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel > 2.6.0
Conflicts:	gtk-engines2 < 2.18.1-2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A default Xfce GTK+ themes.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# (tpg) useless
rm -rf %{buildroot}%{_libdir}/gtk-2.0/2.10.0/engines/libxfce.la

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/libxfce.so
%{_datadir}/themes/Xfce*/gtk-2.0/gtkrc
