Summary:	Systray plugin for XChat
Summary(pl):	Wtyczka obszaru systemowego dla XChat
Name:		xchat-systray-plugin
Version:	2.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xchat2-plugins/xchat-systray-integration-%{version}-src.tar.gz
# Source0-md5:	c6e7e936b643ef5570dce91d40478bcf
URL:		http://blight.altervista.org/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	xchat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to minimize and maximize XChat to the systray and alerts
you when somebody is trying to talk to you.

%description -l pl
Pozwala na zminimalizowanie XChat do obszaru systemowego oraz
powiadamia o nowo rozpoczętych rozmowach.

%prep
%setup -q -n xchat-systray-integration-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall `pkg-config gtk+-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

sh install.sh --prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/README Docs/TODO
%attr(755,root,root) %{_libdir}/xchat/plugins/systray.so
