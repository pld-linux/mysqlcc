Summary:	The MySQL Control Center
Summary(pl):	Centrum sterowania MySQL-a
Name:		mysqlcc
Group:		Applications/Databases
Version:	0.8.7
Release:	1mdk
License:	GPL
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/MyCC/%{name}-%{version}-src.tar.bz2
Patch0:		%{name}-0.8.7-defaultpath.patch.bz2
URL:		http://www.mysql.com/products/mysqlcc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ImageMagick
BuildRequires:	mysql-devel
BuildRequires:	qt-devel >= 3.0

%description
mysqlcc is a platform independent graphical MySQL administration
client. It is based on Trolltech's Qt toolkit.

%description -l pl
mysqlcc jest niezale¿nym od platformy graficznym clientem
administracji MySQL-em. Dzia³a w oparciu o toolkit Qt Trolltecha.

%prep
%setup -n %{name}-%{version}-src -q
%patch -p1

%build
export CFLAGS="%{rpmcflags}"
./configure --prefix=%{_prefix}
export QTDIR=%{_libdir}/qt3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install mysqlcc $RPM_BUILD_ROOT%{_bindir}
install {*.wav,syntax.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install translations/*.{qm,ts} \
		$RPM_BUILD_ROOT%{_datadir}/%{name}/translations

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="Applications/Databases" \
title="MySqlCC" \
longtitle="MySqlCC" \
command="%{_bindir}/mysqlcc" needs="X11" \
icon="%{name}.png"
EOF

install -d %{buildroot}/{%{_miconsdir},%{_liconsdir},%{_iconsdir}}
convert xpm/applicationIcon.xpm -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert xpm/applicationIcon.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert xpm/applicationIcon.xpm -resize 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}
/sbin/ldconfig

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt INSTALL.txt LICENSE.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/mysqlcc
%{_datadir}/%{name}
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_liconsdir}/%{name}.*
%{_menudir}/%{name}
