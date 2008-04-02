#
# TODO:
# - better workaround (try to avoid using config file to build)
# - better handle of language
#
Summary:	Jagged Alliance 2 port
Summary(pl.UTF-8):	Port gry Jagged Alliance 2
Name:		ja2
Version:	0.8
Release:	1
License:	SFI
Group:		Applications/Games
Source0:	http://ja2.dragonriders.de/files/%{name}-%{version}-source.tar.bz2
# Source0-md5:	a9562d6b02cc632acbc0febd47374293
Source1:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-linking.patch
URL:		http://ja2.dragonriders.de/
BuildRequires:	SDL-devel >= 1.2.0
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
%patch2 -p1
%patch3 -p1
%{__sed} -i 's@#CFLAGS += -g@CFLAGS += %{rpmcflags}@' config.template

mv config.template config.default

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog TODO *.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/*.6*
%{_desktopdir}/ja2-stracciatella.desktop
%{_pixmapsdir}/%{name}.png
