Summary:	UNIX manual page integrated development environment
Summary(pl.UTF-8):	Zintegrowane środowisko uniksowe do tworzenia stron podręcznika
Name:		manedit
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	a7ee1835e32ed3c9279412af7caf13ef
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-bzip2.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-dont_strip.patch
Patch4:		%{name}-man_path.patch
Patch5:		%{name}-man.patch
URL:		http://freecode.com/projects/manedit
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	perl-base
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ManEdit is a UNIX Manual Page Integrated Development Environment.
It has full UNIX manual page editing capabilities using an XML
interface with instant preview. ManEdit uses the GTK+ widget set
and requires the X Window System.

%description -l pl.UTF-8
ManEdit jest zintegrowanym środowiskiem uniksowym do tworzenia
stron podręcznika. Pozwala na kompletną edycję stron wykorzystując
interfejs XML-owy z ciągłym podglądem. ManEdit używa kontrolek
GTK+ i działa w środowisku X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%{__perl} -pi -e 's@/lib/$@/%{_lib}/@' manedit/platforms.ini

%build
# This is a nasty hack to trick configure
# (proper way is to hack ./configure or pconf)
echo -e "Linux\n"`grep UTS_RELEASE /usr/include/linux/version.h|awk '{print $3}'|sed 's/"//g'`"\n"%{_target_cpu} > manedit/this_platform.ini

./configure Linux -v \
	--prefix=%{_prefix}

%{__make} all \
	OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/manedit
%attr(755,root,root) %{_bindir}/manview
%attr(755,root,root) %{_bindir}/manwrap
%{_datadir}/manedit
%{_mandir}/man1/manedit.1*
%{_desktopdir}/manedit.desktop
%{_pixmapsdir}/manedit.png
%{_pixmapsdir}/manedit.xpm
%{_pixmapsdir}/manview.xpm
