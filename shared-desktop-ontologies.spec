Summary:	Shared Desktop Ontologies
Summary(pl.UTF-8):	Ontologia dla aplikacji desktopowych
Name:		shared-desktop-ontologies
Version:	0.10.0
Release:	1
License:	BSD or CC-BY-SA v3.0, CC v3.0, w3c (see LICENSE.README)
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/oscaf/%{name}-%{version}.tar.bz2
# Source0-md5:	bfb7b5acbb43e5e45466c87dbe9c45b7
URL:		http://sourceforge.net/apps/trac/oscaf/
# leave only required ones
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.603
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The shared-desktop-ontologies package brings the semantic web to the
desktop in terms of vocabulary. It contains the well known core
ontologies such as RDF and RDFS as well as the Nepomuk ontologies
which are used by projects like KDE or Strigi.

%description -l pl.UTF-8
Pakiet shared-desktop-ontologies dostarcza aplikacjom desktopowym sieć
semantyczną w sensie słownictwa. Zawiera dobrze znaną ontologię, taką
jak RDF i RDFS, a także ontologię z Nepomuka, używaną przez projekty
takie jak KDE i Strigi.

%package devel
Summary:	Development files for shared-desktop-ontologies
Summary(pl.UTF-8):	Pliki programistyczne dla shared-desktop-ontologies
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development (cmake and pkgconfig) files for shared-desktop-ontologies.

%description devel -l pl.UTF-8
Pliki programistyczne (dla cmake i pkg-configa) dla pakietu
shared-desktop-ontologies.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}" \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.{BSD,CC-BY,DCMI,README,w3c}  README
%{_datadir}/ontology

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/shared-desktop-ontologies.pc
%{_datadir}/cmake/SharedDesktopOntologies
