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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 10.1-7mdv2011.0
+ Revision: 665428
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 10.1-6mdv2011.0
+ Revision: 605871
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 10.1-5mdv2010.1
+ Revision: 520706
- rebuilt for 2010.1

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 10.1-4mdv2009.0
+ Revision: 218433
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 10.1-4mdv2008.1
+ Revision: 150269
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 Funda Wang <fwang@mandriva.org> 10.1-3mdv2008.0
+ Revision: 83340
- SILNET: add desktop file
- Rebuild for new era
- Import howto-html-nl



* Thu Jul 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-2mdk
- fix menu entry (#16633)

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-1mdk
- new snapshot

* Thu Feb 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.5mdk
- new menu scheme

* Sat Feb 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.4mdk
- fix menu generation
- fix buildroot directory name

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.3mdk
- synchronize all howtos spec files
- use new howto-utils

* Wed Feb 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.2mdk
- fix menu entry
- rebuild for latest makehowtoindex %%lang %%language > index.html)

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.1mdk
- new release

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.0-0.1mdk
- new snapshot
- add real url
- sanitize menu entry (fix menu-command-not-in-package)

* Thu Jan 29 2002 Adrien DEMAREZ <ademarez@mandrakesoft.com> 8.2-2mdk
- updated howtos

* Thu Jan 17 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-1mdk
- Fix menu entry (icon)

* Fri Sep 07 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-2mdk
- Modified menu entry so that it works with KDE and gnome

* Thu Aug 30 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Automatically updated

* Fri Mar  9 2001 Etienne Faure  <etienne@mandrakesoft.com> 8.0-2mdk
- Small fixes 
- Include Bootdisk howto

* Wed Feb 28 2001 Andre van Blokland <ablokland@go.com> 8.0-1
- First Dutch Howto using English and French spec-files
