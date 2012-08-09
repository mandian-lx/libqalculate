%define bname qalculate
%define major 5
%define libname %mklibname %{bname} %{major}
%define develname %mklibname %{bname} -d

Summary:	The library for qalculate
Name:		libqalculate
Version:	0.9.7
Release:	12
License:	GPLv2+
Group:		System/Libraries
URL:		http://qalculate.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/qalculate/libqalculate/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(cln)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	perl(XML::Parser)
BuildRequires:	gmp-devel
BuildRequires:	readline-devel

%description
Libraries needed by qalculator.

%package -n %{libname}
Group:		System/Libraries
Summary:	The library for qalculate
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
Libraries needed by qalculate.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{bname}-devel
Provides:	%{name}-devel

%description -n %{develname}
Headers and development files for %{name}.

%package data
Summary:	Data files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname %{bname} 4} < 0.9.7-4
Conflicts:	%{mklibname %{bname} 5} < 0.9.7-4

%description data
Data files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_bindir}/*

%find_lang %{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files data -f %{name}.lang
%{_datadir}/qalculate/*.xml

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README* TODO
%doc %dir %{_datadir}/qalculate
%doc %{_docdir}/%{name}-%{version}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

