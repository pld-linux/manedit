Summary:	UNIX manual page integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko uniksowe do tworzenia stron podrêcznika
Name:		manedit
Version:	0.5.6
Release:	3
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-bzip2.patch
Patch1:		%{name}-opt.patch
URL:		http://wolfpack.twu.net/ManEdit/
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%prep -q
%setup -q
%patch0 -p1
%patch1 -p1

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Development/Editors}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/man*
%{_datadir}/manedit
%{_mandir}/man1/*.1*
%{_applnkdir}/Development/Editors/*
%{_pixmapsdir}/*
