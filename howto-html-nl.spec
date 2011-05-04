%define	DATE	20040813
%define    language  Dutch
%define    lang      nl
%define format1      html-%{lang}
%define format2      HTML/%{lang}


Summary:   %language HOWTO documents (html format) from the Linux Documentation Project
Name:      howto-%{format1}
Version:	10.1
Release:	%mkrel 7
Group:		Books/Howtos

Source0:   %name.tar

Url:		http://nl.linux.org/doc/nlhowto.php
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format1}-root
BuildArch:	noarch

BuildRequires: howto-utils
Requires:    locales-%lang xdg-utils

%description
Linux HOWTOs in Dutch documents are located at
http://nl.linux.org/doc/nlhowto.php and
ftp://fjordland.nl.linux.org/pub/HOWTO-NL/all-howtos-html.tar.gz

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %lang %language > index.html; cp -a * $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

perl -p -i -e "s|<LI><A HREF=\"Bootdisk-HOWTO-NL.html\">De Linux Bootdisk HOWTO</A>|<LI><A HREF=\"Bootdisk-HOWTO-NL.html\">De Linux Bootdisk HOWTO</A>\n<LI><A HREF=\"Bootdisk/t1.html\">De Linux Bootdisk HOWTO</A>|" $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}/index.html
# this perl line is needed to include the Bootdisk-howto which is in a directory with strange file name. 

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}
%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
