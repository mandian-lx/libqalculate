%define bname qalculate
%define name libqalculate
%define	version	 0.9.6
%define	release	 %mkrel 1

%define major 3
%define libname %mklibname %{bname} %{major}
%define develname %mklibname %{bname} -d  

Summary:	Libqalculate is the library for qalculate
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source:		http://prdownloads.sourceforge.net/libqalculate/libqalculate-%{version}.tar.bz2
URL:		http://qalculate.sourceforge.net/
BuildRequires:	cln-devel
BuildRequires:	libgmp-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libraries needed by qalculator.

#-----------------------------------------------------------

%package -n %libname 
Group:		System/Libraries
Summary:	Libqalculate is the library for qalculate 

%description -n %libname
Libraries needed by qalculator.

%package -n	%{develname}
Summary:	Headers and development files for libqalculator
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:       %{bname}-devel  
Obsoletes:	%{libname}-devel 

%description -n	 %{develname}
Headers and development files for libqalculator.

%prep
%setup -q

#libtoolize --copy --force 
#aclocal
#autoconf-2.5x
#automake-1.9 

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_bindir}/*

%find_lang %{bname}

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname} -f %{bname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README* TODO
%doc %dir %{_datadir}/qalculate
%{_datadir}/qalculate/*.xml
%doc %dir %{_docdir}/libqalculate-0.9.4/reference/html
%{_docdir}/libqalculate-0.9.4/reference/html/*
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%lang(all) %{_datadir}/locale/*/*/libqalculate.mo
