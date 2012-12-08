Summary:	Dog better than cat
Name:		dog
Version:	1.7
Release:	10
Group:		Text tools
License:	GPL
# Seems to be dead
Url:		http://jl.photodex.com/dog/
Source0:	%{name}-%{version}.tar.bz2

%description
Dog is intended as a replacement for the obscure utility "cat". 
In addition to emulating all of the behavior of cat, 
dog also has some functionality that would normally require a 
freaky perl hacker to spew out line noise for perl to interpret. 
This includes extracting ranges of lines of text and strfry()ing text.

%prep
%setup -q

%build
%make

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -s dog %{buildroot}%{_bindir}/%{name}
install -m644 dog.1 %{buildroot}%{_mandir}/man1/dog.1

%files
%doc README AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/*/*

%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-9mdv2011.0
+ Revision: 617870
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.7-8mdv2010.0
+ Revision: 428323
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.7-7mdv2009.0
+ Revision: 244449
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.7-5mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import dog


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.7-5mdv2007.0
- rebuild

* Thu Jul 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.7-4mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.7-3mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.7-2mdk
- rebuild

* Tue Apr 16 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.7-1mdk
- 1.7 by Olivier Thauvin <thauvin@aerov.jussieu.fr>

* Wed Mar 13 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 
- First Mandrake release
