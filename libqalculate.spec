%define bname qalculate
%define major 5
%define libname %mklibname %{bname} %{major}
%define develname %mklibname %{bname} -d

Summary:	The library for qalculate
Name:		libqalculate
Version:	0.9.7
Release:	%mkrel 6
License:	GPLv2+
Group:		System/Libraries
URL:		http://qalculate.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/qalculate/libqalculate/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	cln-devel
BuildRequires:	libgmp-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libglib2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Libraries needed by qalculator.

%package -n %{libname}
Group:		System/Libraries
Summary:	The library for qalculate
Obsoletes:	%{mklibname %{bname} 3}
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
Libraries needed by qalculate.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:       %{bname}-devel
Provides:	%{name}-devel
Obsoletes:	%mklibname %{bname} 3 -d

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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_bindir}/*

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig 
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig 
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files data -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/qalculate/*.xml

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README* TODO
%doc %dir %{_datadir}/qalculate
%doc %{_docdir}/%{name}-%{version}
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
