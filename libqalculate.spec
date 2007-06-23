%define bname qalculate
%define major 4
%define libname %mklibname %{bname} %{major}
%define develname %mklibname %{bname} -d  

Summary:	Libqalculate is the library for qalculate
Name:		libqalculate
Version:	0.9.6
Release:	%mkrel 1
License:	GPL
Group:		System/Libraries
Source:		http://prdownloads.sourceforge.net/libqalculate/libqalculate-%{version}.tar.bz2
URL:		http://qalculate.sourceforge.net/
BuildRequires:	cln-devel
BuildRequires:	libgmp-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libglib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libraries needed by qalculator.

%package -n %{libname}
Group:		System/Libraries
Summary:	Libqalculate is the library for qalculate 

%description -n %{libname}
Libraries needed by qalculator.

%package -n %{develname}
Summary:	Headers and development files for libqalculator
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:       %{bname}-devel  
Obsoletes:	%{libname}-devel 

%description -n %{develname}
Headers and development files for libqalculator.

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

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README* TODO
%doc %dir %{_datadir}/qalculate
%doc %{_docdir}/%{name}-%{version}
%{_datadir}/qalculate/*.xml
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
