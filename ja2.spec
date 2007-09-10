Summary:	Jagged Alliance 2 port
Summary(pl.UTF-8):	Port gry Jagged Alliance 2
Name:		ja2
Version:	0.6
Release:	0.1
License:	SFI
Group:		Applications/Games
Source0:	http://ja2.dragonriders.de/files/%{name}-%{version}-source.tar.bz2
# Source0-md5:	b7adb0fd016e4d467657127d4134089d
Patch0:		%{name}-config.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://ja2.dragonriders.de/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jagged Alliance 2 is a turn based strategy game in which you hire
mercs to free the country of Arulco. Over 150 different characters, a
nonlinear gameplay, deep strategic battles and more-than-average
detailed equipment do their best, to keep you playing on and on.

%description -l pl.UTF-8
Jagged Alliance 2 to turowa gra strategiczna, w której gracz
wynajmuje najemników aby wyswobodzić kraj Arulco. Ponad 150
rozmaitych postaci, nieliniowa rozgrywka, rozbudowane taktycznie bitwy
oraz bardzo szczegółowo opisany ekwipunek sprawiają, że chce się
grać cały czas.

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
%{_desktopdir}/ja2-stracciatella.desktop
%{_pixmapsdir}/jagged2.ico
