Summary:	Jagged Alliance 2 port
Summary(pl.UTF-8):	Port gry Jagged Alliance 2
Name:		ja2
Version:	0.5
Release:	0.1
License:	SFI
Group:		Applications
Source0:	http://ja2.dragonriders.de/files/%{name}-%{version}-source.tar.bz2
# Source0-md5:	22003ee20037cdd24a900c978280bd38
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-config.patch
URL:		http://ja2.dragonriders.de/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	sed >= 4.0
BuildRequires:	zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jagged Alliance 2 port using SDL.

%description -l pl.UTF-8
Port gry Jagged Alliance 2 używający SDL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i 's@#CFLAGS += -g@CFLAGS += %{rpmcflags}@' config.template

mv config.template config.default
%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LIBS="-lSDL"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog TODO *.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/*.6*
