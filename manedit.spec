Summary:	ManEdit - UNIX Manual Page Integrated Development Environment
Summary(pl):	ManEdit - zintegrowane ¶rodowisko uniksowe do tworzenia stron podrêcznika
Name:		manedit
Version:	0.5.6
Release:	2
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Patch0:		manedit-bzip2.patch
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
URL:		http://wolfpack.twu.net/ManEdit/
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
interfejs XML'owy z ci±g³ym podgl±dem. ManEdit u¿ywa kontrolek
GTK+ i dzia³a w ¶rodowisku X Window.

%prep -q
%setup -q
%patch -p1

%build
# This is a nasty hack to trick configure
# (proper way is to hack ./configure or pconf)
./configure Linux
echo -e "Linux\n"`grep UTS_RELEASE /usr/include/linux/version.h|awk '{print $3}'|sed 's/"//g'`"\n"%{_target_cpu} > manedit/this_platform.ini

./configure Linux --prefix=$RPM_BUILD_ROOT%{_prefix} -v

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

gzip -9nf AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/man*
%dir %{_datadir}/manedit/
%attr(644,root,root) %{_datadir}/manedit/help/*
%attr(644,root,root) %{_datadir}/manedit/templates/*
%attr(644,root,root) %{_datadir}/icons/*
%attr(644,root,root) %{_mandir}/man1/*.1*
