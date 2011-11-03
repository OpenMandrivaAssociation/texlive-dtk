# revision 23484
# category Package
# catalog-ctan /usergrps/dante/dtk
# catalog-date 2011-08-06 19:26:43 +0200
# catalog-license lppl1.3
# catalog-version 1.26
Name:		texlive-dtk
Version:	1.26
Release:	1
Summary:	Document class for the journal of DANTE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/usergrps/dante/dtk
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides a class and style file for typesetting "Die
TeXnische Komodie" -- the communications of the German TeX
Users Group DANTE e.V. This means that this class can be used
by article writers to typeset a single article as well as to
produce the complete journal.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/dtk/dtk.bst
%{_texmfdistdir}/makeindex/dtk/dtk-adr.ist
%{_texmfdistdir}/makeindex/dtk/dtk-idx.ist
%{_texmfdistdir}/tex/latex/dtk/dtk-pdf.sty
%{_texmfdistdir}/tex/latex/dtk/dtk.clo
%{_texmfdistdir}/tex/latex/dtk/dtk.cls
%{_texmfdistdir}/tex/latex/dtk/dtk11.clo
%{_texmfdistdir}/tex/latex/dtk/dtklogos.sty
%doc %{_texmfdistdir}/doc/latex/dtk/Changes
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel-lua.pdf
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel-lua.tex
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel-xtx.pdf
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel-xtx.tex
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel.bib
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel.pdf
%doc %{_texmfdistdir}/doc/latex/dtk/doc/beispiel.tex
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk00.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk01.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk02.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk03.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk05.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk06.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk10.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk95.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk96.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk97.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk98.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/dtk99.clo
%doc %{_texmfdistdir}/doc/latex/dtk/historical/textlist.sty
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/Makefile
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/Makefile.in
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/adressen.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/editorial.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/grusswort.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/impressum.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/komoedie.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/ruecken.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/rueckenNeu.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/stammtische.tex
%doc %{_texmfdistdir}/doc/latex/dtk/komoedie/termine.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
