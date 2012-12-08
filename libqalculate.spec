%define bname qalculate
%define major 5
%define libname %mklibname %{bname} %{major}
%define develname %mklibname %{bname} -d

Summary:	The library for qalculate
Name:		libqalculate
Version:	0.9.7
Release:	13
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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-8mdv2011.0
+ Revision: 661518
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-7mdv2011.0
+ Revision: 602598
- rebuild

* Wed Jan 27 2010 Anssi Hannula <anssi@mandriva.org> 0.9.7-6mdv2010.1
+ Revision: 496912
- fix conflicts against libqalculate4 in data package (reported by
  Thierry Vignaud)
- remove unneeded conflicts against older version of itself from the
  library package

* Tue Jan 26 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.7-3mdv2010.1
+ Revision: 496825
- fix conflicts

* Mon Jan 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.7-2mdv2010.1
+ Revision: 496463
- move data files, translations into a separate subpackage
- add conflicts on older library

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.7-1mdv2010.1
+ Revision: 495575
- update to new version 0.9.7
- bump major to 5
- drop both pacthes as they were merged by upstream

* Sun Sep 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-11mdv2010.0
+ Revision: 449885
- rebuild for new cln

* Wed Aug 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-10mdv2010.0
+ Revision: 410340
- rebuild against new cln

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-9mdv2009.0
+ Revision: 229884
- added a gcc43 patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-7mdv2008.1
+ Revision: 182177
- Patch0: fix building against latest cln-1.2
- add missing buildrequires on readline and ncurses
- rebuild for new cln

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Jan 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-5mdv2008.1
+ Revision: 157616
- do not package COPYING files
- new license policy
- new devel policy
- move *.xml to library package, bug #36944

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-3mdv2008.0
+ Revision: 49821
- obsolete library

* Sat Jun 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-2mdv2008.0
+ Revision: 43510
-- obsolete older release

* Sat Jun 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 43493
- adjust buildrequires
- new version
- new devel library policy
- spec file clean


* Tue Jun 27 2006 Charles A Edwards <eslrahc@mandriva.org> 0.9.4-1mdv2007.0
- now a totally modular pkg
- 0.9.4
- update filelist

* Fri Dec 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.7.2-2mdk
- rebuild for new cln
- patch 0: fix compiling with g++-4

* Tue Feb 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

* Sat Jan 22 2005 Per Ãyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.1-4mdk
- rebuild for new readline

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.1-3mdk 
- Rebuild with latest howl

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.7.1-2mdk
- Fix BuildRequires
- Run scrollkeeper during post/postun

* Mon Nov 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

* Tue Oct 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-1mdk
- 0.7.0

* Wed Jul 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6.2-1mdk
- 0.6.2

* Fri Jul 09 2004 Austin Acton <austin@mandrake.org> 0.6.1-1mdk
- 0.6.1
- configure 2.5

* Fri Jun 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-1mdk
- 0.6

* Wed Feb 18 2004 Austin Acton <austin@mandrake.org> 0.4-1mdk
- 0.4

* Mon Oct 27 2003 Austin Acton <aacton@yorku.ca> 0.3.1-1mdk
- 0.3.1

* Wed Oct 22 2003 Austin Acton <aacton@yorku.ca> 0.3-1mdk
- initial package

