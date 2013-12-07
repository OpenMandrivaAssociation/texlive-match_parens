# revision 26313
# category Package
# catalog-ctan /support/match_parens
# catalog-date 2012-04-05 17:28:29 +0200
# catalog-license gpl
# catalog-version 1.4
Name:		texlive-match_parens
Version:	1.4
Release:	6
Summary:	Easily detect mismatched parens
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/match_parens
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/match_parens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/match_parens.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-match_parens.bin = %{EVRD}

%description
Mismatches of parentheses, braces, (angle) brackets, especially
in TeX sources which may be rich in those, may be difficult to
trace. This little script helps you by writing your text to
standard output, after adding a left margin to your text, which
will normally be almost empty, but will clearly show any
mismatches.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/match_parens
%{_texmfdistdir}/scripts/match_parens/match_parens
%doc %{_texmfdistdir}/doc/support/match_parens/Object.html
%doc %{_texmfdistdir}/doc/support/match_parens/README
%doc %{_texmfdistdir}/doc/support/match_parens/add.png
%doc %{_texmfdistdir}/doc/support/match_parens/brick.png
%doc %{_texmfdistdir}/doc/support/match_parens/brick_link.png
%doc %{_texmfdistdir}/doc/support/match_parens/bug.png
%doc %{_texmfdistdir}/doc/support/match_parens/bullet_black.png
%doc %{_texmfdistdir}/doc/support/match_parens/bullet_toggle_minus.png
%doc %{_texmfdistdir}/doc/support/match_parens/bullet_toggle_plus.png
%doc %{_texmfdistdir}/doc/support/match_parens/created.rid
%doc %{_texmfdistdir}/doc/support/match_parens/darkfish.js
%doc %{_texmfdistdir}/doc/support/match_parens/date.png
%doc %{_texmfdistdir}/doc/support/match_parens/delete.png
%doc %{_texmfdistdir}/doc/support/match_parens/find.png
%doc %{_texmfdistdir}/doc/support/match_parens/index.html
%doc %{_texmfdistdir}/doc/support/match_parens/jquery.js
%doc %{_texmfdistdir}/doc/support/match_parens/loadingAnimation.gif
%doc %{_texmfdistdir}/doc/support/match_parens/macFFBgHack.png
%doc %{_texmfdistdir}/doc/support/match_parens/navigation.js
%doc %{_texmfdistdir}/doc/support/match_parens/package.png
%doc %{_texmfdistdir}/doc/support/match_parens/page_green.png
%doc %{_texmfdistdir}/doc/support/match_parens/page_white_text.png
%doc %{_texmfdistdir}/doc/support/match_parens/page_white_width.png
%doc %{_texmfdistdir}/doc/support/match_parens/plugin.png
%doc %{_texmfdistdir}/doc/support/match_parens/rdoc.css
%doc %{_texmfdistdir}/doc/support/match_parens/ruby.png
%doc %{_texmfdistdir}/doc/support/match_parens/search.js
%doc %{_texmfdistdir}/doc/support/match_parens/search_index.js
%doc %{_texmfdistdir}/doc/support/match_parens/searcher.js
%doc %{_texmfdistdir}/doc/support/match_parens/table_of_contents.html
%doc %{_texmfdistdir}/doc/support/match_parens/tag_blue.png
%doc %{_texmfdistdir}/doc/support/match_parens/tag_green.png
%doc %{_texmfdistdir}/doc/support/match_parens/transparent.png
%doc %{_texmfdistdir}/doc/support/match_parens/wrench.png
%doc %{_texmfdistdir}/doc/support/match_parens/wrench_orange.png
%doc %{_texmfdistdir}/doc/support/match_parens/zoom.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/match_parens/match_parens match_parens
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 812573
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 779616
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 753768
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718958
- texlive-match_parens
- texlive-match_parens
- texlive-match_parens
- texlive-match_parens

