
Summary:	Shared Desktop Ontologies
Summary(pl.UTF-8):	Shared Desktop Ontologies
Name:		shared-desktop-ontologies
%define	mver	0.8
Version:	%{mver}.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	https://sourceforge.net/projects/oscaf/files/shared-desktop-ontologies/%{mver}/%{name}-%{version}.tar.bz2/download#/%{name}-%{version}.tar.bz2
# Source0-md5:	3abbd4ddc683aaa0504ed8499b57285e
URL:		http://sourceforge.net/apps/trac/oscaf/
# leave only required ones
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared desktop ontologies.

#%description -l pl.UTF-8

%package devel
Summary:	Cmake files for shared-desktop-ontologies
Summary(pl.UTF-8):	Pliki cmake dla shared-desktop-ontologies
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Cmake files for shared-desktop-ontologies.

%description devel -l pl.UTF-8
Pliki cmake dla shared-desktop-ontologies.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%{_datadir}/ontology

%files devel
%defattr(644,root,root,755)
%{_datadir}/pkgconfig/shared-desktop-ontologies.pc
%{_datadir}/cmake/SharedDesktopOntologies
