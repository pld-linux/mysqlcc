Summary:	The MySQL Control Center
Summary(pl):	Centrum sterowania MySQL-a
Name:		mysqlcc
Group:		Applications/Databases
# all higher versions than 0.8.7 require mysql 4.0
Version:	0.8.7
Release:	1
License:	GPL
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/MyCC/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-defaultpath.patch
Patch1:		%{name}-m4.patch
URL:		http://www.mysql.com/products/mysqlcc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ImageMagick
BuildRequires:	mysql-devel < 4.0
BuildRequires:	zlib-devel
BuildRequires:	qt-devel >= 3.0.5

%description
mysqlcc is a platform independent graphical MySQL administration
client. It is based on Trolltech's Qt toolkit.

%description -l pl
mysqlcc jest niezale¿nym od platformy graficznym clientem
administracji MySQL-em. Dzia³a w oparciu o toolkit Qt Trolltecha.

%prep
%setup -n %{name}-%{version}-src -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
QTDIR=%{_prefix}; export QTDIR
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++; export QMAKESPEC
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install mysqlcc $RPM_BUILD_ROOT%{_bindir}
install {*.wav,syntax.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install translations/*.{qm,ts} \
		$RPM_BUILD_ROOT%{_datadir}/%{name}/translations

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
convert xpm/applicationIcon.xpm -resize 48x48 $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt INSTALL.txt LICENSE.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/mysqlcc
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.*
