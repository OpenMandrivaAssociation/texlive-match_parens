Name:		texlive-match_parens
Version:	36270
Release:	2
Summary:	Easily detect mismatched parens
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/match_parens
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/match_parens.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/match_parens.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/support/match_parens/README
%doc %{_texmfdistdir}/doc/support/match_parens/match_parens.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/match_parens/match_parens match_parens
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
