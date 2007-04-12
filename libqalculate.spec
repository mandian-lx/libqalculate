%define bname qalculate
%define name libqalculate
%define	version	 0.9.4	
%define	release	 %mkrel 1

%define major 3
%define libname %mklibname %{bname} %major
%define libnamedev %mklibname %{bname} %major -d  

Summary:	Libqalculate is the library for qalculate
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source:		http://prdownloads.sourceforge.net/libqalculate/libqalculate-%{version}.tar.bz2
URL:		 http://qalculate.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot 
BuildRequires:	cln-devel
BuildRequires:	libgmp-devel
BuildRequires:	libxml2-devel

%description
Libraries needed by qalculator  

#-----------------------------------------------------------

%package -n %libname 
Group: System/Libraries
Summary: Libqalculate is the library for qalculate 
Provides: %{name} = %{version}
Obsoletes: %{name}0
Provides:   %{name}0

%description -n %libname
Libraries needed by qalculator    

%package -n	%{libnamedev}
Summary:	Headers and development files for libqalculator
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	 %{name}-devel = %{version}-%{release}
Obsoletes:     %{name}0-devel 
Provides:       %{name}0-devel  
 

%description -n	 %{libnamedev}
Headers and development files for libqalculator.

%prep
%setup -q -n  libqalculate-0.9.4

libtoolize --copy --force 
aclocal
autoconf-2.5x
automake-1.9 
%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_bindir}/*

%find_lang %{bname}

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libnamedev} -f %{bname}.lang
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

 
