Summary:	Tartan - Clang tools and plugins to improve GLib/GNOME applications development
Summary(pl.UTF-8):	Tartan - narzędzia i wtyczki Clanga ułatwiające tworzenie aplikacji GLiba/GNOME
Name:		clang-tartan
Version:	0.3.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://freedesktop.org/software/tartan/releases/tartan-%{version}.tar.xz
# Source0-md5:	ccc5377157e2b7a9daf0cc4b2b14d055
URL:		https://freedesktop.org/software/tartan/
BuildRequires:	clang-devel >= 3.4
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gobject-introspection-devel >= 1.38.0
Requires:	clang >= 3.4
Requires:	glib2 >= 1:2.38.0
Requires:	gobject-introspection >= 1.38.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tartan is a set of tools and plugins for Clang which aim to improve
its usefulness for developing GLib and GNOME applications and
libraries.

%description -l pl.UTF-8
Tartan to zbiór narzędzi i wtyczek Clanga mających na celu
usprawnienie rozwijania aplikacji i bibliotek opartych na GLibie oraz
GNOME.

%prep
%setup -q -n tartan-%{version}

%build
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/tartan/3.*/libtartan.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/tartan
%attr(755,root,root) %{_bindir}/tartan-build
%dir %{_libdir}/tartan
%dir %{_libdir}/tartan/3.*
%attr(755,root,root) %{_libdir}/tartan/3.*/libtartan.so
