Summary:	Better than cat
Name:		dog
Version:	1.7
Release:	13
Group:		Text tools
License:	GPLv2
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
%make CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install %{name} %{buildroot}%{_bindir}/%{name}
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/*/%{name}.1*

