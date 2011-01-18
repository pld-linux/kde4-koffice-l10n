# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n | awk '/.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then ':r out' in vim and ./builder -a5 the spec
#   and ':%s#koffice-1.6.3#koffice-%{version}#g'
# - ISO 639-1 language codes maybe be looked up from http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#
# TODO:
# - package hne lang
#

%define		orgname		koffice-l10n
%define		kdever		4.5.5

Summary:	KOffice suite - international support
Summary(pl.UTF-8):	KOffice - wsparcie dla wielu języków
Name:		kde4-koffice-l10n
Version:	2.3.0
Release:	1
License:	GPL
Group:		I18n
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-ca-%{version}.tar.bz2
# Source0-md5:	bdf2eb94055f51ebe4a59c58fb8fefc2
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-da-%{version}.tar.bz2
# Source1-md5:	ae6ae9ef63b0e52e0dc1813a87506890
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-de-%{version}.tar.bz2
# Source2-md5:	3554bb5887af3af71166ce027637273e
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-el-%{version}.tar.bz2
# Source3-md5:	4d7dc252a659a9fe3da59590fcb05ac8
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-en_GB-%{version}.tar.bz2
# Source4-md5:	d08426e1591675831a338e2bd54be10b
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-es-%{version}.tar.bz2
# Source5-md5:	f7ebe904ae522716dae85f117f5d08af
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-et-%{version}.tar.bz2
# Source6-md5:	8b32e4620dc3f314dd9ca57c22856e6c
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-fr-%{version}.tar.bz2
# Source7-md5:	f1df28bed38e9cdb5366e18e16f094f0
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-gl-%{version}.tar.bz2
# Source8-md5:	7c5d43cf75eb2216bf124886d3f60d26
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-it-%{version}.tar.bz2
# Source9-md5:	4871c3c1fb2658f643f743daa6dfab81
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-ja-%{version}.tar.bz2
# Source10-md5:	21309edfc75a9be6500de31e40c36c36
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-kk-%{version}.tar.bz2
# Source11-md5:	0c170c2c0c91eb329d153a297d8dd6e2
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nb-%{version}.tar.bz2
# Source12-md5:	876e81adaf70b8627b2aa0963bc85f61
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nds-%{version}.tar.bz2
# Source13-md5:	5d5654f8744df637f9c5defb477191d4
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-nl-%{version}.tar.bz2
# Source14-md5:	631c3a748caa1bcf9eec72d96733e82f
#Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pl-%{version}.tar.bz2
# Source15-md5:	6068c8b3530a1827a5a61300ae009355
Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pt-%{version}.tar.bz2
# Source16-md5:	9ad09a3b7d07ec17071da57647cbd751
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-pt_BR-%{version}.tar.bz2
# Source17-md5:	0af6e5efaf7d8303ded3950e6c901d7d
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-sv-%{version}.tar.bz2
# Source18-md5:	86c409e03ef996ea533d5ab32bebda19
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-tr-%{version}.tar.bz2
# Source19-md5:	6ef89202523607122e4679dd6c748296
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-uk-%{version}.tar.bz2
# Source20-md5:	9e0b77d44a396a135366fc8a4938d6d6
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-zh_CN-%{version}.tar.bz2
# Source21-md5:	1ac692eea52fd74bc4f0761947b71770
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/koffice-l10n/%{orgname}-zh_TW-%{version}.tar.bz2
# Source22-md5:	47e58533f2ab1a4c4a674748087dd919
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package Greek
Summary:	KOffice suite - Greek language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka greckiego
Group:		I18n

%description Greek
KOffice suite - Greek language support.

%description Greek -l pl.UTF-8
KOffice - wsparcie dla języka greckiego.

%package Kazakh
Summary:	KOffice suite - Kazakh language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka kazachskiego
Group:		I18n

%description Kazakh
KOffice suite - Kazakh language support.

%description Kazakh -l pl.UTF-8
KOffice - wsparcie dla języka kazachskiego.

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

%package Frisian
Summary:	KOffice suite - Frisian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka fryzyjskiego
Group:		I18n

%description Frisian
KOffice suite - Frisian language support.

%description Frisian -l pl.UTF-8
KOffice - wsparcie dla języka fryzyjskiego.

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

%package Low_Saxon
Summary:	KOffice suite - Low Saxon language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka dolnosaksońskiego
Group:		I18n

%description Low_Saxon
KOffice suite - Low Saxon language support.

%description Low_Saxon -l pl.UTF-8
KOffice - wsparcie dla języka dolnosaksońskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Dutch
Summary:	KOffice suite - Dutch language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka holenderskiego
Group:		I18n

%description Dutch
KOffice suite - Dutch language support.

%description Dutch -l pl.UTF-8
KOffice - wsparcie dla języka holenderskiego.

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
%setup -q -c -T %(seq -f '-a %g' 0 22 |sed -e 's/-a 15//;/^$/d' | xargs)

%build
for dir in koffice-l10n-*-%{version}; do
	cd $dir
	install -d build
	cd build
	%cmake \
		../
	%{__make}
	cd ../..
done

%install
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in %{orgname}-*-%{version}; do
		%{__make} -C $dir/build install \
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
FindLang el > Greek.lang
FindLang en_GB > English_UK.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang fr > French.lang
FindLang gl > Galician.lang
FindLang kk > Kazakh.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang nds > Low_Saxon.lang
FindLang nl > Dutch.lang
#FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
FindLang sv > Swedish.lang
FindLang tr > Turkish.lang
FindLang uk > Ukrainian.lang
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
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_languages

%clean
check_installed_files() {
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{name}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
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

%files -f Greek.lang Greek
%defattr(644,root,root,755)

%files -f Kazakh.lang Kazakh
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

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

#%files -f Polish.lang Polish
#%defattr(644,root,root,755)

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

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)
