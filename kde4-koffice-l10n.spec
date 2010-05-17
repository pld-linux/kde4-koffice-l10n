# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n | awk '/.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then ':r out' in vim and ./builder -a5 the spec
#   and ':%s#koffice-1.6.3#koffice-%{version}#g'
# - ISO 639-1 language codes maybe be looked up from http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#
%define		orgname		koffice-l10n
%define		kdever		4.4.3

Summary:	KOffice suite - international support
Summary(pl.UTF-8):	KOffice - wsparcie dla wielu języków
Name:		kde4-koffice-l10n
Version:	2.1.2
Release:	1
License:	GPL
Group:		I18n
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-ca-%{version}.tar.bz2
# Source0-md5:	29244b391dc54fe9baf9f0f8521a1cca
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-da-%{version}.tar.bz2
# Source1-md5:	08cd347c2bd4b4bfc14f6051e362aaa5
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-de-%{version}.tar.bz2
# Source2-md5:	0681301fab47e669d79c228696551e87
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-el-%{version}.tar.bz2
# Source3-md5:	adaf70d6d64ac7630e1b890d55dc8a8b
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-en_GB-%{version}.tar.bz2
# Source4-md5:	00cd2fa01d4cd840ba575cdf4bbcfa00
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-es-%{version}.tar.bz2
# Source5-md5:	a821811db9da0605f34c4fba18567705
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-et-%{version}.tar.bz2
# Source6-md5:	28251ab477c12442a48843ef03ecc748
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-fr-%{version}.tar.bz2
# Source7-md5:	0221e91c3aea51dbdf24ca2e91c73bec
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-fy-%{version}.tar.bz2
# Source8-md5:	019883e5c3a9ad4269ecfd80b2db9ffb
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-gl-%{version}.tar.bz2
# Source9-md5:	580d0dbc7b88ccc0d04ac77c9cb355cd
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-hne-%{version}.tar.bz2
# Source10-md5:	2342fb0f49f1580e360eb90b2c78079e
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-it-%{version}.tar.bz2
# Source11-md5:	89d6d81e74b3b1e3c3ecd6850ac62046
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-ja-%{version}.tar.bz2
# Source12-md5:	05aa3337116efa30f2849e728e0b6bf3
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-kk-%{version}.tar.bz2
# Source13-md5:	9bdad29df26b4f14b97fa4c3fed74388
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nb-%{version}.tar.bz2
# Source14-md5:	9224176ac1b4bef5deb85597a4796ddb
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nds-%{version}.tar.bz2
# Source15-md5:	b861d372b406a61f294d4902fa3107ba
Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nl-%{version}.tar.bz2
# Source16-md5:	5267bf49b0b0056f1305a1ff6979be60
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pl-%{version}.tar.bz2
# Source17-md5:	c9fda5bc0113d440bd3549fd53c4c70a
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pt-%{version}.tar.bz2
# Source18-md5:	74d0555fae13e83cc40b93ff5226f198
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pt_BR-%{version}.tar.bz2
# Source19-md5:	d71c26092b7c756a31798e7138c15ca5
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-sv-%{version}.tar.bz2
# Source20-md5:	1ebae75a34aeac34dd0eb0ff21e62d57
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-tr-%{version}.tar.bz2
# Source21-md5:	c1e6228e678ea26f6361edfa30633367
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-uk-%{version}.tar.bz2
# Source22-md5:	3229dc3f043cfcfc5cd2483931007a10
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-wa-%{version}.tar.bz2
# Source23-md5:	b572b46a959da595945d077aa7d89f42
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-zh_CN-%{version}.tar.bz2
# Source24-md5:	90c4193e3f980cc5558d7f1b507880c8
Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-zh_TW-%{version}.tar.bz2
# Source25-md5:	0eb9dfed48496f149bbd89dc4a60d3bf
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{orgname}-%{version}-root-%(id -u -n)

%description
KOffice suite - international support.

%description -l pl.UTF-8
KOffice - wsparcie dla wielu języków.

%package Catalan
Summary:	KOffice suite - Catalan language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka katalońskiego
Group:		I18n

%description Catalan
KOffice suite - Catalan language support.

%description Catalan -l pl.UTF-8
KOffice - wsparcie dla języka katalońskiego.

%package Danish
Summary:	KOffice suite - Danish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka duńskiego
Group:		I18n

%description Danish
KOffice suite - Danish language support.

%description Danish -l pl.UTF-8
KOffice - wsparcie dla języka duńskiego.

%package German
Summary:	KOffice suite - German language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka niemieckiego
Group:		I18n

%description German
KOffice suite - German language support.

%description German -l pl.UTF-8
KOffice - wsparcie dla języka niemieckiego.

%package English_UK
Summary:	KOffice suite - KOffice suite - English (UK) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		I18n

%description English_UK
KOffice suite - English (UK) language support.

%description English_UK -l pl.UTF-8
KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Spanish
Summary:	KOffice suite - Spanish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hiszpańskiego
Group:		I18n

%description Spanish
KOffice suite - Spanish language support.

%description Spanish -l pl.UTF-8
KOffice - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	KOffice suite - Estonian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka estońskiego
Group:		I18n

%description Estonian
KOffice suite - Estonian language support.

%description Estonian -l pl.UTF-8
KOffice - wsparcie dla języka estońskiego.

%package French
Summary:	KOffice suite - French language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka francuskiego
Group:		I18n

%description French
KOffice suite - French language support.

%description French -l pl.UTF-8
KOffice - wsparcie dla języka francuskiego.

%package Galician
Summary:	KOffice suite - Galician language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka galicyjskiego
Group:		I18n

%description Galician
KOffice suite - Galician language support.

%description Galician -l pl.UTF-8
KOffice - wsparcie dla języka galicyjskiego.

%package Italian
Summary:	KOffice suite - Italian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka włoskiego
Group:		I18n

%description Italian
KOffice suite - Italian language support.

%description Italian -l pl.UTF-8
KOffice - wsparcie dla języka włoskiego.

%package Japanese
Summary:	KOffice suite - Japanese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka japońskiego
Group:		I18n

%description Japanese
KOffice suite - Japanese language support.

%description Japanese -l pl.UTF-8
KOffice - wsparcie dla języka japońskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Polish
Summary:	KOffice suite - Polish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka polskiego
Group:		I18n

%description Polish
KOffice suite - Polish language support.

%description Polish -l pl.UTF-8
KOffice - wsparcie dla języka polskiego.

%package Portuguese
Summary:	KOffice suite - Portuguese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego
Group:		I18n

%description Portuguese
KOffice suite - Portuguese language support.

%description Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	KOffice suite - Portuguese (Brazil) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		I18n

%description Brazil_Portuguese
KOffice suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Swedish
Summary:	KOffice suite - Swedish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka szwedzkiego
Group:		I18n

%description Swedish
KOffice suite - Swedish language support.

%description Swedish -l pl.UTF-8
KOffice - wsparcie dla języka szwedzkiego.

%package Turkish
Summary:	KOffice suite - Turkish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tureckiego
Group:		I18n

%description Turkish
KOffice suite - Turkish language support.

%description Turkish -l pl.UTF-8
KOffice - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	KOffice suite - Ukrainian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka ukraińskiego
Group:		I18n

%description Ukrainian
KOffice suite - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
KOffice - wsparcie dla języka ukraińskiego.

%package Walloon
Summary:	KOffice suite - Walloon language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka walońskiego
Group:		I18n

%description Walloon
KOffice suite - Walloon language support.

%description Walloon -l pl.UTF-8
KOffice - wsparcie dla języka walońskiego.

%package Simplified_Chinese
Summary:	KOffice suite - simplified Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla uproszczonego języka chińskiego
Group:		I18n

%description Simplified_Chinese
KOffice suite - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
KOffice - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	KOffice suite - Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka chińskiego
Group:		I18n

%description Chinese
KOffice suite - Chinese language support.

%description Chinese -l pl.UTF-8
KOffice - wsparcie dla języka chińskiego.

%prep
%setup -q -c -T %(seq -f '-a %g' 0 25 | xargs)

%build
for dir in koffice-l10n-*-%{version}; do
	cd $dir
	%cmake \
		-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DCMAKE_VERBOSE_MAKEFILE=OFF \
		-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
		.
	%{__make}
	cd ..
done

%install
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in %{orgname}-*-%{version}; do
		%{__make} -C $dir install \
			DESTDIR=$RPM_BUILD_ROOT
	done
	touch installed.stamp
fi

rm -f *.lang

FindLang() {
	#    $1 - short language name
	local lang="$1"

	# share/doc/kde/HTML/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang"
	fi

	# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo"
	fi

	# share/apps/koffice/autocorrect/*.xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/koffice/autocorrect/$lang.xml"
	fi

	touch $lang.ok
}

files="\
example \
graphite \
kdatabase \
kdgantt \
kexi \
kformdesigner \
kontour \
kplato \
krita \
"

for i in $files; do
	rm -rf $(find $RPM_BUILD_ROOT -name "$i*.mo")
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/$i
done

FindLang ca > Catalan.lang
FindLang da > Danish.lang
FindLang de > German.lang
FindLang en_GB > English_UK.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang fr > French.lang
FindLang gl > Galician.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
FindLang sv > Swedish.lang
FindLang tr > Turkish.lang
FindLang uk > Ukrainian.lang
FindLang wa > Walloon.lang
FindLang zh_CN > Simplified_Chinese.lang
FindLang zh_TW > Chinese.lang

check_installed_languages() {
	err=0
	# we ignore dialects (currently sr@latin is the only case)
	for a in $(ls -1d %{orgname}-*-%{version} | %{__sed} '/@/d'); do
		l=${a#%{orgname}-}
		l=${l%%-%{version}}
		if [ ! -f $l.ok ]; then
			echo >&2 "language $l not processed"
			err=1
		fi
	done
	#if [ "$err" = 1 ]; then
		#exit 1
	#fi
}
check_installed_languages

%clean
check_installed_files() {
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{orgname}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $lang"
			exit 1
		fi
	done
}
check_installed_files
%{!?debug:rm -rf $RPM_BUILD_ROOT}

%files -f Catalan.lang Catalan
%defattr(644,root,root,755)

%files -f Danish.lang Danish
%defattr(644,root,root,755)

%files -f German.lang German
%defattr(644,root,root,755)

%files -f English_UK.lang English_UK
%defattr(644,root,root,755)

%files -f Spanish.lang Spanish
%defattr(644,root,root,755)

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

%files -f Galician.lang Galician
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

%files -f Polish.lang Polish
%defattr(644,root,root,755)

%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)

%files -f Turkish.lang Turkish
%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)

%files -f Walloon.lang Walloon
%defattr(644,root,root,755)

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)
