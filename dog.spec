%define name dog
%define version 1.7
%define release %mkrel 8

Summary: Dog better than cat
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Url: http://jl.photodex.com/dog/
License: GPL
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-buildroot

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
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -s dog $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 dog.1 $RPM_BUILD_ROOT%{_mandir}/man1/dog.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/*/*

