Summary:	The MySQL Control Center
Summary(pl):	Centrum sterowania MySQL-a
Name:		mysqlcc
Group:		Applications/Databases
Version:	0.9.2
Release:	1
License:	GPL
Source0:	http://sunsite.icm.edu.pl/mysql/Downloads/MySQLCC/%{name}-%{version}-src.tar.gz
# Source0-md5:	812c762b91011f0d1c2d834ce05fd5c3
Patch0:		%{name}-defaultpath.patch
Patch1:		%{name}-m4.patch
URL:		http://www.mysql.com/products/mysqlcc/
BuildRequires:	ImageMagick
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel >= 4.0.0
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
