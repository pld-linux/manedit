Summary:	UNIX manual page integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko uniksowe do tworzenia stron podrêcznika
Name:		manedit
Version:	0.5.10
Release:	2
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	a0d9ff519221fee53e3c7c8b10ddc7af
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-bzip2.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-dont_strip.patch
Patch4:		%{name}-man_path.patch
URL:		http://wolfpack.twu.net/ManEdit/
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ManEdit is a UNIX Manual Page Integrated Development Environment.
It has full UNIX manual page editing capabilities using an XML
interface with instant preview. ManEdit uses the GTK+ widget set
and requires the X Window Systems.

%description -l pl
ManEdit jest zintegrowanym ¶rodowiskiem uniksowym do tworzenia
stron podrêcznika. Pozwala na kompletn± edycjê stron wykorzystuj±c
interfejs XML-owy z ci±g³ym podgl±dem. ManEdit u¿ywa kontrolek
GTK+ i dzia³a w ¶rodowisku X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# This is a nasty hack to trick configure
# (proper way is to hack ./configure or pconf)
./configure Linux
echo -e "Linux\n"`grep UTS_RELEASE /usr/include/linux/version.h|awk '{print $3}'|sed 's/"//g'`"\n"%{_target_cpu} > manedit/this_platform.ini

./configure Linux --prefix=%{_prefix} -v

%{__make} all \
	OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/man*
%{_datadir}/manedit
%{_mandir}/man1/*.1*
%{_desktopdir}/*
%{_pixmapsdir}/*
