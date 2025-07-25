#
%bcond_with	mysql40 # support for mysql 4.0.x

Summary:	The MySQL Control Center
Summary(pl.UTF-8):	Centrum sterowania MySQL-a
Name:		mysqlcc
Group:		Applications/Databases
Version:	0.9.4
Release:	20
License:	GPL
Source0:	http://sunsite.icm.edu.pl/mysql/Downloads/MySQLCC/%{name}-%{version}-src.tar.gz
# Source0-md5:	26ee3528dce690b227d8bfb71b46ae66
Source1:	%{name}.desktop
Patch0:		%{name}-defaultpath.patch
Patch1:		%{name}-m4.patch
Patch2:		%{name}-shutdown.patch
Patch3:		%{name}-enablessl.patch
Patch4:		%{name}-reconnect.patch
Patch5:		%{name}-gptr.patch
Patch6:		%{name}-mysql55-link.patch
URL:		http://www.mysql.com/products/mysqlcc/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	autoconf
BuildRequires:	automake
%{!?with_mysql40:BuildRequires:	mysql-devel >= 4.1.0}
%if %{with mysql40}
BuildRequires:	mysql-devel >= 4.0.0
# mysqlcc uses some internal functions from mysql which are no longer exported
# in dynamic version. Linkt these functions statically while the rest of mysql
# functions dynamicly (see mysql55-link.patch)
BuildRequires:	mysql-static >= 4.0.0
%endif
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3:3.0.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlcc is a platform independent graphical MySQL administration
client. It is based on Trolltech's Qt toolkit.

%description -l pl.UTF-8
mysqlcc jest niezależnym od platformy graficznym klientem
administracji MySQL-em. Działa w oparciu o toolkit Qt Trolltecha.

%prep
%setup -q -n %{name}-%{version}-src
%patch -P0 -p1
%patch -P1 -p1
%{!?with_mysql40:%patch2 -p1}
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
QTDIR=%{_prefix}; export QTDIR
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++; export QMAKESPEC
LDFLAGS="%{rpmldflags} -Wl,-static -lmysqlclient -Wl,-Bdynamic"; export LDFLAGS
%configure \
	--with-mysql-lib=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/translations,%{_desktopdir},%{_pixmapsdir}}

install mysqlcc $RPM_BUILD_ROOT%{_bindir}
install {*.wav,syntax.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install translations/*.qm \
		$RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

convert xpm/applicationIcon.xpm -resize 48x48 $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt INSTALL.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/mysqlcc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.wav
%{_datadir}/%{name}/syntax.txt
%dir %{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/Deutsch.qm
%lang(fr) %{_datadir}/%{name}/translations/French.qm
%lang(it) %{_datadir}/%{name}/translations/Italian.qm
%lang(pl) %{_datadir}/%{name}/translations/Polish.qm
%lang(ru) %{_datadir}/%{name}/translations/Russian.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/Simplified_Chinese.qm
%lang(es) %{_datadir}/%{name}/translations/Spanish.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/Traditional_Chinese.qm
%{_pixmapsdir}/%{name}.*
%{_desktopdir}/*.desktop
