Name: 		mysqlcc
Version: 	0.8.7
Release:	1mdk
License:	GPL
Group:		Databases
Summary:	The MySQL Control Center
URL:		http://www.mysql.com/products/mysqlcc/
Source:		%{name}-%{version}-src.tar.bz2
Patch:		mysqlcc-0.8.7-defaultpath.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libqt3-devel mysql-devel ImageMagick
%define 	prefix	%{_prefix}

%description
mysqlcc is a platform independent graphical MySQL administration client.
It is based on Trolltech's Qt toolkit.

%prep
%setup -n %{name}-%{version}-src -q
%patch -p1
%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%{prefix}
export QTDIR=%{_libdir}/qt3
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install -m 755 mysqlcc $RPM_BUILD_ROOT%{prefix}/bin
install -m 644 {*.wav,syntax.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 translations/*.{qm,ts} \
               $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="Applications/Databases" \
title="MySqlCC" \
longtitle="MySqlCC" \
command="/usr/bin/mysqlcc" needs="X11" \
icon="%{name}.png"
EOF

mkdir -p %{buildroot}/{%{_miconsdir},%{_liconsdir},%{_iconsdir}}
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
%defattr(-,root,root)
%doc Changelog.txt INSTALL.txt LICENSE.txt README.txt TODO.txt
%{_bindir}/mysqlcc
%{_datadir}/%{name}
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_liconsdir}/%{name}.*
%{_menudir}/%{name}

%changelog
* Sun Jan 12 2003 Buchan Milne <bgmilne@linux-mandrake.com 0.8.7-1mdk
- 0.8.7

* Tue Nov 12 2002 Buchan Milne <bgmilne@linux-mandrake.com 0.8.6a-1mdk
- First mandrake package (based on shipped spec file)
