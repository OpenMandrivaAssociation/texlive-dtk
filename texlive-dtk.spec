Name:		texlive-dtk
Version:	70112
Release:	1
Summary:	Document class for the journal of DANTE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/usergrps/dante/dtk
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a class and style file for typesetting "Die
TeXnische Komodie" -- the communications of the German TeX
Users Group DANTE e.V. The arrangement means that the class may
be used by article writers to typeset a single article as well
as to produce the complete journal.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dtk
%doc %{_texmfdistdir}/doc/latex/dtk

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
